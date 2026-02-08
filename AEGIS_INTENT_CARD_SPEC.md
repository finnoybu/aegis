← [Back to README](README.md)

# AEGIS INTENT CARD SPEC v0.1

## Purpose
The Intent Card is the primary human–AI interface primitive for Aegis.
Every meaningful action must be representable on a single card before execution.

If an action cannot be fully expressed on an Intent Card, it must not run.

---

## Card Sections (Fixed Order)

### 1. Intent
- Plain-language goal stated by the human.
- No instructions, no steps.
- Example: "Publish my notes as a public webpage."

### 2. Proposed Plan
- Ordered list of steps Aegis intends to take.
- Each step references a capability and scope.
- Each step has a risk level: Low / Medium / High.

### 3. Impact Summary
- Concrete changes that will occur if approved.
- Examples:
  - Files created/modified/deleted
  - External services contacted
  - Applications automated

### 4. Risk Disclosure
- What could go wrong.
- What assumptions Aegis is making.
- What context might be missing.

### 5. Energy & Resource Cost (Estimate)
- Compute class: Local-small / Local-large / Remote
- Expected runtime
- Optional carbon/energy note if available

### 6. Reversibility
- Can this be undone?
- If yes: how (snapshot, restore, rollback)
- If no: explicit warning and confirmation required

---

## Required Controls
- Approve
- Edit (human modifies intent or plan)
- Simulate (dry run, no side effects)
- Cancel

---

## Visual Rules
- Entire card must fit on a single screen without scrolling.
- Diffs and details open in secondary panels.
- High-risk steps must be visually distinct.

---

## Failure Modes
If any section cannot be populated clearly:
- Aegis must pause
- Aegis must ask a clarifying question
- Or Aegis must refuse

---

## Non-Goals
- The Intent Card is not a chat transcript.
- The Intent Card is not a workflow editor.
- The Intent Card is not optional.

---

## Intent Lifecycle States

Every intent submitted to Aegis progresses through a fixed, explicit lifecycle.
These states govern mediation only and do not imply permission to execute actions.

### States

**draft**
- The intent exists but is incomplete or unvalidated.
- No analysis or planning is performed.
- This is the initial state for all new intents.

**clarifying**
- Aegis requires additional information to safely understand the intent.
- Ambiguity, missing fields, or unsafe assumptions have been detected.
- Human input is required to proceed.

**blocked**
- The intent cannot proceed as stated.
- A blocking reason must be explicit, human-readable, and auditable.
- This state is terminal until the intent is revised by a human.

**approved**
- The intent is complete, understood, and allowed *in principle*.
- Approval does not grant permission to execute actions.
- Approved intents may proceed to planning.

**planned**
- A non-executable plan has been generated.
- The plan is explanatory, auditable, and mediation-only.
- This is a terminal state in Phase 1.

---

### Allowed State Transitions

draft → clarifying
draft → blocked
draft → approved

clarifying → draft
clarifying → blocked
clarifying → approved

approved → planned

blocked → draft

---

### Forbidden Transitions

- blocked → approved
- draft → planned
- clarifying → planned
- planned → any other state
- Skipping lifecycle states

---

### Invariants

- Every state transition must record:
  - previous state
  - new state
  - timestamp
  - rationale
- Aegis may not advance intent state without explicit human action.
- No lifecycle state grants permission to execute actions.
- “Approved” does not imply authority to act.


