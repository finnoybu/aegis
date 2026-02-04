# Aegis

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
| ***Governance & Philosophy*** |
| [`AEGIS_CANON.md`](AEGIS_CANON.md) | Immutable philosophy and constraints |
| [`AEGIS_META_INDEX.md`](AEGIS_META_INDEX.md) | Governance index and authority routing |
| [`AEGIS_DECISIONS.log`](AEGIS_DECISIONS.log) | Append-only record of major design decisions and rationale |
| ***Architecture & Mediation*** |
| [`AEGIS_RUNTIME_ARCHITECTURE.md`](AEGIS_RUNTIME_ARCHITECTURE.md) | System architecture |
| [`AEGIS_INTENT_CARD_SPEC.md`](AEGIS_INTENT_CARD_SPEC.md) | Human–Aegis interface contract |
| [`AEGIS_ACTION_SCHEMA.json`](AEGIS_ACTION_SCHEMA.json) | Machine-readable execution schema |
| ***Security & Boundaries*** |
| [`AEGIS_SECURITY_MODEL.md`](AEGIS_SECURITY_MODEL.md) | Threat model and enforcement assumptions |
| [`AEGIS_ALLOWED_ACTIONS_V1.json`](AEGIS_ALLOWED_ACTIONS_V1.json) | Explicit power boundary |
| [`AEGIS_REFUSAL_GUIDELINES.md`](AEGIS_REFUSAL_GUIDELINES.md) | Refusal and clarification behavior |
| ***Planning & Roadmap*** |
| [`AEGIS_IMPLEMENTATION_ROADMAP.md`](AEGIS_IMPLEMENTATION_ROADMAP.md) | Planned execution phases |
| [`AEGIS_END_TO_END_WALKTHROUGH.md`](AEGIS_END_TO_END_WALKTHROUGH.md) | Illustrative end-to-end validation of system coherence |
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
