# Firmware / BIOS Configuration

## Boot Mode
- UEFI: Enabled
- Legacy / CSM: Disabled
- Secure Boot: Disabled

## SATA Configuration
- Controller Mode: AHCI
- RAID / RST / VMD: Disabled
- Aggressive LPM: Disabled
- SATA HDD Unlock: Enabled

## SATA Port Usage (X11DAi-N)
- SATA1–SATA8 (Black ports): Used
- SATA9–SATA10 (sSATA / Orange): Unused

## Video OPROM
- Onboard Video OPROM: UEFI
- PCIe Slot OPROMs: EFI / UEFI

## Rationale
- Ensures clean UEFI-only boot path
- Avoids RAID metadata conflicts
- Prevents partial disk enumeration issues seen with sSATA
