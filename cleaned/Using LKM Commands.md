# Kernel Module Management Commands

### Concept
Linux provides a suite of tools for interacting with kernel modules, allowing users to load, unload, and query information about drivers at runtime.

### Key Points
- **lsmod**: Lists all currently loaded modules. It reads information from `/proc/modules`.
- **insmod**: A low-level tool to insert a module into the kernel. Requires the full path to the `.ko` file.
- **modprobe**: The preferred high-level tool for loading and unloading modules. It automatically resolves dependencies using `modules.dep`.
- **rmmod**: Removes a module from the kernel. Fails if the module is in use.
- **modinfo**: Displays metadata for a module, including its description, author, license, and parameters.
- **depmod**: Analyzes all modules in `/lib/modules/$(uname -r)` and generates dependency files.

![Modinfo Command Output](../files/019dd79b-54b0-7371-85ea-9994f19caadb/image.png)

### Example
**Handling Module Dependencies:**
```bash
sudo modprobe macvtap         # Automatically loads macvtap and its dependencies
modinfo macvtap               # Check what other modules it depends on
```

**Force Removing a Module (Dangerous):**
```bash
sudo rmmod -f <module_name>   # Use with extreme caution; can cause kernel panics
```

### Notes / Observations
- **Usage Count**: `lsmod` shows a "Used by" count. A module with a non-zero count cannot be removed by `rmmod` without forcing.
- **Modprobe vs Insmod**: Always prefer `modprobe` for daily use; `insmod` is primarily used during development.

![Modprobe and Dependency Resolution](../files/019dd7be-47ff-765c-b4e1-4837bd93fa71/image.png)

### Questions
- How does `modprobe` handle module parameters defined in `/etc/modprobe.d/`?
- What is the difference between `modprobe -r` and `rmmod`?
