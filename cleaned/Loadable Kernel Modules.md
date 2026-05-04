# Loadable Kernel Modules (LKM)

### Concept
Loadable Kernel Modules are object files containing code that can be dynamically loaded into or removed from the Linux kernel at runtime. This allows for a modular kernel that supports a wide range of hardware without requiring all drivers to be built into the core kernel binary.

![LKM Overview and Dynamic Loading](../src/files/019dae79-9d0a-737d-acbd-e4ef4d11ddde/image.png)

### Key Points
- **File Format**: LKMs use the `.ko` (kernel object) extension.
- **Privilege**: Modules execute in Ring 0 (kernel space) with full system access.
- **Lifecycle**:
    - **Initialization**: Managed by the `module_init()` macro.
    - **Cleanup**: Managed by the `module_exit()` macro.
- **Binary Compatibility**: Modules are strictly tied to a specific kernel version. A module compiled for kernel 6.1.x will likely not load on 6.2.x due to ABI/API changes.
- **In-Tree vs Out-of-Tree**:
    - **In-Tree**: Included in the main Linux kernel source.
    - **Out-of-Tree**: Third-party modules (e.g., NVIDIA drivers) maintained separately.

![Advantages of a Modular Kernel](../src/files/019dae7a-e21c-74d9-8233-1bf1ab3bf7a8/image.png)

### Example
**Listing Loaded Modules:**
```bash
lsmod                         # Lists name, size, and usage count
```

**Viewing Module Metadata:**
```bash
modinfo <module_name>         # Displays author, license, parameters, and dependencies
```

![Dynamic Linking and Symbol Resolution](../src/files/019dae7b-c91f-735f-bd52-61189b5955d5/image.png)

### Notes / Observations
- **No Standard C Library**: Modules cannot use `libc` (e.g., `printf`); they must use kernel equivalents like `printk`.
- **Memory Management**: Modules must carefully manage memory (e.g., `kmalloc`/`kfree`) as any leak or corruption can crash the entire system.
- **Binary Stability**: LKMs must be compiled against the specific kernel headers of the target system to ensure compatibility.

![Kernel Headers and Build Consistency](../src/files/019dae8f-d7cc-7170-8570-6aa264a2d4a4/image.png)

- **Symbol Resolution**: The kernel resolves symbols (functions/variables) when a module is loaded, similar to dynamic linking in user space.

![Symbol Resolution and Metadata](../src/files/019d84b1-08e3-75ff-ab46-b89f8c6a6ccb/image.png)

### Questions
- What are the security risks of allowing unsigned kernel modules to be loaded?
- How does the kernel handle circular dependencies between multiple modules?
