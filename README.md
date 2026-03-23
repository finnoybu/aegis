# Aegis (Archived)

> **This repository is archived.** It represents the original AEGIS V0 — the founding design from which the entire [AEGIS Initiative](https://github.com/aegis-initiative) ecosystem was built. Active development continues across the organization's repositories. See the [Decomposition](#decomposition) section below for where each component evolved.
>
> **Conceptual birth:** January 26, 2026
> **First commit:** February 4, 2026
> **Archived:** March 2026

---

Aegis is an **OS-adjacent AI mediation system**.

It is not an autonomous agent.
It does not execute actions on its own.
It exists to **mediate intent**, **explain consequences**, **enforce boundaries**, and **require explicit human approval** before any power is exercised.

Aegis is designed to be:
- governed, not clever
- explicit, not implicit
- mediated, not autonomous

---

## Project Status

- **Current Phase:** V0 — Mediation Skeleton
- **Execution:** ❌ Disabled
- **Languages:**
  - V0: Python (entirely)
  - V0.5: Python + Go
  - V1: Rust (surgically, for power boundaries)

---

## Lab Environment (Reference)

The reference development host (`aegis-lab`) used for controlled mediation testing
is documented separately:

- `docs/Aegis_Lab_Configuration.md`

This document records:
- OS hardening decisions
- User and permission boundaries
- Storage preparation state
- Explicit non-capabilities (no execution, no autonomy)

All Aegis development assumes this baseline unless explicitly stated otherwise.

---

## Repository Structure (V0)

```
daemon/         # Long-running mediation daemon (no execution)
orchestrator/   # Intent, planning, verification (mediation logic)
ui/             # Human-facing interfaces (CLI first)
schemas/        # Canonical schemas (JSON, etc.)
```

---

## Local Setup (Windows)

Aegis V0 requires **Python 3.11+** (tested with Python 3.14).

### 1. Verify Python

```powershell
python --version
```

Expected:
```
Python 3.x.x
```

### 2. Create a virtual environment

From the repository root:

```powershell
python -m venv .venv
```

> **Note:** On Windows, if venv creation hangs, close VS Code and run this from a standalone PowerShell first.  
> Reopen VS Code after the venv is created.

### 3. Activate the virtual environment

```powershell
.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Then activate again.

Your prompt should show:

```
(.venv) PS ...
```

### 4. Run Aegis V0

```powershell
python -m daemon.main
```

Expected output:

```
Aegis V0 daemon starting (mediation-only).
```

---

## Development Principles

- Always use a virtual environment
- Never commit `.venv/`
- No execution logic may exist in V0
- All authority derives from canonical documents

---

## Canonical Documentation

| Document | Purpose |
|--------|---------|
| ***Planning & Roadmap*** |
| [`AEGIS_IMPLEMENTATION_ROADMAP.md`](AEGIS_IMPLEMENTATION_ROADMAP.md) | Planned execution phases |
| [`AEGIS_END_TO_END_WALKTHROUGH.md`](AEGIS_END_TO_END_WALKTHROUGH.md) | Illustrative end-to-end validation of system coherence |
| ***Architecture & Mediation*** |
| [`AEGIS_RUNTIME_ARCHITECTURE.md`](AEGIS_RUNTIME_ARCHITECTURE.md) | System architecture |
| [`AEGIS_INTENT_CARD_SPEC.md`](AEGIS_INTENT_CARD_SPEC.md) | Human–Aegis interface contract |
| [`AEGIS_ACTION_SCHEMA.json`](AEGIS_ACTION_SCHEMA.json) | Machine-readable execution schema |
| ***Security & Boundaries*** |
| [`AEGIS_ALLOWED_ACTIONS_V1.json`](AEGIS_ALLOWED_ACTIONS_V1.json) | Explicit power boundary |
| [`AEGIS_REFUSAL_GUIDELINES.md`](AEGIS_REFUSAL_GUIDELINES.md) | Refusal and clarification behavior |
| [`AEGIS_SECURITY_MODEL.md`](AEGIS_SECURITY_MODEL.md) | Threat model and enforcement assumptions |
| [`AEGIS_THREAT_MODEL_APPENDIX.md`](AEGIS_THREAT_MODEL_APPENDIX.md) | Threat class enumeration |
| ***Governance & Philosophy*** |
| [`AEGIS_CANON.md`](AEGIS_CANON.md) | Immutable philosophy and constraints |
| [`AEGIS_META_INDEX.md`](AEGIS_META_INDEX.md) | Governance index and authority routing |
| [`AEGIS_DECISIONS.log`](AEGIS_DECISIONS.log) | Append-only record of major design decisions and rationale |
| [`AEGIS_GLOSSARY.md`](AEGIS_GLOSSARY.md) | Glossary of terms |
| ***Contribution & Process*** | *Before contributing, please read docs below* |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | Contribution rules and governance expectations |
| [`VERSIONING.md`](VERSIONING.md) | Versioning policy for specs and implementation |
| [`CI_AND_LINTING.md`](CI_AND_LINTING.md) | Continuous integration and code quality standards |
| [`LICENSE`](LICENSE) | Project licensing terms |
|||

Canonical authority is defined in [`AEGIS_META_INDEX.md`](AEGIS_META_INDEX.md)

---

## Reminder

Aegis advances when **understanding increases**, not when power increases.

---

## Decomposition

This repository was the monolithic origin of the AEGIS project. Its contents were decomposed into the [`aegis-initiative`](https://github.com/aegis-initiative) organization as the project matured:

| Origin Content | Destination | What It Became |
|---|---|---|
| AEGIS_CANON.md, Core Values, Human-Aegis Contract | [aegis-constitution](https://github.com/aegis-initiative/aegis-constitution) | Eleven Constitutional Articles, Doctrine, Principles, Protocols |
| Runtime Architecture, Action Schema, Intent Card Spec | [aegis-governance](https://github.com/aegis-initiative/aegis-governance) | AGP-1 protocol, reference architecture, JSON schemas |
| Security Model, Threat Model, Refusal Guidelines | [aegis-governance](https://github.com/aegis-initiative/aegis-governance), [aegis-core](https://github.com/aegis-initiative/aegis-core) | ATM-1 threat model, enforcement engine design |
| Python code (daemon, orchestrator, verification, refusal) | [aegis-core](https://github.com/aegis-initiative/aegis-core) | Governance runtime, policy engine, risk scoring |
| Meta Index, Decisions Log, Glossary, Versioning | [aegis](https://github.com/aegis-initiative/aegis) | ADR framework, governance doctrine, org standards |
| Intent Card UI concept, approval workflows | [aegis-platform](https://github.com/aegis-initiative/aegis-platform) | Operator dashboard, API surface |
| ALLOW/DENY/ESCALATE/REQUIRE_CONFIRMATION outcomes | [aegis-sdk](https://github.com/aegis-initiative/aegis-sdk) | SDK governance outcomes |

---

*AEGIS™ — "Capability without constraint is not intelligence"™*
*AEGIS Initiative — Finnoybu IP LLC*
