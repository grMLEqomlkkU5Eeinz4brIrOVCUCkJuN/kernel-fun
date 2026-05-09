# Recommended Reading Order

This guide organizes the notes into a logical learning path. Each phase builds on concepts from the previous one.

---

## Phase 1: Foundations

Establishes what the kernel is, how it communicates with user space, and the virtual filesystems that expose kernel state.

| # | File | Covers |
|---|------|--------|
| 1 | [The Linux kernel: what it actually is and what it does](The%20Linux%20kernel%3A%20what%20it%20actually%20is%20and%20what%20it%20does.md) | Kernel binary, Ring 0/3 privilege model, `rest_init` sequence, PID 0/1/2, `bzImage` format |
| 2 | [Systemcalls](Systemcalls.md) | Syscall interface, registers per architecture, vDSO, libc wrappers, errno |
| 3 | [Virtual File System](Virtual%20File%20System.md) | VFS abstraction, inodes, dentries, `/proc`, `/sys`, `/dev` |

**Why this order:** You need to understand what the kernel is (1) before you can understand how user space talks to it (2), and how the kernel exposes its internal state through virtual filesystems (3).

---

## Phase 2: Boot Process and Hardware

Covers how the kernel gets loaded, how it discovers hardware, and how device files bridge drivers to user space.

| # | File | Covers |
|---|------|--------|
| 4 | [GRUB and the bootloaders](GRUB%20and%20the%20bootloaders.md) | GRUB, initramfs structure, kexec, boot execution flow |
| 5 | [Hardware discovery and control](Hardware%20discovery%20and%20control%20in%20the%20linux%20kernel.md) | lspci/lsusb, uevent mechanism, udev, UIO framework |
| 6 | [Device file](Device%20file.md) | Device nodes, major/minor numbers, mknod, devtmpfs, block vs character devices |

**Why this order:** GRUB loads the kernel (4), the kernel discovers hardware (5), and device files are the user-space interface to that hardware (6). Device files also depend on VFS concepts from Phase 1.

---

## Phase 3: Kernel Modules

Covers the modular driver system from theory through practical usage.

| # | File | Covers |
|---|------|--------|
| 7 | [Loadable Kernel Modules](Loadable%20Kernel%20Modules.md) | LKM concepts, vermagic, symbol versioning, MODULE_LICENSE, reference counting, blacklisting |
| 8 | [Using LKM Commands](Using%20LKM%20Commands.md) | lsmod, insmod, modprobe, rmmod, modinfo, depmod |
| 9 | [LKM deps](LKM%20deps.md) | EXPORT_SYMBOL, modules.dep, dependency resolution, loading order |
| 10 | [Messages of the linux kernel](Messages%20of%20the%20linux%20kernel.md) | printk, ring buffer, log levels, debugfs, tracefs, netconsole |

**Why this order:** Understand module theory (7), then the commands to manage them (8), then how dependencies between modules work (9). Kernel messaging (10) is placed here because `printk` is how modules produce output, and debugfs/tracefs are how you observe module and kernel behavior.

---

## Phase 4: Building the Kernel

Covers the source tree, configuration, compilation, and installation.

| # | File | Covers |
|---|------|--------|
| 11 | [Kernel sources](Kernel%20sources.md) | Source tree layout, `arch/x86` map, configuration tools, `make oldconfig`, `.config` file |
| 12 | [Make MenuConfig](Make%20MenuConfig.md) | menuconfig interface, `scripts/config`, allyesconfig vs allmodconfig, Kconfig dependencies |
| 13 | [Compiling modules](Compiling%20modules.md) | Kbuild system, Module.symvers, obj-m vs obj-y, out-of-tree builds |
| 14 | [Build and install kernel modules](Build%20and%20install%20kernel%20modules.md) | Build targets (`make all`/`bzImage`/`modules`), System.map, installation steps |
| 15 | [Manually Building kernels, extra info](Manually%20Building%20kernels%2C%20extra%20info.md) | localmodconfig, ccache, DKMS, LOCALVERSION, randstruct plugin |

**Why this order:** Navigate the source (11), configure it (12), understand how compilation works (13), perform the build and install (14), then optimize and customize (15). This phase assumes familiarity with modules from Phase 3.

---

## Phase 5: Debugging and Practice

Applies everything from previous phases to real debugging and hands-on challenges.

| # | File | Covers |
|---|------|--------|
| 16 | [Usage of Strace](Usage%20of%20Strace.md) | strace, `-f` for child processes, ltrace, ptrace mechanism |
| 17 | [Challenges](Challenges.md) | Kworker investigation, module inventory, sysfs vendor extraction script, dmesg |

**Why this order:** Strace (16) is the primary tool for observing syscall behavior covered in Phase 1. The challenges (17) are hands-on exercises that pull from every previous phase.

---

## Dependency Graph

```
Phase 1: Foundations
  [1] Kernel Overview
       |
  [2] Syscalls ---------> [16] Strace (Phase 5)
       |
  [3] VFS
       |
Phase 2: Boot & Hardware
  [4] GRUB/Boot
       |
  [5] Hardware Discovery
       |
  [6] Device Files
       |
Phase 3: Modules
  [7] LKM Theory
       |
  [8] LKM Commands
       |
  [9] LKM Dependencies
       |
  [10] Kernel Messaging
       |
Phase 4: Building
  [11] Kernel Sources
       |
  [12] MenuConfig
       |
  [13] Compiling Modules
       |
  [14] Build & Install
       |
  [15] Build Optimization
       |
Phase 5: Practice
  [16] Strace / Ltrace
       |
  [17] Challenges
```

---

## Quick Reference: File by Topic

| Topic | Files |
|-------|-------|
| "What is the kernel?" | 1 |
| Boot process | 1, 4 |
| Syscalls and tracing | 2, 16 |
| Virtual filesystems | 3, 6, 10 |
| Hardware and drivers | 5, 6 |
| Modules (theory) | 7, 9 |
| Modules (practical) | 8, 13, 14 |
| Kernel configuration | 11, 12, 15 |
| Debugging | 10, 16, 17 |
