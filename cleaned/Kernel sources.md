# Kernel Source Tree and Configuration

### Concept
The Linux kernel source tree is organized into a strict directory structure that separates architecture-specific code from generic subsystems. Configuration tools allow developers to customize the kernel by selecting which features and drivers to include.

![Kernel Source Directory Structure](../files/019ddcdc-4828-7258-848b-a14dadfa34d8/image.png)

### Key Points
- **Source Structure**:
    - `arch/`: Architecture-specific code (x86, arm, riscv).
    - `drivers/`: The largest directory; contains all hardware driver source.
    - `include/`: Kernel header files.
    - `kernel/`: Core subsystems like the scheduler and signal handling.
    - `mm/`: Memory management code.
    - `net/`: Networking protocols.
- **Configuration Tools**:
    - `make menuconfig`: Ncurses-based menu for configuration.
    - `make localmodconfig`: Strips the config to only include currently loaded modules.
    - `make defconfig`: Generates a default config for the current architecture.
- **The .config File**: The resulting file that tells the build system what to compile as built-in (`y`), as a module (`m`), or not at all (`n`).

![Locating Drivers in Source](../files/019ddcf8-0927-75c5-8d70-7665148df7a6/image.png)

### Example
**Locating a Driver in Source:**
A Realtek ethernet driver might be located at:
`/usr/src/linux/drivers/net/ethernet/realtek/r8169.c`

**Trimming a Configuration:**
```bash
make localmodconfig           # Uses lsmod to disable unused drivers
```

### Notes / Observations
- **In-Tree vs Out-of-Tree**: Source for in-tree drivers is found directly in the `drivers/` directory.
- **Kconfig**: Files throughout the source tree that define the menu structure and dependencies for the configuration tools.
- **Distribution Configs**: Most users start by copying their current distribution's config from `/boot/config-$(uname -r)`.

![Kconfig and Build System Integration](../files/019ddd02-ac0d-7328-a42f-cf67875b05f2/image.png)

### Questions
- What is the difference between `make oldconfig` and `make olddefconfig`?
- How does the `Kbuild` system handle conditional compilation based on `.config` values?
