# class `flame.PyTimewarpNode`(PyNode)

> **2027 additions not shown below.** Autodesk's published pydoc predates some Flame 2027 API changes. New/renamed/deprecated members for this class (or its bases) are in What's New: [PyNode](../../guides/whats-new-2027.md#pynode). Treat those as authoritative where they differ.

Object representing a Timewarp node.

**Method resolution order:** PyTimewarpNode → PyNode → PyFlameObject

> Cannot be instantiated from Python (obtained from other API objects).

## Methods

### `get_duration_timing`

```python
get_duration_timing( (PyTimewarpNodearg1, (float)frame) -> float
```

Return the timing value for the current frame while in the duration mode.

### `get_speed`

```python
get_speed( (PyTimewarpNodearg1, (float)frame) -> float
```

Return the speed attribute at the requested frame.

### `get_timing`

```python
get_timing( (PyTimewarpNodearg1, (float)frame) -> float
```

Return the timing value at the requested frame.

### `get_speed_timing`

```python
get_speed_timing( (PyTimewarpNodearg1, (float)frame) -> float
```

The timing value for the current frame while in the speed mode.

### `set_speed`

```python
set_speed( (PyTimewarpNodearg1, (float)frame, (float)new_speed) -> None
```

Set the speed at the requested frame.

### `set_timing`

```python
set_timing( (PyTimewarpNodearg1, (float)frame, (float)new_timing) -> None
```

Set the timing at the requested frame.

## Inherited members

- **Static methods inherited from PyNode:** `delete`, `duplicate`, `load_node_setup`, `save_node_setup`, `set_context`
- **Read-only properties inherited from PyNode:** `input_sockets`, `output_sockets`, `sockets`
- **Read-only properties inherited from PyFlameObject:** `attributes`, `parent`

## Attributes (documented values)

Source: "PyTimewarpNode Attributes" help page. Access via `obj.<attr>`; most return a `PyAttribute` — use `.get_value()` / `.set_value()` (see PyAttribute.md).

Use the following commands to set or get attributes for a Timewarp node or a Timeline Timeline FX.

---

### Timewarp Node (PyTimewarpNode)

| Command | Type | Description |
|---|---|---|
| `PyTimewarpNode>.pos_x` | integer | The x position of a node in the Batch schematic.<br><br>An integer number must be passed when the attribute is set: • Min: -2147483647 • Max: 2147483647 |
| `PyTimewarpNode>.pos_y` | int | The y position of a node in the Batch schematic.<br><br>An integer number must be passed when the attribute is set: • Min: -2147483647 • Max: 2147483647 |
| `PyTimewarpNode>.name` | string | Used to set or get name of the Batch node.<br><br>A string must be passed when the attribute is set. |
| `PyTimewarpNode>.note` | string | Used to set or get the content of the note associated with the Batch node.<br><br>A string must be passed when the attribute is set. |
| `PyTimewarpNode>.note_collapsed` | bool | Used to set or get the collapsed status of a note in the Batch schematic.<br><br>One of the following must be passed when the attribute is set: • True • False |
| `PyTimewarpNode>.selected` | bool | Used to select or deselect a node in the Batch schematic.<br><br>One of the following must be passed when the attribute is set: • True • False |
| `PyTimewarpNode>.type` | string | Return the type of the node. |
| `PyTimewarpNode>.bypass` | bool | Used to set or get the bypass status of a node in the Batch schematic.<br><br>One of the following must be passed when the attribute is set: • True • False |
| `PyTimewarpNode>.schematic_colour` | tuple | Used to set or get the schematic colour of a node in the Batch schematic.<br><br>A tuple with three values (Red, Green, and Blue) must be passed to set the colour. |
| `PyTimewarpNode>.schematic_colour_label` | string | Used to set of get the schematic colour of a node in the Batch schematic using the label of a colour coding preset.<br><br>A string must be passed when the attribute is set. |

---

### Timewarp Timeline FX (PyTimewarpTimelineFX)

| Command | Type | Description |
|---|---|---|
| `PyTimewarpTimelineFX>.duration` | integer | Used to get or set the Duration value for timeline segment. An integer number must be passed as the argument when the attribute is set. |
| `PyTimewarpTimelineFX>.duration_speed` | float | Used to get the Speed value for the current frame while in the Duration mode. |

---

### Common (PyTimewarpNode and PyTimewarpTimelineFX)

| Command | Type | Description |
|---|---|---|
| `PyTimewarpNode>.mode` | string | Used to get or set the Timewarp mode.<br><br>One of the following must be passed as the argument when the attribute is set: • Speed • Timing |
| `PyTimewarpNode>.frame_interpolation_mode` | string | Used to get or set the Frame Interpolation mode.<br><br>One of the following must be passed as the argument when the attribute is set: • Motion • Trails • Mix • ML(2026) • ML(2025.1) |
| `PyTimewarpNode>.sample_mode` | string | Used to get or set the Sample Mode being for the Mix and Trails frame interpolation modes.<br><br>One of the following must be passed as the argument when the attribute is set: • Start • Middle • End |
| `PyTimewarpNode>.mix_amount` | float | Used to get or set the Amount for the Mix frame interpolation mode. A float number between 0.0 and 1000.0 must be passed as an argument when the attribute is set. |
