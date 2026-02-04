# CI_AND_LINTING.md

## Purpose
Defines continuous integration and linting expectations for Aegis.

---

## CI Goals
- Prevent unsafe changes from merging
- Enforce schema correctness
- Preserve governance boundaries

---

## Required Checks

### Documentation
- Markdown lint
- Link validation

### Schemas
- JSON schema validation
- Backward compatibility checks

### Code (when present)
- Unit tests
- Static analysis
- No execution without tests

---

## Security Gates
- No new permissions without explicit approval
- No removal of enforcement hooks
- No modification of Canon without decision log entry

---

## Philosophy
CI exists to protect humans from mistakes — including their own.
