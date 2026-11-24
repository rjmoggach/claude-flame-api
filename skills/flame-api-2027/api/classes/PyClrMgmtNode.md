# class `flame.PyClrMgmtNode`(PyNode)

> **2027 additions not shown below.** Autodesk's published pydoc predates some Flame 2027 API changes. New/renamed/deprecated members for this class (or its bases) are in What's New: [PyNode](../../guides/whats-new-2027.md#pynode). Treat those as authoritative where they differ.

Class derived from PyNode. This class represents a Colour Management node.

**Method resolution order:** PyClrMgmtNode → PyNode → PyFlameObject

> Cannot be instantiated from Python (obtained from other API objects).

## Methods

### `get_context_variables`

```python
get_context_variables( (PyClrMgmtNode)arg1) -> dict
```

Get the context variables in a dictionary.

### `import_transform`

```python
import_transform( (PyClrMgmtNode)arg1, (str)file_path) -> None
```

Used to import a CDL, CTF, LUT, or 3D LUT form a file.

### `reset_context_variables`

```python
reset_context_variables( (PyClrMgmtNode)arg1) -> None
```

Reset the context variables to their initial state from the OCIO config.

### `set_context_variable`

```python
set_context_variable( (PyClrMgmtNode)arg1, (str)name, (str)value) -> None
```

Set the value for the specified context variable.

## Inherited members

- **Static methods inherited from PyNode:** `clear_schematic_colour`, `delete`, `duplicate`, `load_node_setup`, `save_node_setup`, `set_context`
- **Read-only properties inherited from PyNode:** `colour_space`, `input_sockets`, `output_sockets`, `sockets`
- **Read-only properties inherited from PyFlameObject:** `attributes`, `parent`
