> Source: Autodesk Flame Family 2027 Help — "Creating a Matchbox Shader", "Shader Builder", "Matchbox Shader Examples" (code verified against the original HTML).

# Writing Matchbox shaders

See also: [README.md](README.md) (overview, CLI), [shader-api.md](shader-api.md) (`adsk_*` uniforms/functions), [xml-reference.md](xml-reference.md), [examples.md](examples.md).

## Structure

A Matchbox shader is always structured as:

1. A **forward declaration** where all uniforms and APIs used are declared.
2. A `main()` function. (Matchbox shaders are not part of an established shading pipeline like Lightbox, hence `main()`.)

Inputs are `sampler2D` uniforms; each becomes a node input socket. Non-`adsk_` uniforms become UI controls. `adsk_`-prefixed uniforms are supplied by Flame and hidden from the UI.

Simple Add effect (verbatim from the docs):

```glsl
uniform float adsk_result_w, adsk_result_h;

void main()
{
   vec2 coords = gl_FragCoord.xy / vec2( adsk_result_w, adsk_result_h );
   vec3 sourceColor1 = texture2D(input1, coords).rgb;
   vec3 sourceColor2 = texture2D(input2, coords).rgb;

   gl_FragColor = vec4( sourceColor1+sourceColor2, 1.0 );
}
```

> Source bug: `input1` and `input2` are used but never declared. Per the forward-declaration rule, add `uniform sampler2D input1, input2;` (agent correction).

Key idioms shown by the docs:
- Normalised texture coordinate: `gl_FragCoord.xy / vec2( adsk_result_w, adsk_result_h )`.
- Legacy GLSL: `texture2D(...)`, write `gl_FragColor`.
- Modern GLSL: `texture(...)`, write a declared `layout ( location = 0 ) out vec4`.

## Forward declaration

"Matchbox requires that you forward declare your uniforms and used APIs. This ensures that shader_builder provides accurate file locations for warnings and errors." E.g. if you call `adsk_getLuminance`, declare `float adsk_getLuminance( in vec3 color );` at the top (signatures in [shader-api.md](shader-api.md)).

## GLSL versions

- Legacy: Linux GLSL **130**; macOS GLSL **120** (Action does not comply with the OpenGL core profile; an X server such as XQuartz is required for `shader_builder` to compile on macOS).
- Modern (as of 2025.1 Update): `#version 430`, `440`, `450`, `460` are supported for Matchbox. Requirements:
  - The `#version` directive must be in **each** `.glsl` file header (each pass file).
  - **Uniforms must be declared inside a uniform block** (Vulkan / SPIR-V rules).
  - Compilation is stricter than before; some former warnings are now errors.
  - Additional functions: double precision math/vector/matrix, packing/unpacking & bit functions, atomics, matrix determinant, fused multiply-add.

### Modern GLSL (430–460)

Scale effect, legacy (version 2025 and earlier):

```glsl
uniform float size;
uniform sampler2D myInputTex;

void main (void) {
        vec4 tex0 = texture2D(myInputTex, gl_TexCoord[0] * size);
        gl_FragColor = vec4 (tex0.rgb, 1.0);
}
```

Same effect, modern GLSL (as of 2025.1 Update), verbatim:

```glsl
#version 430
layout ( location = 0 ) out vec4 fragColor;

layout( binding = 1 ) uniform AdskUniformBlock
{
   float adsk_result_w, adsk_result_h;
};
layout( binding = 2 ) uniform UniformBlock
{
   float size;
};

layout( binding = 3 ) uniform sampler2D myInputTex;

void main (void) {
        vec2 uv = gl_FragCoord.xy / vec2( adsk_result_w, adsk_result_h );
        vec4 tex0 = texture( myInputTex, uv * size );
        fragColor = vec4( tex0.rgb, 1.0 );
}
```

Observations (from this example only — the docs give no further rules):
- Output: `layout ( location = 0 ) out vec4 fragColor;` replaces `gl_FragColor`.
- Flame `adsk_` uniforms and user uniforms are put in separate blocks here (`AdskUniformBlock`, `UniformBlock`); samplers are declared outside blocks with their own `layout( binding = N )`.
- Binding numbers used: 1, 2, 3. **The docs do not state binding-number rules** (whether specific numbers, uniqueness, or the block names are required). Mirror this pattern and/or consult shipped `EXAMPLES/` shaders.
- `gl_TexCoord` is not used; coordinates are derived from `gl_FragCoord`.

## Inputs (node sockets)

- **Up to 6 node inputs.** A Matchbox designed for more than 6 inputs loads, but only the first 6 are processed.
- Matchbox-only input features (XML, on `sampler2D` uniforms): `InputType` (`Front`/`Back`/`Matte`/`Selective`), `InputColor` (`r,g,b` 0–255), and root attribute `LimitInputsToTexture="True"` to show only as many sockets as textures required. See `EXAMPLES/InputSockets`.
- `NoInput` (`Error`/`Black`/`White`) controls behaviour when a socket is not connected.
- Per-texture info uniforms: `adsk_{sampler_name}_w`, `_h`, `_frameratio`, `_pixelratio`.

## Matte output

Set `MatteProvider="True"` on `<ShaderNodePreset>` if the Matchbox operates on alpha and the alpha must be passed to the child node; otherwise (default `False`) the child uses the matte from the Matchbox's parent. `MatteColourSpace` / `ResultColourSpace` can force output colour-space tags.

## Multipass shaders

- Split the effect into multiple `.glsl` files using the `adsk_` pass uniforms, e.g. `PyramidBlur.1.glsl`, `PyramidBlur.2.glsl`.
- In the Load Shaders browser select the **root group** `PyramidBlur.glsl` to load all passes as one effect.
- `shader_builder -p` packages everything into a single `.mx` (less confusing to load).
- In XML there is one `<Shader Index="N">` per pass (1-based). Uniforms shared between passes are defined once and marked `<Duplicate>` in later passes.
- A later pass reads an earlier pass result via the sampler `adsk_results_pass{N}` (e.g. `adsk_results_pass1`), declared and used like any sampler; its size via `adsk_results_pass{N}_w` / `_h`.
- Per-pass render target controls: `OutputBitDepth`, `OutputWidth`/`OutputHeight` (only needed on the last pass; ignored in Action/Timeline), `OutputWidthScaleFactor`/`OutputHeightScaleFactor`/`OutputScaleFactorEffect`, `OutputNbLevels` (custom mipmaps), `OutputNbResults` (multiple textures from an intermediate pass).
- Shipped examples: `PyramidBlur`, `DecodeZDepthHQ` (32-bit depth used by other passes), `MultiExecutionSeparableGaussianBlur` (execute a shader multiple times, count defined in XML — attribute not documented), `MultiTargetCustomMipmaps`, `Mipmaps`.

> Agent note (derived): a minimal two-pass legacy-GLSL pass 2 would declare `uniform sampler2D adsk_results_pass1; uniform float adsk_result_w, adsk_result_h;` and sample `adsk_results_pass1` at `gl_FragCoord.xy / vec2(adsk_result_w, adsk_result_h)`. The docs show no complete multipass source; verify against `PyramidBlur`.

## Temporal effects

- **Previous/next frames**: `adsk_previous_frame_{sampler_name}` / `adsk_next_frame_{sampler_name}` samplers. Not available when the Matchbox is loaded in Action. The current-frame sampler must be declared and used. Sampler parameters come from the `{sampler_name}` XML entry. Example: `EXAMPLES/TemporalSampling`.
- **Accumulation**: `adsk_accum_texture` (`sampler2D`, previous output of the Matchbox) and `adsk_accum_no_prev_frame` (bool, `True` if no history). XML `AccumulatePass` (accumulate an intermediate pass instead of the final result, 1-based) and `AccumulationFromStartFrame` (recursive accumulation, default `True`). Example: `EXAMPLES/Accumulate`.
- `adsk_time` (1-based float uniform) / `adsk_getTime()`.

## Adaptive degradation

Set `SupportsAdaptiveDegradation="True"` **and** branch on the `adsk_degrade` bool uniform (`True` when a degraded frame is requested) to provide a cheaper path or bypass. The XML flag alone does nothing.

## Texture grid

`adsk_texture_grid` (`sampler2D`) bundles an image file with the shader (Alias, Cineon, DPX, jpeg, Maya, OpenEXR, Pict, Pixar, SGI, Softimage, Targa, Tiff, Wavefront). Templates: `GridFetchingComp`, `GridFetchingCompMulti`, `GridFetchingReplace`.

## Contexts

XML hints on `<ShaderNodePreset>`: `SupportsAction` (usable as an Action node), `SupportsTransition` (timeline transition; see `EXAMPLES/TransitionShader`), `TimelineUseBack` (use timeline background, default `True`). Batch is always supported. Availability per product: see [README.md](README.md#availability-by-product).

## Selective FX Matchbox

A Selective FX modulates the effect with an incoming selective input (the isolation result of a Selective node), letting you modulate any shader value with it.

- Declare a `sampler2D` input with `InputType="Selective"` in the XML.
- Use the selective input so the effect applies in the **white** portion of its alpha and leaves the **black** portion intact.
- Connecting it to a Selective node in **Serial** pipeline mode connects the input automatically.
- Flame adds two parameters to the Shader section: **Mix** (global gain of the incoming isolation) and **Outside** (inverts the isolation so the effect works outside it).

## UI-only Matchbox

`EXAMPLES/UIOnly`: a Matchbox used only to provide UI for expression usage.

## Step-by-step (from the docs)

1. Write the fragment shader; save as e.g. `scale.glsl`.
2. `shader_builder -m -x scale.glsl` → compiles and writes `scale.xml`. Success output:
   ```text
   compiling shader file scale.glsl ... [OK]
   all shaders compiled ... [OK]
   generating XML interface ...
   creating XML file (scale.xml) ... [OK]
   ```
   Legacy (≤2025) warning example — the XML is still produced because it is only a warning:
   ```text
   Shader pass 0:
   Fragment info
   -------------
   0(5) : warning C7011: implicit cast from "vec4" to "vec2"
   compiling shader file scale.glsl ... [OK]
   all shaders compiled ... [OK]
   generating XML interface ...
   creating XML file (scale.xml) ... [OK]
   ```
   Same problem as of 2025.1 Update (now an error; no XML):
   ```text
   Error compiling: scale.glsl
   ERROR: 0:17: '=' :  cannot convert from ' temp highp 4-component vector of float' to ' temp highp 2-component vector of float'
   ERROR: 0:17: '' : compilation terminated
   ERROR: 2 compilation errors.  No code generated.
   ```
   `shader_builder` builds the XML only if there are no errors.
3. Fix errors and rerun.
4. Edit the XML (defaults, names, ranges, tooltips) — full example in [xml-reference.md](xml-reference.md#complete-example-matchbox-verbatim-from-creating-a-matchbox-shader).
5. Put `.glsl` + `.xml` (+ optional `.p` or `.png` thumbnail, 8-bit 128×92 PNG, same base name) in the same directory. Shipped shaders live in `/opt/Autodesk/presets/<application version>/matchbox/shaders/`.
6. Optionally package/encrypt: `shader_builder -m -p <name>.glsl` → `.mx`.
7. Test in Flame, Flare, or Flame Assist. If not visible in Load Shaders, toggle the Mode box between Matchbox and GLSL.

## Cross-version compatibility

Older-version Matchboxes work in the current version; current-version Matchboxes may not work in previous versions.

## Shipped examples

See [examples.md](examples.md#shipped-matchbox-examples) for the full list of `/opt/Autodesk/presets/<application_version>/matchbox/shaders/EXAMPLES/` shaders and what each demonstrates.

## Python API hook

`flame.batch.create_node("Matchbox", "Blur.mx")` creates a Matchbox node with a shader from the default path; `node.shader_name` returns the loaded shader name (see `../api/`).
