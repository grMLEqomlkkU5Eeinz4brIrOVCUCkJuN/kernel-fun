# Hardware Discovery and Control

### Concept
The Linux kernel is responsible for detecting hardware, loading appropriate drivers, and providing interfaces for both monitoring and control. Discovery occurs during boot and dynamically when devices are hot-plugged.

![Hardware Hierarchy Overview](../files/019d7f3e-39f8-75b0-9cde-319367991520/image.png)

### Key Points
- **Discovery Tools**:
    - `lshw`: Comprehensive hardware list.
    - `lspci`: Lists all PCI/PCIe devices.
    - `lsusb`: Lists all USB devices.
    - `lsblk`: Displays block device hierarchy.
    - `lscpu`: Detailed CPU architecture information.
- **Hardware Control**:
    - **Sysfs/Procfs**: Writing to specific virtual files (e.g., `echo` to a brightness file).
    - **I/O Ports**: Direct hardware communication via `inb` and `outb` (highly restricted).
    - **Specialized Utilities**: Tools like `hdparm` for disk parameters or `setpci` for PCI configuration.

### Example
**Inspecting Disk Information:**
```bash
sudo hdparm -I /dev/sda       # View detailed hardware identity and capabilities
lsblk -t                      # View block devices with topology info
```

### Notes / Observations
- **User-space vs Kernel-space Drivers**: Most hardware is managed by kernel modules, but some (like FUSE filesystems or certain USB devices via `libusb`) operate in user space for safety or flexibility.
- **Loop Devices**: Frequently used for mounting ISO images or container filesystems.
- **I/O vs Info**: `/dev` nodes are used for actual data transfer (I/O), while `/sys` entries are used to query or modify device metadata and state.

![Disk Identification and Control](../files/019d7f45-fcd6-700f-8a02-fb790515626e/image.png)

### Questions
- How does `udev` decide which driver to associate with a newly discovered VendorID/ProductID?
- What are the performance penalties for user-space drivers compared to kernel-level drivers?
