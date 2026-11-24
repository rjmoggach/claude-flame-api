<!-- source: Autodesk Flame Family 2027 Help _ PyTimewarpNode Attributes _ Autodesk.html -->
# PyTimewarpNode Attributes

Use the following commands to set or get attributes for a Timewarp node or a Timeline Timeline FX.

---

## Timewarp Node (PyTimewarpNode)

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

## Timewarp Timeline FX (PyTimewarpTimelineFX)

| Command | Type | Description |
|---|---|---|
| `PyTimewarpTimelineFX>.duration` | integer | Used to get or set the Duration value for timeline segment. An integer number must be passed as the argument when the attribute is set. |
| `PyTimewarpTimelineFX>.duration_speed` | float | Used to get the Speed value for the current frame while in the Duration mode. |

---

## Common (PyTimewarpNode and PyTimewarpTimelineFX)

| Command | Type | Description |
|---|---|---|
| `PyTimewarpNode>.mode` | string | Used to get or set the Timewarp mode.<br><br>One of the following must be passed as the argument when the attribute is set: • Speed • Timing |
| `PyTimewarpNode>.frame_interpolation_mode` | string | Used to get or set the Frame Interpolation mode.<br><br>One of the following must be passed as the argument when the attribute is set: • Motion • Trails • Mix • ML(2026) • ML(2025.1) |
| `PyTimewarpNode>.sample_mode` | string | Used to get or set the Sample Mode being for the Mix and Trails frame interpolation modes.<br><br>One of the following must be passed as the argument when the attribute is set: • Start • Middle • End |
| `PyTimewarpNode>.mix_amount` | float | Used to get or set the Amount for the Mix frame interpolation mode. A float number between 0.0 and 1000.0 must be passed as an argument when the attribute is set. |

## Related pages

- Autodesk Flame Python: flame module
