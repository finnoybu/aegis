← [Back to repository README](../README.md)

# Aegis Lab Documentation

This directory contains authoritative documentation for the **Aegis development and testing laboratory**.

These documents capture the **hardware configuration, firmware decisions, storage layout, OS installation, and safety posture** of the system as it exists today. They are intended to make the environment:

- Reproducible
- Auditable
- Safe for iterative experimentation
- Easy to reason about months later

This is **not production documentation**. It is a lab record.

---

## Scope

These documents describe:

- A bare-metal Debian system prepared specifically for Aegis testing
- Decisions made to prioritize stability, debuggability, and isolation
- What has been intentionally configured **and** what has been intentionally deferred

They do **not** describe:
- Autonomous execution
- Privileged automation
- ZFS pools or data layouts beyond preparation
- GPU compute enablement
- Security hardening beyond baseline

Those will be documented when (and if) implemented.

---

## Document Index

### `hardware-inventory.md`
Authoritative inventory of:
- Motherboard, CPUs, RAM
- GPUs
- Storage devices and intended roles

---

### `firmware-bios-config.md`
Records all relevant firmware decisions:
- UEFI-only boot
- AHCI (no RAID / RST)
- SATA port usage
- Video OPROM configuration

This document explains *why* these choices were made.

---

### `storage-layout.md`
Describes:
- SSD partitioning (EFI + root)
- HDD wipe state
- Explicitly deferred storage configuration (ZFS, mirroring)

No assumptions are made beyond what exists now.

---

### `os-installation.md`
Captures:
- Debian version and installer choice
- Partitioning strategy
- User and privilege model
- Installed base packages

This is the reference for recreating the system from scratch.

---

### `post-install-validation.md`
Evidence-based validation:
- Disk enumeration
- SMART health checks
- Kernel error review
- Confirmation of system stability

This is the “green light” record.

---

### `rationale-and-safety.md`
Explains:
- Why this system is treated as a laboratory
- What safety boundaries exist today
- What is intentionally *not* implemented yet
- How future Aegis phases should respect these boundaries

This document is normative.

---

## Change Policy

Any of the following **must** be reflected in these docs:

- Firmware changes
- Storage reconfiguration
- Filesystem creation (e.g., ZFS)
- Privilege model changes
- Execution enablement
- GPU compute enablement

If the system changes and the docs don’t, the docs are wrong.

---

## Philosophy

> If it isn’t documented, it didn’t happen.  
> If it isn’t intentional, it isn’t allowed.

These documents exist to ensure Aegis development proceeds **deliberately, safely, and reversibly**.
