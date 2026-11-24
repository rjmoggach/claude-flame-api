# class `flame.PyImageNode`(PyActionFamilyNode)

> **2027 additions not shown below.** Autodesk's published pydoc predates some Flame 2027 API changes. New/renamed/deprecated members for this class (or its bases) are in What's New: [PyNode](../../guides/whats-new-2027.md#pynode), [PyActionFamilyNode](../../guides/whats-new-2027.md#pyactionfamilynode). Treat those as authoritative where they differ.

Class derived from PyActionFamilyNode. Represents an Image node object.

**Method resolution order:** PyImageNode → PyActionFamilyNode → PyNode → PyFlameObject

> Cannot be instantiated from Python (obtained from other API objects).

## Methods

### `add_media`

```python
add_media( (PyActionFamilyNode)arg1) -> object
```

Add a Media layer to the Batch Image node.

## Read-only properties defined here

### `media_nodes`

Return a list of the Media nodes attached to the Image node.

## Inherited members

- **Static methods inherited from PyActionFamilyNode:** `clear_schematic`, `connect_nodes`, `create_node`, `disconnect_nodes`, `encompass_nodes`, `get_node`, `organize`
- **Read-only properties inherited from PyActionFamilyNode:** `all_tabs`, `cursor_position`, `left_tabs`, `media_layers`, `node_types`, `nodes`, `right_tabs`
- **Static methods inherited from PyNode:** `delete`, `duplicate`, `load_node_setup`, `save_node_setup`, `set_context`
- **Read-only properties inherited from PyNode:** `input_sockets`, `output_sockets`, `sockets`
- **Read-only properties inherited from PyFlameObject:** `attributes`, `parent`
