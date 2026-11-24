<!-- source: Autodesk Flame Family 2027 Help _ Creating Presets for a Shader _ Autodesk.html -->
# Creating Presets for a Shader

You can create presets from the settings in a shader directly from within the application. Users of your shader can then select different starting points, by selecting Sepia in the Duotone shader, for example.

Creating presets requires the use of a working shader within the application.

To create shader presets:

1.
Within the application, load the Matchbox or Lightbox shader that you want to create presets for.

2.
Use the existing shader menu settings to create the exact look you want.
 Note: Curve position and tangent menu settings are not supported in shader presets.
3.
Click the UI XML Shell Printout button (found within the Node Prefs menu, or within the Shader tab if accessed from Action). If you launched the software from a shell command, this shell is used for the output (on a Mac workstation, it is preferable to launch the application from a shell command to avoid issues in the preset shell output).

4.
Navigate to the shell to find the XML output for the preset you created. For example, here is the shell output for a new preset in the Duotone shader:

Copy&Paste this XML in the preset file:

`python
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
`
 Tip: A user can perform the above steps and send you this shell output for you to include as a preset in future iterations of your shader.
5.
Copy and paste the contents into an XML file, changing Preset Name to something more meaningful. You can have multiple `<Preset Name> </Preset>` instances within a file, as long as they are within a `<Presets> </Presets>` tag.

You can also create a blankpreset.xml template from an existing GLSL with the –t option, and use this to paste the shell output.

6.
Name the XML file as `<name of shader>.preset.xml`, and include this file when packaging your shader.

7.
The next time the shader is loaded in the application, the new preset is available from the Presets list.

## Related pages

- Shader Builder
