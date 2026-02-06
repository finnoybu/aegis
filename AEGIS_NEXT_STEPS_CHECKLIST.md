# Aegis — Near-Term Execution Checklist

This checklist represents the recommended next steps for Aegis, ordered to
maximize learning, safety, and momentum while minimizing rework.

Use this as a living execution guide. Items may be reordered as constraints
become clearer.

---

## Phase 0 — Foundations

- [X] Choose implementation language for V0 (Python vs Go) 
    - Decision: V0 Python; V0.5 Python + Go split; V1 Rust, surgically
- [X] Decide process model (single daemon vs daemon + UI service)
    - Decision: Single daemon (UI can be CLI for now)
- [X] Scaffold repo directories (`/daemon`, `/orchestrator`, `/ui`, `/schemas`)
- [X] Add `.editorconfig` and basic formatting rules
- [X] Add minimal project makefile / task runner

---

## Phase 0.5 — Infrastructure & Lab Bring-Up (Non-Executing)

This phase captures the baseline infrastructure work required to support
Aegis development safely and reproducibly.

Work in this phase:
- Does NOT add execution capability
- Does NOT expand Aegis authority
- Exists solely to support later mediation and validation work

This phase may be partially complete without blocking Phase 1.

### Phase 0.5a — Baseline OS & Host Hardening
- [X] Bare-metal Debian install (no hypervisor)
- [X] System fully updated
- [X] Security-only unattended upgrades enabled
- [X] Host firewall enabled (SSH-only inbound)
- [X] Journald logging verified

### Phase 0.5b — Aegis Runtime Scaffolding
- [X] Create dedicated `aegis` system user and group
- [X] Create runtime directories with restrictive permissions
- [X] Document explicit non-capabilities (no execution, no services)
- [X] Ensure admin access is intentional and auditable

### Phase 0.5c — Storage Preparation (Pre-ZFS)
- [X] Inventory all disks
- [X] Validate SMART health
- [X] Identify mixed sector sizes
- [X] Re-label HDDs with GPT
- [ ] Design ZFS topology (no pool creation yet)
- [ ] Create ZFS pool (explicit future decision)

### Phase 0.5d — SSD Strategy
- [X] Install OS on primary SSD
- [ ] Decide on root mirroring strategy (optional)
- [ ] Implement SSD mirroring (if chosen)

### Phase 0.5e — Network Baseline
- [X] Stable SSH access
- [X] DHCP reservation and local DNS mapping
- [ ] Decide on multi-NIC / DMZ model (future)
- [ ] Implement network isolation (future, if required)

---

## Phase 1 — Mediation Skeleton (No Execution)

- [ ] Stub Intent object creation (schema-valid, no side effects)
- [ ] Implement dry-run planner (plan generation only)
- [ ] Implement verifier stub (explain-only, never execute)
- [ ] Implement refusal paths end-to-end
- [ ] Render first Intent Card (CLI or simple local web UI)
- [ ] Wire append-only audit log writer

---

## Phase 2 — Validation & Guardrails

- [ ] Validate action schema against sample intents
- [ ] Add mock “allowed action” evaluator
- [ ] Implement scope token concept (non-enforcing initially)
- [ ] Add basic unit tests for planner/verifier boundaries
- [ ] Add schema validation to CI (JSON lint + structure checks)

---

## Phase 3 — First Walkthrough

- [ ] Walk a single benign use case through V0 (no execution)
- [ ] Review logs for clarity, completeness, and human readability
- [ ] Identify friction points in intent → explanation → approval flow
- [ ] Decide what qualifies as V0 → V0.5 transition

---

## Phase 4 — Governance Checkpoint

- [ ] Add decision log entry for first executable action class
- [ ] Re-review Canon, Security Model, and Allowed Actions
- [ ] Pause and reassess architecture before real execution

---

## Reminder

Aegis advances when **understanding increases**, not when power increases.
If a step feels rushed, stop and explain first.
