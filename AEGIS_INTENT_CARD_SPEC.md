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
