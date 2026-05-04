# Virtual File System (VFS) and Kernel Interfaces

### Concept
The Virtual File System (VFS) is a kernel abstraction layer that allows user space to interact with various data sources (physical disks, network protocols, or kernel state) using standard file I/O system calls. Virtual filesystems like `/proc` and `/sys` generate their content dynamically in RAM when accessed.

![VFS and Process Information](../files/019d84ad-e05e-731a-8a9e-789038a3b0eb/image.png)

### Key Points
- **/proc (procfs)**:
    - Focuses on process and kernel state information.
    - Each process has a directory at `/proc/<pid>/` containing memory maps, file descriptors, and status.
    - System-wide info includes `/proc/cpuinfo`, `/proc/meminfo`, and `/proc/cmdline`.
- **/sys (sysfs)**:
    - Provides a structured view of the kernel's device model (buses, devices, drivers).
    - Used for both viewing information and configuring hardware.
    - Key paths: `/sys/class/` (device types), `/sys/bus/` (PCI/USB/etc), `/sys/devices/` (physical hierarchy).
- **/dev (devtmpfs)**:
    - Contains device nodes representing hardware (e.g., `/dev/sda`) or virtual devices (`/dev/null`).
    - Character devices (tty, random) vs. Block devices (disks).
- **Dynamic Content**: Files are synthesized on the fly by kernel functions, ensuring data is always current.

### Example
**Interacting with VFS:**
```bash
cat /proc/meminfo             # View system memory usage
cat /sys/block/sda/size       # Check disk size in sectors
ls /proc/self/fd              # List open file descriptors of the current shell
echo 1 > /sys/class/backlight/intel_backlight/brightness  # Adjust hardware state
```

### Notes / Observations
- **/proc/sys**: A specific subtree for tuning kernel parameters (sysctl) at runtime.
- **Device Nodes**: Major numbers identify the driver; Minor numbers identify the specific instance or partition.
- **Safety**: Do not write to files in `/dev` unless their function is known (e.g., `dd` to a disk node can destroy data).
- **VFS Abstraction**: The kernel translates generic calls (`read()`) into filesystem-specific or driver-specific operations.

![Sysfs Hierarchy and Device Links](../files/019d84f1-220c-746e-9ee8-31d1cb06ab73/image.png)

### Questions
- What are the technical differences between `ramfs`, `tmpfs`, and the mechanisms used by `procfs`?
- How does `udev` manage the dynamic creation of entries in `/dev` upon hardware discovery?
