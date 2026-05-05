# Project TODO List

## Core Architecture
- [x] Document the `rest_init()` sequence and the creation of the idle process (PID 0).
- [x] Detail the `bzImage` segment splitting for legacy BIOS memory constraints.
- [x] Document the `vDSO` (virtual Dynamic Shared Object) mechanism for high-frequency syscalls like `gettimeofday`.
- [x] Map syscall argument registers for ARM64 and RISC-V architectures.
- [x] Explain the `inode` and `dentry` structures within the VFS layer.

## Subsystems and Drivers
- [x] Document the `debugfs` and `tracefs` filesystems used for kernel debugging.
- [x] Document `loglevel` configurations in `/proc/sys/kernel/printk`.
- [x] Research the `netconsole` module for sending kernel logs over the network.
- [x] Research the `mknod` system call implementation.
- [x] Document the role of `Major 8` specifically for SCSI/SATA disk drivers.
- [x] Document the `uevent` mechanism used for notifying user space of hardware changes.
- [x] Add a section on `UIO` (Userspace I/O) for high-speed hardware access.

## Boot and Modules
- [x] Document the `kexec` mechanism for booting a new kernel without a full hardware reset.
- [x] Detail the directory structure and contents of a typical `initramfs` image.
- [x] Document the `vermagic` string used to enforce version compatibility.
- [x] Research the `MODULE_LICENSE` macro and its impact on symbol visibility (`EXPORT_SYMBOL_GPL`).
- [x] Document the use of `Kbuild` files vs. traditional `Makefiles`.
- [x] Explain the role of `Module.symvers` in the build process.
- [x] Document the `blacklisting` mechanism in `modprobe.d`.
- [x] Research the `try_module_get` and `module_put` functions in kernel source.
- [x] Document the format of the `modules.dep.bin` binary file.
- [x] Explain the role of `symbol versioning` (`CONFIG_MODVERSIONS`).

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
