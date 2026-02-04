## Aegis Canonical Document Index & Governance

## What this is
The table of contents + governance layer for the entire Aegis project.

This document defines the purpose, authority, and maintenance rules
for each canonical Aegis artifact. It exists to prevent drift,
duplication, and ambiguity as the system evolves.

If there is ever a conflict between documents, this index determines
which document is authoritative for a given concern.

---

## Canonical Philosophy & Identity
- **AEGIS_CANON.md** — Highest authority. Immutable philosophy and constraints.

---

## Governance & History
- **AEGIS_META_INDEX.md** — Canonical index and authority resolver.
- **AEGIS_DECISIONS.log** — Append-only decision record.

---

## Language & Interface
- **AEGIS_GLOSSARY.md** — Canonical terminology.
- **AEGIS_INTENT_CARD_SPEC.md** — Human–Aegis interaction contract.

---

## Security & Power Boundaries
- **AEGIS_SECURITY_MODEL.md** — Threat model and enforcement assumptions.
- **AEGIS_ALLOWED_ACTIONS_V1.json** — Allowed actions (deny-by-default).
- **AEGIS_REFUSAL_GUIDELINES.md** — Refusal and clarification behavior.

---

## Architecture & Execution
- **AEGIS_RUNTIME_ARCHITECTURE.md** — Runtime architecture.
- **AEGIS_ACTION_SCHEMA.json** — Execution schema.
- **AEGIS_END_TO_END_WALKTHROUGH.md** — System coherence validation.

---

## Implementation & Operations
- **AEGIS_IMPLEMENTATION_ROADMAP.md** — Build plan.
- **AEGIS_THREAT_MODEL_APPENDIX.md** — Threat enumeration.
- **CI_AND_LINTING.md** — CI expectations.
- **VERSIONING.md** — Versioning rules.

---

## Contribution & Ownership
- **CONTRIBUTING.md** — Contribution rules.
- **CODEOWNERS** — Approval authority.
- **LICENSE** — Legal terms.

---

## Governance Rule
If a document is not listed here, it is not canonical.

If documents conflict, defer in order to:
1. AEGIS_CANON.md
2. AEGIS_META_INDEX.md
3. AEGIS_SECURITY_MODEL.md
4. AEGIS_ALLOWED_ACTIONS_V1.json

---

Aegis remembers because its documents do — not because any model does.
