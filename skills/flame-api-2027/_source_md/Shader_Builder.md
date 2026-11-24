<!-- source: Autodesk Flame Family 2027 Help _ Shader Builder _ Autodesk.html -->
# Shader Builder

A great benefit of working with customized shaders in Autodesk Flame, Flare, and Flame Assist is being able to create your own effects, depending on your particular needs. Creating a custom shader can be as simple as copying and pasting GLSL code snippets, or it can be a complex multi-pass effect with multiple inputs and dozens of user interface elements. Custom shaders can also be encrypted for distribution.
 Tip: You can find many shaders by visiting the community-driven shader repository at https://logik-matchbook.org/ and in the Logik Portal. You can download free shaders created by fellow users, or share your own custom shaders with other users.

Here's the high-level workflow to follow when creating custom shaders:

1.
Write or copy/paste GLSL fragment shader code.

2.
Use the provided shader_builder command-line tool to test the shader and generate XML files for the user interface and optional presets displayed in the application.

3.
Fix any errors in the GLSL code.

4.
Edit the XML output from the shader_builder to customize the user interface and optional presets.

5.
Package and maybe encrypt the XML and GLSL code together.

Matchbox and Lightbox availability depends on the application being used.

| Product | Lightbox (in Action) | Matchbox (in Action) | Matchbox (in Batch/BFX) | Matchbox (in Timeline) | Matchbox (in Modular Keyer) | Matchbox (in Tools tab) |
|---|---|---|---|---|---|---|
| Flame | Available | Available | Available | Available | Available | Available |
| Flare | Available | Available | Available | Available (as source in Batch) | Available | Not Available |
| Flame Assist | Not Available | Not Available | Available (BFX only) | Available | Available | Not Available |

---

## Action Single Panel User Interface

To support the Action Single Panel user interface, a shader page now has three different names, defined in its associated XML file:

-
<Name>: This name is used when all 6 columns of a page are displayed at once. This is the name used in the expanded user interface.

-
<ColName0_2>: This name is used for the page that contains the first 3 columns of a shader page, like in Action Dual Panel user interface.

-
<ColName3_5>: This name is used for the page that contains the last 3 columns of a shader page, like in Action Dual Panel user interface.

---

## What is GLSL?

GLSL stands for OpenGL Shading Language, and is a language based on C syntax.

GLSL was created to facilitate the manipulation of the graphics pipeline by developers, without requiring deep machine code knowledge. In GLSL, normals, texture maps, complex vector and matrices operations are all central to language, making the creation of shaders simpler. The specifications for OpenGL and GLSL can be found at the OpenGL Foundation website.

Lightbox and Matchbox shaders are all GLSL-created shaders.

You will also find resources on the web, such as Lighthouse 3D. When looking for online resources, keep in mind that on Linux the supported version of GLSL is 130. If you want your Lightbox (or Matchbox) snippet to run on macOS, you must use GLSL version 120.

### Modern GLSL Versions for Matchbox

The GLSL versions 430, 440, 450, and 460 can be used in Matchbox shaders, making additional functions such as these available:

- Double precision for many mathematics, vector and matrix functions
- Packing, unpacking and bit functions
- Atomic functions
- Matrix determinant
- Fused Multiply-Add

For more details and a complete list of available functions, see the GLSLangSpec document for the version of your choice.
 Note: The shader version must be specified using a "#version" directive in each glsl file header. Warning: It is important to declare the uniforms inside a uniform block to respect the Vulkan and SPIR-V rules.

### Modern GLSL Versions for Lightbox

GLSL version 460 can be used in Lightbox shaders.

Contrary to Matchbox, Lightbox supports only version 460 of GLSL. This is a limitation caused by the fact that multiple shaders are combined in an Action scene and it is not possible to combine shaders from different recent versions. However, old Lightbox shaders (up to version 130) can be merged with Lightbox shaders using GLSL version 460.
 Note: The list of newly available functions is the same as for Matchbox.

For more details and a complete list of available functions, see the GLSLangSpec.4.60.pdf document.

## Related pages

- Creating a Matchbox Shader
- Creating a Lightbox Shader
- Creating Presets for a Shader
- About shader_builder XML
- Shader API Documentation
