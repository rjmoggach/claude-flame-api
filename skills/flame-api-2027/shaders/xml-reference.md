> Source: Autodesk Flame Family 2027 Help — "About shader_builder XML" (plus attributes observed in the XML samples of "Creating a Matchbox Shader" / "Creating a Lightbox Shader"; all XML verified against the original HTML).

# Shader sidecar XML reference (`shader_builder` XML)

A Matchbox/Lightbox can be just a `.glsl` file; Flame then generates a rough UI. A sidecar `<name>.xml` (same base name, same folder) customises the UI. Generate it with `shader_builder -m -x <name>.glsl` (Matchbox) or `shader_builder -l -x <name>.glsl` (Lightbox), then edit it.

- Any uniform whose name starts with `adsk_` is not shown in the UI and is not considered by `shader_builder`.
- Shipped XML examples: `/opt/Autodesk/presets/<application_version>/matchbox/shaders/EXAMPLES/` (e.g. `InputSockets.xml`, `ConditionalUI.xml`, `BuildList.xml`, `TemporalSampling.xml`, `Curves.glsl`).
- All attribute values are XML attribute strings; booleans are written `"True"` / `"False"`.

## Structure (DTD from the source)

```xml
<!DOCTYPE ShaderNodePreset [

<!ELEMENT ShaderNodePreset (Shader+, Page+)>
<!ELEMENT Shader (Uniform+)>
<!ELEMENT Uniform (SubUniform* | PopupEntry* | Duplicate*)>
<!ELEMENT SubUniform EMPTY>
<!ELEMENT PopupEntry EMPTY>
<!ELEMENT Duplicate EMPTY>
<!ELEMENT Page (Col+)>
<!ELEMENT Col EMPTY>
]>
```

Element tree:

```text
ShaderNodePreset                 (root, mandatory)
├── Shader  (1..n; Lightbox: exactly 1)   one per pass, Index 1-based
│   └── Uniform (1..n)                    one per uniform of that pass
│       ├── SubUniform*   (one per component, when ValueType is not PopUp)
│       ├── PopupEntry*   (only when ValueType="PopUp")
│       └── Duplicate     (only one, when uniform already defined in an earlier pass)
└── Page (1..n)
    └── Col (1..6)
```

Note: the examples write empty elements with explicit closing tags (`<Uniform ...>\n</Uniform>`); follow that style.

---

## `<ShaderNodePreset>`

Root element. Mandatory. Children: `<Shader>` (at least one for a Matchbox; only one for a Lightbox) and `<Page>` (at least one).

| Attribute | Scope | Description | Allowed values | Default |
|---|---|---|---|---|
| `Description` | both | Description of the preset; appears in the Matchbox node Note (Schematic). | Character data | Empty |
| `Name` | both | Name shown in the node's Name field. **Overrides the filename**: if the `.xml` is present, this name is displayed even if the user loads the `.glsl`. | Character data | Name of the preset |
| `HelpLink` | both, optional | URL for external documentation (valid XML characters only). Adds a **Help** button to the interface. | Character data | EMPTY |
| `LimitInputsToTexture` | both, optional | Limit the number of node input sockets to the number of textures required by the shader. | `True` / `False` | `False` |
| `MatteProvider` | Matchbox only | Whether the Matchbox provides a matte to its child node (`True`) or is a pass-through where the child uses the matte from the Matchbox's parent. **If the Matchbox operates on alpha, must be `True`** for the alpha to be passed on. | `True` / `False` | `False` |
| `SupportsAction` | Matchbox only | Hint: usable as an Action node. Batch is always supported. | `True` / `False` | `False` |
| `SupportsTransition` | Matchbox only | Hint: usable as a timeline transition. Batch is always supported. | `True` / `False` | `False` |
| `SupportsAdaptiveDegradation` | Matchbox only | Node supports Batch adaptive degradation. Must be combined with code paths using the `adsk_degrade` uniform — setting `True` alone does **not** turn the node off. | `True` / `False` | `False` |
| `CommercialUsePermitted` | both | Creator's declaration of whether commercial use is allowed. **Not enforced** by the application. | `True` / `False` | `True` |
| `AccumulatePass` | not stated (accumulation is a Matchbox feature) | Numeric value letting the Matchbox accumulate an intermediate pass (`ShaderIndex`) rather than the final result. One-based. | Numeric (pass index, 1-based) | not stated |
| `AccumulationFromStartFrame` | not stated (accumulation is a Matchbox feature) | Whether accumulation proceeds recursively. See `Accumulate` example in `EXAMPLES`. | `True` / `False` | `True` |
| `ShaderType` | both | Set by `shader_builder`: type of shader. | `Matchbox` / `Lightbox` | Depends on the `.glsl` used to create the XML |
| `SoftwareVersion` | both | Set by `shader_builder`: version of the application used to build the XML. | Character data | `shader_builder` defined |
| `TimelineUseBack` | Matchbox only | Whether the Matchbox uses the timeline background. Only used in the timeline context. | `True` / `False` | `True` |
| `Version` | both | Shader version; user metadata, not processed. | Character data | `1` |
| `ResultColourSpace` | both | Forces the tagged colour space of the **Result** output socket. Omitted → node's tagged colour space. | Character data (colour space name) | Empty |
| `MatteColourSpace` | both | Forces the tagged colour space of the **Matte** output socket. Omitted → Matte data colour space. | Character data | Empty |

Attributes that appear in Autodesk's own XML samples but are **not in the attribute table**:

| Attribute | Seen in | Note |
|---|---|---|
| `SupportsTimeline` | Matchbox `scale.xml` sample (`SupportsTimeline="False"`) | Undocumented; presumably a hint like `SupportsAction`/`SupportsTransition`. |
| `OverrideNormals` | Lightbox `gain.xml` sample (`OverrideNormals="False"`) | Undocumented. |

---

## `<Shader>`

Parent: `<ShaderNodePreset>`. Children: `<Uniform>` (at least one). Mandatory. One `<Shader>` per shader pass: a Matchbox can have several passes, a Lightbox only one. Lists the uniforms required by that pass.

| Attribute | Description | Allowed values | Default |
|---|---|---|---|
| `Index` | Index of the associated shader pass. Indexed from **1**. | Integer | `1` |
| `OutputBitDepth` | Bit depth of the render target for this pass. | `Output`, `8`, `16`, `Float16`, `Float32` | `Output` |
| `OutputWidth` | Render-target width if none can be determined from inputs (none existing / not connected). In multipass, only the last pass needs it. Ignored in Action and on the Timeline. | Integer | — |
| `OutputHeight` | Render-target height, same rules as `OutputWidth`. | Integer | — |
| `OutputWidthScaleFactor` | Scale this pass's render-target width relative to the output resolution. | e.g. `1` = no scaling, `0.5` = half | — |
| `OutputHeightScaleFactor` | Scale this pass's render-target height relative to the output resolution. | e.g. `1`, `0.5` | — |
| `OutputScaleFactorEffect` | Effect of the scale factors on sizes (rounding). | `0` = floor, `1` = round, `2` = ceiling | — |
| `OutputNbLevels` | Number of levels for a custom mipmap intermediate pass (see example `MultiTargetCustomMipmaps`). | (not stated; numeric) | — |
| `OutputNbResults` | Number of textures produced by an intermediate pass. | (not stated; numeric) | — |

The docs do not document how to address the multiple results of an `OutputNbResults` pass from GLSL; see shipped example `MultiTargetCustomMipmaps`. Similarly, the example `MultiExecutionSeparableGaussianBlur` "shows how to execute a shader multiple times. The number of times can be defined [in] the shader's XML" — the attribute used is **not documented** on the XML page.

---

## `<Uniform>`

Parent: `<Shader>`. One per uniform in the current pass. Children: `<SubUniform>` (as many as the `Type` requires, when `ValueType` is not `PopUp`), `<PopupEntry>` (only if `ValueType="PopUp"`), `<Duplicate>` (only one, only if the uniform is a duplicate of one in an earlier pass).

The source table has no Default column for `<Uniform>` attributes except where stated in the description.

### General attributes

| Attribute | Applies to | Description | Allowed values |
|---|---|---|---|
| `Type` | all | GLSL type of the uniform. | `float` `vec2` `vec3` `vec4` `int` `ivec2` `ivec3` `ivec4` `bool` `bvec2` `bvec3` `bvec4` `mat2` `mat3` `mat4` `mat2x3` `mat2x4` `mat3x2` `mat3x4` `mat4x2` `mat4x3` `sampler2D` |
| `Name` | all | Uniform name in the GLSL file, set by `shader_builder`. **Cannot be changed** — it links the UI element to the GLSL uniform. | Character data |
| `Tooltip` | all | Tooltip text. Displayed for the corresponding buttons in the **Input Configuration** section of the **Shader** submenu. | Character data |
| `DisplayName` | all | Name shown in the tooltip of the node's corresponding input socket (Batch, Batch FX, Modular Keyer). (Agent note: Autodesk's samples use it as the parameter's human label, e.g. `DisplayName="Scale"`; that it is also the field label is implied, not stated.) | Character data |
| `ChannelName` | all | Name of this uniform's Animation Channel. | Character data |
| `Row` | UI uniforms | Row position in the UI. | `0`–`4` |
| `Col` | UI uniforms | Column position in the UI. | `0`–`3` |
| `Page` | UI uniforms | Page position in the UI. | `0`–`6` |
| `Default` | numeric/bool | Default value. | bool/bvec*: `True`/`False`; int/ivec*: an integer; float/vec*/mat*: a float |
| `Inc` | numeric | Drag stepping. | int types: integer; float/vec/mat types: float |
| `Min` | numeric | Minimum allowed value. | int types: integer; float/vec/mat types: float |
| `Max` | numeric | Maximum allowed value. | int types: integer; float/vec/mat types: float |
| `ResDependant` | `float` `vec2` `vec3` `vec4` | Resolution dependence. **Spelling:** the table says `ResDependant`; Autodesk's sample XML uses `ResDependent="None"`. | `None`, `Width` (scaled by width), `Height` (scaled by height) |
| `IconType` | `vec2` / `vec3` | Viewport control icon. In the Timeline Player only `None` and `Pick` exist; `Light` and `Axis` are replaced by `Pick`. | `None`, `Pick`, `Axis`, `Light` |
| `IconDefaultState` | (listed as "bool") | Default On/Off state of the icon. | `False` (default), `True` |
| `Action3DWidgets` | `vec2` `vec3` `vec4` | Widget measured in Action space (origin = image centre, top-right = (W/2, H/2)). | `False` (default), `True` |
| `ValueType` | `vec3`, `ivec2`, `ivec3`, `ivec4`, `int` (per source; see note) | Presentation mode. | see table below |
| `UIConditionSource` | optional | Name of the uniform that conditionally disables/hides this uniform. | Name of a uniform |
| `UIConditionValue` | optional | Value of `UIConditionSource` required for this uniform to be active. | Character data |
| `UIConditionInvert` | optional | Invert the `UIConditionValue` logic. | `True` / `False` |
| `UIConditionType` | optional | Disable or hide when the condition is not met. Example: `matchbox/shaders/EXAMPLES/ConditionalUI.xml`. | `Disable`, `Hide` |

### `ValueType` values

| Value | Description |
|---|---|
| `Position` | Numeric fields. |
| `Colour` | Colour, with a colour pot (SubUniforms give starting RGB). |
| `ColourWheel` | HGS colour wheel. Channels can be named with the tokens `AngleName`, `IntensityName1`, `IntensityName2`. The bool `HueShift` tag controls whether the outer wheel rotates with the chosen hue. (Example: `ColourWheel`.) |
| `ColourWheelRGBOffset` | 0-based basic model. |
| `ColourWheelRGBSlope` | 1.0-based model, no negative values. |
| `ColourWheelRGBPower` | Inverse of Slope. |
| `PopUp` | Drop-down menu; add `<PopupEntry>` children for names/int values. (Spelled `PopUp` here; the `<PopupEntry>` section writes `ValueType = Popup` — see Ambiguities.) |
| `Curve` | Curves. The `int` (`ivec2`/`ivec3`/`ivec4`) value is a **handle** on 1 (2/3/4) curves, evaluated in GLSL with `adskEvalDynCurves(handle, x)` returning `float` (`vec2`/`vec3`/`vec4`). Example: `EXAMPLES/Curves.glsl`. |
| `LargeCurve` | Three-column-wide curve widget, Proportional mode for every curve, X/Y fields for the current selection. |
| `Proportional` | For `vec3`/`vec4`: numeric field next to its label (larger fields, better layout). |
| `Trackball` | Trackball controlling two values (angle and radial amount) plus a numeric field for each. Use `<SubUniform>` to set `Min`/`Max`/`Default`/`Inc` per channel; `ChannelName` and `DisplayName` on each `SubUniform` set animation channel and UI label (default labels **Angle** and **Radial**). Example: `Trackball`. |

> The `ValueType` "applies to" line in the source lists only `vec3, ivec2, ivec3, ivec4, and int`, but individual values mention `vec4` (`Proportional`) and two-value widgets (`Trackball`), so the applicability list is not exhaustive. Check the shipped examples for the exact uniform type each widget expects.

### `sampler2D` attributes

| Attribute | Description | Allowed values |
|---|---|---|
| `Index` | Position of the sampler (input) in the UI. | Integer |
| `GL_TEXTURE_MIN_FILTER`, `GL_TEXTURE_MAG_FILTER` | Interpolation modes. | `GL_NEAREST`, `GL_LINEAR`, `GL_NEAREST_MIPMAP_NEAREST`, `GL_LINEAR_MIPMAP_NEAREST`, `GL_NEAREST_MIPMAP_LINEAR`, `GL_LINEAR_MIPMAP_LINEAR` |
| `GL_TEXTURE_WRAP_T`, `GL_TEXTURE_WRAP_S` | Wrapping modes. | `GL_CLAMP`, `GL_CLAMP_TO_BORDER`, `GL_CLAMP_TO_EDGE`, `GL_REPEAT`, `GL_MIRRORED_REPEAT` |
| `NoInput` | Behaviour when the input is missing. | `Error` (generates an error), `Black`, `White` |
| `Mipmaps` | Use mipmaps on this sampler. Requires `GL_TEXTURE_MIN_FILTER` to be one of the `*_MIPMAP_*` modes. | `True` / `False` |
| `GL_TEXTURE_BORDER_COLOR` | Optional border colour. | `"r,g,b"` |
| `InputType` | Optional, Matchbox only. Socket type. `Selective` makes it a Selective FX (see [matchbox.md](matchbox.md#selective-fx-matchbox)). | `Front` (red), `Back` (green), `Matte` (blue), `Selective` |
| `InputColor` | Optional, Matchbox only. Custom 8-bit input tab colour. `InputType` takes precedence if both are set. Example: `matchbox/shaders/EXAMPLES/InputSockets.xml`. | `r,g,b`, each 0–255 (sample uses `InputColor="67, 77, 83"`) |

### Curve attributes (when `ValueType="Curve"`)

Example in context: `/opt/Autodesk/presets/<application_version>/matchbox/shaders/EXAMPLES/Curves.glsl`.

| Attribute | Description | Allowed values | Default |
|---|---|---|---|
| `CurveMinX`, `CurveMaxX`, `CurveMinY`, `CurveMaxY` | x/y range of the curves. | Float | Min: `0.0`; Max: `1.0` |
| `CurveBackground` | Curve editor background. | `0` empty, `1` hue gradient, `2` intensity gradient | `0` |
| `CurveWrapArround` (sic) | Behaviour at the border. | `0` no wraparound, `1` wraparound | `0` |
| `CurveShape` | Default shape. | `0` linear (MinX,MinY)→(MaxX,MaxY); `1` linear (MinX,MaxY)→(MaxX,MinY); `2` S; `3` inverse S; `4` constant MaxY; `5` constant MinY; `6` constant MinY + 0.5*(MaxY−MinY) | `0` |
| `CurveR` | R colour of all curves of this uniform. | Integer | `0` |
| `CurveG` | G colour. | Integer | `0` |
| `CurveB` | B colour. | Integer | `0` |

`CurveWrapArround` is spelled with a double "r" in the source — use it exactly as written.

---

## `<SubUniform>`

Parent: `<Uniform>`. Empty. One per value required by the parent uniform's type (source says "based on the Value attribute" — meaning the `Type`): `vec3` → 3 `<SubUniform>`, `float` → none. With `ValueType="Colour"` they define the starting RGB of the colour pot; with `Position` + `vec3`, three numeric fields.

| Attribute | Description | Allowed values |
|---|---|---|
| `Default` | Default value (of this component). | bool types: `True`/`False`; int types: integer; float types: float |
| `Inc` | Drag stepping. Overrides the parent `<Uniform>`'s `Inc`. | int/float per type |
| `Max` | Maximum. | int/float per type |
| `Min` | Minimum. | int/float per type |
| `ResDependant` | (`float`/`vec2`/`vec3`/`vec4`) Resolution dependence. | `None`, `Width`, `Height` |
| `ChannelName`, `DisplayName` | Documented only under `ValueType="Trackball"`: per-channel animation channel name and UI label. | Character data |

Curve attributes (override the parent `<Uniform>`'s values when `ValueType="Curve"`):

| Attribute | Description | Allowed values | Default |
|---|---|---|---|
| `CurveMinX`, `CurveMaxX`, `CurveMinY`, `CurveMaxY` | x/y range. | Float | Min `0.0`, Max `1.0` |
| `CurveBackground` | Background. | `0`, `1`, `2` (as above) | `0` |
| `CurveWrapArround` | Border behaviour. | `0`, `1` | `0` |
| `CurveShape` | Default shape. | `0`–`6` (as above) | `0` |
| `CurveName` | Name of the curve represented by this SubUniform. | Character data | — |
| `CurveR`, `CurveG`, `CurveB` | Colour of this SubUniform's curve. | Integer | `0` |

In preset files, `<SubUniform>` carries a `Value` attribute instead (see [presets.md](presets.md)).

---

## `<Duplicate>`

Parent: `<Uniform>`. Empty. No attributes. When a uniform is present in more than one pass, it is shown once in the UI: define it fully in the first `<Shader>` and mark it as a duplicate in later ones. Otherwise it appears twice in the node UI.

First `<Shader>`:

```xml
<Uniform Row="0" Col="0" Page="0" Default="True" Tooltip="" DisplayName="Filtering" Type="bool" Name="filtering">
</Uniform>
```

Second `<Shader>`:

```xml
<Uniform Type="bool" Name="filtering">
<Duplicate>
</Duplicate>
</Uniform>
```

---

## `<PopupEntry>`

Parent: `<Uniform>` (only if `ValueType` is PopUp). Empty. Each one is a drop-down item. Example: `/opt/Autodesk/presets/<application_version>/matchbox/shaders/EXAMPLES/BuildList.xml`.

```xml
<PopupEntry Title="ReplaceMe" Value="0">
</PopupEntry>
```

| Attribute | Description | Allowed values |
|---|---|---|
| `Title` | Entry text shown in the drop-down. | Character data |
| `Value` | Value passed to the uniform. | Character data (an int for an `int` uniform) |

---

## `<Page>`

Parent: `<ShaderNodePreset>`. Children: `<Col>`, up to 6. Defines a page name and index. Expanded UI shows all 6 columns under `Name`; collapsed UI splits them into two pages: `ColName0_2` (first three `<Col>`) and `ColName3_5` (last three), ordered by each `<Col>`'s index.

| Attribute | Description | Allowed values | Default |
|---|---|---|---|
| `Name` | Page name in the expanded UI (all columns at once). | Character data | `Page 1` |
| `ColName0_2` | Page name for the first 3 columns (collapsed / dual-panel UI). | Character data | `Page 1` |
| `ColName3_5` | Page name for the last 3 columns (collapsed UI). | Character data | `Page 2` |
| `Page` | Page index. | From 0, max 6 | `0` |

## `<Col>`

Parent: `<Page>`. Empty. Names a column within a page.

| Attribute | Description | Allowed values | Default |
|---|---|---|---|
| `Name` | Column name displayed in the UI. | Character data | `Column 1` |
| `Col` | Column index. | From 0, max 6 (per source) | `0` |
| `Page` | Index of the `<Page>` where the column appears. | From 0, max 6 | `0` |

---

## Complete example (Matchbox, verbatim from "Creating a Matchbox Shader")

```xml
<ShaderNodePreset
   SupportsAdaptiveDegradation="False" SupportsAction="False"
   SupportsTransition="False" SupportsTimeline="False"
   TimelineUseBack="False" MatteProvider="False" ShaderType="Matchbox"
   SoftwareVersion="2016.0.0" LimitInputsToTexture="True"
   Version="1" Description="" Name="Next Generation Scaling">

   <Shader OutputBitDepth="Output" Index="1">
        <Uniform Index="0" NoInput="Error"
                 Tooltip="" DisplayName="Front"
                 InputColor="67, 77, 83" Mipmaps="False"
                 GL_TEXTURE_WRAP_T="GL_REPEAT"
                 GL_TEXTURE_WRAP_S="GL_REPEAT"
                 GL_TEXTURE_MAG_FILTER="GL_LINEAR"
                 GL_TEXTURE_MIN_FILTER="GL_LINEAR"
                 Type="sampler2D" Name="myInputTex">
        </Uniform>

        <Uniform ResDependent="None"
                 Max="100.00"
                 Min="-100.00"
                 Default="0.0"
                 Inc="0.01"
                 Tooltip="Displays the percentage of scaling applied."
                 Row="0" Col="0" Page="0"
                 Type="float"
                 DisplayName="Scale"
                 Name="size">
        </Uniform>
    </Shader>

    <Page Name="Page 1" Page="0">
        <Col Name="Effect Settings" Col="0" Page="0">
        </Col>
    </Page>

</ShaderNodePreset>
```

Lightbox example: see [lightbox.md](lightbox.md) / [examples.md](examples.md).

## Ambiguities / inconsistencies in the source

- `ResDependant` (attribute tables) vs `ResDependent` (both Autodesk sample XMLs). Prefer generating the XML with `shader_builder -x` and keeping whatever spelling it emits.
- `PopUp` (ValueType list) vs `Popup` (PopupEntry usage text). Prefer the `shader_builder` output / `BuildList.xml`.
- `<Uniform>` `Col` is `0`–`3` but `<Page>` can hold up to 6 `<Col>` and `<Col Col>` allows 0–6; `Page` index allowed 0–6. The docs do not reconcile these ranges.
- `IconDefaultState` is labelled "*bool*" (likely meaning the attribute type, or bool uniforms); unclear.
- `SupportsTimeline` and `OverrideNormals` appear in samples but are not documented.
- `AccumulatePass`, `OutputNbLevels`, `OutputNbResults` have no allowed values/defaults given.
- The `<SubUniform>` usage text says the count is "based on the Value attribute"; it is evidently the parent's `Type`.
- The `adsk_previous_frame_` XML snippet in "Shader API Documentation" is a prose/XML fragment (see [shader-api.md](shader-api.md#general-purpose-mb--flame-provided-uniforms)).
