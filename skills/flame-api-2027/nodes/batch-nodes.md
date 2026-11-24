> Source: PyNode: Batch Nodes Attributes

# Batch node attributes (node-specific)

Per Batch node type: only attributes that are NOT in the common set (see `README.md` → "Common Batch attributes"). Every node also has the common attributes unless stated otherwise. Section names are the source section titles with the trailing " Attributes" removed.

Values column: `Min: x; Max: y` = numeric range; backticked items = accepted values (enum); `None` = source gives no range ("Value range: None"). Access every attribute as `node.<attr>` (see README).

## 2D Histogram

Common attrs: all 10. No node-specific attributes.

## 2D Transform

Common attrs: all 10. No node-specific attributes.

## 3D Blur

Common attrs: all 10. No node-specific attributes.

## Action

Common attrs: all 10.

| attr | type | description | value range |
|---|---|---|---|
| `collapsed` | `bool` | The collapsed status of a node in the Batch schematic. | `True`; `False` |
| `selected_nodes` | `list` | The list of Action object nodes that are currently selected in the Action schematic. | None |
| `current_node` | `NoneType` | Return the currently selected action object node in the Action schematic. | None |

## Auto Stabilize

Common attrs: all 10. No node-specific attributes.

## Average

Common attrs: all 10.

| attr | type | description | value range |
|---|---|---|---|
| `over` | `int` | The Average Over attribute of the Average node. | Min: 2; Max: 1000 |
| `mode` | `str` | The Weighted / Uniform attribute of the Average node. | `Uniform Average`; `Weighted Average` |
| `frames` | `str` | The Past Frames / Past & Future attribute of the Average node. | `Past Frames`; `Past & Future` |

## Blend & Comp

Common attrs: all 10. No node-specific attributes.

## Blur

Common attrs: all 10. No node-specific attributes.

## Bump Displace

Common attrs: all 10. No node-specific attributes.

## Burn-in Letterbox

Common attrs: all 10.

| attr | type | description | value range |
|---|---|---|---|
| `mode` | `str` | The Letterbox mode attribute of the Burn-In Letterbox node. | `Custom`; `4.00:1 (Polyvision)`; `2.75:1 (Ultra 70)`; `2.40:1 (CinemaScope)`; `2.39:1 (CinemaScope)`; `2.35:1 (CinemaScope)`; `2.00:1 (Red Cameras)`; `1.89:1 (American 35mm)`; `1.85:1 (American 35mm)`; `1.77:1 (HDTV)`; `1.66:1 (European 35mm)`; `1.50:1 (3:2 Vertical)`; `1.37:1 (Academy)`; `1.33:1 (NTSC/PAL)`; `1.00:1 (Square)`; `0.80:1 (4:5 Vertical)`; `0.67:1 (2:3 Vertical)`; `0.56:1 (9:16 Vertical)` |
| `ratio` | `float` | The Ratio attribute of the Burn-In Letterbox node. | Min: 0.00999999977648; Max: 100.0 |
| `colour` | `tuple` | The Colour attribute of the Burn-In Letterbox node. | `(0.0, 0.0, 0.0)`; `(1.0, 1.0, 1.0)` |

## Burn-in Metadata

Common attrs: all 10. No node-specific attributes.

## Clamp

Common attrs: all 10.

| attr | type | description | value range |
|---|---|---|---|
| `min_clamp` | `bool` | Clamp all values lower than the defined one. | `True`; `False` |
| `max_clamp` | `bool` | Clamp all values higher than the defined one. | `True`; `False` |
| `min_value` | `float` | The Minimum value before a clamp is performed. | Min: -2147483647; Max: 2147483647 |
| `max_value` | `float` | The Maximum value before a clamp is performed. | Min: -2147483647; Max: 2147483647 |

## Colour Blend

Common attrs: all 10. No node-specific attributes.

## Colour Correct

Common attrs: all 10. No node-specific attributes.

## Colour Curves

Common attrs: all 10. No node-specific attributes.

## Colour Mgmt

Common attrs: all 10.

| attr | type | description | value range |
|---|---|---|---|
| `bit_depth` | `int` | Set the bit depth in all modes. Not available in the Timeline FX | `8`; `10`; `12`; `16`; `32` |
| `context_variables_from_project` | `bool` | Use the local or project context variables. | `True`; `False` |
| `custom` | `bool` | Enable/Disable the Custom parameter in Colour Transform mode. | `True`; `False` |
| `display` | `str` | Set the Display in View Transform mode. | None |
| `invert` | `bool` | Enable/Disable the invert parameter in View Transform, Input Transform and Colour Transform (Custom). | `True`; `False` |
| `mode` | `str` | Set the current colour management mode. | None |
| `tagged_colour_space` | `str` | Set the tagged colour space in Tag Only, View Transform and Colour Transform modes. Set the input colour space in Input Transform mode. | None |
| `view` | `str` | Set the View in View Transform mode. | None |
| `working_space` | `str` | Set the Working Space in Input Transform mode. | None |

## Colour Source

Common attrs: all 10. No node-specific attributes.

## Colour Warper

Common attrs: all 10. No node-specific attributes.

## Combine

Common attrs: all 10.

| attr | type | description | value range |
|---|---|---|---|
| `mode` | `str` | The Combine mode attribute of the Combine node. | `RGB`; `YUV`; `HSL` |

## Comp

Common attrs: all 10.

| attr | type | description | value range |
|---|---|---|---|
| `front_transparency` | `float` | The transparency attribute of the Front input of the Comp node. | Min: 0.0; Max: 100.0 |
| `back_transparency` | `float` | The transparency attribute of the Back input of the Comp node. | Min: 0.0; Max: 100.0 |
| `flame_blend_mode` | `str` | The Flame blending mode attribute used by the Comp node. Available only of `blend_type` = 'Flame'. | `Add`; `Subtract`; `Multiply`; `Divide`; `Average`; `Max/Lighten`; `Min/Darken`; `Spotlight`; `Spotlight Blend`; `Soft Light`; `Hard Light`; `And`; `Nand`; `AndRev`; `AndInv`; `Or`; `Nor`; `OrRev`; `OrInv`; `Xor`; `Xnor`; `Screen`; `Overlay`; `Difference`; `Exclusion`; `Blend`; `Non Additive`; `Inv Non Add` |
| `photoshop_blend_mode` | `str` | The Photoshop blending mode attribute used by the Comp node. Available only of `blend_type` = 'Photoshop'. | `Subtract`; `Multiply`; `Divide`; `Lighten`; `Color Dodge`; `Linear Dodge`; `Darken`; `Color Burn`; `Linear Burn`; `Hard Light`; `Pin Light`; `Hard Mix`; `Hue`; `Saturation`; `Color`; `Luminosity`; `Soft Light`; `Linear Light`; `Vivid Light`; `Darker Color`; `Lighter Color`; `Screen`; `Overlay`; `Difference`; `Exclusion`; `Normal` |
| `gimp_blend_mode` | `str` | The Gimp blending mode attribute used by the Comp node. Available only of `blend_type` = 'Gimp'. | `Addition`; `Subtraction`; `Multiply`; `Divide`; `Lighten`; `Dodge`; `Darken`; `Burn`; `Hard Light`; `Overlay`; `Hue`; `Saturation`; `Color`; `Value`; `Soft Light`; `Screen`; `Difference`; `Normal` |
| `blend_type` | `str` | The blend type attribute of the Comp node. | `Flame`; `Photoshop`; `Gimp` |
| `swap_inputs` | `bool` | The status attribute of the Swap Inputs function of the Comp node. | `True`; `False` |
| `front_clamp` | `str` | The Clamp attribute of the Front input of the Comp node. | `No Clamp`; `Clamp`; `Clamp Negative` |
| `back_clamp` | `str` | The Clamp attribute of the Back input of the Comp node. | `No Clamp`; `Clamp`; `Clamp Negative` |
| `front_premultiplied` | `bool` | The Premultiplied attribute of the Front input of the Comp node. | `True`; `False` |
| `back_premultiplied` | `bool` | The Premultiplied attribute of the Back input of the Comp node. | `True`; `False` |
| `back_matte` | `str` | The Matte attribute of the Back input of the Comp node. | `Matte Off`; `Matte On`; `Matte Invert` |
| `front_matte` | `str` | The Matte attribute of the Front input of the Comp node. | `Matte Off`; `Matte On`; `Matte Invert` |
| `matte_composition` | `str` | The Matte Composition attribute of the Comp node. | `Replace`; `Over`; `Atop`; `Inside`; `Outside`; `Cutout`; `Xor` |
| `matte_correlation` | `str` | The Matte Correlation attribute of the Comp node. | `Uncorrelated`; `Superposed`; `Adjacent` |
| `output_clamp` | `str` | The Clamp attribute of the outputs of the Comp node. | `No Clamp`; `Clamp`; `Clamp Negative` |
| `output_premultiplied` | `bool` | The Premultiplied attribute of the outputs of the Comp node. | `True`; `False` |

## Compass

Common attrs: all except `schematic_colour`, `schematic_colour_label` (not listed for this node in source).

| attr | type | description | value range |
|---|---|---|---|
| `width` | `int` | The width attribute of the Compass node. | Min: 200; Max: 2147483647 |
| `height` | `int` | The height attribute of the Compass node. | Min: 200; Max: 2147483647 |
| `colour` | `tuple` | The Colour attribute of the Compass node. | `(0.0, 0.0, 0.0)`; `(1.0, 1.0, 1.0)` |

## Compound

Common attrs: all 10.

| attr | type | description | value range |
|---|---|---|---|
| `over` | `int` | The Over attribute of the Compound node. | Min: 1; Max: 1000 |

## Cryptomatte

Common attrs: all 10.

| attr | type | description | value range |
|---|---|---|---|
| `collapsed` | `bool` | The collapsed status of a node in the Batch schematic. | `True`; `False` |

## Damage

Common attrs: all 10. No node-specific attributes.

## Deal

Common attrs: all 10.

| attr | type | description | value range |
|---|---|---|---|
| `clips` | `int` | The Clips attribute of the Deal node. | Min: 2; Max: 999 |
| `start_frame` | `int` | The Start Frame attribute of the Deal node. | Min: 1; Max: 999 |

## Deform

Common attrs: all 10. No node-specific attributes.

## Degrain

Common attrs: all 10. No node-specific attributes.

## DeInterlace

Common attrs: all 10. No node-specific attributes.

## Denoise

Common attrs: all 10. No node-specific attributes.

## Depth Of Field

Common attrs: all 10.

| attr | type | description | value range |
|---|---|---|---|
| `collapsed` | `bool` | The collapsed status of a node in the Batch schematic. | `True`; `False` |

## Difference Matte

Common attrs: all 10. No node-specific attributes.

## Dissolve

Common attrs: all 10. No node-specific attributes.

## Distort

Common attrs: all 10. No node-specific attributes.

## Edge Detect

Common attrs: all 10. No node-specific attributes.

## Exposure

Common attrs: all 10. No node-specific attributes.

## Field Merge

Common attrs: all 10. No node-specific attributes.

## Filter

Common attrs: all 10. No node-specific attributes.

## Flip

Common attrs: all 10. No node-specific attributes.

## Frequency

Common attrs: all 10.

| attr | type | description | value range |
|---|---|---|---|
| `separation` | `str` | The separation attribute of the Frequency node. | `2 Bands`; `3 Bands` |
| `blur_mode_low` | `str` | The low blur mode attribute of the Frequency node. | `Gaussian`; `Box` |
| `blur_width_low` | `float` | The low blur width attribute of the Frequency node. | Min: 0.00; Max: 1000.00 |
| `blur_height_low` | `float` | The low blur height attribute of the Frequency node. | Min: 0.00; Max: 1000.00 |
| `blur_mode_mid` | `str` | The mid blur mode attribute of the Frequency node. | `Gaussian`; `Box` |
| `blur_width_mid` | `float` | The mid blur width attribute of the Frequency node. | Min: 0.00; Max: 1000.00 |
| `blur_height_mid` | `float` | The mid blur height attribute of the Frequency node. | Min: 0.00; Max: 1000.00 |
| `centre_scale` | `bool` | The centre and scale mode attribute of the Frequency node. | `True`; `False` |

## Glow

Common attrs: all 10. No node-specific attributes.

## GMask

Common attrs: all 10. No node-specific attributes.

## GMask Tracer

Common attrs: all 10.

| attr | type | description | value range |
|---|---|---|---|
| `collapsed` | `bool` | The collapsed status of a node in the Batch schematic. | `True`; `False` |
| `selected_nodes` | `list` | The list of Action object nodes that are currently selected in the Action schematic. | None |
| `current_node` | `NoneType` | Return the currently selected action object node in the Action schematic. | None |

## Gradient

Common attrs: all 10. No node-specific attributes.

## HDR

Common attrs: all 10.

| attr | type | description | value range |
|---|---|---|---|
| `hdr_mode` | `str` | The current HDR mode. | None |
| `apply_trims` | `bool` | Apply trims when viewing or processing. | `True`; `False` |
| `lock_trims` | `bool` | Prevent any modification to the trims. | `True`; `False` |
| `analysis_min` | `float` | The analysis minimum value. | Min: 0.0; Max: 1.0 |
| `analysis_max` | `float` | The analysis maximum value. | Min: 0.0; Max: 1.0 |
| `analysis_avr` | `float` | The analysis average value. | Min: 0.0; Max: 1.0 |
| `lift` | `float` | The lift attribute of the hdr effect. | Min: -1.0; Max: 1.0 |
| `gain` | `float` | The gain attribute of the hdr effect. | Min: -1.0; Max: 1.0 |
| `gamma` | `float` | The gamma attribute of the hdr effect. | Min: -1.0; Max: 1.0 |
| `chroma_weight` | `float` | The chroma weight attribute of the hdr effect. | Min: -1.0; Max: 1.0 |
| `saturation_gain` | `float` | The saturation gain attribute of the hdr effect. | Min: -1.0; Max: 1.0 |
| `tone_detail` | `float` | The tone detail attribute of the hdr effect. | Min: -1.0; Max: 1.0 |
| `tone_offset_min` | `float` | The min tone offset attribute of the hdr effect. | Min: -1.0; Max: 1.0 |
| `tone_offset_mid` | `float` | The mid tone offset attribute of the hdr effect. | Min: -1.0; Max: 1.0 |
| `tone_offset_max` | `float` | The max tone offset attribute of the hdr effect. | Min: -1.0; Max: 1.0 |
| `mid_contrast_bias` | `float` | The mid contrast bias attribute of the hdr effect. | Min: -1.0; Max: 1.0 |
| `highlight_clipping` | `float` | The highlight clipping attribute of the hdr effect. | Min: -1.0; Max: 1.0 |
| `saturation_red` | `float` | The red saturation attribute of the hdr effect. | Min: -1.0; Max: 1.0 |
| `saturation_green` | `float` | The green saturation attribute of the hdr effect. | Min: -1.0; Max: 1.0 |
| `saturation_blue` | `float` | The blue saturation attribute of the hdr effect. | Min: -1.0; Max: 1.0 |
| `saturation_cyan` | `float` | The cyan saturation attribute of the hdr effect. | Min: -1.0; Max: 1.0 |
| `saturation_magenta` | `float` | The magenta saturation attribute of the hdr effect. | Min: -1.0; Max: 1.0 |
| `saturation_yellow` | `float` | The yellow saturation attribute of the hdr effect. | Min: -1.0; Max: 1.0 |
| `hue_red` | `float` | The red hue attribute of the hdr effect. | Min: -1.0; Max: 1.0 |
| `hue_green` | `float` | The green hue attribute of the hdr effect. | Min: -1.0; Max: 1.0 |
| `hue_blue` | `float` | The blue hue attribute of the hdr effect. | Min: -1.0; Max: 1.0 |
| `hue_cyan` | `float` | The cyan hue attribute of the hdr effect. | Min: -1.0; Max: 1.0 |
| `hue_magenta` | `float` | The magenta hue attribute of the hdr effect. | Min: -1.0; Max: 1.0 |
| `hue_yellow` | `float` | The yellow hue attribute of the hdr effect. | Min: -1.0; Max: 1.0 |
| `mastering_display_id` | `int` | Mastering Display Id / None if not available. | None |
| `target_display_id` | `int` | Target Display Id / None if not available. | None |
| `active_image_area` | `float` | Image Ratio of the hdr effect. | None |

## Image

Common attrs: all 10.

| attr | type | description | value range |
|---|---|---|---|
| `collapsed` | `bool` | The collapsed status of a node in the Batch schematic. | `True`; `False` |
| `selected_nodes` | `list` | The list of Action object nodes that are currently selected in the Action schematic. | None |
| `current_node` | `flame.PyCoNode` (class) | Return the currently selected action object node in the Action schematic. | None |

## Interlace

Common attrs: all 10. No node-specific attributes.

## Keyer 3D

Common attrs: all 10. No node-specific attributes.

## Keyer Channel

Common attrs: all 10. No node-specific attributes.

## Keyer HLS

Common attrs: all 10. No node-specific attributes.

## Keyer Luma

Common attrs: all 10. No node-specific attributes.

## Keyer RGB

Common attrs: all 10. No node-specific attributes.

## Keyer RGBCMYL

Common attrs: all 10. No node-specific attributes.

## Keyer YUV

Common attrs: all 10. No node-specific attributes.

## Look

Common attrs: all 10. No node-specific attributes.

## Luma Matte

Common attrs: all 10.

| attr | type | description | value range |
|---|---|---|---|
| `minimum` | `float` | The Minimum attribute of the Luma Matte node. | Min: 0.0; Max: 65504.0 |
| `maximum` | `float` | The Maximum attribute of the Luma Matte node. | Min: 0.0; Max: 65504.0 |
| `gain` | `float` | The Gain attribute of the Luma Matte node. | Min: 0.0; Max: 100000.0 |

## Map Convert

Common attrs: all 10. No node-specific attributes.

## Master Keyer

Common attrs: all 10. No node-specific attributes.

## Matchbox

Common attrs: all 10.

| attr | type | description | value range |
|---|---|---|---|
| `shader_name` | `str` | Return the current shader name. | None |

## Matte Blend

Common attrs: all 10. No node-specific attributes.

## Matte Curves

Common attrs: all 10. No node-specific attributes.

## Matte Edge

Common attrs: all 10. No node-specific attributes.

## Modular Keyer

Common attrs: all 10. No node-specific attributes.

## Mono

Common attrs: all 10. No node-specific attributes.

## Morph

Common attrs: all 10.

| attr | type | description | value range |
|---|---|---|---|
| `interpolation` | `str` | The Frame Interpolation mode attribute of the Morph node. | `Machine Learning`; `Motion Vectors` |
| `rendering_platform` | `str` | The Rendering Platform attribute of the Morph node. (Rocky Linux only) | `GPU`; `CPU` |
| `ml_engine_cache` | `bool` | The ML Engine Cache attribute of the Morph node. (Rocky Linux only) | `True`; `False` |
| `use_16_bit_fp` | `bool` | The Bit Depth attribute of the Morph node. (Rocky Linux only) | `True`; `False` |
| `motion_analysis_quality` | `str` | The Motion Analysis Quality attribute of the Morph node. | `Use 1/16 Resolution`; `Use 1/8 Resolution`; `Use 1/4 Resolution`; `Use 1/2 Resolution`; `Use Full Resolution` |
| `motion_blur` | `bool` | The Motion Blur Active attribute of the Morph node. | `True`; `False` |
| `samples` | `int` | The Motion Blur Samples attribute of the Morph node. | Min: 3; Max: 25 |
| `shutter` | `float` | The Motion Blur Shutter attribute of the Morph node. | Min: 0.05; Max: 10.00 |
| `reference` | `bool` | The Motion Blur Reference Active attribute of the Morph node. | `True`; `False` |
| `reference_colour` | `tuple` | The Motion Blur Reference colour attribute of the Morph node. | None |
| `reference_position_x` | `int` | The Motion Blur Reference Position X attribute of the Morph node. | Min: 0; Max: 10 000 |
| `reference_position_y` | `int` | The Motion Blur Reference Position Y attribute of the Morph node. | Min: 0; Max: 10 000 |
| `range_mode` | `str` | The Range mode attribute of the Morph node. | `All Frames`; `Custom Range` |
| `range_first_frame` | `int` | The Range's First Frame attribute of the Morph node. | Min: Batch Group's start frame; Max: Batch Group's start frame |
| `range_last_frame` | `int` | The Range's Last Frame attribute of the Morph node. | Min: Batch Group's start frame; Max: Batch Group's start frame |
| `mix` | `float` | The Mix attribute of the Morph node. | Min: 0.00; Max: 100.00 |
| `freeze_first_frame` | `bool` | The Freeze First Frame attribute of the Morph node. | `True`; `False` |
| `freeze_last_frame` | `bool` | The Freeze Last Frame attribute of the Morph node. | `True`; `False` |

## Motif

Common attrs: all 10. No node-specific attributes.

## Motion Analysis

Common attrs: all 10. No node-specific attributes.

## Motion Blur

Common attrs: all 10. No node-specific attributes.

## Motion Convert

Common attrs: all 10.

| attr | type | description | value range |
|---|---|---|---|
| `collapsed` | `bool` | The collapsed status of a node in the Batch schematic. | `True`; `False` |

## Negative

Common attrs: all 10. No node-specific attributes.

## OpenFX

Common attrs: all 10.

| attr | type | description | value range |
|---|---|---|---|
| `collapsed` | `bool` | The collapsed status of a node in the Batch schematic. | `True`; `False` |
| `plugin_name` | `str` | Return the name of the node's active plugin. | None |

## Optics

Common attrs: all 10. No node-specific attributes.

## Paint

Common attrs: all 10. No node-specific attributes.

## Pixel Spread

Common attrs: all 10. No node-specific attributes.

## Posterize

Common attrs: all 10. No node-specific attributes.

## Pulldown

Common attrs: all 10. No node-specific attributes.

## Pybox

Common attrs: all 10.

| attr | type | description | value range |
|---|---|---|---|
| `handler_name` | `str` | Return the handler's name. | None |

## Recursive Ops

Common attrs: all 10. No node-specific attributes.

## Regrain

Common attrs: all 10. No node-specific attributes.

## Resize

Common attrs: all 10. No node-specific attributes.

## Separate

Common attrs: all 10.

| attr | type | description | value range |
|---|---|---|---|
| `collapsed` | `bool` | The collapsed status of a node in the Batch schematic. | `True`; `False` |
| `mode` | `str` | The Separate mode. | `RGB`; `YUV`; `HSL` |

## Stereo Filter

Common attrs: all 10. No node-specific attributes.

## Stereo Toolbox

Common attrs: all 10.

| attr | type | description | value range |
|---|---|---|---|
| `collapsed` | `bool` | The collapsed status of a node in the Batch schematic. | `True`; `False` |

## STMap

Common attrs: all 10.

| attr | type | description | value range |
|---|---|---|---|
| `framing_mode` | `str` | The framing mode attribute of the STMap node. | `Use Entire Front Frame`; `Use STMap to Front Ratio`; `Use Data & Display Window` |
| `windows_source` | `str` | The framing mode attribute of the STMap node. | `From STMap Clip`; `Custom Values` |
| `data_window_min_x` | `bool` | The data window minimum x attribute of the STMap node. | `True`; `False` |
| `data_window_min_y` | `int` | The data window minimum y attribute of the STMap node. | Min: -16384; Max: 16384 |
| `data_window_max_x` | `int` | The data window maximum x attribute of the STMap node. | Min: -16384; Max: 16384 |
| `data_window_max_y` | `int` | The data window maximum y attribute of the STMap node. | Min: -16384; Max: 16384 |
| `display_window_min_x` | `int` | The display window minimum x attribute of the STMap node. | Min: 0; Max: 16384 |
| `display_window_min_y` | `int` | The display window minimum y attribute of the STMap node. | Min: 04; Max: 16384 |
| `display_window_max_x` | `int` | The display window maximum x attribute of the STMap node. | Min: 0; Max: 16384 |
| `display_window_max_y` | `int` | The display window maximum y attribute of the STMap node. | Min: 0; Max: 16384 |
| `offset_x` | `float` | The offset x attribute of the STMap node. | Min: -2147483647; Max: 2147483647 |
| `offset_y` | `float` | The offset y attribute of the STMap node. | Min: -2147483647; Max: 2147483647 |
| `repeat_mode` | `str` | The repeat mode attribute of the STMap node. | `Repeat Off`; `Mirrored Repeat`; `Tiled Repeat`; `Repeat Last` |
| `filter_mode` | `str` | The filter mode attribute of the STMap node. | `Nearest`; `Linear`; `Mitchell-Netravali`; `Catmull-Rom`; `Anisotropic`; `Aniso + Linear`; `EWA`; `EWA + Linear` |

## Stylize

Common attrs: all 10. No node-specific attributes.

## Substance Noise

Common attrs: all 10. No node-specific attributes.

## Substance Splatter

Common attrs: all 10. No node-specific attributes.

## Text

Common attrs: all 10. No node-specific attributes.

## Timewarp

Common attrs: all 10. No node-specific attributes.

## Note

Common attrs: all 10.

| attr | type | description | value range |
|---|---|---|---|
| `collapsed` | `bool` | The collapsed status of a node in the Batch schematic. | `True`; `False` |

## MUX

Common attrs: all 10.

| attr | type | description | value range |
|---|---|---|---|
| `collapsed` | `bool` | The collapsed status of a node in the Batch schematic. | `True`; `False` |
| `hide_input` | `bool` | The hidden status of the Input links of the Mux node. True = Hide, False = Display. | `True`; `False` |
| `hide_output` | `bool` | The hidden status of the Output links of the Mux node. True = Hidden, False = Displayed. | `True`; `False` |
| `input_amount` | `int` | The number of Inputs sockets of the Mux node. | Min: 1; Max: 20000 |
| `input_selection` | `int` | The currently active Input socket of the Mux node. | Min: 0; Max: 19999 |
| `timing_offset` | `int` | The Timing Offset value of the Mux node. | Min: -20000000; Max: 20000000 |
| `range_active` | `bool` | The FX Range status of the Mux node. True = Active, False = Disabled. | `True`; `False` |
| `range_start` | `int` | The FX Range start frame of the MUX node. | Min: -2147483647; Max: 2147483647 |
| `range_end` | `int` | The FX Range end frame of the MUX node. | Min: -2147483647; Max: 2147483647 |
| `before_range` | `str` | The FX before range type of the MUX node. | `Repeat First`; `No Media`; `Use Black`; `Use White`; `No Offset`; `Loop`; `Ping Pong +`; `Ping Pong` |
| `after_range` | `str` | The FX after range type of the MUX node. | `Repeat Last`; `No Media`; `Use Black`; `Use White`; `No Offset`; `Loop`; `Ping Pong +`; `Ping Pong` |

## Write File

Common attrs: all 10.

| attr | type | description | value range |
|---|---|---|---|
| `collapsed` | `bool` | The collapsed status of a node in the Batch schematic. | `True`; `False` |
| `range_start` | `int` | The Render Range From frame. | Min: -2147483647; Max: 2147483647 |
| `range_end` | `int` | The Render Range To frame. | Min: -2147483647; Max: 2147483647 |
| `frame_rate` | `str` | The frame rate. | `23.976 fps`; `24 fps`; `25 fps`; `29.97 DF`; `29.97 NDF`; `30 fps`; `50 fps`; `59.94 DF`; `59.94 NDF`; `60 fps` |
| `shot_name` | `str` | The shot name. | None |
| `tape_name` | `str` | The tape name. | None |
| `stereo` | `bool` | The status of the the Stereo option. | `True`; `False` |
| `nb_channels` | `int` | The number of channels when the format is set to Multi-Channel. | Min: 1; Max: 50 |
| `full_resolution` | `bool` | Select the Full resolution. | `True`; `False` |
| `source_timecode` | `flame.PyTime` (class) | The source timecode. | None |
| `record_timecode` | `flame.PyTime` (class) | The record timecode. | None |
| `media_path` | `str` | The path attribute where the rendered clip is exported by the Write File node. | None |
| `media_path_pattern` | `str` | The pattern attribute used to be generated the clip name by the Write File node.. Tokens can be included in the string, and are resolved by the Write File node at export time. | None |
| `create_clip_path` | `str` | The path attribute where the Open Clip file is exported by the Write File node. | None |
| `include_setup_path` | `str` | The path attribute where the Batch setup file is exported by the Write File node. | None |
| `create_clip` | `bool` | The Create Open Clip attribute of the Write File node. Determines if an Open Clip is created by the Write File node. | `True`; `False` |
| `include_setup` | `bool` | The Include Setup attribute of the Write File node. Determines if a Batch Setup file is created by the Write File node. | `True`; `False` |
| `version_mode` | `str` | The versioning mode of the Open Clip exported by the Write File node. Only available if `create_clip` = True. | `No Versioning`; `Custom Version`; `Follow Iteration` |
| `version_name` | `str` | The name attribute of the version in the Open Clip exported by the Write File node. The `<version>` token can be used in the string. | None |
| `version_padding` | `int` | The padding attribute used for the version number. | Min: 1; Max: 50 |
| `version_number` | `int` | The version number in the Open Clip. Only available if `version_mode` = 'Custom Version'. | Min: 1; Max: 50 |
| `format_extension` | `str` | The file extension for the files written by the Write File node. This attribute resets to match `file_type` whenever `file_type` is set. If you require a specific extension, you must set `format_extension` after setting `file_type`. | None |
| `bit_depth` | `str` | The bit depth for the files written by the Write File node. This attribute resets to match `file_type` whenever `file_type` is set. If you require a specific bit depth, you must set `bit_depth` after setting `file_type`. | `1`; `4`; `5`; `8`; `10`; `12`; `16`; `32` |
| `frame_padding` | `int` | The sequence padding attribute of the Write File node. | Min: 0; Max: 50 |
| `offset` | `int` | The export offset attribute of the Write File node. | Min: -2147483647; Max: 2147483647 |
| `file_type` | `str` | The file type for the files written by the Write File node. Setting this attribute also overwrites `format_extension`, `bit_depth` and `compress_mode` to match the defaults for this file type. | `Wavefront`; `Tx`; `Tiff`; `Targa`; `SoftImage`; `Sgi`; `Pixar`; `Pict`; `OpenEXR`; `Maya`; `Jpeg`; `Dpx`; `Cineon`; `Alias` |
| `compress` | `bool` | The compressing attribute for the files exported by the Write File node. Only relevant when `file_type` in 'OpenEXR', 'Sgi', 'Tiff'. | `True`; `False` |
| `compress_mode` | `str` | The compression format attribute for the specific File Types export by the Write File node. You must set `compress_mode` after setting `file_type`. | `Uncompressed`; `RLE`; `LZW`; `Scanline`; `Multi_Scanline`; `PIZ`; `PXR24`; `B44`; `B44A`; `DWAA`; `DWAB`; `Packed` |
| `level` | `int` | The compression level attribute for the files exported by the Write File node. Only relevant when `file_type` = 'Png', or `file_type` = 'OpenEXR' and `compress_mode` = 'DWAx'. | Min: 0; Max: 999 |
| `quality` | `int` | The Jpeg Quality attribute for the files exported by the Write File node. Only relevant when `file_type` = 'Jpeg'. | Min: 0; Max: 100 |
| `transfer_type` | `str` | The Dpx Transfer type attribute for the files exported by the Write File node. Only relevant when `file_type` = 'Dpx'. | `Printing Density`; `Linear`; `Logarithmic`; `Unspecified`; `SMPTE 274M`; `CCIR 709-4`; `CCIR 601 (625)`; `CCIR 601 (525)`; `NTSC`; `PAL`; `Z linear`; `Z homogeneous` |
| `colour_type` | `str` | The Dpx Color space attribute for the files exported by the Write File node. Only relevant when `file_type` = 'Dpx'. | `Printing Density`; `Unspecified`; `SMPTE 274M`; `CCIR 709-4`; `CCIR 601 (625)`; `CCIR 601 (525)`; `NTSC`; `PAL` |
| `frame_index_mode` | `str` | The frame index mode attribute of the Write File node. | `Use Timecode`; `Use Start Frame` |
| `add_to_workspace` | `bool` | Add the exported clip to the Workspace after the rendering is complete. | `True`; `False` |
| `destination` | `tuple` | Where the rendered clip is added. The following arguments can be set: | (no value range given) Arguments: Mode: "Reel Groups", "Batch Reels", or "Libraries"; Destination: The name of the reel when Batch Reels is set as the mode. One of "Topmost Reel", "Bottommost Reel", or the name of a reel present in the selected Reel Groups when Reel Groups is set as the mode.; Reel Groups: The name of the reel groups when Reel Groups is set as the mode |
| `smart_replace` | `bool` | Replace the destination timeline segment with the new rendered clip after the rendering is complete. | `True`; `False` |
| `apply_colour_coding` | `bool` | Activate the propagation of the node colour coding to its resulting clip. | `True`; `False` |
| `metadata_overlay` | `bool` | Burn in the current Metadata Overlay setup on export. | `True`; `False` |
| `metadata_overlay_context` | `str` | Context used by the Write File node for the metadata overlay context. | `WriteFile`; `Context 1`; `Context 2`; `Context 3`; `Context 4`; `Context 5`; `Context 6`; `Context 7`; `Context 8`; `Context 9`; `Context 10` |
| `basic_metadata` | `str` | The status of the Basic Metadata option. | `Custom Values`; `Use Input Values` |
| `basic_metadata_input` | `str` | The status of the Basic Metadata Input option. | `Use Front Input`; `Use Metadata Input` |

## Render

Common attrs: all 10.

| attr | type | description | value range |
|---|---|---|---|
| `collapsed` | `bool` | The collapsed status of a node in the Batch schematic. | `True`; `False` |
| `range_start` | `int` | The Render Range From frame. | Min: -2147483647; Max: 2147483647 |
| `range_end` | `int` | The Render Range To frame. | Min: -2147483647; Max: 2147483647 |
| `frame_rate` | `str` | The frame rate. | `23.976 fps`; `24 fps`; `25 fps`; `29.97 DF`; `29.97 NDF`; `30 fps`; `50 fps`; `59.94 DF`; `59.94 NDF`; `60 fps` |
| `stereo` | `bool` | The status of the Stereo option. | `True`; `False` |
| `split_rgba` | `bool` | The status of the Split RGB/A option. | `True`; `False` |
| `shot_name` | `str` | The shot name. | None |
| `tape_name` | `str` | The tape name. | None |
| `nb_channels` | `int` | The number of channels when the format is set to Multi-Channel. | Min: 1; Max: 50 |
| `full_resolution` | `bool` | Select the Full resolution. | `True`; `False` |
| `setup_mode` | `bool` | Select the Range setup mode. | `True`; `False` |
| `range_offset` | `bool` | Activate the Range Timecode Offset | `True`; `False` |
| `source_timecode` | `flame.PyTime` (class) | The source timecode. | None |
| `record_timecode` | `flame.PyTime` (class) | The record timecode. | None |
| `bit_depth` | `str` | The output bit depth | `8-bit`; `10-bit`; `12-bit`; `16-bit fp`; `32-bit fp` |
| `destination` | `tuple` | Where the rendered clip is added. The following arguments can be set: | (no value range given) Arguments: Mode: "Reel Groups", "Batch Reels", or "Libraries"; Destination: The name of the reel when Batch Reels is set as the mode. One of "Topmost Reel", "Bottommost Reel", or the name of a reel present in the selected Reel Groups when Reel Groups is set as the mode.; Reel Groups: The name of the reel groups when Reel Groups is set as the mode |
| `smart_replace` | `bool` | Replace the destination timeline segment with the new rendered clip after the rendering is complete. | `True`; `False` |
| `apply_colour_coding` | `bool` | Activate the propagation of the node colour coding to its resulting clip. | `True`; `False` |
| `in_mark` | `flame.PyTime` (class) | The in mark. | `Frame number`; `Timecode value`; `PyTime` |
| `out_mark` | `flame.PyTime` (class) | The out mark. | `Frame number`; `Timecode value`; `PyTime` |
| `tags` | `list` | The tag list of the render node. | None |
| `basic_metadata` | `str` | The status of the Basic Metadata option. | `Custom Values`; `Use Input Values` |
| `basic_metadata_input` | `str` | The status of the Basic Metadata Input option. | `Use Front Input`; `Use Metadata Input` |
