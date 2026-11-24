> Source: PyCoNode: Action Nodes Attributes

# Action object (PyCoNode) attributes (node-specific)

Per Action object (node inside an Action/Image/GMask Tracer schematic, class `flame.PyCoNode`): only attributes NOT in the common Action set (see `README.md` → "Common Action object attributes"). Section names are the source section titles with the trailing " Attributes" removed.

Values column: `Min: x; Max: y` = numeric range; backticked items = accepted values or (min tuple; max tuple) for tuple ranges; `None` = source gives no range.

## 3D Path

Common attrs: all 6. No node-specific attributes.

## 3D Shape

Common attrs: all 6.

| attr | type | description | value range |
|---|---|---|---|
| `text` | `unicode` | The text string of the 3D Text node. | None |

## 3D Text

Common attrs: all 6.

| attr | type | description | value range |
|---|---|---|---|
| `text` | `unicode` | The text string of the 3D Text node. | None |

## Analyzer

Common attrs: all 6. No node-specific attributes.

## Atomize

Common attrs: all 6. No node-specific attributes.

## Axis

Section appears 5x in source with identical content (deduplicated here). Common attrs: all 6. Common attr(s) with a different definition here: `position` (listed below).

| attr | type | description | value range |
|---|---|---|---|
| `position` | `tuple` | **Differs from common definition.** The Position attribute of the Axis node in the Action 3D space. | `(-1000000.0, -1000000.0, -1000000.0)`; `(1000000.0, 1000000.0, 1000000.0)` |
| `center` | `tuple` | The Center attribute of the Axis node in the Action 3D space. | `(-1000000.0, -1000000.0, -1000000.0)`; `(1000000.0, 1000000.0, 1000000.0)` |
| `shear` | `tuple` | The Shear attribute of the Axis node in the Action 3D space. | `(-1000000.0, -1000000.0, -1000000.0)`; `(1000000.0, 1000000.0, 1000000.0)` |
| `scale` | `tuple` | The Scale attribute of the Axis node in the Action 3D space. | `(-1000000.0, -1000000.0, -1000000.0)`; `(1000000.0, 1000000.0, 1000000.0)` |
| `rotation` | `tuple` | The Rotation attribute of the Axis node in the Action 3D space. | `(-1000000.0, -1000000.0, -1000000.0)`; `(1000000.0, 1000000.0, 1000000.0)` |

## Blooming

Common attrs: all 6. No node-specific attributes.

## Border FX

Common attrs: all 6. No node-specific attributes.

## Camera

Common attrs: all 6. Common attr(s) with a different definition here: `position` (listed below).

| attr | type | description | value range |
|---|---|---|---|
| `physical_camera_active` | `bool` | The Physical Camera Mode attribute of the Camera Action node. With this True, `film_type`, `fstop`, and `focal` are active. | `True`; `False` |
| `film_type` | `str` | The Focal attribute of the Camera Action node. Only active when `physical_camera_active` is True. | `35mm Full`; `35mm Pana`; `35mm Vista`; `16mm`; `Super 16`; `65mm Pana`; `65mm Imax`; `User-Defined` |
| `fstop` | `str` | The f-stop attribute of the Camera Action node. Only active when `physical_camera_active` is True. | `f-stop 1`; `f-stop 1.4`; `f-stop 2`; `f-stop 2.8`; `f-stop 4`; `f-stop 5.6`; `f-stop 8`; `f-stop 11`; `f-stop 16`; `f-stop 22`; `f-stop 32` |
| `focal` | `float` | The Focal attribute of the Camera Action node. Only active when `physical_camera_active` is True. | Min: 1.0; Max: 91615.0 |
| `fov` | `float` | The FOV (Field Of View) attribute of the Camera node. | Min: 0.01; Max: 179.5 |
| `near` | `float` | The Near clipping plane attribute of the Camera node. | Min: 0.00999999977648; Max: 1000000.0 |
| `far` | `float` | The Far clipping plane attribute of the Camera node. | Min: 0.019999999553; Max: 1000000.0 |
| `target_mode` | `bool` | The Targeting Mode attribute of the Camera node. True = Target, False = Free | `True`; `False` |
| `position` | `tuple` | **Differs from common definition.** The Position attribute of the Camera node in the Action 3D space. | `(-1000000.0, -1000000.0, -1000000.0)`; `(1000000.0, 1000000.0, 1000000.0)` |
| `rotation` | `tuple` | The Rotation attribute of the Camera node in the Action 3D space. Only active when `target_mode` = False. | `(-1000000.0, -1000000.0, -1000000.0)`; `(1000000.0, 1000000.0, 1000000.0)` |
| `interest` | `tuple` | The Interest attribute of the Camera node. Only active when `target_mode` = True. | `(-1000000.0, -1000000.0, -1000000.0)`; `(1000000.0, 1000000.0, 1000000.0)` |
| `distance` | `float` | The Distance attribute of the Camera node. Only active when `target_mode` = False. | Min: -1000000.0; Max: 1000000.0 |
| `roll` | `float` | The Roll attribute of the Camera node. Only active when `target_mode` = True. | Min: -1000000.0; Max: 1000000.0 |

## Camera 3D

Common attrs: all 6. Common attr(s) with a different definition here: `position` (listed below).

| attr | type | description | value range |
|---|---|---|---|
| `position` | `tuple` | **Differs from common definition.** The Position attribute of the Camera 3D node in the Action 3D space. | `(-1000000.0, -1000000.0, -1000000.0)`; `(1000000.0, 1000000.0, 1000000.0)` |
| `rotation` | `tuple` | The Rotation attribute of the Camera 3D node in the Action 3D space. | `(-1000000.0, -1000000.0, -1000000.0)`; `(1000000.0, 1000000.0, 1000000.0)` |
| `rotation_order` | `str` | The Rotation Order attribute of the Camera 3D node in the Action 3D space. | `Rot XYZ`; `Rot YZX`; `Rot ZXY`; `Rot XZY`; `Rot YXZ`; `Rot ZYX` |
| `aim` | `tuple` | The Aim attribute of the Camera 3D node in the Action 3D space. | `(-1000000.0, -1000000.0, -1000000.0)`; `(1000000.0, 1000000.0, 1000000.0)` |
| `scale` | `tuple` | The Scale attribute of the Camera 3D node in the Action 3D space. | `(-1000000.0, -1000000.0, -1000000.0)`; `(1000000.0, 1000000.0, 1000000.0)` |
| `shear` | `tuple` | The Shear attribute of the Camera 3D node in the Action 3D space. | `(-1000000.0, -1000000.0, -1000000.0)`; `(1000000.0, 1000000.0, 1000000.0)` |
| `camera_scale` | `float` | The Camera Scale attribute of the Camera 3D node in the Action 3D space. | Min: -1000000.0; Max: 1000000.0 |
| `roll` | `float` | The Roll attribute of the Camera 3D node. | Min: -1000000.0; Max: 1000000.0 |
| `up` | `tuple` | The Up attribute of the Camera 3D node. | `(-1000000.0, -1000000.0, -1000000.0)`; `(1000000.0, 1000000.0, 1000000.0)` |
| `focal` | `float` | The Focal length attribute of the Camera 3D node. | Min: 1.0; Max: 91615.0 |
| `fov` | `float` | The FOV (Field Of View) attribute of the Camera 3D node. | Min: 0.01; Max: 179.5 |
| `near` | `float` | The Near clipping plane attribute of the Camera 3D node. | Min: 0.00999999977648; Max: 1000000.0 |
| `far` | `float` | The Far clipping plane attribute of the Camera 3D node. | Min: 0.019999999553; Max: 1000000.0 |
| `gate_type` | `str` | The Film Gate Type attribute of the Camera 3D node. | `User`; `16mm Theatrical`; `Super 16mm`; `35mm Academy`; `35mm TV Proj`; `35mm Full`; `35mm 1.85`; `35mm Anamorphic`; `70mm Proj`; `VistaVision`; `Imax` |
| `gate_fit_type` | `str` | The Film Gate Resolution Fit Type attribute of the Camera 3D node. | `Fill`; `Horizontal`; `Vertical`; `Overscan` |
| `aperture_x` | `float` | The Aperture X attribute of the Camera 3D node. | Min: -1000000.0; Max: 1000000.0 |
| `aperture_y` | `float` | The Aperture Y attribute of the Camera 3D node. | Min: -1000000.0; Max: 1000000.0 |
| `film_fit_offset` | `float` | The Film Fit Offset attribute of the Camera 3D node. | Min: -1000000.0; Max: 1000000.0 |
| `film_aspect` | `float` | The Film Aspect attribute of the Camera 3D node. | Min: -1000000.0; Max: 1000000.0 |
| `lens_squeeze` | `float` | The Lens Squeeze attribute of the Camera 3D node. | Min: -1000000.0; Max: 1000000.0 |
| `film_roll` | `float` | The Lens Film Roll attribute of the Camera 3D node. | Min: -1000000.0; Max: 1000000.0 |
| `film_offset_x` | `float` | The Film Offset X attribute of the Camera 3D node. | Min: -1000000.0; Max: 1000000.0 |
| `film_offset_y` | `float` | The Film Offset Y attribute of the Camera 3D node. | Min: -1000000.0; Max: 1000000.0 |
| `film_translate_x` | `float` | The Film Translate X attribute of the Camera 3D node. | Min: -1000000.0; Max: 1000000.0 |
| `film_translate_y` | `float` | The Film Translate Y attribute of the Camera 3D node. | Min: -1000000.0; Max: 1000000.0 |
| `film_roll_pivot_x` | `float` | The Film Roll Pivot X attribute of the Camera 3D node. | Min: -1000000.0; Max: 1000000.0 |
| `film_roll_pivot_y` | `float` | The Film Roll Pivot Y attribute of the Camera 3D node. | Min: -1000000.0; Max: 1000000.0 |
| `pre_scale` | `float` | The Pre Scale attribute of the Camera 3D node. | Min: -1000000.0; Max: 1000000.0 |
| `post_scale` | `float` | The Post Scale attribute of the Camera 3D node. | Min: -1000000.0; Max: 1000000.0 |
| `interaxial` | `float` | The Interaxial attribute of the Camera 3D node. | Min: -1000000.0; Max: 1000000.0 |
| `zero_parallax` | `float` | The Zero Parallax attribute of the Camera 3D node. | Min: -1000000.0; Max: 1000000.0 |
| `toe_in_adjust` | `float` | The Toe In Adjust attribute of the Camera 3D node. | Min: -1000000.0; Max: 1000000.0 |
| `film_offset_left` | `float` | The Film Offset Left attribute of the Camera 3D node. | Min: -1000000.0; Max: 1000000.0 |
| `film_offset_right` | `float` | The Film Offset Right attribute of the Camera 3D node. | Min: -1000000.0; Max: 1000000.0 |

## Compass

Common attrs: all 6.

| attr | type | description | value range |
|---|---|---|---|
| `colour` | `tuple` | The Colour attribute of the Compass node. | `(0.0, 0.0, 0.0)`; `(1.0, 1.0, 1.0)` |
| `width` | `int` | The Width attribute of the Compass node. | Min: 1.0; Max: 10000.0 |
| `height` | `int` | The Height attribute of the Compass node. | Min: 1.0; Max: 10000.0 |

## Deform Mesh

Common attrs: all 6. No node-specific attributes.

## Diffuse Map

Common attrs: all 6. No node-specific attributes.

## Displace Map

Common attrs: all 6. No node-specific attributes.

## Emissive Map

Common attrs: all 6. No node-specific attributes.

## Surface

Common attrs: all 6. No node-specific attributes.

## Glint Texture

Common attrs: all 6. No node-specific attributes.

## Glow Texture

Common attrs: all 6. No node-specific attributes.

## GMask

Common attrs: all 6. No node-specific attributes.

## IBL

Common attrs: all 6.

| attr | type | description | value range |
|---|---|---|---|
| `use_as_back` | `bool` | The Use As Back attribute of the IBL node. | `True`; `False` |

## Iris Texture

Common attrs: all 6. No node-specific attributes.

## Lens Flare

Common attrs: all 6. No node-specific attributes.

## Lens Texture

Common attrs: all 6. No node-specific attributes.

## Light

Common attrs: all 6. Common attr(s) with a different definition here: `position` (listed below).

| attr | type | description | value range |
|---|---|---|---|
| `light_type` | `str` | The Light Type attribute of the Light node. | `Point / Spot`; `Directional`; `Ambient`; `Rectangle Area`; `Ellipse Area` |
| `active` | `bool` | The Active attribute of the Light node. | `True`; `False` |
| `intensity` | `float` | The Intensity attribute of the Light node. | Min: -3.40282346639e+38; Max: 3.40282346639e+38 |
| `colour` | `tuple` | The Colour attribute of the Light node. | `(0.0, 0.0, 0.0)`; `(1.0, 1.0, 1.0)` |
| `width` | `float` | The Width attribute of the Light node. | Min: 1.0; Max: 10000.0 |
| `height` | `float` | The Height attribute of the Light node. | Min: 1.0; Max: 10000.0 |
| `spread` | `float` | The Spread attribute of the Light node. | Min: 0.0; Max: 180.0 |
| `shade` | `float` | The Shade attribute of the Light node. | Min: 0.0; Max: 100.0 |
| `decay_type` | `str` | The Decay Type attribute of the Light node. | `No Decay`; `Linear Decay`; `Quadratic Decay`; `Cubic Decay`; `Exp Decay`; `Exp2 Decay` |
| `decay` | `float` | The Decay attribute of the Light node. | Min: 0.0; Max: 10000.0 |
| `attenuation` | `float` | The Attenuation attribute of the Light node. | Min: 0.0; Max: 100.0 |
| `falloff` | `float` | The Fall Off attribute of the Light node. | Min: 0.0; Max: 100.0 |
| `falloff_in` | `float` | The Attenuation attribute of the Light node. | Min: 0.0; Max: 100.0 |
| `falloff_out` | `float` | The Attenuation attribute of the Light node. | Min: 0.0; Max: 100.0 |
| `target_mode` | `bool` | The Target Mode attribute of the Light node. True = Target, False = Free | `True`; `False` |
| `position` | `tuple` | **Differs from common definition.** The Position attribute of the Light node. | `(-1000000.0, -1000000.0, -1000000.0)`; `(1000000.0, 1000000.0, 1000000.0)` |
| `rotation` | `tuple` | The Rotation attribute of the Light node. Only active when `target_mode` = False. | `(-1000000.0, -1000000.0, -1000000.0)`; `(1000000.0, 1000000.0, 1000000.0)` |
| `interest` | `tuple` | The Interest attribute of the Light node. Only active when `target_mode` = True. | `(-1000000.0, -1000000.0, -1000000.0)`; `(1000000.0, 1000000.0, 1000000.0)` |
| `distance` | `float` | The Distance attribute of the Light node. Only active when `target_mode` = False. | Min: -1000000.0; Max: 1000000.0 |
| `roll` | `float` | The Roll attribute of the Light node. Only active when `target_mode` = True. | Min: -1000000.0; Max: 1000000.0 |

## Matchbox

Common attrs: all 6. No node-specific attributes.

## Material

Common attrs: all 6. No node-specific attributes.

## Motion Vectors Map

Common attrs: all 6. No node-specific attributes.

## Normal Map

Common attrs: all 6. No node-specific attributes.

## Object ID Map

Common attrs: all 6. No node-specific attributes.

## Parallax Map

Common attrs: all 6. No node-specific attributes.

## Particle Animator

Common attrs: all 6. Common attr(s) with a different definition here: `position` (listed below).

| attr | type | description | value range |
|---|---|---|---|
| `position` | `tuple` | **Differs from common definition.** The Position attribute of the Axis node in the Action 3D space. | `(-1000000.0, -1000000.0, -1000000.0)`; `(1000000.0, 1000000.0, 1000000.0)` |
| `center` | `tuple` | The Center attribute of the Axis node in the Action 3D space. | `(-1000000.0, -1000000.0, -1000000.0)`; `(1000000.0, 1000000.0, 1000000.0)` |
| `shear` | `tuple` | The Shear attribute of the Axis node in the Action 3D space. | `(-1000000.0, -1000000.0, -1000000.0)`; `(1000000.0, 1000000.0, 1000000.0)` |
| `scale` | `tuple` | The Scale attribute of the Axis node in the Action 3D space. | `(-1000000.0, -1000000.0, -1000000.0)`; `(1000000.0, 1000000.0, 1000000.0)` |
| `rotation` | `tuple` | The Rotation attribute of the Axis node in the Action 3D space. | `(-1000000.0, -1000000.0, -1000000.0)`; `(1000000.0, 1000000.0, 1000000.0)` |

## Particle Bouncer

Common attrs: all 6. No node-specific attributes.

## Particle Generator

Common attrs: all 6. No node-specific attributes.

## PBS Map

Common attrs: all 6. No node-specific attributes.

## Perspective Grid

Common attrs: all 6. Common attr(s) with a different definition here: `position` (listed below).

| attr | type | description | value range |
|---|---|---|---|
| `position` | `tuple` | **Differs from common definition.** The Position attribute of the Axis node in the Action 3D space. | `(-1000000.0, -1000000.0, -1000000.0)`; `(1000000.0, 1000000.0, 1000000.0)` |
| `center` | `tuple` | The Center attribute of the Axis node in the Action 3D space. | `(-1000000.0, -1000000.0, -1000000.0)`; `(1000000.0, 1000000.0, 1000000.0)` |
| `shear` | `tuple` | The Shear attribute of the Axis node in the Action 3D space. | `(-1000000.0, -1000000.0, -1000000.0)`; `(1000000.0, 1000000.0, 1000000.0)` |
| `scale` | `tuple` | The Scale attribute of the Axis node in the Action 3D space. | `(-1000000.0, -1000000.0, -1000000.0)`; `(1000000.0, 1000000.0, 1000000.0)` |
| `rotation` | `tuple` | The Rotation attribute of the Axis node in the Action 3D space. | `(-1000000.0, -1000000.0, -1000000.0)`; `(1000000.0, 1000000.0, 1000000.0)` |

## Position Map

Common attrs: all 6. No node-specific attributes.

## Projector

Common attrs: all 6. Common attr(s) with a different definition here: `position` (listed below).

| attr | type | description | value range |
|---|---|---|---|
| `active` | `bool` | The Active attribute of the Projector node. | `True`; `False` |
| `colour` | `tuple` | The Colour attribute of the Projector node. | `(0.0, 0.0, 0.0)`; `(1.0, 1.0, 1.0)` |
| `blending` | `str` | The Blend Mode attribute of the Projector node. | `Blend`; `PunchBack`; `Multiply`; `Spotlight`; `Spot Blend`; `Add`; `Subtract`; `Screen`; `Min/Darken`; `Max/Lighten`; `Exclusion` |
| `premultiplied` | `bool` | The Premultiplied attribute of the Projector node. True = Premultiplied, False = Unpremultiplied | `True`; `False` |
| `transparency` | `float` | The Transparency attribute of the Projector node. | Min: 0.0; Max: 100.0 |
| `shaded` | `bool` | The Shaded attribute of the Projector node. | `True`; `False` |
| `occlusion` | `bool` | The Occlusion attribute of the Projector node. | `True`; `False` |
| `occlusion_softness` | `float` | The Occlusion Softness attribute of the Projector node. | Min: 0.0; Max: 100.0 |
| `front_face_only` | `bool` | The Front Face Only attribute of the Projector node. | `True`; `False` |
| `front_face_threshold` | `float` | The Front Face Only Threshold attribute of the Projector node. | Min: 0.0; Max: 100.0 |
| `motion_vectors_softness` | `float` | The Motion Vectors Softness attribute of the Projector node. | Min: 0.0; Max: 100.0 |
| `fov` | `float` | The FOV attribute of the Projector node. | Min: 1.0; Max: 180.0 |
| `aspect` | `float` | The Aspect attribute of the Projector node. | Min: 0.10000000149; Max: 100.0 |
| `near` | `float` | The Near attribute of the Projector node. | Min: 0.00999999977648; Max: 1000000.0 |
| `far` | `float` | The Far attribute of the Projector node. | Min: 0.019999999553; Max: 1000000.0 |
| `target_mode` | `bool` | The Target Mode attribute of the Projector node. True = Target, False = Free | `True`; `False` |
| `position` | `tuple` | **Differs from common definition.** The Position attribute of the Projector node. | `(-1000000.0, -1000000.0, -1000000.0)`; `(1000000.0, 1000000.0, 1000000.0)` |
| `rotation` | `tuple` | The Rotation attribute of the Projector node. Only active when `target_mode` = False. | `(-1000000.0, -1000000.0, -1000000.0)`; `(1000000.0, 1000000.0, 1000000.0)` |
| `interest` | `tuple` | The Interest attribute of the Projector node. Only active when `target_mode` = True. | `(-1000000.0, -1000000.0, -1000000.0)`; `(1000000.0, 1000000.0, 1000000.0)` |
| `distance` | `float` | The Distance attribute of the Projector node. Only active when `target_mode` = False. | Min: -1000000.0; Max: 1000000.0 |
| `roll` | `float` | The Roll attribute of the Projector node. Only active when `target_mode` = True. | Min: -1000000.0; Max: 1000000.0 |

## Rays

Common attrs: all 6. No node-specific attributes.

## Reflection Map

Common attrs: all 6. No node-specific attributes.

## Ring Texture

Common attrs: all 6. No node-specific attributes.

## Selective

Common attrs: all 6. No node-specific attributes.

## Shader

Common attrs: all 6.

| attr | type | description | value range |
|---|---|---|---|
| `roughness` | `float` | The Roughness attribute of the Shader node. | Min: 0.0; Max: 1.0 |
| `metallic` | `float` | The Metallic attribute of the Shader node. | Min: 0.0; Max: 1.0 |
| `subsurface` | `float` | The SubSurface attribute of the Shader node. | Min: 0.0; Max: 1.0 |
| `emissive_colour` | `tuple` | The Emissive Colour attribute of the Shader node. | `(0.0, 0.0, 0.0)`; `(1.0, 1.0, 1.0)` |
| `sheen` | `float` | The Sheen attribute of the Shader node. | Min: 0.0; Max: 1.0 |
| `sheen_tint` | `float` | The Sheen Tint attribute of the Shader node. | Min: 0.0; Max: 1.0 |
| `clearcoat` | `float` | The Clearcoat attribute of the Shader node. | Min: 0.0; Max: 1.0 |
| `clearcoat_gloss` | `float` | The Clearcoat Gloss attribute of the Shader node. | Min: 0.0; Max: 1.0 |
| `thinfilm_ior` | `float` | The Thin Film IOR attribute of the Shader node. | Min: 1.0; Max: 2.0 |
| `thinfilm_thickness` | `float` | The Thin Film Thickness attribute of the Shader node. | Min: 0.01; Max: 1.0 |
| `thinfilm` | `float` | The Thin Film attribute of the Shader node. | Min: 0.0; Max: 1.0 |
| `emissive_intensity` | `float` | The Emissive Intensity attribute of the Shader node. | Min: 0.0; Max: 10.0 |
| `specular_level` | `float` | The Specular Level attribute of the Shader node. | Min: 0.0; Max: 1.0 |
| `specular_tint` | `float` | The Specular Tint attribute of the Shader node. | Min: 0.0; Max: 1.0 |
| `anisotropic` | `float` | The Specular Anisotropic attribute of the Shader node. | Min: 0.0; Max: 1.0 |
| `specular_angle` | `float` | The Specular Angle attribute of the Shader node. | Min: -180.0; Max: 180.0 |

## Shadow

Common attrs: all 6. No node-specific attributes.

## Shadow Cast

Common attrs: all 6. No node-specific attributes.

## Specular Map

Common attrs: all 6. No node-specific attributes.

## Streak Texture

Common attrs: all 6. No node-specific attributes.

## UV Map

Common attrs: all 6. No node-specific attributes.

## Z-Depth

Common attrs: all 6. No node-specific attributes.
