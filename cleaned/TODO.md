# Project TODO List

## Core Architecture
- [ ] Document the `rest_init()` sequence and the creation of the idle process (PID 0).
- [ ] Detail the `bzImage` segment splitting for legacy BIOS memory constraints.
- [ ] Document the `vDSO` (virtual Dynamic Shared Object) mechanism for high-frequency syscalls like `gettimeofday`.
- [ ] Map syscall argument registers for ARM64 and RISC-V architectures.
- [ ] Explain the `inode` and `dentry` structures within the VFS layer.

## Subsystems and Drivers
- [ ] Document the `debugfs` and `tracefs` filesystems used for kernel debugging.
- [ ] Document `loglevel` configurations in `/proc/sys/kernel/printk`.
- [ ] Research the `netconsole` module for sending kernel logs over the network.
- [ ] Research the `mknod` system call implementation.
- [ ] Document the role of `Major 8` specifically for SCSI/SATA disk drivers.
- [ ] Document the `uevent` mechanism used for notifying user space of hardware changes.
- [ ] Add a section on `UIO` (Userspace I/O) for high-speed hardware access.

## Boot and Modules
- [ ] Document the `kexec` mechanism for booting a new kernel without a full hardware reset.
- [ ] Detail the directory structure and contents of a typical `initramfs` image.
- [ ] Document the `vermagic` string used to enforce version compatibility.
- [ ] Research the `MODULE_LICENSE` macro and its impact on symbol visibility (`EXPORT_SYMBOL_GPL`).
- [ ] Document the use of `Kbuild` files vs. traditional `Makefiles`.
- [ ] Explain the role of `Module.symvers` in the build process.
- [ ] Document the `blacklisting` mechanism in `modprobe.d`.
- [ ] Research the `try_module_get` and `module_put` functions in kernel source.
- [ ] Document the format of the `modules.dep.bin` binary file.
- [ ] Explain the role of `symbol versioning` (`CONFIG_MODVERSIONS`).

## Build and Tools
- [ ] Detail the differences between `make all`, `make bzImage`, and `make modules`.
- [ ] Document the `System.map` file and its role in kernel debugging.
- [ ] Create a comprehensive map of the `arch/x86` directory.
- [ ] Document the use of `scripts/config` for command-line configuration editing.
- [ ] Compare `make allyesconfig` vs `make allmodconfig` for testing purposes.
- [ ] Document the `randstruct` plugin and its impact on build reproducibility.
- [ ] Document the use of `make oldconfig` for updating a `.config` from an older kernel version.
- [ ] Research the `LOCALVERSION` string for uniquely identifying custom builds.
- [ ] Document the use of `-f` to trace child processes spawned by `fork`.
- [ ] Research `ltrace` for tracing library calls instead of system calls.

## Practical Challenges
- [ ] Create a script to automate the extraction of vendor information from `sysfs`.
- [ ] Document the `debugfs` mount process if `/sys/kernel/debug` is empty.
