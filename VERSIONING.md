← [Back to README](README.md)

# VERSIONING.md

## Purpose
Defines how versions are assigned to Aegis artifacts.

---

## Versioning Scheme

Aegis uses semantic versioning where applicable:

MAJOR.MINOR.PATCH

### MAJOR
- Canon changes
- Security model changes
- Permission boundary changes

### MINOR
- New capabilities (explicitly approved)
- Backward-compatible schema changes

### PATCH
- Clarifications
- Bug fixes
- Documentation improvements

---

## Document Versioning
- Canonical documents may include version headers
- Append-only logs are not versioned

---

## Breaking Changes
Breaking changes require:
- Explicit documentation
- Decision log entry
- Clear migration guidance

---

## Authority
If versioning conflicts arise, AEGIS_META_INDEX.md is authoritative.
