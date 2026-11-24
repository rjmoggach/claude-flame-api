> Source: Autodesk Flame Family 2027 Help — "Shader API Documentation" (verified against the original HTML; the Markdown conversion had merged several adjacent signatures, which are separated here).

# Shader API (`adsk_*` functions and uniforms) — Matchbox & Lightbox

General rules from the source:
- All positions and directions are in **camera space** (local positions multiplied by the modelView matrix).
- Any uniform whose name starts with `adsk_` is **not shown in the UI** (and is not considered by `shader_builder`).
- Matchbox and Lightbox require **forward declaration** of every uniform and every API function used (see [matchbox.md](matchbox.md#forward-declaration), [lightbox.md](lightbox.md#structure)).

Scope legend: **LB** = Lightbox only, **MB** = Matchbox only, **LB+MB** = both.

## Index (alphabetical)

`adskEvalDynCurves` · `adsk_accum_no_prev_frame` · `adsk_accum_texture` · `adsk_degrade` · `adsk_getAngularMapIBL` · `adsk_getAreaLightHeight` · `adsk_getAreaLightWidth` · `adsk_getBinormal` · `adsk_getBlendedValue` · `adsk_getCameraPosition` · `adsk_getComputedDiffuse` · `adsk_getComputedDiffuseMapValue` · `adsk_getComputedNormal` · `adsk_getComputedShadowCoefficient` · `adsk_getComputedSpecular` · `adsk_getCubeMapIBL` · `adsk_getDiffuseMapCoord` · `adsk_getDiffuseMapValue` · `adsk_getEmissiveMapCoord` · `adsk_getEmissiveMapValue` · `adsk_getIBLDiffuseOffset` · `adsk_getIBLRotationMatrix` · `adsk_getLightAlpha` · `adsk_getLightColour` · `adsk_getLightDecayRate` · `adsk_getLightDirection` · `adsk_getLightPosition` · `adsk_getLightShadowDecayType` · `adsk_getLightTangent` · `adsk_getLuminance` · `adsk_getLuminanceWeights` · `adsk_getMaterialAmbient` · `adsk_getMaterialAnisotropy` · `adsk_getMaterialDiffuse` · `adsk_getMaterialMetalness` · `adsk_getMaterialRoughness` · `adsk_getMaterialSpecular` · `adsk_getMaterialSpecularity` · `adsk_getMaterialSubSurfaceScattering` · `adsk_getModelViewInverseMatrix` · `adsk_getModelViewMatrix` · `adsk_getNormal` · `adsk_getNormalMapCoord` · `adsk_getNormalMapValue` · `adsk_getNumberIBLs` · `adsk_getParallaxMapCoord` · `adsk_getParallaxMapValue` · `adsk_getReflectionMapCoord` · `adsk_getReflectionMapValue` · `adsk_getShininess` · `adsk_getSpecularMapCoord` · `adsk_getSpecularMapValue` · `adsk_getSpotlightParametricFalloffIn` · `adsk_getSpotlightParametricFalloffOut` · `adsk_getSpotlightSpread` · `adsk_getTangent` · `adsk_getTime` · `adsk_getUVMapValue` · `adsk_getVertexPosition` · `adsk_highlights` · `adsk_hsv2rgb` · `adsk_isAmbientIBL` · `adsk_isAmbientLight` · `adsk_isAngularMapIBL` · `adsk_isAreaEllipseLight` · `adsk_isAreaRectangleLight` · `adsk_isCubeMapIBL` · `adsk_isDirectionalLight` · `adsk_isLightActive` · `adsk_isLightAdditive` · `adsk_isLightboxRenderedBeforeLight` · `adsk_isLightboxRenderedFromDiffuse` · `adsk_isPointSpotLight` · `adsk_isSceneLinear` · `adsk_isSpotlightFalloffParametric` · `adsk_log2scene` · `adsk_next_frame_{sampler_name}` · `adsk_previous_frame_{sampler_name}` · `adsk_result_frameratio` · `adsk_result_h` · `adsk_result_pixelratio` · `adsk_result_w` · `adsk_results_pass{pass_index}` · `adsk_results_pass{pass_index}_h` · `adsk_results_pass{pass_index}_w` · `adsk_rgb2hsv` · `adsk_rgb2yuv` · `adsk_scene2log` · `adsk_shadows` · `adsk_texture_grid` · `adsk_time` · `adsk_yuv2rgb` · `adsk_{sampler_name}_frameratio` · `adsk_{sampler_name}_h` · `adsk_{sampler_name}_pixelratio` · `adsk_{sampler_name}_w`

---

## Lighting and Shading (LB)

| Signature | Description |
|---|---|
| `vec3 adsk_getNormal();` | Unaltered interpolated normal, **before** any maps are applied. Normal, binormal and tangent form an orthonormal basis with origin at the vertex position. Use `adsk_getComputedNormal` for the post-map value. |
| `vec3 adsk_getComputedNormal();` | Computed normal **once the maps are applied**. |
| `vec3 adsk_getBinormal();` | Interpolated binormal. |
| `vec3 adsk_getTangent();` | Interpolated tangent. |
| `vec3 adsk_getVertexPosition();` | Interpolated vertex position for the current fragment after all maps have been processed. |
| `vec3 adsk_getCameraPosition();` | Camera position. |
| `bool adsk_isLightActive();` | Activity status of the parent light. |
| `bool adsk_isLightAdditive();` | `TRUE` if the light attached to the Lightbox is set as additive, `FALSE` if set to solo. |
| `vec3 adsk_getLightPosition();` | Position of the light attached to the Lightbox. |
| `vec3 adsk_getLightColour();` | Colour of the parent light modulated by intensity (`lightColour * intensity`). |
| `vec3 adsk_getLightDirection();` | Direction of the attached light, if directional. Computed whether the light is in target or free mode. |
| `vec3 adsk_getLightTangent();` | Orthogonal vector to the light direction, origin at the light position (e.g. light looking down −Z → tangent is the X axis). |
| `void adsk_getLightShadowDecayType( out int lightDecayType, out int shadowDecayType );` | Decay type chosen in the parent light's Profile > Decay Type box. Values: see decay constants below. |
| `float adsk_getLightDecayRate();` | Decay rate from Profile > Decay field of the parent light. |
| `bool adsk_isSpotlightFalloffParametric();` | `TRUE` if Profile > Falloff Model = Parametric; `FALSE` if Custom. |
| `float adsk_getSpotlightParametricFalloffIn();` | Profile > Falloff In value. Only enabled if `adsk_isSpotlightFalloffParametric()` is `TRUE`. |
| `float adsk_getSpotlightParametricFalloffOut();` | Profile > Falloff Out value. Only enabled if `adsk_isSpotlightFalloffParametric()` is `TRUE`. |
| `float adsk_getSpotlightSpread();` | Spread angle from Basics > Spread field. |
| `float adsk_getLightAlpha();` | Precomputed alpha of the attached light, from its cutoff, decay, and GMask. |
| `bool adsk_isPointSpotLight();` | `TRUE` if Basics > Light Type = Point/Spot. |
| `bool adsk_isDirectionalLight();` | `TRUE` if Light Type = Directional. |
| `bool adsk_isAmbientLight();` | `TRUE` if Light Type = Ambient. |
| `bool adsk_isAreaRectangleLight();` | `TRUE` if Light Type = Rectangle Area. |
| `bool adsk_isAreaEllipseLight();` | `TRUE` if Light Type = Ellipse Area. |
| `float adsk_getAreaLightWidth();` | Width of the attached light. Only applicable if `adsk_isAreaRectangleLight` or `adsk_isAreaEllipseLight` is `TRUE`. |
| `float adsk_getAreaLightHeight();` | Height of the attached light. Same applicability as width. |
| `bool adsk_isLightboxRenderedFromDiffuse();` | `FALSE` if rendered from the currently lit fragment; `TRUE` if applied on the unlit raw diffuse value. |
| `bool adsk_isLightboxRenderedBeforeLight();` | Returns `FALSE` if the Lightbox is rendered after the attached light. (Source documents only the `FALSE` case; `TRUE` presumably = rendered before.) |
| `vec3 adsk_getComputedDiffuse();` | Computed diffuse for the current fragment, before shading but after all maps processed. |
| `float adsk_getShininess();` | Shininess material property. |
| `vec3 adsk_getComputedSpecular();` | Computed specular for the current fragment, before shading but after all maps processed. |

### Decay type constants (for `adsk_getLightShadowDecayType`)

Listed in the source exactly as:

```glsl
const int NO_DECAY = 0;
const int LINEAR_DECAY = 1;
const int QUADRATIC_DECAY = 2;
const int CUBIC_DECAY = 3;
const int EXP_DECAY = 4;
const int EXP2_DECAY = 5;
```

> Agent note: the source does not say whether these constants are predefined by Flame or must be declared in your shader. In a Lightbox every global symbol you declare must be `adskUID_`-prefixed, so if you declare your own constants, prefix them (e.g. `const int adskUID_NO_DECAY = 0;`) or compare against the integer literals.

## Map Access (LB)

The `get*MapValue` functions give raw access to texture maps. The `get*MapCoord` functions return interpolated coordinates; **safe-divide** (avoid division by 0) `.xy` by the returned `z` to obtain a UV texture coordinate.

| Signature | Description |
|---|---|
| `vec4 adsk_getComputedDiffuseMapValue (in vec3 vertexPos);` | Computed diffuse map value once all maps have been processed. |
| `vec4 adsk_getDiffuseMapValue (in vec2 texCoord);` | Raw diffuse map value. |
| `vec4 adsk_getEmissiveMapValue (in vec2 texCoord);` | Raw emissive map value. |
| `vec4 adsk_getSpecularMapValue (in vec2 texCoord);` | Raw specular map value. |
| `vec4 adsk_getNormalMapValue (in vec2 texCoord);` | Raw normal map value. |
| `vec4 adsk_getReflectionMapValue (in vec2 texCoord);` | Raw reflection map value. |
| `vec4 adsk_getUVMapValue (in vec2 texCoord);` | Raw UV map value. |
| `vec4 adsk_getParallaxMapValue (in vec2 texCoord);` | Raw parallax map value. |
| `vec3 adsk_getDiffuseMapCoord();` | Interpolated coords (divide by z) for the diffuse map. |
| `vec3 adsk_getEmissiveMapCoord();` | … emissive map. |
| `vec3 adsk_getSpecularMapCoord();` | … specular map. |
| `vec3 adsk_getNormalMapCoord();` | … normal map. |
| `vec3 adsk_getParallaxMapCoord();` | … parallax map. |
| `vec2 adsk_getReflectionMapCoord( in vec3 vrtPos, in vec3 normal );` | Reflection map coordinate from a vertex position and normal (returns `vec2`). |

> Agent note (derived): typical use is `vec3 c = adsk_getDiffuseMapCoord(); vec2 uv = c.xy / (c.z != 0.0 ? c.z : 1.0); vec4 v = adsk_getDiffuseMapValue(uv);` — the exact safe-divide strategy is not specified in the source.

## Transforms (LB)

| Signature | Description |
|---|---|
| `mat4 adsk_getModelViewMatrix();` | Converts local coordinates to camera space. |
| `mat4 adsk_getModelViewInverseMatrix();` | Converts camera space to local coordinates. |

## Image Based Lighting (LB)

Performance note: significant degradation when an IBL API call is used together with Hardware Anti-Aliasing and high-resolution maps; disable HWAA or use lower-resolution maps.

| Signature | Description |
|---|---|
| `int adsk_getNumberIBLs();` | Number of supported IBL maps. |
| `bool adsk_isCubeMapIBL( in int idx );` | `TRUE` if IBL `idx` is Cubic; `FALSE` if Angular or Cylindrical. If both `adsk_isAngularMapIBL` and `adsk_isCubeMapIBL` are `FALSE`, the map is Cylindrical. |
| `bool adsk_isAngularMapIBL( in int idx );` | `TRUE` if IBL `idx` is Angular; `FALSE` if Cubic or Cylindrical. |
| `vec3 adsk_getCubeMapIBL( in int idx, in vec3 coords, float lod );` | Sample cube-map IBL `idx`; `lod` = level of detail. |
| `vec3 adsk_getAngularMapIBL( in int idx, in vec2 coords, float lod );` | Sample angular IBL `idx`; `lod` = level of detail. |
| `bool adsk_isAmbientIBL( in int idx );` | `TRUE` if the IBL mapping option is Ambient, `FALSE` if Reflection. |
| `float adsk_getIBLDiffuseOffset( in int idx );` | Diffuse Offset set in the UI for IBL `idx`. |
| `mat4 adsk_getIBLRotationMatrix( in int idx );` | Rotation matrix set in the UI for IBL `idx`. |

No sampling function for Cylindrical IBLs is documented.

## Material Information (LB)

| Signature | Material node property |
|---|---|
| `vec4 adsk_getMaterialDiffuse();` | Diffuse |
| `vec4 adsk_getMaterialSpecular();` | Specular |
| `vec4 adsk_getMaterialAmbient();` | Ambient |
| `float adsk_getMaterialRoughness();` | Roughness |
| `float adsk_getMaterialSpecularity();` | Specularity |
| `float adsk_getMaterialMetalness();` | Metalness |
| `float adsk_getMaterialAnisotropy();` | Anisotropy |
| `float adsk_getMaterialSubSurfaceScattering();` | Sub-Surface Scattering |

## Shadows (LB)

| Signature | Description |
|---|---|
| `vec3 adsk_getComputedShadowCoefficient();` | Coefficient computed from all shadow parameters; multiply it against the light colour. The parent light must be a shadow caster. Example: `/action/lightbox/EXAMPLES/SimpleLight.glsl`. |

## General Purpose (LB)

| Signature | Description |
|---|---|
| `bool adsk_isSceneLinear();` | `TRUE` if the Action scene is in linear colour space, `FALSE` if Log. |

## Curves, Colour Management and Colour Space Conversion (LB+MB)

| Signature | Description |
|---|---|
| `float adskEvalDynCurves(in int dynCurveId, in float x);` | Value of curve uniform `dynCurveId` (a UI curve, see XML `ValueType="Curve"`) read at `x`. |
| `vec2 adskEvalDynCurves(in ivec2 dynCurveId, in vec2 x);` | 2 curves. |
| `vec3 adskEvalDynCurves(in ivec3 dynCurveId, in vec3 x);` | 3 curves. |
| `vec4 adskEvalDynCurves(in ivec4 dynCurveId, in vec4 x);` | 4 curves. |
| `vec3 adsk_scene2log( in vec3 src );` | Scene linear → Cineon log. Inverse of `adsk_log2scene`. |
| `vec3 adsk_log2scene( in vec3 src );` | Cineon log → scene linear. Inverse of `adsk_scene2log`. |
| `vec3 adsk_rgb2hsv( in vec3 src );` | RGB → HSV. Inverse of `adsk_hsv2rgb`. |
| `vec3 adsk_hsv2rgb( in vec3 src );` | HSV → RGB. |
| `vec3 adsk_rgb2yuv( in vec3 src );` | RGB → YUV. Inverse of `adsk_yuv2rgb`. |
| `vec3 adsk_yuv2rgb( in vec3 src );` | YUV → RGB. |
| `vec3 adsk_getLuminanceWeights();` | Weights used to compute luminance. |
| `float adsk_getLuminance( in vec3 color );` | Luminance value. |
| `float adsk_highlights( in float pixel, in float halfPoint );` | Parametric blending curve for Highlights. `pixel` = pixel colour; `halfPoint` = X location where the curve is 50%. |
| `float adsk_shadows( in float pixel, in float halfPoint );` | Parametric blending curve for Shadows. Same parameters. |

Midtone weight (for the same pixel colour): `1 - adsk_shadows - adsk_highlights`.

Note the curve function is `adskEvalDynCurves` (no underscore after `adsk`).

## Blending (LB+MB)

`vec4 adsk_getBlendedValue( int blendType, vec4 srcColor, vec4 dstColor );` — blends `srcColor` and `dstColor` using `blendType`:

| `blendType` | Mode |
|---|---|
| 0 | Add |
| 1 | Sub |
| 2 | Multiply |
| 10 | LinearBurn |
| 11 | Spotlight |
| 13 | Flame_SoftLight |
| 14 | HardLight |
| 15 | PinLight |
| 17 | Screen |
| 18 | Overlay |
| 19 | Diff |
| 20 | Exclusion |
| 29 | Flame_Max |
| 30 | Flame_Min |
| 32 | PsLinearLight |
| 33 | LighterColor |
| 37 | LinearLight |

Only these values are documented (gaps such as 3–9 are not). Since 2025.1 Update: `PsLinearLight` (32) = Photoshop Linear Light; `LinearLight` (37) = Flame Linear Light (same result as Photoshop without clamping). Before 2025.1 Update, `LinearLight` meant the Photoshop mode. See shipped example `Blending` (popup + blend API).

## General Purpose (LB+MB)

| Signature | Description |
|---|---|
| `float adsk_getTime();` | Current time as a frame number. 1-based float. |

## General Purpose (MB) — Flame-provided uniforms

"The following float uniforms are unconditionally sent to each pass." Unless indicated otherwise, Matchbox only. Declare the ones you use (see Agent note below on notation).

| Name (as written in source) | Kind | Description |
|---|---|---|
| `adsk_result_w` | float uniform | Result width — "can be used to set the result resolution". |
| `adsk_result_h` | float uniform | Result height. |
| `adsk_result_frameratio` | float uniform | Result frame ratio. |
| `adsk_result_pixelratio` | float uniform | Result pixel ratio. |
| `adsk_results_pass{pass_index}();` | sampler (texture of a previous pass) | Refers to a previous pass result texture, e.g. `adsk_results_pass1` = first pass result, usable in any subsequent pass. "The sampler must be declared and used normally." |
| `adsk_results_pass{pass_index}_w` `adsk_results_pass{pass_index}_h` | uniforms | Size of a previous pass result texture. |
| `adsk_previous_frame_{sampler_name}();` `adsk_next_frame_{sampler_name}();` | sampler | Previous / next frame of input `{sampler_name}`. **Not available if the Matchbox is loaded in Action.** Sampler parameters come from the `{sampler_name}` uniform's XML entry. Requires the current-frame sampler `{sampler_name}` to be declared **and used** in the fragment shader. Example: `EXAMPLES/TemporalSampling.xml`. |
| `adsk_time` | float uniform (1-based) | Current time in the timebar. |
| `bool adsk_degrade();` | bool uniform | Process degradation setting: `True` = a degraded frame was requested; `False` = full render or preview frame. Pair with XML `SupportsAdaptiveDegradation="True"`. |
| `float adsk_{sampler_name}_w (); float adsk_{sampler_name}_h ();` | float uniforms | Resolution of each texture, e.g. `adsk_frontTex_w`, `adsk_frontTex_h` for `sampler2D frontTex`. |
| `float adsk_{sampler_name}_frameratio` | float uniform | Frame ratio of a texture, e.g. `adsk_frontTex_frameratio`. |
| `float adsk_{sampler_name}_pixelratio` | float uniform | Pixel ratio of a texture, e.g. `adsk_frontTex_pixelratio`. |
| `adsk_accum_texture` | `sampler2D` | Previous output of the Matchbox (temporal effects). "Turns on the support for adaptive degradation." See XML `AccumulatePass`, `AccumulationFromStartFrame`, example `Accumulate`. |
| `adsk_accum_no_prev_frame` | bool uniform | `True` if no history is available. Use with `adsk_accum_texture`. |
| `adsk_texture_grid` | `sampler2D` | Bundles an image file with your Matchbox shader. Supported formats: Alias, Cineon, DPX, jpeg, Maya, OpenEXR, Pict, Pixar, SGI, Softimage, Targa, Tiff, Wavefront. Examples: `GridFetchingComp`, `GridFetchingCompMulti`, `GridFetchingReplace`. How the image file is associated with the shader is not described on this page. |

XML for previous/next frame samplers — **verbatim from the source** (it is a fragment, not valid standalone XML; the first line ends with the prose words "xml entry." and the second is elided with `....`):

```xml
<Uniform Type="sampler2D" Name="adsk_previous_frame_input1"> xml entry.
<Uniform Index="0" NoInput="Error" Tooltip="" DisplayName="input1" Mipmaps="False" GL_TEXTURE_WRAP_T="GL_REPEAT" ....>
```

> Agent note (interpretation): the intent appears to be: the XML contains a `<Uniform Type="sampler2D" Name="adsk_previous_frame_input1">` entry alongside the normal full `<Uniform … Type="sampler2D" Name="input1">` entry, and the previous/next-frame sampler inherits its sampler parameters from the `input1` entry. Consult the shipped `TemporalSampling.xml` / `.glsl` for the exact form.

> Agent note (notation): the source writes several items with `()` (e.g. `adsk_results_pass{pass_index}();`, `bool adsk_degrade();`, `float adsk_{sampler_name}_w ();`) while describing them as **uniforms/samplers**. Only `adsk_getTime()` (and the other `adsk_get*`/`adsk_is*` items) are described as functions. Declare the uniforms as uniforms, e.g.:
>
> ```glsl
> uniform float adsk_result_w, adsk_result_h;   // verbatim from the Matchbox example
> uniform sampler2D adsk_results_pass1;         // "declared and used normally"
> uniform float adsk_frontTex_w, adsk_frontTex_h;
> uniform bool adsk_degrade;
> uniform float adsk_time;
> ```
>
> With modern GLSL (`#version 430+`), non-sampler uniforms must be inside a uniform block (the docs' example uses `layout( binding = 1 ) uniform AdskUniformBlock { float adsk_result_w, adsk_result_h; };`). See [matchbox.md](matchbox.md#modern-glsl-430460).
