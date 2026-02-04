← [Back to README](README.md)

# AEGIS_THREAT_MODEL_APPENDIX.md

## Purpose
This appendix enumerates concrete threat classes relevant to Aegis and explicitly documents what is in-scope and out-of-scope.

This document supports — but does not override — AEGIS_SECURITY_MODEL.md.

---

## Threat Actors

### Malicious User
- Attempts to coerce Aegis into destructive action
- Attempts social engineering or ambiguity exploitation

Mitigations:
- Intent clarification
- Explicit refusal rules
- No silent escalation

---

### Compromised Tool / Plugin
- External tools return malicious output
- Tool attempts privilege escalation

Mitigations:
- Strict schema validation
- Least-privilege execution
- Tool output treated as untrusted

---

### Prompt Injection
- Instruction smuggled via content or tool output

Mitigations:
- Role separation
- Verifier isolation
- No execution without approval

---

### Implementation Error
- Bugs that bypass enforcement
- Logging failures

Mitigations:
- Defense in depth
- Append-only logs
- Conservative defaults

---

## Explicitly Out of Scope
- Kernel-level exploits
- Physical access attacks
- Supply-chain attacks on the OS
- Nation-state adversaries

These are acknowledged but not addressed in V1.

---

## Residual Risk
Aegis reduces risk by:
- Making intent explicit
- Forcing human acknowledgement
- Preventing silent harm

It does not eliminate risk.
It makes it visible.

---

## Alignment With Canon
This appendix reinforces the First Law:
Consequences before action.
