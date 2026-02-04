# AEGIS_RUNTIME_ARCHITECTURE.md
## Aegis Runtime Architecture v0.1

This document defines the runtime architecture for Aegis (v1).
It is canonical for system components, execution flow, and enforcement points,
and must remain consistent with:
- AEGIS_CANON.md
- AEGIS_INTENT_CARD_SPEC.md
- AEGIS_ALLOWED_ACTIONS_V1.json

---

## 1. Design Goals (v1)

1. **Consequences before action**
   - Every non-trivial execution is gated by an Intent Card + human approval when required.

2. **Separation of concerns**
   - Planning, verification, and execution are distinct components.

3. **Capability-scoped execution**
   - Deny-by-default actions; scopes and grants are explicit.

4. **Auditability and replay**
   - Every action is logged as an immutable event record with diffs where applicable.

5. **Local-first**
   - Prefer local models and local data processing; external calls are explicit and allowlisted.

---

## 2. High-Level Component Model

### 2.1 Runtime Components

- **Aegis Daemon (System Service)**
  - Subscribes to OS/app events
  - Enforces policy and capabilities
  - Mediates access to tool drivers
  - Owns audit log append-only store
  - Owns rate limiting and kill-switch

- **Session Orchestrator (User-Space)**
  - Builds context for a single intent session
  - Invokes models (planner/verifier/renderer)
  - Maintains session state and references (mem://)
  - Produces Intent Cards and Action Plans

- **Model Layer**
  - **Planner Model**: proposes structured plans
  - **Verifier Model**: validates plan safety/compliance (may be rules + small model)
  - **Renderer Model** (optional): generates human-facing summaries, HTML, UX strings

- **Tool Drivers (Capability Providers)**
  - Filesystem driver
  - Template/render driver
  - Network fetch driver
  - HTTP response driver
  - App launch + (limited) automation driver
  - Local indexing/search driver

- **UI Surface**
  - Intent Panel / Intent Card UI
  - Diff viewers and detail panels
  - Approval controls and kill switch

---

## 3. Core Execution Pipeline

### 3.1 Event → Intent → Plan → Verify → Card → Execute → Audit

ASCII overview:

```
[Trigger/Event/User] 
      |
      v
[Session Orchestrator] --(context assembly)--> [Planner Model]
      |                                          |
      |<----------- structured plan -------------|
      |
      v
[Verifier] --(policy checks)--> PASS / FAIL / NEEDS_CLARIFICATION
      |
      v
[Intent Card UI] --(Approve/Edit/Simulate/Cancel)--> decision
      |
      v
[Executor] --(capability-scoped tool calls)--> [Tool Drivers]
      |
      v
[Audit Log + Diffs + Snapshots] ---> [User Review / Export]
```

### 3.2 Plan Objects (Conceptual)

A plan is an ordered list of steps. Each step MUST include:
- action (must exist in AEGIS_ALLOWED_ACTIONS_V1.json)
- args (validated per action)
- scope reference
- risk classification (Low/Medium/High)
- reversibility metadata
- confirmation requirement (derived from risk + policy)

---

## 4. Enforcement Points (Non-Negotiable)

Aegis is designed so that *no single component can “just do things”*.

### 4.1 Capability Gate
- Every tool driver call is mediated by the **Aegis Daemon**
- The daemon checks:
  - action is allowed
  - scope is granted
  - rate limits
  - environment posture (e.g., locked screen, no user presence if required)

### 4.2 Verification Gate
- The verifier must pass before presenting an executable card.
- Verifier checks:
  - allowed actions only
  - required snapshot steps before writes
  - no hidden network egress
  - confirmation required for high-risk steps
  - output validators are declared for render/response actions

### 4.3 Intent Card Gate
- A step cannot execute unless:
  - it appears on the Intent Card
  - it has not been materially changed since approval
- If edited, the plan must re-verify.

### 4.4 Snapshot/Diff Gate (Writes)
- Before any `fs.write`:
  - `fs.snapshot` is required (unless writing a new file that does not overwrite)
  - a diff preview MUST be available
- Deletes are not permitted in v1 (deny-by-default posture).

---

## 5. Session Model

A session is created per intent and includes:
- `intent_id`
- user goal (string)
- context refs (`file://`, `template://`, `index://`, `web://`)
- plan steps
- verification report
- approval state
- execution results
- rollback references

**Ephemeral memory**
- Intermediate objects live in `mem://` references during a session.
- Only explicitly exported artifacts persist (files, logs, indexes).

---

## 6. Tool Driver Contracts (v1)

All drivers implement a common envelope:
- `action`
- `args`
- `scope_token`
- `intent_id`
- `dry_run` (simulate)
- `trace_id`

### 6.1 Filesystem Driver
- `fs.read`: read within allowlisted paths
- `fs.write`: write within allowlisted paths, requires snapshot for overwrite
- `fs.snapshot`: creates rollback checkpoint for file(s)

### 6.2 Render Driver
- `render.html`: template + data → HTML (sanitized)

### 6.3 Network Driver
- `net.fetch`: allowlisted domain fetch, read-only
- No `net.post` in v1

### 6.4 HTTP Response Driver
- `http.respond`: returns sanitized HTML with strict CSP injection
- Must declare:
  - max bytes
  - sanitizer profile
  - cache key strategy

### 6.5 App Driver
- `app.launch`: allowed apps only (v1 allowlist)
- `app.automate`: high-risk; requires explicit confirmation each run; bounded macro timeouts

### 6.6 Index Driver
- `index.local`: builds local semantic index (deferred/batched allowed)
- `summarize.local`: local summarization only

---

## 7. Audit Logging (Append-Only)

### 7.1 Event Types (Conceptual)
- `INTENT_CREATED`
- `CONTEXT_ATTACHED`
- `PLAN_PROPOSED`
- `PLAN_VERIFIED`
- `CARD_PRESENTED`
- `USER_DECISION`
- `STEP_EXECUTED`
- `STEP_FAILED`
- `ROLLBACK_CREATED`
- `ROLLBACK_APPLIED`
- `REFUSAL`
- `CLARIFICATION_REQUESTED`

### 7.2 Required Fields per Audit Event
- timestamp (UTC)
- intent_id
- actor (user / aegis / tool)
- action (if relevant)
- scope (if relevant)
- inputs (redacted as needed)
- outputs (hash or diff reference)
- result (success/fail)
- reason (especially for refusal/clarification)

Audit logs MUST be exportable and human-readable.

---

## 8. Refusal, Clarification, and Simulation

### 8.1 Refusal
Aegis MUST refuse when:
- an action is not in the allowed list
- a scope is not granted
- reversibility cannot be stated and risk is non-trivial
- intent cannot be expressed on a card
- plan includes hidden egress or unsafe HTML/automation

Refusal output must include:
- the reason
- what would be needed to proceed (capability/scope or clarified intent)

### 8.2 Clarification
Aegis asks for clarification when:
- missing file paths
- ambiguous target (which account? which folder?)
- uncertain consequences (would overwrite X)

### 8.3 Simulation
Every plan must support a `dry_run` where feasible.
Simulation must produce:
- projected diffs
- projected network calls
- projected outputs
- estimated energy cost class

---

## 9. Energy & Resource Policy (v1)

- Default to **Local-small** models for planning and summarization when sufficient.
- Use heavier models only when:
  - user requests “best quality”, or
  - verifier flags low confidence in the plan.

Background indexing:
- may be deferred to plugged-in power and user-defined schedules (implementation-dependent)

---

## 10. Minimal Deployment Topologies

### 10.1 Local-Only (Preferred v1)
- Daemon + Orchestrator local
- Local models or locally hosted model endpoint
- No external calls except explicit `net.fetch` allowlisted

### 10.2 Hybrid
- Daemon local
- Orchestrator local
- Planner model remote (explicit)
- Verifier local/rules-based
- All sensitive context redacted unless user consents

---

## 11. v1 Scope Boundaries

Explicit v1 constraints:
- No deletes (`fs.delete`) in v1
- No external posting (`net.post`) in v1
- No silent high-risk automation
- No hidden background actions beyond indexing (and only within policy)

---

## 12. Next Canonical Artifacts

This architecture implies the need for:
- **AEGIS_ACTION_SCHEMA.json**: formal schema for plan steps and tool envelopes
- **AEGIS_SECURITY_MODEL.md**: threat model + mitigations + permission UX
- **AEGIS_REFUSAL_GUIDELINES.md**: refusal style, templates, and escalation rules

---

End of document.
