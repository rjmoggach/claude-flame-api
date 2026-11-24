<!-- source: Autodesk Flame Family 2027 Help _ Creating a Lightbox Shader _ Autodesk.html -->
# Creating a Lightbox Shader

Here are the contents of a simple invert colour effect as a Lightbox shader:

`python
vec4 adskUID_lightbox(vec4 source)
{
    source.rgb = vec3(1.0) - source.rgb;
    return source;
}
`

---

## Writing and Testing Lightbox Shader Code

A Lightbox shader is always structured as:

- A forward declaration where all the uniforms and APIs are declared.
- A `vec4 adskUID_lightbox(vec4 source)` function, where the magic happens. Lightbox shaders are part of the Action shading pipeline.

You can re-purpose existing fragment shader code, or create an effect specific to your needs.
 Important: On Linux, the supported version of GLSL is 130. Important: On macOS, you must use GLSL 120; Action does NOT comply with OpenGL core profile. You must also install an X server. Installation and download instructions are available from the X Quartz website.

### Modern GLSL Versions Support

Modern GLSL versions can be used in Matchbox. See the Shader Builder documentation for more information.

Once you're done with coding the shader, use shader_builder to validate and debug your code, and help you design user interface elements via a sidecar XML file. Once validated, you can encrypt and package your custom shader. The shader_builder utility also has an extensive set of uniforms (including a number of Autodesk custom uniforms) and XML entities that allow you to:

- Define the user interface layout.
- Define parameter names.
- Define numerical intervals for specified parameters.
- Disable or hide a button based on the status of another button.
- Define a web link, to direct users to documentation on the shader you are providing.

The shader_builder utility is found in `/opt/Autodesk/<product_home>/bin`. To access its Help file, from the bin directory, type shader_builder --help. All this information is also available in About shader_builder XML.

The main command to process a Lightbox shader is `shader_builder -l <name of shader>.glsl`. You can use the following options with this command:

| Option | Verbose | Description |
|---|---|---|
| -p | --package | Creates a '.mx' or '.lx' encrypted package file. |
| -u | --unpack | Extracts the xml and thumbnail (.png, .p) files from a '.mx' or '.lx' package file. |
| -x | --write-xml | Writes the sidecar .xml interface to a file. |
| -l | --lightbox | Sets the shader type to a lightbox operator. |
| -m | --matchbox | Sets the shader type to the standard matchbox operator. |
| -t | --preset-template | Writes the preset template to a file. |
| -o | --output | Outputs all files to another folder. |
| -d | --do-not-compile | Does not attempt compiling the shaders. Use with -p. |
| -h | --help | Displays full documentation. |

These options can be combined in one command. For example: `shader_builder -l -x <name of shader>.glsl`.
 Important: On macOS, if you get the error message `ERROR: Compiling shaders requires a valid Display`, you must install an X server. Installation and download instructions are available from the X Quartz website.

To create and test a fragment shader:

1.
Write or copy your fragment shader code in a text editor, making sure to include the main `function vec4 adskUID_lightbox ()` .

For example, here is the contents of a gain effect:

`python
uniform float adskUID_gain;
vec4 adskUID_lightbox( vec4 source )
{
      source.rgb = source.rgb * adskUID_gain;
      return vec4( source.rgb, source.a )
}
`

2.
Save the file with the extension `.glsl` .

For the purpose of this example, it is named `gain.glsl`.

3.
From your working directory, run your code through the `shader_builder` utility and generate a sidecar XML file. The existing shader files are located in `/opt/Autodesk/presets/<application version>/action/lightbox/shaders/`.

`shader_builder -l -x gain.glsl` tests the above shader and outputs the results in the shell, while generating the sidecar XML file named `gain.xml`. If an error is detected, the following appears in version 2025 and older:

`python
uniform float adskUID_gain;
vec4 adskUID_lightbox(vec4 source)
{
   source.rgb = source.rgb * adskUID_gain;
   return vec4( source.rgb, source.a)
}
python
0(6) : error C0000: syntax error, unexpected '}', expecting ',' or ';' at token "}"
0(2) : error C1110: function "adskUID_lightbox" has no return statement
`

In this case, instead of the expected xml output, we get a compilation error: line 5 in our glsl fragment is missing an ending semi-colon. Errors must be fixed for the glsl fragment to work properly in Flame. But in other cases, you will just get a compilation warning: whether such a warning can be ignored or not depends on the circumstances.

Here is the same output for that error, but as of 2025.1 Update:

`python
uniform float adskUID_gain;
vec4 adskUID_lightbox(vec4 source)
{
   source.rgb = source.rgb * adskUID_gain;
   return vec4( source.rgb, source.a)
}
python
Error compiling: gain.glsl
ERROR: 0:6: '' :  syntax error, unexpected RIGHT_BRACE, expecting COMMA or SEMICOLON
ERROR: 1 compilation errors.  No code generated.
`

4.
Fix any errors, and rerun the code through `shader_builder`. In the `gain.glsl` example, add the missing semi-colon at the end of line 5 to fix the `unexpected '\}'` error on line 6:

`python
return vec4( source.rgb, source.a);
`

5.
Use the XML file generated by shader_builder to help you set up the user interface of the effect. This can be especially useful if different users are going to be working with these effects. In our example, you can edit `gain.xml` to add default values, better names for inputs and other user interface elements, and even tooltips to help the user.

`python
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
`

6.
Add the .glsl and sidecar .xml file to the same directory, with an optional .png file to be used as a thumbnail in the Lightbox browser. The existing shader files are located in `/opt/Autodesk/presets/<application_version>/action/lightbox/`.

7.
If you want to encrypt and package the shader in the .lx format, from that location, run `shader_builder -l -p <name of shader>.glsl` .

8.
Try your effect in Flame or Flare.

To help you in creating custom shaders, example shaders are available in the `/opt/Autodesk/presets/<application_version>/action/lightbox/EXAMPLES`.

---

## Optional: Create a Browser Proxy Files

Along with the .glsl and .xml files that comprise a fragment shader, you can also create a .png file that displays a proxy of your effect in the Lightbox browser.

To use a .png file as the proxy:

1. Create an 8-bit, 128 pixels wide by 92 pixels high .png,
2. Place the .png file in the same folder as the .glsl and .xml files of the same name.

---

## Forward Declaration

Lightbox requires that you forward declare your uniforms and used APIs. This ensures that shader_builder provides accurate file locations for warnings and errors.

---

## About Lightbox Structure and the Action Shading Pipeline

Some contextual information about Action's rendering pipeline.

Action's fragment shader is split in 3 blocks:

1. Lighting loop, where shading/IBL and shadows are rendered
2. Fog
3. Blending

The Lightbox framework allows you to extend Action's lighting capabilities. By defining a function `adskUID_lightbox` in a GLSL file, Lightbox appends the shader snippet to Action's fragment shader, and can then call it within the lighting loop.

A simple Lightbox example:

`python
uniform vec3 adskUID_lightColor;

vec4 adskUID_lightbox( vec4 source )
{
   vec3 resultColor = source.rgb + adskUID_lightColor;
   return vec4( resultColor, source.a );
}
`

The `adskUID_ prefix` is required for any global symbol in the shader (functions, uniforms, constants...) because namespaces aren't available in GLSL. You must identify uniquely every global symbol in the Lightbox code with `adskUID_` to avoid symbol clashes when the shader snippet is appended to the Action shader string, or users will not be able to load more than one copy of your Lightbox in Action; symbol clashes actually disable all loaded Lightboxes.

Also, when figuring out the input of your shader, remember that the Priority Editor in Action allows the user to reorder lights and their Lightboxes: the order in which lights are applied now matters.

Finally, keep in mind that some Lightbox options are defined in the parented light and affect the behaviour of the attached Lightbox:

- **Pre-/Post-**: When the light is active, the attached Lightboxes can render the pixel without the light effect (Pre), or the Lightboxes can render the pixel with the light effect (Post).
- **Lightbox Normals**: Even with the light inactive, the user can decide to feed the normals information to the Lightbox shader. Or not.
- **Additive Light/Solo Light**: This defines the contribution of the light and its attached Lightboxes. The default is Additive. In the API, `bool adsk_isLightAdditive()` gives you its status.

  - Additive: The input of the light is the output of the light listed before it in the Priority Editor.
  - Solo: The input of the light is the diffuse value, creating a "punch through" effect.

### Lightbox Change Shader Mix

The `vec4source` is the incoming fragment rendered by the previous light or Lightbox in the shading pipeline. The return value is mixed according to the alpha returned by the function and the mix amount from the Lightbox's Shader tab. This alpha blending is the reason why every Lightbox must return a valid `source.a` . Actually, you can override the shape of the light by overriding the alpha component of `return vec4` with an alpha of your own, computed within the Lightbox.

### Lightbox Processing Pipeline

Below is commented pseudocode that should help you understand the Lightbox processing pipeline.

When enabled, the scene ambient light is the first light to be processed. IBL environment maps are then processed next for all other lights. The light loop compute shadings and lightbox sorted according to priority editor.

`python
vec3 computeShading()
{
   vec3 shadedColor = computeSceneAmbientLight();
   shadedColor = applyIBL( shadedColor );
   for ( int i = 0; i < nbLights; ++i )
   {
`

The light user interface settings are:

- [ light : {active, inactive},
- lightbox rendering : {pre, post lighting},
- light blend mode: {additive, solo} ]

The different combinations that can affect the input colours to lightbox:

1. [inactive, n/a, additive] : the current fragment (un-shaded by the current light)
2. [active, post-light, additive] : the current fragment (shaded by the current light)
3. [inactive, n/a, solo] : simply the diffuse value (un-shaded)
4. [active, post-light, solo] : the diffuse value shaded by the current light.

Compute the light alpha: GMask alpha * decay * spotlightAttenuation

`python
      float alpha = getLightAlpha( i );
`

The diffuse colour is the diffuse material colour modulated by the diffuse map.

`python
      vec3 lightboxInputColor = isLightSolo( i ) ? getDiffuseColor() : shadedColor;
`

Light is active and renders before lightbox

`python
      if ( isLightActive( i ) && isLightPre( i ) )
      {
`

computeLight performs the standard (non PBR) shading equation and could be additive or solo. Solo replaces the current colour with the computed light colour.

`python
         lightboxInputColor = computeLight( i, lightboxInputColor );
      }
`

If available process lightboxes.

`python
      float nbLightboxes = getNbLightboxes( i );
      vec4 lightboxColor = vec4( lightboxInputColor, alpha );
      for ( int lx = 0; lx < nbLightboxes; ++lx )
      {
         lightboxColor = computeLightbox( lx, lightboxColor );
      }

      vec4 lightboxResultColor = lightboxColor;
`

If the "use lightbox" option is enabled, the combined lightbox effects for this light can be applied according to the Lightbox effect.

`python
      if ( useLightboxNormals( i ) ) {
         lightboxResultColor.a = mix( lightboxResultColor.a,
                                      lightboxResultColor.a * nDotL,
                                      // you can dose the shading of a lightbox.
                                      // light's lightbox panel effect numeric.
                                      getLightboxEffect( i ) );
      }
`

Light is active and renders after lightbox.

`python
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
`

adskUID is replaced by UID. Given the lx instance we find the corresponding adskUID_lightbox signature.

`python
   vec4 lightboxColor = adskUID_lightbox( inputColor );
`

Each lightbox has mix numeric in its UI. Allows you to dose the lightbox color and **not** the alpha.

`python
   return vec4( mix( inputColor.rgb, lightboxColor, adskUID_mix ), lightboxColor.a );
}
`

Action fragment shader.

`python
void main()
{
   vec4 finalColor = vec4( computeShading(), 1.0 );
   applyFog( finalColor );
   applyBlending( finalColor );
   gl_FragColor = finalColor;
}
`

---

## Why Create a Lightbox

Lightbox is a unique blend of concepts inherited from 3D lighting, colour grading, and Photoshop adjustment layers, delivering an entirely new take on look development for images and 3D geometry. The Lightbox framework provides users the ability to define custom colour lighting effects within Action, Flame's 3D compositing engine.

When working within Lightbox, defining the task to accomplish will help you measure the complexity of the task at hand.

### Starting User

You want to create simple effects to relight your scene; inverse the colours of a specific object, in the scene using all the familiar light controls and behaviours, taking into account the characteristics of the object such as its specularity and normals. For example, the following Lightbox adds red colours wherever it is pointed.

`python
vec4 adskUID_lightbox( vec4 source )
{
    vec3 red = vec3 (1.0, 0.0,0.0 );
    return vec4( source.rgb + red, source.a );
}
`

It is a very simple Lightbox, but it goes to show that you do not need complex mathematics to create one.

Or you can leverage the available Lightbox API to change colour space, as in the following example, where the lighted area is converted from RGB to YUV.

`python
vec4 adskUID_lightbox( vec4 source )
{
    vec3 converted_to_yuv = adsk_rgb2yuv( source.rgb )
    return vec4( converted_to_yuv, source.a );
}
`

But whereas Matchbox can use the MatteProvider xml property to define whether a children node should use its matte or not, Lightbox must always return a matte. And this brings us to the second type of user.

### Intermediate User

You need to modify the shape or other parameters of the light, such as decay, and this means actually editing the alpha of the Lightbox.

In the example below, the Lightbox queries the Action scene to do more advanced processing while still using the Lighting framework.

`python
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
`

In another example, a simple greyscale effect is applied to a target offset, defined by the end-user using adskUID_targetPosition.

`python
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
`
 Note: Be careful to not white out the alpha, or you will lose the whole scene information whenever you use that Lightbox. Unless you are an advanced user, whenever you edit the alpha, make sure to always multiply your result by the entering alpha, as in the example above: `source.a * alpha`.

### Advanced User

The advanced user wants to actually modify the rendering pipeline, ignoring all that was computed upstream from the light, and substitute their own render calculations. This is possible because lighting calculations happen at the end of the rendering pipeline, and means . While this is an interesting proposition that allows truly unique renders, it is also a very expensive one, computationally speaking. The Action render pipeline is static, and substituting your own methods by using a Lightbox essentially means rendering a scene twice: once by Action, and once again by the Lightbox.

While creating such a Lightbox is possible, it is way beyond the scope of this document. But there is an expansive, un-optimized example available, providing an alternative to the current IBL implementation. See `/opt/Autodesk/presets/<application_version>/action/lightbox/EXAMPLES/GGXIBLExample.glsl`.

## Related pages

- Lightbox Shader Examples
- Shader Builder
