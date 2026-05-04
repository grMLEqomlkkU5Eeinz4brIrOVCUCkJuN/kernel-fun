# System Calls (Syscalls)

### Concept
System calls are the standardized interface through which user-space programs request services from the Linux kernel. They transition the CPU from restricted user mode to privileged kernel mode to perform tasks like file operations, process creation, and network communication.

### Key Points
- **Standard Interface**: Approximately 550 system calls exist in the modern Linux kernel.
- **UAPI (User API)**: Headers like `include/uapi/asm-generic/unistd.h` define syscall numbers. Architecture-independent mappings (e.g., `read` mapped to 63) aim for cross-architecture consistency.
- **Invocation**:
    - Performed via the `syscall` instruction on x86-64.
    - Parameters are passed via registers (e.g., `rax` for syscall number, `rdi`, `rsi`, `rdx` for arguments).
- **Libc Wrapper**: The C standard library (glibc) provides high-level functions (e.g., `printf()`) that translate to one or more raw syscalls (e.g., `write`).
- **Return Values**: Success returns a result (often 0 or a count); negative return values indicate errors, which `libc` maps to the global `errno` variable.

### Example
**Syscall Execution (sys_write) via Registers:**
| Register | Purpose | Value |
| --- | --- | --- |
| `rax` | Syscall Number | 1 (`sys_write`) |
| `rdi` | File Descriptor | 1 (`stdout`) |
| `rsi` | Buffer Address | Pointer to "Hello" |
| `rdx` | Length | 5 |

**Tracing Syscalls:**
```bash
strace -c date    # Summary of syscalls used by 'date'
strace -p <pid>   # Trace a running process
```

### Notes / Observations
- **Architecture Differences**: Syscall numbers vary by architecture. For example, `read` is syscall 0 on x86-64 but 63 in the generic `asm-generic` mapping.
- **Errno**: If a syscall fails, the kernel returns a negative error code (e.g., `-EACCES`). `libc` sets `errno` to the positive equivalent (`13`) and returns `-1` to the caller.
- **Tracing Built-ins**: `strace` cannot trace shell built-ins like `cd` directly; you must trace the shell itself (`strace bash -c 'cd /tmp'`).

### Questions
- How does the kernel validate the safety of pointers passed as syscall arguments to prevent kernel memory corruption?
- What is the overhead difference between the `syscall` instruction and older methods like `int 0x80`?
