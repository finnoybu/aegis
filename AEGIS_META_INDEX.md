← [Back to README](README.md)

## Aegis Canonical Document Index & Governance

## What this is
The table of contents + governance layer for the entire Aegis project.

This document defines the purpose, authority, and maintenance rules
for each canonical Aegis artifact. It exists to prevent drift,
duplication, and ambiguity as the system evolves.

If there is ever a conflict between documents, this index determines
which document is authoritative for a given concern.

This document applies to all contributors—human or AI—who participate
in the design, implementation, or governance of Aegis.

### This document answers:
- What is each file for?
- Which document is authoritative for what?
- What happens if documents conflict?
- How are changes made safely?
- Which documents are immutable vs versioned?

### It explicitly prevents:
- philosophical drift
- silent scope creep
- “we thought this lived somewhere else”
- rewriting history by accident

---

## Canonical system documents
Canonical documents define Aegis behavior, constraints, or enforcement.
They may not be overridden by implementation details or repo process files.

### Canonical Philosophy & Identity
- **AEGIS_CANON.md** — Highest authority. Immutable philosophy and constraints.

### Governance & History
- **AEGIS_META_INDEX.md** — Canonical index and authority resolver.
- **AEGIS_DECISIONS.log** — Append-only decision record (never rewritten).

### Language & Interface
- **AEGIS_GLOSSARY.md** — Canonical terminology.
- **AEGIS_INTENT_CARD_SPEC.md** — Human–Aegis interaction contract.

### Security & Power Boundaries
- **AEGIS_SECURITY_MODEL.md** — Threat model and enforcement assumptions.
- **AEGIS_ALLOWED_ACTIONS_V1.json** — Allowed actions boundary (deny-by-default).
- **AEGIS_REFUSAL_GUIDELINES.md** — Refusal and clarification behavior.

### Architecture & Validation
- **AEGIS_RUNTIME_ARCHITECTURE.md** — Runtime architecture and enforcement points.
- **AEGIS_ACTION_SCHEMA.json** — Machine-readable schema for intent/plan/audit.
- **AEGIS_END_TO_END_WALKTHROUGH.md** — Illustrative system coherence validation.

---

## Repository governance documents
These documents support collaboration and professionalism.
They do not define Aegis behavior unless explicitly referenced by a canonical document.

- **README.md** — Project overview and setup notes.
- **CONTRIBUTING.md** — Contribution process and expectations.
- **CODEOWNERS** — Ownership and review routing.
- **VERSIONING.md** — Versioning policy for specs and implementation.
- **CI_AND_LINTING.md** — CI/lint intentions and standards.
- **LICENSE** — Legal terms.

---

## Conflict resolution order
If documents conflict, defer in order to:
1. **AEGIS_CANON.md**
2. **AEGIS_META_INDEX.md**
3. **AEGIS_SECURITY_MODEL.md**
4. **AEGIS_INTENT_CARD_SPEC.md**
5. **AEGIS_ALLOWED_ACTIONS_V1.json**
6. **AEGIS_ACTION_SCHEMA.json**

No implementation detail may override a canonical document.

---

Aegis remembers because its documents do — not because any model does.
