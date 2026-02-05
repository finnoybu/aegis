# Rationale and Safety Posture

## Purpose
This system is a laboratory environment for Aegis development and testing.
It is not production infrastructure.

## Design Principles
- Explain-first, stepwise configuration
- Hardware stability before software complexity
- Explicit deferral of risky operations

## Current Capability
- Mediation-only testing
- Observation and introspection
- No autonomous execution
- No privileged automation

## Deferred by Design
- ZFS creation
- SSD mirroring
- Execution gating
- Sandbox escape testing
- GPU compute enablement

## Safety Boundaries
- No destructive operations without confirmation
- All storage changes intentional and documented
- Firmware and OS choices favor debuggability over hard lockdown

## Next Phases (Not Implemented)
- ZFS pool creation on HDDs
- SSD RAID1
- Namespaced execution testing
- Privilege boundary experiments
