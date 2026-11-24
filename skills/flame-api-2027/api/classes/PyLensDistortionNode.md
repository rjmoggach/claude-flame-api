# class `flame.PyLensDistortionNode`(PyNode)

> **2027 additions not shown below.** Autodesk's published pydoc predates some Flame 2027 API changes. New/renamed/deprecated members for this class (or its bases) are in What's New: [PyNode](../../guides/whats-new-2027.md#pynode). Treat those as authoritative where they differ.

Object representing a Lens Distortion node.

**Method resolution order:** PyLensDistortionNode → PyNode → PyFlameObject

> Cannot be instantiated from Python (obtained from other API objects).

## Methods

### `calculate`

```python
calculate( (PyLensDistortionNodearg1) -> None
```

Calculate the amount of distortion based on the position of vertices.

### `import_lens_distortion`

```python
import_lens_distortion( (PyLensDistortionNode(str)filename) -> None
```

Import a Lens Distortion file.

## Inherited members

- **Static methods inherited from PyNode:** `delete`, `duplicate`, `load_node_setup`, `save_node_setup`, `set_context`
- **Read-only properties inherited from PyNode:** `input_sockets`, `output_sockets`, `sockets`
- **Read-only properties inherited from PyFlameObject:** `attributes`, `parent`

## Attributes (documented values)

Source: "PyLensDistortionNode Attributes" help page. Access via `obj.<attr>`; most return a `PyAttribute` — use `.get_value()` / `.set_value()` (see PyAttribute.md).

Use the following commands to set or get attributes for a Lens Distortion node.

| Command | Type | Description |
|---|---|---|
| `PyLensDistortionNode>.pos_x` | integer | The x position of a node in the Batch schematic.<br><br>An integer number must be passed when the attribute is set: • Min: -2147483647 • Max: 2147483647 |
| `PyLensDistortionNode>.pos_y` | integer | The y position of a node in the Batch schematic.<br><br>An integer number must be passed when the attribute is set: • Min: -2147483647 • Max: 2147483647 |
| `PyLensDistortionNode>.name` | string | Used to set or get name of the Batch node.<br><br>A string must be passed when the attribute is set. |
| `PyLensDistortionNode>.note` | string | Used to set or get the content of the note associated with the Batch node.<br><br>A string must be passed when the attribute is set. |
| `PyLensDistortionNode>.note_collapsed` | bool | Used to set or get the collapsed status of a note in the Batch schematic.<br><br>One of the following must be passed when the attribute is set: • True • False |
| `PyLensDistortionNode>.selected` | bool | Used to select or deselect a node in the Batch schematic.<br><br>One of the following must be passed when the attribute is set: • True • False |
| `PyLensDistortionNode>.type` | string | Return the type of the node. |
| `PyLensDistortionNode>.bypass` | bool | Used to set or get the bypass status of a node in the Batch schematic.<br><br>One of the following must be passed when the attribute is set: • True • False |
| `PyLensDistortionNode>.schematic_colour` | tuple | Used to set or get the schematic colour of a node in the Batch schematic.<br><br>A tuple with three values (Red, Green, and Blue) must be passed to set the colour. |
| `PyLensDistortionNode>.schematic_colour_label` | string | Used to set of get the schematic colour of a node in the Batch schematic using the label of a colour coding preset.<br><br>A string must be passed when the attribute is set. |
| `PyLensDistortionNode>.mode` | string | Used set or get the distortion mode.<br><br>One of the following must be passed when the attribute is set: • Distort • Undistort |
