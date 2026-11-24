# class `flame.PyMorphNode`(PyNode)

> **2027 additions not shown below.** Autodesk's published pydoc predates some Flame 2027 API changes. New/renamed/deprecated members for this class (or its bases) are in What's New: [PyNode](../../guides/whats-new-2027.md#pynode). Treat those as authoritative where they differ.

Object representing a Morph node.

**Method resolution order:** PyMorphNode → PyNode → PyFlameObject

> Cannot be instantiated from Python (obtained from other API objects).

## Methods

### `set_mix_to_range`

```python
set_mix_to_range( (PyMorphNode)arg1) -> None
```

Move the first and last keyframes of the mix curve to the range's first and last frame.

## Inherited members

- **Static methods inherited from PyNode:** `delete`, `duplicate`, `load_node_setup`, `save_node_setup`, `set_context`
- **Read-only properties inherited from PyNode:** `input_sockets`, `output_sockets`, `sockets`
- **Read-only properties inherited from PyFlameObject:** `attributes`, `parent`
