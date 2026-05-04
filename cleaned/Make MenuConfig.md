# Kernel Configuration with Menuconfig

### Concept
`make menuconfig` is an ncurses-based graphical interface used to configure the Linux kernel. It allows developers to browse a hierarchical menu of all available kernel options, drivers, and subsystems, and decide how they should be compiled.

![Menuconfig Main Interface](../src/files/019ddd0e-8197-776c-ad5b-3fe99e28f511/image.png)

### Key Points
- **Configuration Types**:
    - `[*]` (Built-in): Compiled directly into the kernel image (`y`).
    - `<M>` (Module): Compiled as a loadable kernel module (`m`).
    - `[ ]` (Excluded): Feature not included in the build (`n`).
- **Searching**: Use the `/` key to search for specific symbols or hardware strings (e.g., `INTEL_IOMMU`).
- **Dependencies**: Some options are only visible if their parent dependencies are met (e.g., USB drivers require the USB support subsystem to be enabled).
- **Persistence**: Configuration is saved to the `.config` file in the root of the kernel source tree.

![Menuconfig Search and Dependencies](../src/files/019ddd12-99c6-77f6-a29a-0ab0bef5e61d/image.png)

### Example
**Launching Menuconfig:**
```bash
make menuconfig
```
**Searching for a symbol:**
Press `/`, type `NET_SCHED`, and press `Enter`. The output will show the location of the option in the menu hierarchy and any required dependencies.

### Notes / Observations
- **Required Libraries**: On Debian/Ubuntu, `libncurses5-dev` or `libncurses-dev` must be installed to run menuconfig.
- **Help Text**: Selecting an option and pressing `?` or `h` provides detailed documentation on what that specific feature does.
- **Load/Save**: You can load an existing `.config` file or save a custom configuration to a specific filename within the interface.

![Saving Kernel Configuration](../src/files/019ddd14-f152-7139-ad40-1aed0da3f212/image.png)

### Questions
- How does the `Kconfig` language define the relationship between mutually exclusive options?
- What are the advantages of `make nconfig` or `make xconfig` over `menuconfig`?
