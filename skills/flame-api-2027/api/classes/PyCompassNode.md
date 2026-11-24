# class `flame.PyCompassNode`(PyNode)

> **2027 additions not shown below.** Autodesk's published pydoc predates some Flame 2027 API changes. New/renamed/deprecated members for this class (or its bases) are in What's New: [PyNode](../../guides/whats-new-2027.md#pynode). Treat those as authoritative where they differ.

Class derived from PyNode. This class represents a Compass node.

**Method resolution order:** PyCompassNode → PyNode → PyFlameObject

> Cannot be instantiated from Python (obtained from other API objects).

## Methods

## Read-only properties defined here

### `nodes`

Return a list of PyNode objects enclosed by the Compass node.

## Inherited members

- **Static methods inherited from PyNode:** `delete`, `duplicate`, `load_node_setup`, `save_node_setup`, `set_context`
- **Read-only properties inherited from PyNode:** `input_sockets`, `output_sockets`, `sockets`
- **Read-only properties inherited from PyFlameObject:** `attributes`, `parent`

## Attributes (documented values)

Source: "PyCompassNode Attributes" help page. Access via `obj.<attr>`; most return a `PyAttribute` — use `.get_value()` / `.set_value()` (see PyAttribute.md).

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

#### `collapsed (type 'bool')`

The collapsed status of a node in the Batch schematic.

Value range:

- True
- False

#### `note (type 'str')`

The Node's note.

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

#### `width (type 'int')`

The width attribute of the Compass node.

Value range:

- Min: 200
- Max: 2147483647

#### `height (type 'int')`

The height attribute of the Compass node.

Value range:

- Min: 200
- Max: 2147483647

#### `colour (type 'tuple')`

The Colour attribute of the Compass node.

Value range:

- (0.0, 0.0, 0.0)
- (1.0, 1.0, 1.0)
