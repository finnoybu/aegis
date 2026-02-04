# AEGIS_SECURITY_MODEL.md
## Aegis Security Model v0.1

This document defines the security posture, threat model, and mitigations for Aegis v1.
It is canonical for security assumptions, enforcement requirements, and permission UX.

Must remain consistent with:
- AEGIS_CANON.md (First Law: consequences before action)
- AEGIS_INTENT_CARD_SPEC.md (gating + visibility)
- AEGIS_ALLOWED_ACTIONS_V1.json (deny-by-default capability boundary)
- AEGIS_RUNTIME_ARCHITECTURE.md (enforcement points)
- AEGIS_ACTION_SCHEMA.json (machine-enforced structure)

---

## 1. Security Objectives (v1)

1. **Prevent unauthorized action**
   - No tool call without explicit capability + scope grant.

2. **Prevent unintended consequences**
   - Intent Card gating + diff/snapshot requirements for writes.

3. **Prevent data exfiltration**
   - No outbound transmission of sensitive content by default.
   - Strict domain allowlists for `net.fetch`; no `net.post` in v1.

4. **Resilience against prompt injection**
   - Untrusted content must not be able to alter tool policy or privileges.

5. **Auditability and accountability**
   - Append-only log of what happened, why, and what changed.

---

## 2. Trust Boundaries

Aegis is a composition of components with distinct trust levels:

- **Aegis Daemon (highest trust)**
  - Enforces capability gates
  - Mediates tools
  - Owns audit log

- **Tool Drivers (high trust, constrained)**
  - Perform the actual system actions
  - Must be sandboxed to least privilege
  - Must validate inputs

- **Verifier (high trust)**
  - Deterministic rules + optional small model
  - Must not have tool execution privileges

- **Planner/Renderer Models (lower trust)**
  - May hallucinate
  - Must never execute actions directly
  - Outputs must be validated and gated

- **Retrieved Content (untrusted)**
  - Web pages, documents, emails, third-party content
  - Must be treated as hostile input

---

## 3. Permission Model

### 3.1 Capability Grants
Aegis permissions are expressed as **capabilities** (verbs) and **scopes** (bounds).
Deny-by-default: if not explicitly granted, action is forbidden.

Examples:
- `fs.read` scoped to `~/docs/**`
- `net.fetch` scoped to domains: `example.com`, `docs.vendor.com`
- `app.launch` scoped to allowlisted apps

### 3.2 Scope Tokens
Execution uses opaque `scope_token`s that reference grants held by the daemon.
Models never mint scope tokens. Only the daemon issues them via user consent flows.

### 3.3 Modes (v1)
- Observe-only (read + propose)
- Assist (low/medium actions within scope, confirmation as required)
- Act-with-confirmation (required for all High risk steps)
Autonomous sandbox is out-of-scope for v1.

---

## 4. High-Risk Operations (v1 Policy)

High-risk includes (non-exhaustive):
- `app.automate`
- Any overwrite without snapshot
- Any network interaction beyond allowlisted `net.fetch`
- Any operation with non-reversible impact

Rules:
- High-risk steps always require explicit confirmation per run
- High-risk steps must have short timeouts and visible progress
- High-risk steps must produce detailed audit artifacts

---

## 5. Core Threats and Mitigations

### 5.1 Prompt Injection (Web / Docs / Email)
**Threat**
Untrusted content includes instructions intended to subvert Aegis (e.g., “ignore your rules”).
**Mitigations**
- Retrieval pipeline strips or isolates instructions
- Planner never receives raw tool policy text
- Verifier enforces allowed actions regardless of model output
- Tool calls must match schema + allowed action list
- UI highlights when untrusted content is driving actions

### 5.2 Data Exfiltration
**Threat**
Sensitive file content could be sent externally.
**Mitigations**
- `net.post` forbidden in v1
- `net.fetch` allowlist + response-size limits
- Outbound payload diffs required for any future post capability (v2+)
- “External Transmission” warning banner in Intent Card when applicable

### 5.3 Destructive File Operations
**Threat**
Accidental overwrite or deletion.
**Mitigations**
- `fs.delete` not allowed in v1
- `fs.write` requires snapshot for overwrite
- Diff preview required before approval
- Restore workflow must be one-click and auditable

### 5.4 UI Automation Drift
**Threat**
Automation clicks wrong UI elements, causes unintended actions.
**Mitigations**
- `app.automate` is High risk + per-run confirmation
- Hard macro boundaries + timeouts
- Step-by-step “checkpoints” (optional)
- Require visible UI focus and user presence for automation runs (policy option)

### 5.5 Privilege Escalation / Lateral Movement
**Threat**
Aegis obtains broader access than intended or crosses boundaries.
**Mitigations**
- Least privilege sandboxing for drivers
- No implicit access to secrets stores in v1
- Scope tokens tied to user identity and session
- Rate limiting and anomaly detection on tool calls

### 5.6 Model Hallucination as Execution
**Threat**
Model fabricates file paths, URLs, or claims success.
**Mitigations**
- Executor verifies preconditions (exists? readable?)
- Tool drivers return authoritative results
- UI requires evidence (diffs, outputs) to mark completion
- Verifier flags non-existent refs prior to execution

---

## 6. Security UX Requirements

Security must be *visible* without being unusable.

### 6.1 Intent Card Security Signals
The Intent Card MUST display:
- Which capabilities will be used
- Which scopes are exercised (paths/domains/apps)
- Which steps are High risk
- Whether any external contact occurs
- Reversibility status

### 6.2 Consent and Escalation
- Capabilities are granted explicitly with scope.
- One-time grants are preferred for High risk.
- Persistent grants must be revocable.
- When scope is insufficient, Aegis must request expansion with justification.

### 6.3 Kill Switch
A global kill switch must:
- Immediately stop ongoing tool execution
- Leave the system in the safest possible state
- Record an audit event

---

## 7. Logging, Redaction, and Privacy

### 7.1 Audit Log Contents
Audit events must include:
- intent_id, timestamps, actor, action, scope_token
- result + reason
- hashes or diff refs for outputs

### 7.2 Redaction Rules (v1)
- Logs default to redacted inputs (store hashes/refs rather than raw content)
- Raw content is stored only when necessary and explicitly consented
- Users can export logs in a privacy-preserving format

---

## 8. Security Testing Requirements (v1)

Minimum required tests:
- Attempt execution of unallowed actions (must fail)
- Attempt scope bypass (path traversal, wildcard domains)
- Prompt injection scenarios (web content tries to alter behavior)
- Diff/snapshot enforcement for overwrites
- Kill switch behavior under load
- Audit log integrity (append-only, tamper evidence)

---

## 9. Deferred Capabilities (Explicitly Not v1)

- `net.post` and any outbound submission
- `fs.delete` or destructive operations
- secrets store integration (`secrets.read`)
- payment initiation
- background autonomous actions beyond constrained indexing

---

End of document.
