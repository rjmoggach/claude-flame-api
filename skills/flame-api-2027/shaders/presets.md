> Source: Autodesk Flame Family 2027 Help — "Creating Presets for a Shader" (XML verified against the original HTML); `-t` option from "Creating a Matchbox Shader".

# Shader presets (`<name>.preset.xml`)

Presets give users of a Matchbox or Lightbox selectable starting points (e.g. *Sepia* in the Duotone shader). They appear in the shader's **Presets** list.

## File

- Name: `<name of shader>.preset.xml`, included when packaging the shader (same folder as the `.glsl`/`.xml`).
- Root `<Presets>` containing one or more `<Preset Name="…">` elements.
- Each `<Preset>` contains `<Shader Index="N">` elements (pass index, as in the sidecar XML) holding `<Uniform>` values.
- Template: `shader_builder -t` (`--preset-template`) "writes the preset template to a file" — the docs call it a `blankpreset.xml` template created "from an existing GLSL with the –t option".
- **Not supported in presets**: curve position and tangent settings.

## Elements and attributes (as observed in the documented output)

| Element | Attributes seen | Notes |
|---|---|---|
| `<Presets>` | — | Root; wraps all presets. |
| `<Preset>` | `Name` | Preset name shown in the Presets list (replace the default `"Preset Name"`). |
| `<Shader>` | `Index` | Pass index (1-based). |
| `<Uniform>` | `Type`, `DisplayName`, `Name`, `Value`; `CurveShape` (curve uniform) | Scalar values in `Value`. `Name` must match the GLSL uniform. |
| `<SubUniform>` | `Value` | One per vector component (e.g. 3 for `vec3`). |

The docs give no formal schema for preset files; the table is derived from the sample below. Note: bool values are written `Value="0"` in the sample (not `True`/`False`), and a popup int with `Value="-1"`.

## How to create presets (from the docs)

1. Load the Matchbox or Lightbox in the application.
2. Set the shader's controls to the desired look.
3. Click **UI XML Shell Printout** (Node Prefs menu, or the Shader tab when in Action). Output goes to the shell Flame was launched from (on macOS, preferably launch Flame from a shell).
4. Copy the XML printed in the shell ("Copy&Paste this XML in the preset file:").
5. Paste into an XML file, rename `Preset Name`. Multiple `<Preset Name> </Preset>` blocks can live in one file inside `<Presets> </Presets>`. (Alternatively paste into a `blankpreset.xml` template generated with `-t`.)
6. Save as `<name of shader>.preset.xml` and include it when packaging.
7. Next load, the preset appears in the Presets list.

Users can do steps 1–4 and send you the shell output to include in a future version.

## Example shell output (Duotone shader, verbatim)

```xml
<Presets>
   <Preset Name="Preset Name">
      <Shader Index="1">
         <Uniform Type="vec3" DisplayName="Custom Black" Name="adskUID_customBlack">
            <SubUniform Value="0.731429">
            </SubUniform>
            <SubUniform Value="0">
            </SubUniform>
            <SubUniform Value="2.61579e-07">
            </SubUniform>
         </Uniform>
         <Uniform Type="vec3" DisplayName="Custom White" Name="adskUID_customWhite">
            <SubUniform Value="1">
            </SubUniform>
            <SubUniform Value="1">
            </SubUniform>
            <SubUniform Value="1">
            </SubUniform>
         </Uniform>
         <Uniform Value="95.6001" Type="float" DisplayName="Contrast" Name="adskUID_contrast">
         </Uniform>
         <Uniform Value="0.82" Type="float" DisplayName="Pivot" Name="adskUID_pivot">
         </Uniform>
         <Uniform Value="0" Type="bool" DisplayName="Use GMask Input" Name="gmaskInput">
         </Uniform>
         <Uniform CurveShape="0" Type="int" DisplayName="Luminance" Name="adskUID_lumaCurve">
         </Uniform>
         <Uniform Value="-1" Type="int" DisplayName="Blend Modes" Name="adskUID_blendModes">
         </Uniform>
         <Uniform Value="100" Type="float" DisplayName="Mix" Name="adskUID_inputMix">
         </Uniform>
      </Shader>
   </Preset>
</Presets>
```

> Agent note: the `adskUID_` uniform names indicate Duotone is a Lightbox (or uses the Lightbox naming convention); presets work for both Matchbox and Lightbox. The curve uniform (`adskUID_lumaCurve`, `Type="int"`) only records `CurveShape`, consistent with "curve position and tangent menu settings are not supported".
