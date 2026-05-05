# Compiling Kernel Modules

### Concept
Compiling a Linux kernel module involves using the kernel's build system (**Kbuild**) to create a `.ko` file. This process requires the module source code to be compiled against the headers and configuration of the target kernel.

![Module Build Environment](../src/files/019dd7f7-30c5-736b-aa3a-af1a9b919b7b/image.png)

### Key Points
- **Kbuild System**:
    - Unlike traditional Makefiles that contain explicit compilation rules, **Kbuild** files are declarative.
    - You define what to build using variables like `obj-m` (for modules) or `obj-y` (for built-in code).
- **Module.symvers**:
    - A file generated during the kernel build that lists all exported symbols and their CRC checksums.
    - Essential for building out-of-tree modules to verify ABI compatibility with the target kernel.
- **Build Directory**: The standard path for kernel build files is `/lib/modules/$(uname -r)/build`.
- **Compiler Consistency**: Modules must be compiled using the same compiler version and flags as the kernel to ensure structure alignment and binary stability.

![Module Compilation Object Files](../src/files/019ddbff-21ad-7144-96ac-ac67098ce5b2/image.png)

### Example
**Declarative Kbuild / Makefile:**
```makefile
obj-m += mymodule.o

all:
	# -C switches to the kernel source directory to use its Kbuild infrastructure
	make -C /lib/modules/$(uname -r)/build M=$(PWD) modules

clean:
	make -C /lib/modules/$(uname -r)/build M=$(PWD) clean
```

### Notes / Observations
- **M=$(PWD)**: This variable tells the kernel Makefile where your external module source is located.
- **Symbol Check**: During compilation, the build system checks for symbol dependencies against `Module.symvers`.
- **obj-m vs obj-y**: `obj-m` builds a loadable module (`.ko`); `obj-y` builds the code statically into the kernel image (`vmlinuz`).

### Questions
- What are the implications of the `__init` and `__exit` macros on memory management?
- How does the kernel build system handle modules consisting of multiple source files?
