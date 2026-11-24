> Source: Autodesk Flame Family 2027 Help — "Creating a Matchbox Shader", "Creating a Lightbox Shader", "Matchbox Shader Examples", "Lightbox Shader Examples", "About shader_builder XML", "Shader API Documentation".

# Shader examples (verified)

Every code block below is **verbatim** from the Autodesk pages and was checked against the original HTML. Bugs present in the source are flagged with **Source bug** and a corrected line (agent correction) is given; the verbatim code is left untouched.

---

## Matchbox examples

### M1. Add two inputs (legacy GLSL)

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

**Source bug**: `input1`/`input2` are not declared. Add `uniform sampler2D input1, input2;` at the top.

### M2. Scale (legacy GLSL, "version 2025 and earlier")

```glsl
uniform float size;
uniform sampler2D myInputTex;

void main (void) {
        vec4 tex0 = texture2D(myInputTex, gl_TexCoord[0] * size);
        gl_FragColor = vec4 (tex0.rgb, 1.0);
}
```

Note: `gl_TexCoord[0] * size` is a `vec4` passed where a `vec2` is expected — this is the problem the docs' compiler output demonstrates (`warning C7011: implicit cast from "vec4" to "vec2"` in ≤2025; an error as of 2025.1 Update). Use `gl_TexCoord[0].xy * size`, or better the `gl_FragCoord`-based coordinate from M3.

### M3. Scale (modern GLSL, as of 2025.1 Update)

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

### M4. `scale.xml` sidecar for M2/M3

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

Notes: `SupportsTimeline` and `ResDependent` (spelling) are not in the XML attribute tables (which list `ResDependant`). `SoftwareVersion="2016.0.0"` is just what that old sample was built with; `shader_builder` writes the current version.

### M5. Multipass duplicate uniform (XML)

First pass `<Shader>`:

```xml
<Uniform Row="0" Col="0" Page="0" Default="True" Tooltip="" DisplayName="Filtering" Type="bool" Name="filtering">
</Uniform>
```

Second pass `<Shader>`:

```xml
<Uniform Type="bool" Name="filtering">
<Duplicate>
</Duplicate>
</Uniform>
```

### M6. Popup entry (XML)

```xml
<PopupEntry Title="ReplaceMe" Value="0">
</PopupEntry>
```

Full example shipped as `EXAMPLES/BuildList.xml`.

### M7. Previous/next frame sampler (XML fragment, verbatim — not valid standalone XML)

```xml
<Uniform Type="sampler2D" Name="adsk_previous_frame_input1"> xml entry.
<Uniform Index="0" NoInput="Error" Tooltip="" DisplayName="input1" Mipmaps="False" GL_TEXTURE_WRAP_T="GL_REPEAT" ....>
```

The first line ends with prose ("xml entry."), the second is elided (`....`). See `EXAMPLES/TemporalSampling.xml` for a real file.

---

## Lightbox examples

### L1. Invert

```glsl
vec4 adskUID_lightbox(vec4 source)
{
    source.rgb = vec3(1.0) - source.rgb;
    return source;
}
```

### L2. Gain (intentionally broken in the docs to show compiler errors)

```glsl
uniform float adskUID_gain;
vec4 adskUID_lightbox( vec4 source )
{
      source.rgb = source.rgb * adskUID_gain;
      return vec4( source.rgb, source.a )
}
```

Fix given by the docs: `return vec4( source.rgb, source.a);`. Sidecar `gain.xml` is in [lightbox.md](lightbox.md#step-by-step-from-the-docs).

### L3. Add a colour from a UI uniform

```glsl
uniform vec3 adskUID_lightColor;

vec4 adskUID_lightbox( vec4 source )
{
   vec3 resultColor = source.rgb + adskUID_lightColor;
   return vec4( resultColor, source.a );
}
```

### L4. Add red (starting user)

```glsl
vec4 adskUID_lightbox( vec4 source )
{
    vec3 red = vec3 (1.0, 0.0,0.0 );
    return vec4( source.rgb + red, source.a );
}
```

### L5. Convert lit area to YUV (starting user)

```glsl
vec4 adskUID_lightbox( vec4 source )
{
    vec3 converted_to_yuv = adsk_rgb2yuv( source.rgb )
    return vec4( converted_to_yuv, source.a );
}
```

**Source bug**: missing `;` after `adsk_rgb2yuv( source.rgb )`. Also, per the forward-declaration rule, declare `vec3 adsk_rgb2yuv( in vec3 src );` first. Corrected:

```glsl
vec3 adsk_rgb2yuv( in vec3 src );

vec4 adskUID_lightbox( vec4 source )
{
    vec3 converted_to_yuv = adsk_rgb2yuv( source.rgb );
    return vec4( converted_to_yuv, source.a );
}
```

### L6. Distance-based tint (intermediate user)

```glsl
vec3 adsk_getLightPosition(vec3 LightPos);
vec3 adsk_getVertexPosition(vec3 VertexPos);

//Used to create the near clipping plane,
//from a user interface element created by the Lightbox.
uniform float adskUID_near;

//Used to create the far clipping plane,
//from a user interface element created by the Lightbox.
uniform float adskUID_far;

//This value is from a user interface element created by the Lightbox.
uniform vec3 adskUID_tint;
vec4 adskUID_lightbox( vec4 source )
{
    vec3 colour = source.rgb;

    //We are using the Light position and vertex position information
    //to determine the distance in between the two to then allow
    //to modulate the color based on Light versus vertex distance
    float alpha = clamp(length(adsk_getLightPosition() - adsk_getVertexPosition())
                  / (adskUID_far-adskUID_near), 0.0, 1.0);
    vec3 result = colour * adskUID_tint;
    colour = mix(result, colour, alpha);

    return vec4 (colour, source.a);
}
```

**Source bug**: the forward declarations take a `vec3` parameter but the functions are called with no argument, and the Shader API defines them as `vec3 adsk_getLightPosition();` / `vec3 adsk_getVertexPosition();`. Use the API signatures:

```glsl
vec3 adsk_getLightPosition();
vec3 adsk_getVertexPosition();
```

(Despite the name `alpha`, this example modulates only colour and returns `source.a`.)

### L7. Greyscale around a target position (intermediate user)

```glsl
vec3    adsk_getVertexPosition();
float   adsk_getLuminance( vec3 rgb );
uniform float adskUID_distanceMax;
uniform vec3 adskUID_targetPosition;

vec4 adskUID_lightbox( vec4 source )
{
    vec3 vertexPos = adsk_getVertexPosition();

    // Get the radius of the effect
    float distMax = max( adskUID_distanceMax, 1.0 );

    // Get the distance from the centre of the effect
    float dist = length( vertexPos - adskUID_targetPosition );
    float alpha;
    if ( dist > distMax )
        alpha = 0.0; // outside the range of the effect
    else
        alpha = clamp( dist / distMax, 0.0, 1.0 );

    // The effect is simply a conversion to greyscale
    vec3 rgbOut = vec3( adsk_getLuminance(source.rgb) );

   //Since we edited the alpha in this Lightbox, we need to make sure
   //not to override the alphas that was calculated by the previous
   //light in the shading pipeline.
    return vec4( rgbOut, source.a * alpha );
}
```

This is the docs' model for alpha editing: always multiply by the incoming `source.a`.

### L8. Action pipeline pseudocode

Reassembled in [lightbox.md](lightbox.md#action-shading-pipeline-pseudocode-from-the-docs) (not compilable; internal functions).

---

## Presets example

See [presets.md](presets.md#example-shell-output-duotone-shader-verbatim).

---

## Shipped Matchbox examples

Location: `/opt/Autodesk/presets/<application_version>/matchbox/shaders/EXAMPLES/`

| Example | Demonstrates |
|---|---|
| `Accumulate` | Accumulation texture — use the result of the previous frame (`adsk_accum_texture`). |
| `Blending` | int popup + blend mode API (`adsk_getBlendedValue`). |
| `BuildList` | int as popup XML feature only. |
| `ColourWheel` | Colour Wheel widget in xml and glsl. |
| `ConditionalUI` | Conditional UI XML (`UICondition*`). |
| `CubeMapSampler` | Sampling from an input cube map. |
| `Curves` | Curve widget with two curve types, xml and glsl (`adskEvalDynCurves`). |
| `DecodeZDepthHQ` | Decode Action ZDepth HQ output into a 32-bit depth image used by other passes. |
| `GridFetchingComp` | Texture Grid template: comp a logo over a background. |
| `GridFetchingCompMulti` | Texture Grid template: comp up to four logos. |
| `GridFetchingReplace` | Texture Grid template: replace the input by the grid content (e.g. replace Action Lens Flare elements). |
| `ImageLighting` | A light in Matchbox. |
| `ImagePosition` | Image X/Y transforms. |
| `ImageRotation` | Image rotation. |
| `ImageScaling` | Image X/Y scaling. |
| `InputSockets` | Input socket type and colour in xml (`InputType`, `InputColor`). |
| `LightsAPI` | Accessing all light information of a scene. (Note: the Shader API page labels light functions "Lightbox Only"; this example is listed under Matchbox — see its source for what is available.) |
| `MatchboxAPI` | The different Matchbox API calls. |
| `Mipmaps` | Blur via mipmaps. |
| `MultiExecutionSeparableGaussianBlur` | Executing a shader multiple times; count defined in the XML. |
| `MultiTargetCustomMipmaps` | Custom Mipmaps feature (`OutputNbLevels`/`OutputNbResults`). |
| `PyramidBlur` | Fast-Gaussian-blur equivalent; multipass (`PyramidBlur.1.glsl`, `PyramidBlur.2.glsl`). |
| `TemporalSampling` | Previous/next frame input, xml and glsl. |
| `Trackball` | Trackball widget, xml and glsl. |
| `TransitionShader` | Transition Matchbox for the timeline. |
| `UIOnly` | Matchbox used only for UI, for expression usage. |

## Shipped Lightbox examples

Location: `/opt/Autodesk/presets/<application_version>/action/lightbox/EXAMPLES`

| Example | Demonstrates |
|---|---|
| `GGXIBLExample` | Like GGXMaterial but doesn't hijack the Material node; all controls in the Lightbox; no object texture, only a BaseColor set in the Lightbox. Un-optimised alternative IBL implementation (advanced user). |
| `GGXMaterial` | Physically based shading needing Specular, Metallic, Roughness per material, mapped as: Specular **Red** channel → Specular, Specular **Green** channel → Metallic, **Shine** → Roughness. |
| `LightboxAPISimple` | All Lightbox API calls; simple decay using vertex and light position. |
| `LightboxBasics` | Most basic Lightbox: a Gain without the API. |
| `PhysicallyBasedIBL` | Shader Physically Based mode API with Lightbox; computes IBL from these values. |
| `SimpleLight` | Re-creating an Action light with the API (also referenced for `adsk_getComputedShadowCoefficient`). |
