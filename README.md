# Aegis

**Aegis** is an OS-native AI system designed to mediate between human intent and machine execution by making consequences explicit *before* action.

Aegis is not an autonomous agent.
It does not pursue goals.
It waits, explains, refuses when necessary, and executes only with explicit human approval.

---

## Core Principles
- **Mediation, not autonomy**
- **Consequences before action**
- **Explicit authority boundaries**
- **No silent power**
- **Auditability by default**

---

## Repository Structure & Canonical Documents

The Aegis project is governed by a small set of canonical documents.  
If documents conflict, authority is determined by the Meta Index.

### 🧭 Governance & Philosophy
- [`AEGIS_CANON.md`](AEGIS_CANON.md) — Immutable philosophy and first law
- [`AEGIS_META_INDEX.md`](AEGIS_META_INDEX.md) — Canonical document index and governance rules
- [`AEGIS_DECISIONS.log`](AEGIS_DECISIONS.log) — Append-only historical record

### 🗣 Language & Interface
- [`AEGIS_GLOSSARY.md`](AEGIS_GLOSSARY.md) — Canonical terminology
- [`AEGIS_INTENT_CARD_SPEC.md`](AEGIS_INTENT_CARD_SPEC.md) — Human–Aegis interaction contract

### 🔐 Security & Power Boundaries
- [`AEGIS_SECURITY_MODEL.md`](AEGIS_SECURITY_MODEL.md) — Threat model and enforcement assumptions
- [`AEGIS_ALLOWED_ACTIONS_V1.json`](AEGIS_ALLOWED_ACTIONS_V1.json) — Allowed actions (deny-by-default)
- [`AEGIS_REFUSAL_GUIDELINES.md`](AEGIS_REFUSAL_GUIDELINES.md) — Refusal and clarification behavior

### 🧱 Architecture & Validation
- [`AEGIS_RUNTIME_ARCHITECTURE.md`](AEGIS_RUNTIME_ARCHITECTURE.md) — Runtime design
- [`AEGIS_ACTION_SCHEMA.json`](AEGIS_ACTION_SCHEMA.json) — Machine-readable execution schema
- [`AEGIS_END_TO_END_WALKTHROUGH.md`](AEGIS_END_TO_END_WALKTHROUGH.md) — System coherence walkthrough

### 🚀 Implementation & Operations
- [`AEGIS_IMPLEMENTATION_ROADMAP.md`](AEGIS_IMPLEMENTATION_ROADMAP.md) — V0 → V1 build plan
- [`AEGIS_THREAT_MODEL_APPENDIX.md`](AEGIS_THREAT_MODEL_APPENDIX.md) — Concrete threat enumeration
- [`CI_AND_LINTING.md`](CI_AND_LINTING.md) — CI and linting expectations
- [`VERSIONING.md`](VERSIONING.md) — Versioning rules

### 🤝 Contribution & Governance
- [`CONTRIBUTING.md`](CONTRIBUTING.md) — How to propose and review changes
- [`CODEOWNERS`](CODEOWNERS) — Approval authority
- [`LICENSE`](LICENSE) — Project license

---

## Status
Aegis is currently in **design-complete / implementation-planning** phase.
No production execution code exists yet.

---

## Philosophy Reminder
Aegis does not replace human judgment.
It exists to make judgment *informed*.

