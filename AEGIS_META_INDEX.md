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

## Canonical Philosophy & Identity

### AEGIS_CANON.md
**Purpose**  
Defines the immutable philosophy, values, and constraints of Aegis.

**Authority**  
Highest. Supersedes all other documents.

**Scope**
- Identity
- First Law of Aegis
- Core values
- Non-negotiable constraints
- Human–Aegis contract

**Change Policy**
- Rare
- Requires explicit human approval
- All changes must be logged in AEGIS_DECISIONS.log

---

## Language & Semantics

### AEGIS_GLOSSARY.md
**Purpose**  
Provides precise definitions for terms used throughout the project.

**Authority**  
High. Canonical for terminology.

**Scope**
- Definitions
- Semantic boundaries
- Meaning preservation

**Change Policy**
- Additive preferred
- Redefinitions require decision log entry

---

## Historical Record

### AEGIS_DECISIONS.log
**Purpose**  
Append-only record of major design decisions and rationale.

**Authority**  
Historical truth. Never rewritten.

**Scope**
- Design milestones
- Rejected alternatives
- Approved changes

**Change Policy**
- Append-only
- No deletions or edits

---

## Interface Contract

### AEGIS_INTENT_CARD_SPEC.md
**Purpose**  
Defines the primary human–Aegis interface primitive.

**Authority**  
Authoritative for UX, approval flow, and trust mechanics.

**Scope**
- Required UI sections
- Execution gating rules
- Failure modes
- Human control surface

**Change Policy**
- Versioned
- Changes require UX + safety review
- Must remain backward-compatible where possible

---

## Capability & Power Boundary

### AEGIS_ALLOWED_ACTIONS_V1.json
**Purpose**  
Defines the complete set of actions Aegis is allowed to perform in v1.

**Authority**  
Authoritative for execution permissions and safety enforcement.

**Scope**
- Allowed actions
- Risk classification
- Reversibility
- Deny-by-default posture

**Change Policy**
- New actions require:
  - Risk assessment
  - Decision log entry
  - Version bump
- No silent expansion

---

## Runtime Architecture

### AEGIS_RUNTIME_ARCHITECTURE.md
**Purpose**  
Defines the canonical runtime architecture for Aegis.

**Authority**  
Authoritative for system components, execution flow, and enforcement points.

**Scope**
- Daemon / orchestrator / model separation
- Execution pipeline
- Enforcement gates
- Deployment topologies

**Change Policy**
- Versioned
- Must remain consistent with AEGIS_CANON.md
- Changes require decision log entry

---

## Action & Execution Schema

### AEGIS_ACTION_SCHEMA.json
**Purpose**  
Machine-readable schema defining intents, plans, steps, verification, execution results, and audit events.

**Authority**  
Authoritative for structural validation and tool-driver contracts.

**Scope**
- Intent objects
- Plan and step structure
- Scope tokens
- Verification reports
- Audit event format

**Change Policy**
- Versioned
- Backward compatibility strongly preferred
- Changes require decision log entry

---

## Security Model

### AEGIS_SECURITY_MODEL.md
**Purpose**  
Defines the threat model, trust boundaries, mitigations, and permission UX for Aegis.

**Authority**  
Authoritative for security posture and enforcement assumptions.

**Scope**
- Threat modeling
- Capability and scope enforcement
- Prompt injection mitigation
- Audit and redaction rules

**Change Policy**
- Versioned
- Must preserve First Law guarantees
- Changes require security review + decision log entry

---

## Refusal & Clarification Behavior

### AEGIS_REFUSAL_GUIDELINES.md
**Purpose**  
Defines how Aegis refuses, pauses, or proposes safe alternatives.

**Authority**  
Authoritative for refusal structure, tone, and non-execution behavior.

**Scope**
- Refusal conditions
- Clarification rules
- Safe alternative proposals
- Audit requirements

**Change Policy**
- Versioned
- Must remain consistent with Security Model
- Changes require decision log entry

---

## Validation & Coherence

### AEGIS_END_TO_END_WALKTHROUGH.md
**Purpose**  
End-to-end illustrative walkthrough validating coherence across all canonical documents.

**Authority**  
Canonical for system-level consistency checks.

**Scope**
- Intent to execution flow
- UX gating behavior
- Audit completeness

**Change Policy**
- Updated when canonical behavior changes
- Must reflect current architecture and rules

---

## Governance Rule

If a document is not listed here, it is not canonical.

If behavior is unclear or documents appear to conflict, defer in order to:
1. AEGIS_CANON.md
2. AEGIS_INTENT_CARD_SPEC.md
3. AEGIS_ALLOWED_ACTIONS_V1.json

No implementation detail may override a canonical document.

---

## Rationale

This index ensures that:
- Philosophy outlives implementation
- Trust boundaries remain explicit
- The system survives scale, teams, and time
- No single model or contributor becomes a source of truth

Aegis remembers because its documents do — not because any model does.
