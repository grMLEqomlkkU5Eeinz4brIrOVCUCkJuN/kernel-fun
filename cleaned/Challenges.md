# Kernel and Module Challenges

### Concept
A collection of practical tasks designed to reinforce understanding of kernel threads, module management, and virtual filesystem interaction.

### Challenge: Investigating Kernel Threads (kworkers)
- **Task**: Identify what various `kworker` threads are doing.
- **Insight**: `kworker` threads are managed by kernel workqueues for asynchronous execution.
- **Method**: Use `ftrace` to trace workqueue events.
    ```bash
    echo workqueue:workqueue_queue_work > /sys/kernel/debug/tracing/set_event
    cat /sys/kernel/debug/tracing/trace_pipe | grep kworker
    ```
- **Security Note**: Grub interruption can be exploited to gain root access if the bootloader is not password-protected.

![Kernel Thread Status Output](../files/019dae5c-93a8-764a-a8f6-221d6ea61b7b/image.png)

### Challenge: Kernel Module Inventory
- **Task**: Analyze the number and source of loaded modules.
- **Observations**:
    - `lsmod | wc -l`: Count currently loaded modules (subtract 1 for header).
    - Modules can be loaded from the `initramfs` during early boot.
- **Dependency Matching**: `modules.dep` should match the number of installed modules 1:1.

![Lsmod and Module Inventory](../files/019dd7be-ff3a-73f9-b23b-29fc1477a34b/image.png)

### Challenge: Sysfs Interaction
- **Task**: Locate hardware information via `sysfs`.
- **Findings**:
    - `/sys/class/dmi/id/vendor`: Used to find the motherboard/system vendor.
    - `/sys/block/*/slaves`: Shows relationship between block devices.

![Sysfs Vendor Identification](../files/019d84ed-86af-703f-a960-87ccd1aa5ea9/image.png)

### Challenge: Dmesg and Command Line
- **Task**: Retrieve boot-time parameters.
- **Command**: `cat /proc/cmdline`.

![Proc Cmdline Output](../files/019d84dd-bc97-70bc-a81b-2dead84cfe66/image.png)

### Questions
- Why do some `kworker` threads consume more CPU than others during high I/O wait?
- How does the kernel ensure that `sysfs` links remain consistent when hardware is hot-unplugged?
