# Aegis Lab System Configuration

This document records the **baseline laboratory configuration** for the `aegis-lab` host.
It is intentionally factual and non-speculative.

## Host Identity
- Hostname: aegis-lab
- OS: Debian GNU/Linux 12 (Bookworm)
- Purpose: Controlled Aegis mediation testing (no execution)

---

## Phase B — Baseline Hardening

Completed actions:
- System fully updated (`apt update && apt upgrade`)
- Automatic **security-only** updates enabled (`unattended-upgrades`)
- Host firewall enabled (UFW)
  - Default deny inbound
  - Allow SSH (22/tcp)
- Journald logging verified
  - Current usage ~8MB
  - No retention tuning applied yet

Security posture:
- No exposed services
- No ICMP requirement
- SSH is sole management interface

---

## Phase D — Aegis Runtime Scaffolding

### System User & Group
- System group: `aegis`
- System user: `aegis`
  - No login shell
  - Home: `/var/lib/aegis`
- Admin user `finnoybu` is a member of `aegis`

### Directory Layout
| Path | Purpose |
|-----|--------|
| `/opt/aegis` | Code / runtime (future) |
| `/var/lib/aegis` | State |
| `/var/log/aegis` | Logs |
| `/etc/aegis` | Configuration |

Permissions:
- Owner: `aegis:aegis`
- Mode: `750`

Guardrails documented in `/etc/aegis/README.guardrails`.

---

## Phase A — Storage Prep (Pre‑ZFS)

### Disks Identified

**HDDs (1TB):**
- sda — ST31000340NS (512B sectors)
- sdb — WD10EZEX (4096B sectors)
- sdc — ST31000340NS (512B sectors)
- sde — WD10EACS (512B sectors)
- sdf — WD10EAVS (512B sectors)
- sdg — WD10EADS (4096B sectors)

**SSDs (1TB):**
- sdd — Crucial MX500 (OS disk)
- sdh — Crucial MX500 (unused / reserved)

### Sector Size Note
Mixed physical sector sizes detected.
**All future ZFS pools must be created with `ashift=12`.**

### Disk State
- All HDDs re‑labeled with GPT
- No partitions created
- No filesystems created
- No ZFS pools created

---

## Network Notes
- DHCP reservation on EdgeRouter
- Static DNS mapping: `aegis-lab → 192.168.1.215`
- SSH verified via IP
- Browser access intentionally disabled (no web services)

---

## Status
This configuration represents a **stable baseline checkpoint**.
All subsequent capability additions must reference this document.
