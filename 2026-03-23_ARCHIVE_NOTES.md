# AEGIS V0 — Archive Notes

**Date:** 2026-03-23
**Repository:** `finnoybu/aegis` (to be archived as `aegis-initiative/aegis-origin`)
**Archived by:** Finnoybu
**Conceptual birth:** 2026-01-26
**First commit:** 2026-02-04
**Final commit:** 2026-02-27 (f482611)

---

## Purpose of This Document

This document captures the exact state of every component in the AEGIS V0
repository at the time of archival. It is intended as a permanent companion
to the frozen codebase — a snapshot of what existed, what worked, what didn't,
and what was intentionally deferred.

---

## 1. Project Identity at Time of Archive

AEGIS was conceived as an OS-adjacent AI mediation system — a guardian between
human intent and machine action. It was never designed to be an agent, assistant,
or chatbot. Its founding philosophy: **consequences before action**.

The project reached **V0 (Mediation-Only Skeleton)** status. Execution was
always disabled. No system mutation, no OS-level privileges, and no network
side effects were ever implemented.

---

## 2. Canonical Documentation (Complete)

All 13 canonical documents were written and internally consistent at time of
archive. These formed the philosophical and architectural foundation that was
later decomposed into the `aegis-initiative` organization.

| Document | Version | Status |
|---|---|---|
| `AEGIS_CANON.md` | v0.1 | Complete — First Law, Core Values, Human-Aegis Contract |
| `AEGIS_RUNTIME_ARCHITECTURE.md` | v0.1 | Complete — full component model, execution pipeline, enforcement points |
| `AEGIS_INTENT_CARD_SPEC.md` | v0.1 | Complete — card sections, lifecycle states, transition rules |
| `AEGIS_ACTION_SCHEMA.json` | v1 | Complete — machine-readable schema for plans and steps |
| `AEGIS_ALLOWED_ACTIONS_V1.json` | v1 | Complete — 10 allowed actions, deny-by-default |
| `AEGIS_SECURITY_MODEL.md` | v0.1 | Complete — threat model, trust boundaries, permission model |
| `AEGIS_THREAT_MODEL_APPENDIX.md` | v0.1 | Complete — threat class enumeration |
| `AEGIS_REFUSAL_GUIDELINES.md` | v0.1 | Complete — refusal behavior and tone |
| `AEGIS_IMPLEMENTATION_ROADMAP.md` | v0.1 | Complete — V0/V0.5/V1 milestones defined |
| `AEGIS_META_INDEX.md` | v0.1 | Complete — authority routing and governance boundaries |
| `AEGIS_GLOSSARY.md` | v0.1 | Complete — 10 term definitions |
| `AEGIS_DECISIONS.log` | — | Complete — 3 entries (2026-01-26, 2026-02-03, 2026-03-23) |
| `AEGIS_END_TO_END_WALKTHROUGH.md` | v0.1 | Complete — illustrative system coherence validation |

Supporting process documents (`CONTRIBUTING.md`, `VERSIONING.md`, `CI_AND_LINTING.md`,
`LICENSE`) were also in place.

---

## 3. Software Components

### 3a. Orchestrator (`orchestrator/`)

The orchestrator was the most developed part of the codebase. It contained four
modules implementing the mediation pipeline:

**Intent (`orchestrator/intent.py`) — Functional**
- Immutable `Intent` and `IntentMetadata` dataclasses
- Factory function `create_intent()` with safe defaults
- Fields: `raw_input`, `goal`, `scope`, `constraints`, `assumptions`, `metadata`
- Clean, minimal, no dependencies beyond stdlib
- 73 lines

**Plan (`orchestrator/plan.py`) — Functional**
- Most substantial module (317 lines)
- Schema-aligned dataclasses: `PlanStep`, `Plan`, `ScopeSpec`, `ScopeConstraints`, `PlanAudit`
- `RiskLevel` enum matching `AEGIS_ACTION_SCHEMA.json`
- Allowed-action registry helpers with fast lookup
- Structural validation (`validate_step_schema`, `validate_plan`)
- `create_dry_run_plan()` — full plan builder from raw step descriptions
- `plan_from_intent()` — lifecycle-gated entry point (requires `state == "clarified"`)
- No external dependencies

**Verification (`orchestrator/verification.py`) — Functional**
- `VerificationLevel` enum: PASS, WARN, BLOCK
- `VerificationFinding` and `VerificationReport` dataclasses
- Two verifier stubs implemented:
  - `verify_requires_confirmation()` — warns on medium/high risk without confirmation
  - `verify_scope_is_present()` — blocks unbounded scope
- Entry point: `run_verification(plan) -> VerificationReport`
- 122 lines, clean and working in isolation

**Refusal (`orchestrator/refusal.py`) — Broken at import**
- `RefusalDecisionType` enum: PASS, WARN, REFUSE
- `RefusalReason` and `RefusalDecision` dataclasses
- `decide_refusal()` — decision logic (any BLOCK -> REFUSE, WARN only -> WARN, else PASS)
- **Import error on line 24:** imports `VerificationSeverity` which does not exist
  (correct name: `VerificationLevel`)
- **Attribute errors:** references `finding.severity` and `finding.code` which do not
  exist on `VerificationFinding` (correct: `finding.level`, `finding.message`)
- 109 lines; logic is sound but module cannot be imported

**Mediation (`orchestrator/mediation.py`) — Broken at import**
- `MediationResult` dataclass aggregating pipeline outcomes
- `mediate_intent()` — intended to wire Intent -> Plan -> Verification -> Refusal
- **Import errors on line 27:** imports `verify_plan` and `VerificationResult` which do
  not exist (correct: `run_verification` and `VerificationReport`)
- **Attribute errors on lines 64-65:** references `intent.intent_id` and
  `intent.requested_steps` which do not exist on the `Intent` dataclass
- **Signature mismatch on lines 71-76, 88-93:** calls `decide_refusal()` with an
  `error=` keyword argument it does not accept
- 101 lines; conceptually correct but never tested

**Root cause of breakage:** The verification module was likely refactored (names
changed from an earlier draft) but its callers in `refusal.py` and `mediation.py`
were never updated. No tests or CI existed to catch the mismatch.

### 3b. Daemon (`daemon/main.py`) — Stub

Minimal entry point. Prints `"Aegis V0 daemon starting (mediation-only)."` and exits.
No event loop, no policy enforcement, no audit logging. 9 lines.

### 3c. CLI (`ui/cli.py`) — Stub

Prints `"Aegis CLI (stub)"` and exits. No intent input, no card rendering,
no approval workflow. 4 lines.

### 3d. Schemas (`schemas/`)

Directory existed in the repo structure but canonical schemas lived at the
repository root (`AEGIS_ACTION_SCHEMA.json`, `AEGIS_ALLOWED_ACTIONS_V1.json`).

---

## 4. Hardware Lab (`aegis-lab`)

A dedicated bare-metal server was built for controlled Aegis testing. The lab
was documented in `docs/` with seven authoritative records.

### 4a. Hardware

| Component | Specification |
|---|---|
| Motherboard | Supermicro X11DAi-N (rev 1.10) |
| CPUs | 2 x Intel Xeon Silver 4116 (24 cores / 48 threads) |
| RAM | 256 GB (multi-channel, balanced across 2 NUMA nodes) |
| GPU (display) | AMD Radeon RX 450/560-class (Polaris) |
| GPU (compute) | NVIDIA GeForce RTX 5060 Ti (Blackwell, 16 GB VRAM) |
| SSDs | 2 x Crucial MX500 1TB SATA |
| HDDs | 6 x 1TB SATA (mixed Seagate / Western Digital) |

### 4b. Firmware/BIOS

- UEFI-only boot (CSM/Legacy disabled)
- AHCI mode (no RAID/RST/VMD)
- Secure Boot disabled
- SATA1-8 active, sSATA ports unused
- BIOS dated 2023-01-12

### 4c. Operating System

- Debian 12 (Bookworm), minimal netinst
- Hostname: `aegis-lab`
- Primary user: `finnoybu` (sudo-enabled)
- GRUB via UEFI, ext4 root on SSD
- No desktop environment

### 4d. OS Hardening (Complete)

- System fully updated
- Security-only unattended upgrades enabled
- UFW firewall: default deny inbound, SSH only
- Journald logging verified (~8MB at baseline)
- Development tooling installed: git, build-essential, curl, wget, jq, python3+venv

### 4e. Aegis Runtime Scaffolding (Complete)

- System user/group `aegis` created (no login shell)
- Admin user `finnoybu` added to `aegis` group
- Directory layout:
  - `/opt/aegis` — code/runtime (empty)
  - `/var/lib/aegis` — state (empty)
  - `/var/log/aegis` — logs (empty)
  - `/etc/aegis` — configuration (guardrails README only)
- Permissions: `aegis:aegis`, mode `750`

### 4f. Storage State

- **Primary SSD:** GPT partitioned — 512 MB EFI (FAT32) + ~931 GB root (ext4)
- **Secondary SSD:** Present but unused; reserved for future RAID1 mirroring
- **6 HDDs:** All wiped, re-labeled with GPT, SMART health PASSED
  - Mixed sector sizes detected (512B and 4096B physical)
  - Note recorded: future ZFS pools must use `ashift=12`
  - No partitions, no filesystems, no pools created

### 4g. Network

- DHCP reservation on EdgeRouter
- Static DNS mapping: `aegis-lab -> 192.168.1.215`
- SSH verified via IP
- No web services exposed

### 4h. What Was NOT Done on the Lab

These items were explicitly identified and intentionally deferred:

- ZFS pool design and creation
- SSD RAID1 mirroring
- Multi-NIC / DMZ network isolation
- GPU compute enablement (NVIDIA drivers, CUDA)
- Namespaced execution testing
- Privilege boundary experiments
- Sandbox escape testing
- Any form of autonomous execution

---

## 5. Phase Completion Status

### Phase 0 — Foundations: COMPLETE

All 5 items checked:
- Language decision (Python for V0)
- Process model decision (single daemon)
- Repo scaffolded (`/daemon`, `/orchestrator`, `/ui`, `/schemas`)
- `.editorconfig` and formatting rules added
- Minimal Makefile added (`make run` -> `python -m daemon.main`)

### Phase 0.5 — Infrastructure & Lab Bring-Up: PARTIALLY COMPLETE

| Sub-phase | Status | Detail |
|---|---|---|
| 0.5a — OS & Host Hardening | Complete | All 5 items checked |
| 0.5b — Runtime Scaffolding | Complete | All 4 items checked |
| 0.5c — Storage Prep (Pre-ZFS) | Partial | 4/6 items checked; ZFS topology design and pool creation deferred |
| 0.5d — SSD Strategy | Partial | 1/3; OS on primary SSD done; mirroring decision and implementation deferred |
| 0.5e — Network Baseline | Partial | 2/4; SSH and DHCP done; multi-NIC/DMZ deferred |

Phase 0.5 was declared "complete enough to proceed with Phase 1."

### Phase 1 — Mediation Skeleton: PARTIALLY COMPLETE

| Item | Status | Detail |
|---|---|---|
| Stub Intent object creation | Done | Clean, immutable dataclass |
| Dry-run planner | Done | 317 lines, schema-aligned, validated |
| Verifier stub | Done | 2 rules implemented, working in isolation |
| Refusal paths end-to-end | Broken | Marked done but has import errors preventing execution |
| Intent Card rendering | Not done | No renderer exists; CLI is a stub |
| Audit log writer | Not done | No logging infrastructure |

### Phases 2-4: NOT STARTED

Phases 2 (Validation & Guardrails), 3 (First Walkthrough), and 4 (Governance
Checkpoint) were never begun in this repository. Their goals were absorbed into
the `aegis-initiative` organization's roadmap.

---

## 6. Infrastructure NOT Implemented

- **No tests** — No test files, test directories, or test runner configuration
- **No CI/CD** — Requirements documented in `CI_AND_LINTING.md` but no GitHub Actions
- **No type checking** — No mypy or pyright configuration
- **No linting** — No pylint, ruff, or flake8 configuration
- **No dependency management** — No `requirements.txt`, `pyproject.toml`, or `setup.py`
  (project used only stdlib)
- **No audit logging** — Specified as a Canon requirement but never implemented
- **No Intent Card UI** — The primary interface primitive existed only as a spec

---

## 7. What This Repository Became

The contents of this monolithic origin were decomposed into the `aegis-initiative`
GitHub organization:

| Origin | Destination | Evolution |
|---|---|---|
| AEGIS_CANON.md, Core Values, Human-Aegis Contract | aegis-constitution | Eleven Constitutional Articles, Doctrine, Principles, Protocols |
| Runtime Architecture, Action Schema, Intent Card Spec | aegis-governance | AGP-1 protocol, reference architecture, JSON schemas |
| Security Model, Threat Model, Refusal Guidelines | aegis-governance, aegis-core | ATM-1 threat model, enforcement engine design |
| Python code (daemon, orchestrator, verification, refusal) | aegis-core | Governance runtime, policy engine, risk scoring |
| Meta Index, Decisions Log, Glossary, Versioning | aegis | ADR framework, governance doctrine, org standards |
| Intent Card UI concept, approval workflows | aegis-platform | Operator dashboard, API surface |
| ALLOW/DENY/ESCALATE/REQUIRE_CONFIRMATION outcomes | aegis-sdk | SDK governance outcomes |

---

## 8. Final Assessment

The V0 repository served its purpose: it was the proving ground where AEGIS's
philosophy, architecture, and security model were forged. The canonical documents
— not the code — were the primary output. They were mature, internally consistent,
and strong enough to seed an entire multi-repository ecosystem.

The code reached "first draft of the mediation pipeline" stage. The intent and
planning modules were solid. The verification module worked in isolation. The
refusal and mediation modules had the right shape but were never integrated or
tested — a naming mismatch between verification's exports and its callers went
undetected because no tests or CI existed.

The hardware lab was stood up as a real, bare-metal server with deliberate
hardening and explicit non-capabilities. Storage disks were inventoried and
health-checked but never pooled. The GPU compute card was installed but never
enabled. The lab was ready for Phase 1 testing that never happened in this repo.

This repository is frozen. The DOI snapshot preserves its state for provenance
and citation. Development continues in the `aegis-initiative` organization.

---

*AEGIS — "Capability without constraint is not intelligence"*
