# The Linux Kernel: Definition and Core Functions

### Concept
The Linux kernel is a compiled binary that manages hardware resources and provides a execution environment for user-space applications. It operates in a privileged CPU mode (Ring 0), acting as the primary intermediary between hardware and software.

![Kernel Overview](../src/files/019d84a9-1a6c-773c-8bcf-56378a916228/image.png)

### Key Points
- **Binary Image**: Typically stored as `/boot/vmlinuz-<version>`. The `vmlinuz` name stands for "Virtual Memory Linux," with the `z` suffix indicating compression (e.g., gzip, lz4, zstd).
- **Initramfs / Initrd**: A temporary root filesystem loaded into RAM by the bootloader. It contains the essential drivers and tools required to mount the actual root filesystem.
- **Bootloader Handover**: The bootloader (GRUB, systemd-boot) loads the kernel and passes a **boot parameters** data structure (`arch/x86/include/uapi/asm/bootparam.h`) containing hardware info and command-line arguments.
- **Initialization Sequence (`rest_init`)**:
    - After `start_kernel()` finishes basic setup, it calls `rest_init()`.
    - **PID 1 (init)**: `rest_init` spawns the `kernel_init` thread, which eventually executes the user-space `init` process (e.g., systemd).
    - **PID 2 (kthreadd)**: Spawns the manager for all kernel threads.
    - **PID 0 (Idle Process)**: The original boot thread becomes the idle process (or `swapper`). It enters an infinite loop, executing architecture-specific idle logic when no other tasks are runnable.
- **Privilege Rings**: Linux utilizes a two-level privilege model:
    - **Ring 0 (Kernel Space)**: Full hardware access and unrestricted memory access.
    - **Ring 3 (User Space)**: Restricted access; must use system calls to interact with hardware or other processes.
- **The Kernel is Not a Process**: It is a standalone entity that manages the execution and scheduling of all processes.

![Ring Model and Context](../src/files/019d84aa-3195-7209-b82c-1331af3d383d/image.png)

### Example
**Checking Kernel Binary Type:**
```bash
file /boot/vmlinuz-$(uname -r)
# Output: Linux kernel x86 boot executable bzImage
```

**Viewing Kernel Command Line:**
```bash
cat /proc/cmdline
```

### Notes / Observations
- **bzImage and Legacy BIOS**: The "Big ZImage" format was designed to bypass the 640KB "low memory" limit of legacy BIOS.
    - **Setup Code**: Real-mode code loaded into low memory (below 1MB) to handle BIOS interactions.
    - **Protected-mode Kernel**: The compressed kernel image loaded into high memory (above 1MB).
- **Self-Decompression**: `bzImage` includes a decompressor stub that handles unpacking the kernel into RAM during boot.
- **Ring Transitions**: A user-space process attempting direct hardware access triggers a CPU fault, which the kernel intercepts (often resulting in a `SIGSEGV`).
- **PID 1 Persistence**: If the kernel fails to launch PID 1, it results in a "Kernel Panic," as the system has no way to enter user space.

![Capabilities and Permissions](../src/files/019d84ae-0fef-77cf-b982-c54daaf87eaa/image.png)
![Memory and VFS Introspection](../src/files/019d84aa-5b5c-7573-9657-4f920f6c6728/image.png)

### Questions
- How does the kernel transition from the architecture-specific assembly entry point to the generic C `start_kernel()` function?
- What are the implications of the "lazy allocation" strategy for real-time systems?
