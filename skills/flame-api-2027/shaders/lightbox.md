> Source: Autodesk Flame Family 2027 Help — "Creating a Lightbox Shader", "Shader Builder", "Lightbox Shader Examples" (code verified against the original HTML).

# Writing Lightbox shaders

See also: [README.md](README.md), [shader-api.md](shader-api.md) (Lightbox API: lights, normals, maps, IBL, materials, shadows), [xml-reference.md](xml-reference.md), [examples.md](examples.md).

## What a Lightbox is

A Lightbox extends Action's lighting. It is attached to (parented to) an Action **light**. Flame **appends your shader snippet to Action's fragment shader** and calls your function inside Action's lighting loop. Available in Action in Flame and Flare (not Flame Assist).

## Structure

1. A **forward declaration** of all uniforms and APIs used ("Lightbox requires that you forward declare your uniforms and used APIs" — for accurate `shader_builder` error locations).
2. The entry function:

```glsl
vec4 adskUID_lightbox( vec4 source )
```

- `source` = the incoming fragment rendered by the previous light or Lightbox in the shading pipeline.
- Return value = new colour (rgb) and alpha. The return is mixed with the input according to the **returned alpha** and the **Mix** amount from the Lightbox's Shader tab. Therefore every Lightbox **must return a valid alpha** (normally `source.a`). Overriding the alpha lets you change the shape of the light.
- No `main()`; no `gl_FragColor`.

Minimal example (invert):

```glsl
vec4 adskUID_lightbox(vec4 source)
{
    source.rgb = vec3(1.0) - source.rgb;
    return source;
}
```

## The `adskUID_` prefix rule (critical)

"The `adskUID_` prefix is required for any global symbol in the shader (functions, uniforms, constants...) because namespaces aren't available in GLSL." Every global symbol must be uniquely identified with `adskUID_`, otherwise symbols clash when the snippet is appended to the Action shader: users cannot load more than one copy of your Lightbox, and **symbol clashes disable all loaded Lightboxes**. Flame replaces `adskUID` with a unique ID per instance (pseudocode: "adskUID is replaced by UID").

```glsl
uniform vec3 adskUID_lightColor;

vec4 adskUID_lightbox( vec4 source )
{
   vec3 resultColor = source.rgb + adskUID_lightColor;
   return vec4( resultColor, source.a );
}
```

Flame API functions (`adsk_…`) are declared, not defined, by you — they keep their `adsk_` names.

## Alpha rules

- Lightbox must always return a matte (unlike Matchbox, which has `MatteProvider`).
- "Be careful to not white out the alpha, or you will lose the whole scene information whenever you use that Lightbox. Unless you are an advanced user, whenever you edit the alpha, make sure to always multiply your result by the entering alpha": `return vec4( rgbOut, source.a * alpha );`.

## GLSL versions

- Legacy: Linux GLSL 130; macOS GLSL 120 (X server / XQuartz needed for `shader_builder`).
- Modern: **only `#version 460`** (all Lightboxes are combined in one Action shader, so different recent versions cannot be mixed). Old Lightboxes (up to 130) can be merged with 460 Lightboxes. Same additional functions as Matchbox.
- The docs give no modern-GLSL Lightbox code sample. For Matchbox, modern GLSL requires uniforms in uniform blocks; whether/how this applies to Lightbox (where uniforms need the `adskUID_` prefix) is **not documented** — check shipped `EXAMPLES`.

## Light options that affect a Lightbox

Set on the parent light:

- **Pre-/Post-**: with the light active, attached Lightboxes render the pixel without (Pre) or with (Post) the light effect.
- **Lightbox Normals**: even with the light inactive, the user can choose to feed normals to the Lightbox.
- **Additive Light / Solo Light** (default Additive; query with `bool adsk_isLightAdditive()`):
  - Additive: input of the light = output of the light listed before it in the Priority Editor.
  - Solo: input = the diffuse value ("punch through").
- The **Priority Editor** lets users reorder lights and their Lightboxes; order matters.

Input colour received by a Lightbox, by [light, lightbox rendering, blend mode]:

| Light | Lightbox rendering | Blend | `source` is |
|---|---|---|---|
| inactive | n/a | additive | current fragment (un-shaded by the current light) |
| active | post-light | additive | current fragment shaded by the current light |
| inactive | n/a | solo | the diffuse value (un-shaded) |
| active | post-light | solo | the diffuse value shaded by the current light |

Related API: `adsk_isLightActive()`, `adsk_isLightboxRenderedFromDiffuse()`, `adsk_isLightboxRenderedBeforeLight()`, `adsk_getLightAlpha()`.

## Action shading pipeline (pseudocode from the docs)

Action's fragment shader has 3 blocks: (1) lighting loop (shading/IBL/shadows), (2) fog, (3) blending. Scene ambient light is processed first (when enabled), then IBL environment maps, then the light loop in Priority Editor order. The docs' commented pseudocode, reassembled (comments are the docs' prose; this is **illustrative pseudocode, not callable API** — `computeLight`, `getNbLightboxes`, `adskUID_mix`, etc. are internal):

```glsl
vec3 computeShading()
{
   vec3 shadedColor = computeSceneAmbientLight();
   shadedColor = applyIBL( shadedColor );
   for ( int i = 0; i < nbLights; ++i )
   {
      // Compute the light alpha: GMask alpha * decay * spotlightAttenuation
      float alpha = getLightAlpha( i );

      // The diffuse colour is the diffuse material colour modulated by the diffuse map.
      vec3 lightboxInputColor = isLightSolo( i ) ? getDiffuseColor() : shadedColor;

      // Light is active and renders before lightbox
      if ( isLightActive( i ) && isLightPre( i ) )
      {
         // computeLight performs the standard (non PBR) shading equation and could be
         // additive or solo. Solo replaces the current colour with the computed light colour.
         lightboxInputColor = computeLight( i, lightboxInputColor );
      }

      // If available process lightboxes.
      float nbLightboxes = getNbLightboxes( i );
      vec4 lightboxColor = vec4( lightboxInputColor, alpha );
      for ( int lx = 0; lx < nbLightboxes; ++lx )
      {
         lightboxColor = computeLightbox( lx, lightboxColor );
      }

      vec4 lightboxResultColor = lightboxColor;

      // If the "use lightbox" option is enabled, the combined lightbox effects for this
      // light can be applied according to the Lightbox effect.
      if ( useLightboxNormals( i ) ) {
         lightboxResultColor.a = mix( lightboxResultColor.a,
                                      lightboxResultColor.a * nDotL,
                                      // you can dose the shading of a lightbox.
                                      // light's lightbox panel effect numeric.
                                      getLightboxEffect( i ) );
      }

      // Light is active and renders after lightbox.
      if ( isLightActive( i ) && !isLightPre( i ) )
      {
         lightboxResultColor.rgb = computeLight( i, lightboxColor );
      }
      shadedColor = mix( lightboxInputColor, lightboxResultColor, lightboxResultColor.a );
   }
   return shadedColor;
}

vec4 computeLightbox( int lxInstance, vec4 inputColor )
{
   // adskUID is replaced by UID. Given the lx instance we find the corresponding
   // adskUID_lightbox signature.
   vec4 lightboxColor = adskUID_lightbox( inputColor );
   // Each lightbox has mix numeric in its UI. Allows you to dose the lightbox color
   // and **not** the alpha.
   return vec4( mix( inputColor.rgb, lightboxColor, adskUID_mix ), lightboxColor.a );
}

// Action fragment shader.
void main()
{
   vec4 finalColor = vec4( computeShading(), 1.0 );
   applyFog( finalColor );
   applyBlending( finalColor );
   gl_FragColor = finalColor;
}
```

Takeaways: Lightboxes on one light are chained (`source` of Lightbox N+1 is the output of Lightbox N); the Mix slider affects rgb only, not alpha; the final per-light result is `mix(input, result, result.a)`. (The pseudocode is loose with types, e.g. `mix(inputColor.rgb, lightboxColor, …)` mixes vec3 with vec4.)

## Complexity levels (from "Why Create a Lightbox")

- **Starting user**: simple colour effects using the light's controls, e.g. add red, or convert to YUV with `adsk_rgb2yuv`.
- **Intermediate user**: change the shape/decay of the light by editing the **alpha**, querying the scene (`adsk_getLightPosition()`, `adsk_getVertexPosition()`, `adsk_getLuminance()`…).
- **Advanced user**: replace Action's render calculations entirely (very expensive: effectively renders the scene twice). Example: `/opt/Autodesk/presets/<application_version>/action/lightbox/EXAMPLES/GGXIBLExample.glsl`.

Code for all of these is in [examples.md](examples.md#lightbox-examples).

## Step-by-step (from the docs)

1. Write the shader including `vec4 adskUID_lightbox( vec4 source )`. Example `gain.glsl`:
   ```glsl
   uniform float adskUID_gain;
   vec4 adskUID_lightbox( vec4 source )
   {
         source.rgb = source.rgb * adskUID_gain;
         return vec4( source.rgb, source.a )
   }
   ```
   (This sample is **intentionally broken** — missing `;` on the `return` line — to demonstrate the error output.)
2. `shader_builder -l -x gain.glsl`. Error output, version 2025 and older:
   ```text
   0(6) : error C0000: syntax error, unexpected '}', expecting ',' or ';' at token "}"
   0(2) : error C1110: function "adskUID_lightbox" has no return statement
   ```
   As of 2025.1 Update:
   ```text
   Error compiling: gain.glsl
   ERROR: 0:6: '' :  syntax error, unexpected RIGHT_BRACE, expecting COMMA or SEMICOLON
   ERROR: 1 compilation errors.  No code generated.
   ```
3. Fix: `return vec4( source.rgb, source.a);` and rerun.
4. Edit `gain.xml` (verbatim from the docs):
   ```xml
   <ShaderNodePreset
      SupportsAdaptiveDegradation="False"
      OverrideNormals="False" CommercialUsePermitted="True"
      ShaderType="Lightbox" SoftwareVersion="2016.0.0"
      LimitInputsToTexture="True" Version="1"
      Description=""
      Name="Simple Gain">
      <Shader OutputBitDepth="Output" Index="1">
         <Uniform ResDependent="None"
                  Max="100.00"
                  Min="-100.00"
                  Default="0.0" Inc="0.01"
                  Tooltip="Defines the RGB multiplier."
                  Row="0" Col="0" Page="0"
                  Type="float"
                  DisplayName="Gain"
                  Name="adskUID_gain">
         </Uniform>
      </Shader>

      <Page Name="Page 1" Page="0">
         <Col Name="Effect Settings" Col="0" Page="0">
         </Col>
      </Page>
   </ShaderNodePreset>
   ```
   Note: uniform `Name` keeps the `adskUID_` prefix exactly as in GLSL. `OverrideNormals` is not documented in the XML reference.
5. Put `.glsl` + `.xml` (+ optional 8-bit 128×92 `.png` thumbnail, same base name) in the same directory. Shipped Lightboxes: `/opt/Autodesk/presets/<application_version>/action/lightbox/` (step 3 of the docs says `.../action/lightbox/shaders/`).
6. Optionally package/encrypt: `shader_builder -l -p <name>.glsl` → `.lx`.
7. Test in Flame or Flare (Action).

## Shipped examples

`/opt/Autodesk/presets/<application_version>/action/lightbox/EXAMPLES`: `GGXIBLExample`, `GGXMaterial`, `LightboxAPISimple`, `LightboxBasics`, `PhysicallyBasedIBL`, `SimpleLight` — descriptions in [examples.md](examples.md#shipped-lightbox-examples).
