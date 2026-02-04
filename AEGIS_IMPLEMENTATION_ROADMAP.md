← [Back to README](README.md)

# AEGIS_IMPLEMENTATION_ROADMAP.md

## Purpose
This document defines a concrete, buildable path from the current canonical design of Aegis to a working V1 system.
It prioritizes momentum, safety, and learning over completeness.

This is not a promise of features.
It is an execution plan with explicit non-goals.

---

## Guiding Principles
- Build mediation before power
- Prefer stubs over assumptions
- Make irreversible actions impossible in V0
- Optimize for debuggability and auditability
- Preserve Canon over convenience

---

## Target Milestones

### V0 — Skeleton (Non-Executing)
**Goal:** Prove orchestration, not capability.

Includes:
- Intent parsing
- Plan generation (dry-run only)
- Intent Card rendering
- Verification pipeline
- Refusal behavior
- Audit logging (no execution)

Excludes:
- Real system mutation
- OS-level privileges
- Network side effects

---

### V0.5 — Safe Execution (Constrained)
**Goal:** Execute reversible, low-risk actions only.

Includes:
- File read
- Process inspection
- Query-only system calls
- Explicit scope enforcement
- Human approval loop

Excludes:
- Destructive actions
- Privilege escalation
- Silent execution

---

### V1 — Governed Power
**Goal:** Enable controlled, auditable execution.

Includes:
- Versioned allowed actions
- Snapshot / rollback requirements
- Destructive action gating
- Explicit override pathways
- Full audit trail

---

## Proposed Repository Structure

/daemon
  - event loop
  - intent intake
  - policy enforcement hooks

/orchestrator
  - planner
  - verifier
  - refusal engine

/ui
  - intent card renderer
  - approval workflow

/schemas
  - action schema
  - intent schema
  - audit schema

/logs
  - append-only audit output

---

## Technology Assumptions (Non-Binding)
- Language: Python or Go (initial)
- UI: Web-based (local)
- Storage: File-backed JSON / append-only logs
- Model: External LLM (pluggable)

---

## Explicit Non-Goals
- Autonomous goal generation
- Background execution without intent
- Self-modifying Canon
- Undocumented capabilities

---

## Exit Criteria for V1
Aegis can:
- Accept an intent
- Explain consequences
- Refuse unsafe actions
- Execute safe actions
- Log everything
- Stop when uncertain
