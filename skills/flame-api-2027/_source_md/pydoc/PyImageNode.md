# class `flame.PyImageNode`(PyActionFamilyNode)

Class derived from PyActionFamilyNode. Represents an Image node object.

**Method resolution order:** PyImageNode → PyActionFamilyNode → PyNode → PyFlameObject

## Methods

> Cannot be instantiated from Python (obtained from other API objects).

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
