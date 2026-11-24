<!-- source: Autodesk Flame Family 2027 Help _ Lightbox Shader Examples _ Autodesk.html -->
# Lightbox Shader Examples

To help you in creating custom Lightbox shaders, examples are available in the `/opt/Autodesk/presets/<application_version>/action/lightbox/EXAMPLES`.

The following example Lightbox shaders are available:

#### GGXIBLExample

Similar to GGXMaterial, but it doesn't hijack the Material node, and all controls are present in the Lightbox itself. Also, it doesn't support object texture and only a BaseColor which is set in the Lightbox itself.

#### GGXMaterial

This shader performs a rendering of the scene using a physically based shading algorithm which requires three distinct values from each material in the scene: the Specular, Metallic, and Roughness component values. These components are not available natively in the Material settings, so they are mapped as followed in the GGXMaterial Lightbox shader: Specular Red Channel for the Specular value, the Specular Green Channel for the Metallic value, and the Shine parameter to define the Roughness.

#### LightboxAPISimple

This shader shows all possible API calls to the Lightbox API and shows a simple decay example using vertex and light position.

#### LightboxBasics

This is the most basic usage of Lightbox, only applying a Gain without having to use the API at all.

#### PhysicallyBasedIBL

Shows how to use the Shader Physically Based mode API with Lightbox; in this case, it is computing the IBL based on these values.

#### SimpleLight

This is an example of re-creating an Action light in Lightbox using the API.

## Related pages

- Creating a Lightbox Shader
