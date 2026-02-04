# CONTRIBUTING.md

## Purpose
This document defines how changes to Aegis are proposed, reviewed, and accepted.

Aegis prioritizes safety, clarity, and governance over velocity.

---

## Canonical First
Before proposing any change, contributors MUST review:
- AEGIS_CANON.md
- AEGIS_META_INDEX.md

If a change conflicts with Canon, it will be rejected.

---

## Types of Contributions

### Documentation
- Preferred and encouraged
- Must preserve intent and authority boundaries
- Canonical documents require extra scrutiny

### Code
- Must align with documented architecture
- Must not introduce undocumented capabilities
- Must include logging and enforcement hooks

---

## Change Process
1. Open an issue describing intent and impact
2. Reference affected canonical documents
3. Propose changes in a PR
4. Update AEGIS_DECISIONS.log if required
5. Await approval from CODEOWNERS

---

## Non-Negotiables
- No silent scope expansion
- No bypassing safety mechanisms
- No autonomous execution paths
- No undocumented privileges

---

## Tone & Culture
- Assume good faith
- Prefer explicitness over cleverness
- Safety > speed

