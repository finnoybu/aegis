# AEGIS_END_TO_END_WALKTHROUGH.md
## Aegis End-to-End Walkthrough v0.1

This document provides a concrete, end-to-end example of how Aegis operates
from human intent through execution and audit. It is canonical as a
coherence check across architecture, schema, security, and UX.

---

## Scenario
**Human goal:** “Publish my notes as a public webpage.”

Environment:
- Local machine
- Static site directory: `~/site/public/`
- Notes file: `~/docs/notes.md`
- Template: `blog.html`
- No external network calls

---

## 1. Intent Creation

Human states intent (natural language):
> “Publish my notes as a public webpage.”

Aegis creates an intent record:

```json
{
  "intent_id": "a1b2c3",
  "user_goal": "Publish my notes as a public webpage",
  "created_at_utc": "2026-02-03T21:10:00Z",
  "context_refs": [
    {"scheme": "file", "ref": "~/docs/notes.md"},
    {"scheme": "template", "ref": "blog.html"}
  ]
}
```

Audit event:
- `INTENT_CREATED`

---

## 2. Plan Proposal

Planner proposes steps:

1. Read notes file
2. Render HTML using template
3. Snapshot target directory
4. Write HTML to public site

Plan (conceptual):

```json
{
  "plan_id": "plan-001",
  "steps": [
    {
      "step_id": 1,
      "action": "fs.read",
      "args": {"path": "~/docs/notes.md"},
      "risk": "Low",
      "reversible": true,
      "requires_confirmation": false
    },
    {
      "step_id": 2,
      "action": "render.html",
      "args": {"template": "blog.html", "source": "mem://notes"},
      "risk": "Low",
      "reversible": true,
      "requires_confirmation": false
    },
    {
      "step_id": 3,
      "action": "fs.snapshot",
      "args": {"path": "~/site/public/"},
      "risk": "Low",
      "reversible": true,
      "requires_confirmation": false
    },
    {
      "step_id": 4,
      "action": "fs.write",
      "args": {"path": "~/site/public/notes.html"},
      "risk": "Medium",
      "reversible": true,
      "requires_confirmation": true
    }
  ]
}
```

Audit event:
- `PLAN_PROPOSED`

---

## 3. Verification

Verifier checks:
- All actions are allowed (v1)
- Snapshot precedes write
- No deletes
- No network egress
- Reversibility declared

Verification result:
- **PASS**

Audit event:
- `PLAN_VERIFIED`

---

## 4. Intent Card Presentation

Intent Card shows:

**Intent**
Publish my notes as a public webpage.

**Plan**
✓ Read notes  
✓ Render HTML  
✓ Snapshot public directory  
⚠ Write HTML file (confirmation required)

**Impact**
- 1 file created: `notes.html`
- Public visibility enabled

**Risk**
- Medium (public exposure)

**Energy**
- Local-small
- ~0.3s

**Reversibility**
- Snapshot available

Controls:
- Approve / Edit / Simulate / Cancel

Audit event:
- `CARD_PRESENTED`

---

## 5. Human Approval

Human clicks **Approve**.

Approval state:
```json
{
  "state": "APPROVED",
  "approved_at_utc": "2026-02-03T21:12:00Z",
  "approved_by": "user"
}
```

Audit event:
- `USER_DECISION`

---

## 6. Execution

Executor performs steps in order:

- Step 1: fs.read → SUCCESS
- Step 2: render.html → SUCCESS
- Step 3: fs.snapshot → SUCCESS
- Step 4: fs.write → SUCCESS

Execution result:
```json
{
  "status": "COMPLETED",
  "steps": [
    {"step_id": 1, "result": "SUCCESS"},
    {"step_id": 2, "result": "SUCCESS"},
    {"step_id": 3, "result": "SUCCESS"},
    {"step_id": 4, "result": "SUCCESS"}
  ]
}
```

Audit events:
- `STEP_EXECUTED` (per step)

---

## 7. Post-Execution Review

Aegis presents:
- Confirmation of success
- Link to generated file
- Option to rollback snapshot

No further action taken.

---

## 8. Alternative Paths (Illustrative)

### 8.1 Simulation Chosen
If **Simulate** were selected:
- No writes occur
- Diff preview shown
- Audit logs simulation result

### 8.2 Clarification Needed
If multiple note files existed:
- Aegis would pause and ask which file
- No plan executed

### 8.3 Refusal Example
If target path were `/etc/`:
- Immediate refusal
- Safe alternative suggested

---

## 9. Coherence Check

This walkthrough validates:
- Canon (consequences before action)
- Intent Card gating
- Allowed actions enforcement
- Security model assumptions
- Action schema compatibility
- Audit completeness

If this walkthrough ever fails to hold, the system has drifted.

---

End of document.
