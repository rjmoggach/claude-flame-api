<!-- source: Autodesk Flame Family 2027 Help _ Creating a Matchbox Shader _ Autodesk.html -->
# Creating a Matchbox Shader

Here are the contents of a simple Add effect as a Matchbox shader:

`python
uniform float adsk_result_w, adsk_result_h;

void main()
{
   vec2 coords = gl_FragCoord.xy / vec2( adsk_result_w, adsk_result_h );
   vec3 sourceColor1 = texture2D(input1, coords).rgb;
   vec3 sourceColor2 = texture2D(input2, coords).rgb;

   gl_FragColor = vec4( sourceColor1+sourceColor2, 1.0 );
}
`

---

## Writing and Testing Matchbox Shader Code

A Matchbox shader is always structured as:

- A forward declaration where all the uniforms and APIs are declared.
- A `main()` function where the magic happens. Matchbox shaders are not part of an established shading pipeline like Lightbox shaders are, hence the use of `main().`

You can re-purpose existing fragment shader code, or create an effect specific to your needs.
 Important: On Linux, the supported version of GLSL is 130. Important: On macOS, you must use GLSL 120; Action does NOT comply with OpenGL core profile. You must also install an X server. Installation and download instructions are available from the X Quartz website.

### Modern GLSL Versions Support

GLSL version 460 can be used in Lightbox. See the Shader Builder documentation for more information.

Once you're done coding the shader, use shader_builder to validate and debug your code, and help you design user interface elements via a sidecar XML file. Once validated, you can encrypt and package your custom shader. shader_builder also has an extensive set of uniforms (including a number of Autodesk custom uniforms) and XML entities that allow you to:

- Define the user interface layout.
- Define parameter names.
- Define numerical intervals for specified parameters.
- Disable or hide a button based on the status of another button.
- Define a web link, to direct users to documentation on the shader you are providing.

Because Matchbox shaders can be used in Batch and Batch FX, there are some Matchbox-only uniforms:

- Setting an Input Type for a Matchbox Input socket (Front, Back, Matte).
- Defining custom colours for a Matchbox Input Socket.
- Limiting the number of Input Sockets displayed on the Matchbox node to the number of Textures required by the current shader.
 Important: A Matchbox shader can have up to 6 node inputs. While you can load in Flame a Matchbox that was designed to use more than 6 inputs, the application will disregard the extraneous inputs and only process the first 6 inputs.

### `shader_builder` Utility

The shader_builder utility is found in `/opt/Autodesk/<product_home>/bin`. To access its Help file, from the bin directory, type shader_builder --help. All this information is also available in About shader_builder XML.

The main command to process a Matchbox shader is `shader_builder -m <name of shader>.glsl`. You can use the following options with this command:

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
| -h | --help. | Displays full documentation. |

These options can be combined in one command. For example: `shader_builder -m -x <name of shader>.glsl`.
 Important: On macOS, if you get the error message `ERROR: Compiling shaders requires a valid Display`, you must install an X server. Installation and download instructions are available from the X Quartz website.

To create and test a fragment shader:

1.
Write or copy your fragment shader code in a text editor. For example, here is a scaling effect in version 2025 and earlier:

`python
uniform float size;
uniform sampler2D myInputTex;

void main (void) {
        vec4 tex0 = texture2D(myInputTex, gl_TexCoord[0] * size);
        gl_FragColor = vec4 (tex0.rgb, 1.0);
}
`

Here is the same effect using a modern GLSL version as of 2025.1 Update:

`python
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
`

2.
Save the file with the extension .glsl. For the purpose of this example, it is named `scale.glsl`.

3.
From your working directory, run your code through the `shader_builder` utility and generate a sidecar XML file. The existing shader files are located in `/opt/Autodesk/presets/<application version>/matchbox/shaders/`.

`shader_builder -m -x scale.glsl` tests the above shader and outputs the results in the shell, while generating the sidecar XML file named `scale.xml`. If everything works properly, the following appears in the Shell/Terminal:

`python
compiling shader file scale.glsl ... [OK]
all shaders compiled ... [OK]
generating XML interface ...
creating XML file (scale.xml) ... [OK]
`

If an error is detected, the following appears in version 2025 and earlier:

`python
Shader pass 0:
Fragment info
-------------
0(5) : warning C7011: implicit cast from "vec4" to "vec2"
compiling shader file scale.glsl ... [OK]
all shaders compiled ... [OK]
generating XML interface ...
creating XML file (scale.xml) ... [OK]
`

In the example above, the fourth line displays a compilation warning that you might want to fix, indicating the number of the line where the error is located. In other cases, you'll receive errors that need to be fixed; `shader_builder` builds the XML file only if it encounters no errors while testing the .glsl file.

Here is the same output for that error, but as of 2025.1 Update:

`python
Error compiling: scale.glsl
ERROR: 0:17: '=' :  cannot convert from ' temp highp 4-component vector of float' to ' temp highp 2-component vector of float'
ERROR: 0:17: '' : compilation terminated
ERROR: 2 compilation errors.  No code generated.
`
 Note: In version 2025 and earlier, some problems detected by the `shader_builder` utility issue a warning but do not prevent the compilation from completing. As of 2025.1 Update, the compilation is more strict and some previous warnings are now detected as errors, making the compilation fail.
4.
Fix any errors, and rerun the code through the `shader_builder` utility.

5.
Use the XML file generated by `shader_builder` to help you set up the user interface of the effect. This can be especially useful if different users are going to be working with these effects. In our example, you can edit `scale.xml` to add default values, better names for inputs and other user interface elements, and even tooltips to help the user.

`python
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
`

6.
Add the .glsl and sidecar .xml file to the same directory, with an optional .p or .png file to be used as a thumbnail in the Matchbox browser. The existing shader files are located in `/opt/Autodesk/presets/<application version>/matchbox/shaders/`.

7.
If you want to encrypt and package the shader in the .mx format, from that location, run `shader_builder -m -p <name of shader>.glsl`.

8.
Try your effect in Flame, Flare, or Flame Assist.

If you cannot see your shader in the Load Shaders file browser, try toggling the Mode box between Matchbox and GLSL.

To help you in creating custom shaders, example shaders are available in `/opt/Autodesk/presets/<application_version>/matchbox/shaders/EXAMPLES/`.

---

## Forward Declaration

Matchbox requires that you forward declare your uniforms and used APIs. This ensures that shader_builder provides accurate file locations for warnings and errors.

---

## Creating Multipass Shaders

In order to build more efficient, complex, or sophisticated effects, you can split your effects into multiple passes. In order to do this, you separate your effect into multiple .glsl files using advanced adsk_ uniforms. For example, the existing Pyramid Blur filter preset consists of `PyramidBlur.1.glsl` and `PyramidBlur.2.glsl`. In this case, when selecting this effect from the Load Shaders browser in the application, you need to select the root group `PyramidBlur.glsl` file to incorporate all of the passes as one effect. Use the `-p` switch to package everything into a single file, making it less confusing to load from the browser.

---

## About Cross-Version Compatibility

Due to updates to both the Matchbox API and the schema of the sidecar XML, you may not be able to use a Matchbox created for the current version in a previous version. But you can use a Matchbox created in a previous version in the current version.

---

## Optional: Create a Browser Proxy Files

Along with the .glsl and .xml files that comprise a fragment shader, you can also create a .png file that displays a proxy of your effect in the Matchbox browser.

To use a .png file as the proxy:

1. Create an 8-bit, 128 pixels wide by 92 pixels high .png
2. Place the .png file in the same folder as the .glsl and .xml files of the same name.

---

## Creating a Selective FX Matchbox

A Selective FX is a specialization of Matchbox. It modulates effect with an incoming selective input, itself the result of the isolation performed by the Selective node. This allows you to do more than traditional blending: you can now modulate any value in the shader with the result of the isolation. This allows you to have effects that leak out naturally from the isolated portion, or to have filters, such as Blur, with a clearly defined transition lines.

To create a Selective FX you declare a Selective input as `InputType` in the XML of any shader, and make sure your shader is using the incoming Selective input appropriately in the white portion of the alpha, leaving the black portion intact.

Connecting this Selective FX shader to a Selective node set to Serial pipeline mode automatically connect the input.

A Selective FX Matchbox shader has two additional parameters under the Shader section of every Matchbox shader:

- **Mix**: This enables the modulation of the intensity of the effect globally by attenuating or increasing the gain of the incoming isolation result(Selective InputType).
- **Outside**: This inverts the incoming isolation result (Selective InputType) and to allow a shader to work outside of the isolation result. This setting is very powerful as you can have effects working inside and outside of the same isolation result on the same Selective node.

## Related pages

- Matchbox Shader Examples
- Shader Builder
