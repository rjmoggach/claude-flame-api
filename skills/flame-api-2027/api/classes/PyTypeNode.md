# class `flame.PyTypeNode`(PyTimelineFX)

> **2027 additions not shown below.** Autodesk's published pydoc predates some Flame 2027 API changes. New/renamed/deprecated members for this class (or its bases) are in What's New: [PyTypeNode](../../guides/whats-new-2027.md#pytypenode-and-pytypetimelinefx), [PyTimelineFX](../../guides/whats-new-2027.md#pytimelinefx). Treat those as authoritative where they differ.

Object representing a Type TimelineFX.

**Method resolution order:** PyTypeNode → PyTimelineFX → PyFlameObject

> Cannot be instantiated from Python (obtained from other API objects).

## Methods

### `add_layer`

```python
add_layer( (PyTypeNode)arg1, (float)frame) -> float
```

Create a new layer.

Keyword argument:

layer_type -- Must be one of Left, Centre(default), Right, Roll, or Crawl.

### `append_type_setup`

```python
append_type_setup( (PyTypeNode)arg1, (str)file_name) -> bool
```

Append a setup to the current Type setup.

## Read-only properties defined here

### `layers`

Return the layers list.

## Inherited members

- **Static methods inherited from PyTimelineFX:** `load_setup`, `save_setup`, `slide_keyframes`, `sync_connected_segments`
- **Read-only properties inherited from PyTimelineFX:** `type`
- **Read-only properties inherited from PyFlameObject:** `attributes`, `parent`

## Attributes (documented values)

Source: "PyTypeNode Attributes" help page. Access via `obj.<attr>`; most return a `PyAttribute` — use `.get_value()` / `.set_value()` (see PyAttribute.md).

Use the following commands to set or get attributes for a Type node, Type Timeline FX or a Type Layer.

---

### Type Node (PyTypeNode)

| Command | Type | Description |
|---|---|---|
| `PyTypeNode>.pos_x` | integer | The x position of a node in the Batch schematic.<br><br>An integer number must be passed when the attribute is set: • Min: -2147483647 • Max: 2147483647 |
| `PyTypeNode>.pos_y` | integer | The y position of a node in the Batch schematic.<br><br>An integer number must be passed when the attribute is set: • Min: -2147483647 • Max: 2147483647 |
| `PyTypeNode>.name` | string | Used to set or get name of the Batch node.<br><br>A string must be passed when the attribute is set. |
| `PyTypeNode>.note` | string | Used to set or get the content of the note associated with the Batch node.<br><br>A string must be passed when the attribute is set. |
| `PyTypeNode>.note_collapsed` | bool | Used to set or get the collapsed status of a note in the Batch schematic.<br><br>One of the following must be passed when the attribute is set: • True • False |
| `PyTypeNode>.selected` | bool | Used to select or deselect a node in the Batch schematic.<br><br>One of the following must be passed when the attribute is set: • True • False |
| `PyTypeNode>.type` | string | Return the type of the node. |
| `PyTypeNode>.bypass` | bool | Used to set or get the bypass status of a node in the Batch schematic.<br><br>One of the following must be passed when the attribute is set: • True • False |
| `PyTypeNode>.schematic_colour` | tuple | Used to set or get the schematic colour of a node in the Batch schematic.<br><br>A tuple with three values (Red, Green, and Blue) must be passed to set the colour. |
| `PyTypeNode>.schematic_colour_label` | string | Used to set of get the schematic colour of a node in the Batch schematic using the label of a colour coding preset.<br><br>A string must be passed when the attribute is set. |

---

### Common (PyTypeNode and PyTypeTimelineFX)

| Command | Type | Description |
|---|---|---|
| `<PyTypeNode>.show_layer_axis` | bool | Used to get or set the status of Show Axis for the Layer Axis.<br><br>One of the following must be passed as the argument when the attribute is set: • True • False |
| `<PyTypeNode>.show_para_axis` | bool | Used to get or set the status of Show Axis for the Paragraph Axis.<br><br>One of the following must be passed as the argument when the attribute is set: • True • False |
| `<PyTypeNode>.show_char_axis` | bool | Used to get or set the status of Show Axis for the Characters Axis.<br><br>One of the following must be passed as the argument when the attribute is set: • True • False |
| `<PyTypeNode>.show_char_pos` | bool | Used to get or set the status of Show Position for the Characters Axis.<br><br>One of the following must be passed as the argument when the attribute is set: • True • False |
| `PyTypeNode>.selected_layers` | list | Used to access the attributes, functions, and read-only properties of the selected layers. |
| `PyTypeNode>.current_layer` | PyTypeLayer | Used to access the attributes, functions, and read-only properties of the current layer. |
| `PyTypeNode>.swaa` | string | Used to get or set the amount of software anti-aliasing samples.<br><br>One of the following must be passed as the argument when the attribute is set: • SWAA 1x • SWAA 4x • SWAA 9x • SWAA 16x • SWAA 25x • SWAA 36x • SWAA 49x • SWAA 64x |
| `PyTypeNode>.use_hwaa` | bool | Used to get or set the status of Use HWAA.<br><br>One of the following must be passed as the argument when the attribute is set: • True • False |
| `PyTypeNode>.motion_blur` | bool | Used to get or set the status of Motion Blur.<br><br>One of the following must be passed as the argument when the attribute is set: • True • False |
| `PyTypeNode>.motion_blur_samples` | integer | Used to get or set the amount of motion blur samples. An integer number between 2 and 100 must be passed as an argument when the attribute is set. |
| `PyTypeNode>.motion_blur_phase` | float | Used to get or set the motion blur phase. A float number between -1.0 and 1.0 must be passed as an argument when the attribute is set. |
| `PyTypeNode>.motion_blur_shutter` | float | Used to get or set the motion blur shutter. A float number between 0.10 and 50.0 must be passed as an argument when the attribute is set. |
| `PyTypeNode>.resolution_mode` | string | Used to get or set the resolution mode.<br><br>One of the following must be passed as a string to set the mode: • Resolution List • Adaptive • Scaling Presets |
| `PyTypeNode>.scaling_presets_value` | float | Used to get or set the Scaling Presets value. A float must be passed as an argument to set the value. The value represents the scaling percentage. |
| `PyTypeNode>.adaptive_mode` | string | Used to get or set the Adaptive mode.<br><br>One of the following must be passed as a string to set the mode: • Width based on Ratio • Height based on Ratio |

---

### Type Layer (PyTypeLayer)

A Type layer as its own set of attributes.

| Command | Type | Description |
|---|---|---|
| `PyTypeLayer>.hidden` | bool | Used to get or set the visibility status of a Layer.<br><br>One of the following must be passed as the argument when the attribute is set: • True • False |
| `PyTypeLayer>.text` | string | Used to get or set the characters of a Layer. A string must be passed as an argument to change the characters. |
| `PyTypeLayer>.font` | tuple | Used to get or set the characters font. A tuple with a maximum of three values between Font Family, Font Style, and Project Font Index is returned when getting the current font.<br><br>When the attribute is set, one of the following values can be used: • Font Family: A string representing the name of the Font Family • Font Style: A string representing the name of the Font Style • Font Path: A string representing the path to a font • Project Font Index: An integer number representing the index of the Font in the Project Fonts table. <br><br>One of the following combinations must used when the attribute is set: • (Font Family, Font Style) • (Font Family, Font Style, Project Font Index) • (Font Path, Font Style) • Font Path • Project Font Index |
| `PyTypeLayer>.font_size` | float | Used to get or set the characters Size. A float number between 0.0 and 2000.0 must be passed as an argument when the attribute is set. |
| `PyTypeLayer>.fill` | bool | Used to get or set the status of the Fill Active button.<br><br>One of the following must be passed as the argument when the attribute is set: • True • False |
| `PyTypeLayer>.fill_colour` | tuple | Used to get or set the Fill Colour of the characters. A tuple with three values (Red, Green, and Blue) must be passed to set the colour. |
| `PyTypeLayer>.fill_opacity` | float | Used to get or set the characters Opacity. A float number between 0.0 and 100.0 must be passed as an argument when the attribute is set. |
| `PyTypeLayer>.italic_angle` | float | Used to get or set the characters Italic angle. A float number between -60.0 and 60.0 must be passed as an argument when the attribute is set. |
| `PyTypeLayer>.kerning` | float | Used to get or set the characters Kerning. A float number between -100000.0 and 10000.0 must be passed as an argument when the attribute is set. |
| `PyTypeLayer>.tracking` | float | Used to get or set the characters Tracking. A float number between -100000.0 and 10000.0 must be passed as an argument when the attribute is set. |
| `PyTypeLayer>.underline` | bool | Used to get or set the status of the Underline Active button.<br><br>One of the following must be passed as the argument when the attribute is set: • True • False |
| `PyTypeLayer>.underline_width` | float | Used to get or set the Underline Width. A float number between -9999.0 and 9999.0 must be passed as an argument when the attribute is set. |
| `PyTypeLayer>.underline_offset_y` | float | Used to get or set the Underline Y Offset. A float number between -9999.0 and 9999.0 must be passed as an argument when the attribute is set. |
| `PyTypeLayer>.outline` | bool | Used to get or set the status of the Outline Active button.<br><br>One of the following must be passed as the argument when the attribute is set: • True • False |
| `PyTypeLayer>.outline_colour` | tuple | Used to get or set the Outline Colour of the characters. A tuple with three values (Red, Green, and Blue) must be passed to set the colour. |
| `PyTypeLayer>.outline_width` | float | Used to get or set the Outline Width. A float number between 1.0 and 500.0 must be passed as an argument when the attribute is set. |
| `PyTypeLayer>.outline_join` | string | Used to get or set the Outline Join mode.<br><br>One of the following must be passed as the argument when the attribute is set: • Round Join • Square Join • Bevel Join • Miter Join |
| `PyTypeLayer>.outline_miter_limit` | float | Used to get or set the Outline Miter Limit. A float number between 0.0 and 100.0 must be passed as an argument when the attribute is set. |
| `PyTypeLayer>.case` | string | Used to get or set the characters Case.<br><br>One of the following must be passed as the argument when the attribute is set: • Original • Uppercase • Lowercase • Title Caps • Small Caps |
| `PyTypeLayer>.superscript` | bool | Used to get or set the status of the Superscript option.<br><br>One of the following must be passed as the argument when the attribute is set: • True • False |
| `PyTypeLayer>.subscript` | bool | Used to get or set the status of the Subscript option.<br><br>One of the following must be passed as the argument when the attribute is set: • True • False |
| `PyTypeLayer>.strikeout` | bool | Used to get or set the status of the Strikeout option.<br><br>One of the following must be passed as the argument when the attribute is set: • True • False |
| `PyTypeLayer>.mask_mode` | string | Used to get or set the Mask mode.<br><br>One of the following must be passed as the argument when the attribute is set: • Disabled • Top • Bottom • Left • Right |
| `PyTypeLayer>.mask_position` | float | Used to get or set the Mask Position. A float number between 0.0 and 100.0 must be passed as an argument when the attribute is set. |
| `PyTypeLayer>.background` | bool | Used to get or set the status of the Background Active button.<br><br>One of the following must be passed as the argument when the attribute is set: • True • False |
| `PyTypeLayer>.background_colour` | tuple | Used to get or set the Background Colour. A tuple with three values (Red, Green, and Blue) must be passed to set the colour. |
| `PyTypeLayer>.background_opacity` | float | Used to get or set the Background Opacity. A float number between 0.0 and 100.0 must be passed as an argument when the attribute is set. |
| `PyTypeLayer>.background_radius` | float | Used to get or set the Background Radius. A float number between 0.0 and 1.0 must be passed as an argument when the attribute is set. |
| `PyTypeLayer>.background_offset` | float | Used to get or set the Background Offset. Float numbers for the X and Y values must be passed as arguments when the attribute is set. |
| `PyTypeLayer>.background_scale` | tuple | Used to get or set the Background Scale. A tuple with two float values (X, Y) must be passed as an argument when the attribute is set. |
| `PyTypeLayer>.background_outline` | bool | Used to get or set the status of the Background Outline.<br><br>One of the following must be passed as the argument when the attribute is set: • True • False |
| `PyTypeLayer>.background_outline_colour` | tuple | Used to get or set the Background Outline Colour. A tuple with three values (Red, Green, and Blue) must be passed to set the colour. |
| `PyTypeLayer>.background_outline_width` | float | Used to get or set the Background Outline Width. A float number between 1.0 and 500.0 must be passed as an argument when the attribute is set. |
| `PyTypeLayer>.background_outline_join` | string | Used to get or set the Background Outline Join mode.<br><br>One of the following must be passed as the argument when the attribute is set: • Round Join • Square Join • Bevel Join • Miter Join |
| `PyTypeLayer>.background_outline_miter_limit` | float | Used to get or set the Background Outline Miter Limit. A float number between 0.0 and 100.0 must be passed as an argument when the attribute is set. |
| `PyTypeLayer>.shadow` | bool | Used to get or set the status of the Shadow Active button.<br><br>One of the following must be passed as the argument when the attribute is set: • True • False |
| `PyTypeLayer>.shadow_colour` | tuple | Used to get or set the Shadow Colour of the characters. A tuple with three values (Red, Green, and Blue) must be passed to set the colour. |
| `PyTypeLayer>.shadow_opacity` | float | Used to get or set the Shadow Opacity. A float number between 0.0 and 100.0 must be passed as an argument when the attribute is set. |
| `PyTypeLayer>.shadow_blur` | tuple | Used to get or set the Shadow Blur. A tuple with two float values (X, Y) between 0.0 and 100.0 must be passed as an argument when the attribute is set. |
| `PyTypeLayer>.shadow_position` | tuple | Used to get or set the Shadow Position. A tuple with two float values (X, Y) between -1000000.0 and 1000000.0 must be passed as an argument when the attribute is set. |
| `PyTypeLayer>.shadow_scale` | tuple | Used to get or set the Shadow Scale. A tuple with two float values (X, Y) between -1000000.0 and 1000000.0 must be passed as an argument when the attribute is set. |
| `PyTypeLayer>.shadow_shear` | tuple | Used to get or set the Shadow Shear. A tuple with two float values (X, Y) between -60.0 and 60.0 must be passed as an argument when the attribute is set. |
| `PyTypeLayer>.shadow_rotation` | float | Used to get or set the Shadow Rotation. A float number between -1000000.0 and 1000000.0 must be passed as an argument when the attribute is set. |
| `PyTypeLayer>.position` | tuple | Used to get or set the Layer Position. A tuple with two float values (X, Y) between -1000000.0 and 1000000.0 must be passed as an argument when the attribute is set. |
| `PyTypeLayer>.scale` | tuple | Used to get or set the Layer Scale. A tuple with two float values (X, Y) between -1000000.0 and 1000000.0 must be passed as an argument when the attribute is set. |
| `PyTypeLayer>.shear` | tuple | Used to get or set the Layer Shear. A tuple with two float values (X, Y) between -60.0 and 60.0 must be passed as an argument when the attribute is set. |
| `PyTypeLayer>.rotation` | float | Used to get or set the Layer Rotation. A float number between -1000000.0 and 1000000.0 must be passed as an argument when the attribute is set. |
| `PyTypeLayer>.centre` | tuple | Used to get or set the Layer Centre. A tuple with two float values (X, Y) between -1000000.0 and 1000000.0 must be passed as an argument when the attribute is set. |
| `PyTypeLayer>.axis_alignment` | string | Used to get or set the Layer Axis Alignment.<br><br>One of the following must be passed as the argument when the attribute is set: • Bottom / Right • Bottom • Bottom / Left • Right • Centre • Left • Top / Right • Top • Top / Left |
| `PyTypeLayer>.width` | float | Used to get the Layer Width. |
| `PyTypeLayer>.opacity` | float | Used to get or set the layer Opacity. A float number between 0.0 and 100.0 must be passed as an argument when the attribute is set. |
| `PyTypeLayer>.justification` | string | Used to get or set the Layer Justification.<br><br>One of the following must be passed as the argument when the attribute is set: • Left • Centre • Right • Justified |
| `PyTypeLayer>.leading` | float | Used to get or set the Layer Leading. A float number between -1000000.0 and 1000000.0 must be passed as an argument when the attribute is set. |
| `PyTypeLayer>.separation` | float | Used to get or set the Layer Separation. A float number between -999.0 and 999.0 must be passed as an argument when the attribute is set. |
| `PyTypeLayer>.indent` | integer | Used to get or set the Layer Indent. An integer number between 0 and 1000.0 must be passed as an argument when the attribute is set. |
