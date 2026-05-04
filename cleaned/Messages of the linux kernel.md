# Kernel Messaging and Logging

### Concept
The kernel provides mechanisms for code to output informational and debugging messages. These messages are stored in a ring buffer in RAM and can be viewed or logged by user-space daemons.

![Kernel Log Levels](../src/files/019d84e9-a860-73fe-9339-f2a4d8e23481/image.png)

### Key Points
- **printk()**: The primary internal kernel function for generating messages. It is the kernel-space equivalent of `printf()`.
- **Kernel Ring Buffer**: A fixed-size RAM buffer that stores `printk` output. This ensures logging is available even if the disk is unavailable.

![Kernel Ring Buffer Overwrites](../src/files/019d84e6-1219-77db-bb8c-493d50a1467a/image.png)

- **Viewing Messages**:
    - **dmesg**: Command to display the contents of the kernel ring buffer.
    - **/proc/kmsg**: A virtual file that provides a stream of kernel messages.
- **Logging Daemons**: Modern systems use `journald` or `syslogd` to capture these messages and store them persistently.
- **Log Levels**: Important messages (e.g., kernel panics) are often mirrored to the system console depending on configuration.

### Example
**Viewing Kernel Logs:**
```bash
dmesg | tail                  # View the last 10 kernel messages
journalctl -k -f              # Follow kernel logs in real-time
```

### Notes / Observations
- **dmesg -w**: Follows the ring buffer, similar to `tail -f`.
- **Buffer Overwrites**: Because it is a ring buffer, older messages are overwritten when the buffer fills.
- **Early Boot**: Kernel messages are critical for debugging boot failures before the root filesystem is mounted.

![Systemd-journald and Kernel Logging](../src/files/019d84eb-b428-7166-8dd8-52f4275ca1f3/image.png)

### Questions
- How can the size of the kernel ring buffer be adjusted via boot parameters?
- What is the impact of high-frequency `printk` calls on system performance?
