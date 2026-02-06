← [Back to docs README](README.md)

# Storage Layout

## SSD Layout (Primary OS Disk)
- Disk: Crucial MX500 1TB
- Partition Table: GPT

### Partitions
1. EFI System Partition
   - Size: ~512 MB
   - Filesystem: FAT32
   - Mount: /boot/efi

2. Root Filesystem
   - Size: Remainder of disk (~931 GB)
   - Filesystem: ext4
   - Mount: /

## Secondary SSD
- Present but unused
- Reserved for future RAID1 mirroring or failover

## HDDs
- All HDDs wiped during installation
- No filesystems created
- No mount points assigned
- Reserved for future ZFS pool creation

## Explicitly Deferred
- ZFS pool creation
- RAID/mirroring on HDDs
- Any data ingestion