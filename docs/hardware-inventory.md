# Hardware Inventory

## System Overview
- Purpose: Aegis development & controlled testing lab
- Platform: Bare metal (no hypervisor)
- OS: Debian 12 (Bookworm)

## Motherboard
- Manufacturer: Supermicro
- Model: X11DAi-N
- Revision: 1.10
- BIOS Date: 2023-01-12

## CPU
- 2 × Intel Xeon Silver 4116
- Architecture: x86_64 (Skylake-SP)
- Cores: 12 per CPU (24 total)
- Threads: 48 total
- NUMA Nodes: 2 (balanced)

## Memory
- Total RAM: 256 GB
- Configuration: Evenly distributed across NUMA nodes
- Mode: Multi-channel (optimal bandwidth)

## GPUs
- AMD Radeon RX 450 / RX 560-class (Polaris)
  - Role: Console / display
- NVIDIA GeForce RTX 5060 Ti
  - Architecture: Blackwell
  - VRAM: 16 GB
  - Role: Future AI compute

## Storage Devices
### SSDs
- 2 × Crucial MX500 1TB SATA SSD
  - Role: OS + Aegis runtime

### HDDs
- 6 × 1TB SATA HDDs (mixed Seagate / Western Digital)
  - Role: Future bulk storage (ZFS planned)
