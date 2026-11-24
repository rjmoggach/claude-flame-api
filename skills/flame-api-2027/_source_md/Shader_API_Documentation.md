<!-- source: Autodesk Flame Family 2027 Help _ Shader API Documentation _ Autodesk.html -->
# Shader API Documentation

In the following API, all positions and directions are in camera space: their local positions are multiplied by the modelView matrix. Apart from that, most of the calls are self- explanatory or are mapped directly to the UI.
 Note: Any uniform with a name that starts with `adsk_` is not shown in the user interface.

---

## Lighting and Shading (Lightbox Only)

`vec3 adsk_getNormal();`

Returns unaltered interpolated normal, before any maps are applied. Use adsk_getComputedNormal to get the value computed after the maps. The normal, binormal and tangent form an orthonormal basis where the origin is at the vertex position.

`vec3 adsk_getComputedNormal();`

Returns the computed normal once the maps are applied. Use adsk_getNormal to get the value before the maps.

`vec3 adsk_getBinormal();`

Returns the interpolated binormal.

`vec3 adsk_getTangent();`

Returns the interpolated tangent.

`vec3 adsk_getVertexPosition();`

Returns the interpolated vertex position for the current fragment after all maps have been processed.

`vec3 adsk_getCameraPosition();`

Returns the camera position.

`bool adsk_isLightActive();`

Returns the activity status of the parent light.

`bool adsk_isLightAdditive();`

Returns TRUE if the light attached to the Lightbox is set as additive, or FALSE if the light is set to solo.

`vec3 adsk_getLightPosition();`

Returns the position of the light attached to the Lightbox.

`vec3 adsk_getLightColour();`

Returns the colour of the light parented to the Lightbox, but modulated by the intensity (lightColour * intensity).

`vec3 adsk_getLightDirection();`

Returns the direction of the light attached to the Lightbox, if that light is directional. The direction is computed whether the light is in target or free mode.

`vec3 adsk_getLightTangent();`

Given the light direction, the light tangent vector is an orthogonal vector where the origin is at the light position. For example, given the light direction looking down negative z-axis. The light tangent would be the x-axis.

`void adsk_getLightShadowDecayType( out int lightDecayType, out int shadowDecayType );`

Returns the type of decay selected by the user for the light parented to the Lighbox, using Profile > Decay Type box.

- `const int NO_DECAY = 0;`
- `const int LINEAR_DECAY = 1;`
- `const int QUADRATIC_DECAY = 2;`
- `const int CUBIC_DECAY = 3;`
- `const int EXP_DECAY = 4;`
- `const int EXP2_DECAY = 5;float adsk_getLightDecayRate();`

Returns the decay rate selected by the user for the light parented to the Lighbox, using Profile > Decay field.

`bool adsk_isSpotlightFalloffParametric();`

Returns TRUE if the user set Profile > Falloff Model box to Parametric for the light parented to the Lightbox. Returns FALSE if the user set the Falloff Model box to Custom.

`float adsk_getSpotlightParametricFalloffIn();`

Returns the value selected by the user for Profile > Falloff In field. Only enabled if adsk_isSpotlightFalloffParametric returns TRUE.

`float adsk_getSpotlightParametricFalloffOut();`

Returns the value selected by the user for Profile > Falloff Out field. Only enabled if adsk_isSpotlightFalloffParametric returns TRUE.

`float adsk_getSpotlightSpread();`

Returns the spread angle selected by the user for Basics > Spread field.

`float adsk_getLightAlpha();`

Returns the precomputed alpha of the light attached to the Lightbox, calculated from its cutoff, decay, and GMask.

`bool adsk_isPointSpotLight();`

Returns TRUE if the user sets Basics > Light Type box to Point/Spot for the light parented to the Lightbox.

`bool adsk_isDirectionalLight();`

Returns TRUE if the user sets Basics > Light Type box to Directional for the light parented to the Lightbox .

`bool adsk_isAmbientLight();`

Returns TRUE if the user sets Basics > Light Type box to Ambient for the light parented to the Lightbox .

`bool adsk_isAreaRectangleLight();`

Returns TRUE if the user sets Basics > Light Type box to Rectangle Area for the light parented to the Lightbox .

`bool adsk_isAreaEllipseLight();`

Returns TRUE if the user sets Basics > Light Type box to Ellipse Area for the light parented to the Lightbox.

`float adsk_getAreaLightWidth();`

Returns the width of the light attached to the Lightbox. Only applicable if adsk_isAreaRectangleLight or adsk_isAreaEllipseLight is TRUE.

`float adsk_getAreaLightHeight();`

Returns the height of the light attached to the Lightbox. Only applicable if adsk_isAreaRectangleLight or adsk_isAreaEllipseLight is TRUE.

`bool adsk_isLightboxRenderedFromDiffuse();`

Returns FALSE if the Lightbox is rendered from the currently lit fragment. Returns TRUE if Lightbox is being applied on the unlit raw diffuse value.

`bool adsk_isLightboxRenderedBeforeLight();`

Returns FALSE if the Lightbox is rendered after the attached light.

`vec3 adsk_getComputedDiffuse();`

Returns the computed diffuse value for the current fragment, before shading but after all the maps have been processed.

`float adsk_getShininess();`

Returns the shininess material property.

`vec3 adsk_getComputedSpecular();`

Returns the computed specular value for the current fragment, before shading but after all the maps have been processed.

---

## Map Access (Lightbox Only)

The getMapValue functions give raw access to the texture maps. The getMapCoord functions return the interpolated coordinates used to fetch in those texture maps. The coordinates need to be safe divided (to avoid divisions by 0) by the returned z value to get a UV texture coordinate.

`vec4 adsk_getComputedDiffuseMapValue (in vec3 vertexPos);`

Returns the computed diffuse map value once all maps have been processed.

The following return the raw map values. Use the getMapCoord functions below to compute the texture map coordinates (texCoord) required for the current fragment.

- `vec4 adsk_getDiffuseMapValue (in vec2 texCoord);`
- `vec4 adsk_getEmissiveMapValue (in vec2 texCoord);`
- `vec4 adsk_getSpecularMapValue (in vec2 texCoord);`
- `vec4 adsk_getNormalMapValue (in vec2 texCoord);`
- `vec4 adsk_getReflectionMapValue (in vec2 texCoord);`
- `vec4 adsk_getUVMapValue (in vec2 texCoord);`
- `vec4 adsk_getParallaxMapValue (in vec2 texCoord);`

The following return the interpolated coordinates that will need to be safe divided by z to fetch the corresponding map value for the current fragment.

- `vec3 adsk_getDiffuseMapCoord();`
- `vec3 adsk_getEmissiveMapCoord();`
- `vec3 adsk_getSpecularMapCoord();`
- `vec3 adsk_getNormalMapCoord();`
- `vec3 adsk_getParallaxMapCoord();vec2 adsk_getReflectionMapCoord( in vec3 vrtPos, in vec3 normal );`

---

## Transforms (Lightbox Only)

`mat4 adsk_getModelViewMatrix();`

Converts local coordinates to camera space.

`mat4 adsk_getModelViewInverseMatrix();`

Converts camera space to local coordinates.

---

## Image Based Lighting (Lightbox Only)
Note: There is significant performance degradation with shaders that use an IBL-based API call if that shader is used in combination with Hardware Anti-Aliasing and high resolution maps. To mitigate this, disable HWAA, or use lower-resolution maps.

`int adsk_getNumberIBLs();`

Returns the supported the number of IBL maps.

`bool adsk_isCubeMapIBL( in int idx );`

Returns TRUE of the IBL map with the `idx` index is Cubic. FALSE if the map is Angular or Cylindrical. If both `adsk_isAngularMapIBL` and `adsk_isCubeMapIBL` are FALSE, the map is Cylindrical.

`bool adsk_isAngularMapIBL( in int idx );`

Returns TRUE of the IBL map with the `idx` index is Angular. FALSE if the map is Cubic or Cylindrical. If both `adsk_isAngularMapIBL` and `adsk_isCubeMapIBL` are FALSE, the map is Cylindrical.

`vec3 adsk_getCubeMapIBL( in int idx, in vec3 coords, float lod );`

Where lod is the Level of Detail of the IBL with the `idx` index.

`vec3 adsk_getAngularMapIBL( in int idx, in vec2 coords, float lod );`

Where lod is the Level of Detail of the IBL with the `idx` index.

`bool adsk_isAmbientIBL( in int idx );`

Returns TRUE if the IBL mapping option is set to Ambient, FALSE if it is set to Reflection.

`float adsk_getIBLDiffuseOffset( in int idx );`

The Diffuse Offset defined in the user interface for the IBL with the `idx` index.

`mat4 adsk_getIBLRotationMatrix( in int idx );`

The rotation matrix defined in the user interface for the IBL with the `idx` index.

---

## Material Information (Lightbox Only)

`vec4 adsk_getMaterialDiffuse();`

Material node's Diffuse property.

`vec4 adsk_getMaterialSpecular();`

Material node's Specular property.

`vec4 adsk_getMaterialAmbient();`

Material node's Ambient property.

`float adsk_getMaterialRoughness();`

Material node's Roughness property.

`float adsk_getMaterialSpecularity();`

Material node's Specularity property.

`float adsk_getMaterialMetalness();`

Material node's Metalness property.

`float adsk_getMaterialAnisotropy();`

Material node's Anisotropy property.

`float adsk_getMaterialSubSurfaceScattering();`

Material node's Sub-Surface Scattering property.

---

## Colour Management and Colour Space Conversion (Lightbox and Matchbox)

The following return the value of a curve uniform in the user interface (dynCurveId) read at x.

- `float adskEvalDynCurves(in int dynCurveId, in float x);`
- `vec2 adskEvalDynCurves(in ivec2 dynCurveId, in vec2 x);`
- `vec3 adskEvalDynCurves(in ivec3 dynCurveId, in vec3 x);`
- `vec4 adskEvalDynCurves(in ivec4 dynCurveId, in vec4 x);vec3 adsk_scene2log( in vec3 src );`

Converts src from scene linear colour space to Cineon log colour space. Inverse operation of adsk_log2scene.

`vec3 adsk_log2scene( in vec3 src );`

Converts src from Cineon log colour space to scene linear colour space. Inverse operation of adsk_scene2log.

`vec3 adsk_rgb2hsv( in vec3 src );`

Converts src from RGB colour space to HSV colour space. Inverse operation of adsk_hsv2rgb.

`vec3 adsk_hsv2rgb( in vec3 src );`

Converts src from HSV colour space to RGB colour space. Inverse operation of adsk_rgb2hsv.

`vec3 adsk_rgb2yuv( in vec3 src );`

Converts src from RGB colour space to YUV colour space. Inverse operation of adsk_yuv2rgb.

`vec3 adsk_yuv2rgb( in vec3 src );`

Converts src from YUV colour space to RGB colour space. Inverse operation of adsk_rgb2yuv.

`vec3 adsk_getLuminanceWeights();`

Returns the weights used to compute the Luminance value.

`float adsk_getLuminance( in vec3 color );`

Returns the luminance value.

`float adsk_highlights( in float pixel, in float halfPoint );`

Parametric blending curves suitable for blending effects for Shadows, Midtones, Highlights. The parameters are:

- **pixel**: the colour of the pixel.
- **halfpoint**: the X-axis location where the curve is 50% .

To get the midtone weight, you compute for the same pixel colour: `1 - adsk_shadows - adsk_highlightsfloat adsk_shadows( in float pixel, in float halfPoint );`

Parametric blending curves suitable for blending effects for Shadows (of the Shadows-Midtones-Highlights triumvirate). The parameters are:

- **pixel**: the colour of the pixel.
- **halfpoint**: the X-axis location where the curve is 50%.

To get the midtone weight, you compute for the same pixel colour: `1 - adsk_shadows - adsk_highlights`

---

## Shadows (Lightbox Only)

`vec3 adsk_getComputedShadowCoefficient();`

Returns a coefficient which is computed from all the shadow parameters. The coefficient needs to be multiplied against the light colour. The parent light must be a shadow caster. See the example `/action/lightbox/EXAMPLES/SimpleLight.glsl`.

---

## Blending (Lightbox and Matchbox)

`vec4 adsk_getBlendedValue( int blendType, vec4 srcColor, vec4 dstColor );`

Blends srcColor and dstColor using the blendType.

- Add = 0
- Sub = 1
- Multiply = 2
- LinearBurn = 10
- Spotlight = 11
- Flame_SoftLight = 13
- HardLight = 14
- PinLight = 15
- Screen = 17
- Overlay = 18
- Diff = 19
- Exclusion = 20
- Flame_Max = 29
- Flame_Min = 30
- PsLinearLight = 32
- LighterColor = 33
- LinearLight = 37
 Note: In versions older than 2025.1 Update, the LinearLight option was used to recreate the Photoshop Linear Light blend mode. This option is now named PsLinearLight and the LinearLight option is used for the Flame Linear Light blend mode, which gives the same result as the Photoshop one without any clamping.

---

## General Purpose (Lightbox Only)

`bool adsk_isSceneLinear();`

Return TRUE if the Action scene is in linear colour space, or FALSE if Log.

---

## General Purpose (Lightbox and Matchbox)

`float adsk_getTime();`

Returns the current time as a frame number. 1-based float.

---

## General Purpose (Matchbox Only)

The following float uniforms are unconditionally sent to each pass. You can use them in the shader you are creating, if needed. Unless indicated otherwise, the following uniforms are only available to Matchbox shaders.

The following can be used to set the result resolution.

- `adsk_result_w`
- `adsk_result_h`
- `adsk_result_frameratio`
- `adsk_result_pixelratioadsk_results_pass{pass_index}();`

Can be used to refer to a previous pass result texture. For example, `adsk_results_pass1` refers to the first pass result and can be used in any subsequent pass. The sampler must be declared and used normally.

`adsk_results_pass{pass_index}_w adsk_results_pass{pass_index}_h`

Can be used to refer to a previous pass result texture size.

`adsk_previous_frame_{sampler_name}(); adsk_next_frame_{sampler_name}();`

Not available if the Matchbox is loaded in Action.

Can be used to fetch the texture of the previous or next `{sampler_name}`frame. All uniform sampler parameters for previous and next will come from the `{sampler_name}` uniform xml entry. For example, to use both current and previous frames given a sampler input1 the XML entries would look like this.

`python
<Uniform Type="sampler2D" Name="adsk_previous_frame_input1"> xml entry.
<Uniform Index="0" NoInput="Error" Tooltip="" DisplayName="input1" Mipmaps="False" GL_TEXTURE_WRAP_T="GL_REPEAT" ....>
`
 Note: Requires that the sampler `sampler_name` for the current frame be declared and used in the fragment shader. Refer to `/opt/Autodesk/presets/<application_version>/matchbox/shaders/EXAMPLES/TemporalSampling.xml` for an example.

`adsk_time`

This 1-based float uniform can be used to obtain the current time in the timebar.

`bool adsk_degrade();`

This boolean uniform can be used to obtain the process degradation setting. When True, a degraded frame was requested. When False, a full rendered frame or a preview frame was requested.

`float adsk_{sampler_name}_w (); float adsk_{sampler_name}_h ();`

This uniform gives access to each texture's resolution. For example, `adsk_frontTex_w` and `adsk_frontTex_h` refer to the resolution of the sampler2D named frontTex.

`float adsk_{sampler_name}_frameratio`

This gives access to texture frame ratio. For instance, `adsk_frontTex_frameratio`refers to the frame ratio of the sampler2D named frontTex.

`float adsk_{sampler_name}_pixelratio`

This gives access to texture pixel ratio. For instance, `adsk_frontTex_pixelratio` refers to the pixel ratio of the sampler2D named frontTex.

`adsk_accum_texture`

sampler2D that contains the previous output of the matchbox. Useful when creating temporal effects. Turns on the support for adaptive degradation.

`adsk_accum_no_prev_frame`

Boolean uniform. True if there is no history available. Uniform is useful together with `adsk_accum_texture`.

`adsk_texture_grid`

Sampler2D used to bundle an image file with your Matchbox shader. The following format are supported:

- Alias
- Cineon
- DPX
- jpeg
- Maya
- OpenEXR
- Pict
- Pixar
- SGI
- Softimage
- Targa
- Tiff
- Wavefront

## Related pages

- Shader Builder
