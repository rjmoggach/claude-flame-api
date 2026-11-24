# class `flame.PyOFXNode`(PyNode)

> **2027 additions not shown below.** Autodesk's published pydoc predates some Flame 2027 API changes. New/renamed/deprecated members for this class (or its bases) are in What's New: [PyNode](../../guides/whats-new-2027.md#pynode). Treat those as authoritative where they differ.

Object representing a OpenFX node.

**Method resolution order:** PyOFXNode → PyNode → PyFlameObject

> Cannot be instantiated from Python (obtained from other API objects).

## Methods

### `change_plugin`

```python
change_plugin( (PyOFXNode)arg1, (str)plugin_name) -> bool
```

Change the active plugin for the openFX node

## Inherited members

- **Static methods inherited from PyNode:** `delete`, `duplicate`, `load_node_setup`, `save_node_setup`, `set_context`
- **Read-only properties inherited from PyNode:** `input_sockets`, `output_sockets`, `sockets`
- **Read-only properties inherited from PyFlameObject:** `attributes`, `parent`

## Attributes (documented values)

Source: "PyOFXNode Attributes" help page. Access via `obj.<attr>`; most return a `PyAttribute` — use `.get_value()` / `.set_value()` (see PyAttribute.md).

#### `pos_x (type 'int')`

The x position of a node in the Batch schematic.

Value range:

- Min: -2147483647
- Max: 2147483647

#### `pos_y (type 'int')`

The y position of a node in the Batch schematic.

Value range:

- Min: -2147483647
- Max: 2147483647

#### `name (type 'str')`

The name of the node in the Batch schematic.

Value range: None

#### `collapsed (type 'bool')`

The collapsed status of a node in the Batch schematic.

Value range:

- True
- False

#### `note (type 'str')`

The Node's note.

Value range: None

#### `note_collapsed (type 'bool')`

The collapsed status of a note in the Batch schematic.

Value range:

- True
- False

#### `selected (type 'bool')`

Select a Node in the Batch schematic.

Value range:

- True
- False

#### `type (type 'str')`

Return the type of the node.

Value range: None

#### `bypass (type 'bool')`

The bypass status of a node.

Value range:

- True
- False

#### `plugin_name (type 'str')`

Return the name of the node's active plugin.

Value range: None

#### `preserve_input_colour_space (type 'bool')`

The status of the Preserve Input Colour Space setting.

Value range:

- True
- False
