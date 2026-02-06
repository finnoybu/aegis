← [Back to docs README](README.md)

# Post-Install Validation

## Disk Enumeration
- lsblk confirms:
  - 2 × SSDs visible
  - 6 × HDDs visible
  - No unexpected devices

## SMART Health
- Command used:
  smartctl -H /dev/sdX

- Result:
  - All HDDs: PASSED
  - SSDs: No errors reported

## Kernel Errors
- dmesg scan for error/reset/timeout:
  - No relevant errors present

## System Health
- Stable boot
- No audible disk issues
- Clean UEFI boot path