# Usage of Strace

### Concept
`strace` is a diagnostic, debugging, and instructional user-space utility for Linux. It is used to monitor and record the system calls made by a process and the signals it receives.

### Key Points
- **System Call Interception**: `strace` intercepts syscalls before they enter the kernel, allowing you to see arguments and return values.
- **Filtering**: You can filter for specific syscalls (e.g., `-e open,read`) to reduce output noise.
- **Output Redirection**: Syscall logs are sent to `stderr` by default; use `-o` to save to a file.
- **Process Attachment**: You can trace an already running process by specifying its PID with `-p`.

### Example
**Summarizing Syscall Activity:**
```bash
strace -c date
# Shows a table of syscalls, counts, and time spent.
```

**Tracing File Redirection:**
To see which process opens `/dev/null` during `date > /dev/null`:
```bash
strace -f -o trace.out bash -c 'date > /dev/null'
grep "/dev/null" trace.out
# Reveals that the shell (bash) performs the open() call before executing 'date'.
```

### Notes / Observations
- **Performance Impact**: `strace` significantly slows down the traced process because it triggers a context switch for every syscall.
- **Tracing Built-ins**: Since `cd` is a shell built-in, you must trace the shell itself: `strace bash -c 'cd /tmp'`.
- **Interpreting Return Values**: `strace` decodes return values into human-readable strings.

### Questions
- How does the `ptrace` system call enable `strace` to intercept execution?
- What are the security implications of using `strace` on a setuid binary?
