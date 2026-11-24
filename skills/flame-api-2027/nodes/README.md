> Source: PyNode: Batch Nodes Attributes; PyCoNode: Action Nodes Attributes (Autodesk Flame 2027 Help)

# Node attributes — Batch nodes & Action objects (Flame 2027)

Compact, lossless re-packaging of two very repetitive help pages. Every attribute name, type, description and value
range below is copied from the source; only duplicate text has been factored out.

| file | content |
|---|---|
| `README.md` (this) | how node attributes work, the COMMON attribute sets, indexes of every node type |
| [batch-nodes.md](batch-nodes.md) | per Batch node (`flame.PyNode` and subclasses): node-specific attributes only |
| [action-nodes.md](action-nodes.md) | per Action object (`flame.PyCoNode` and subclasses): node-specific attributes only |
| [node-attributes.json](node-attributes.json) | full machine-readable data (every node with ALL its attributes, incl. common ones) |

To get the complete attribute list of one node: common table below (minus any "missing common" listed in the index)
+ that node's section in `batch-nodes.md` / `action-nodes.md`. Or read `node-attributes.json["batch"]["<Node>"]`.

## How node attributes work

- Batch nodes are `flame.PyNode` objects (some types return a subclass with extra methods, e.g. `PyActionNode`,
  `PyClrMgmtNode`, `PyCompassNode`, `PyHDRNode`, `PyMorphNode`, `PyOFXNode`, `PyPaintNode`, `PyRenderNode`,
  `PyWriteFileNode`, `PyTimewarpNode` — see `../api/classes/`). Get them from `flame.batch.nodes`,
  `flame.batch.current_node.get_value()`, `flame.batch.get_node( (PyBatch)arg1, (str)node_name) -> object`, or create them with
  `flame.batch.create_node(node_type)`.
- `PyBatch.create_node( (PyBatch)arg1, (str)node_type [, (str)file_path='']) -> object` — `node_type` "Must be a value
  from the PyBatch.node_types or the name of a node in the User, Project, or Shared bin."
  `flame.batch.node_types` lists the valid type strings for the running Flame.
- Action objects (nodes inside an Action / Image / GMask Tracer schematic) are `flame.PyCoNode` objects (subclasses
  `PyCoCameraAnalysis`, `PyCoCompass`). Get them from `<action_node>.nodes`, or create them with
  `<action_node>.create_node( (PyActionFamilyNode)arg1, (str)node_type [, (str)file_path='' [, (bool)is_udim=False [, (int)tile_resolution=0]]]) -> object`;
  valid strings: `<action_node>.node_types`. `file_path` is "Required by nodes that load an asset, such as Matchbox."
- Node type string: read `node.type` (Batch; common attr "Return the type of the node.") or the `type` read-only
  property of `PyCoNode`. The section names used in this folder are the source section titles minus the trailing
  " Attributes" (e.g. `## Write File Attributes` → **Write File**). In the official examples these match the type
  strings (`create_node("Comp")`, `create_node("Write File")`, `create_node("Colour Mgmt")`,
  `create_node("2D Transform")`, `n.type == "Comp"`, `action.create_node("Compass")`, `node_type="IBL"`), but the
  source does not state this for every section — confirm with `node_types` before relying on a name.
- Access: `node.<attr>` (e.g. `node.pos_x`, `comp.flame_blend_mode`). Most attributes return a `flame.PyAttribute`
  wrapper: `.get_value()` returns the Python value, `.set_value(v) -> bool` sets it, `.values` lists the possible
  values/range. Direct assignment also works and is used in the official examples:
  `i.pos_y -= 100`, `n.flame_blend_mode = "Add"`, `mux.bypass = True`, `mux.range_start = frame`.
  `PyAttribute` supports arithmetic/comparison operators (`+ - * / //`, `+=`, `<`, `==` …) with int/float (and `+`
  with str). `node.attributes` (read-only, inherited from `PyFlameObject`: "The attributes of a python object.") can be
  inspected at runtime to discover what a node exposes — useful for nodes whose section here has no node-specific entries
  (the help page documents only these attributes; nodes may expose more at runtime).
- Value-range column conventions: `Min: x; Max: y` = numeric range; backticked items = accepted values (enumeration)
  as listed by the source; for tuple attributes the source gives two tuples (first = lower bound, second = upper bound);
  `None` = the source says "Value range: None" (free value / no range given).
- Types are as printed in the source `(type 'x')`; `(class)` marks attributes the source declares as
  `(class 'flame.PyTime')` / `(class 'flame.PyCoNode')`.

## Common Batch attributes

Present with this exact definition on (almost) every Batch node. Per-node sections in `batch-nodes.md` say
"Common attrs: all 10" or list the exceptions.

| attr | type | description | value range | nodes listing it |
|---|---|---|---|---|
| `pos_x` | `int` | The x position of a node in the Batch schematic. | Min: -2147483647; Max: 2147483647 | 92/92 |
| `pos_y` | `int` | The y position of a node in the Batch schematic. | Min: -2147483647; Max: 2147483647 | 92/92 |
| `name` | `str` | The name of the node in the Batch schematic. | None | 92/92 |
| `note` | `str` | The Node's note. | None | 92/92 |
| `note_collapsed` | `bool` | The collapsed status of a note in the Batch schematic. | `True`; `False` | 92/92 |
| `selected` | `bool` | Select a Node in the Batch schematic. | `True`; `False` | 92/92 |
| `type` | `str` | Return the type of the node. | None | 92/92 |
| `bypass` | `bool` | The bypass status of a node. | `True`; `False` | 92/92 |
| `schematic_colour` | `tuple` | The schematic colour of the Node. | None | 91/92 |
| `schematic_colour_label` | `str` | The schematic colour label of the Node. | None | 91/92 |

Other attributes that recur with identical definitions on several Batch nodes (still listed in full under each node in
`batch-nodes.md`):

| attr | nodes (identical definition) |
|---|---|
| `collapsed` | Action, Cryptomatte, Depth Of Field, GMask Tracer, Image, Motion Convert, OpenFX, Separate, Stereo Toolbox, Note, MUX, Write File, Render |
| `selected_nodes` | Action, GMask Tracer, Image |
| `current_node` | Action, GMask Tracer |
| `range_start` | Write File, Render |
| `range_end` | Write File, Render |
| `frame_rate` | Write File, Render |
| `shot_name` | Write File, Render |
| `tape_name` | Write File, Render |
| `nb_channels` | Write File, Render |
| `full_resolution` | Write File, Render |
| `source_timecode` | Write File, Render |
| `record_timecode` | Write File, Render |
| `destination` | Write File, Render |
| `smart_replace` | Write File, Render |
| `apply_colour_coding` | Write File, Render |
| `basic_metadata` | Write File, Render |
| `basic_metadata_input` | Write File, Render |

## Common Action object attributes

Present with this exact definition on most Action objects. Note: `position` here is the generic definition (±3.4028234663852886e+38);
7 objects (Axis, Camera, Camera 3D, Light, Particle Animator, Perspective Grid, Projector) redefine `position` with a different
description/range — those are flagged "Differs from common definition" in `action-nodes.md`.

| attr | type | description | value range | nodes listing it |
|---|---|---|---|---|
| `name` | `str` | The name of the Action node in the Action schematic. | None | 48/48 |
| `position` | `tuple` | The XYZ position of the Action node in the Action 3D space. | `(-3.4028234663852886e+38, -3.4028234663852886e+38, -3.4028234663852886e+38)`; `(3.4028234663852886e+38, 3.4028234663852886e+38, 3.4028234663852886e+38)` | 41/48 |
| `selected` | `bool` | The Action node is selected. | `True`; `False` | 48/48 |
| `collapsed_in_manager` | `bool` | The Action node is collapsed in the Action Manager | `True`; `False` | 48/48 |
| `pos_x` | `int` | The x position of the Action Node in the Action schematic. | Min: -2147483647; Max: 2147483647 | 48/48 |
| `pos_y` | `int` | The y position of the Action Node in the Action schematic. | Min: -2147483647; Max: 2147483647 | 48/48 |

Other attributes that recur with identical definitions on several Action objects:

| attr | nodes (identical definition) |
|---|---|
| `text` | 3D Shape, 3D Text |
| `position` | Axis, Particle Animator, Perspective Grid |
| `center` | Axis, Particle Animator, Perspective Grid |
| `shear` | Axis, Particle Animator, Perspective Grid |
| `scale` | Axis, Particle Animator, Perspective Grid |
| `rotation` | Axis, Particle Animator, Perspective Grid |

## Index — Batch nodes

"specific attrs" = rows in `batch-nodes.md` (non-common attributes + common attributes whose definition differs).

| node | specific attrs | missing common | link |
|---|---|---|---|
| 2D Histogram | 0 | - | [batch-nodes.md#2d-histogram](batch-nodes.md#2d-histogram) |
| 2D Transform | 0 | - | [batch-nodes.md#2d-transform](batch-nodes.md#2d-transform) |
| 3D Blur | 0 | - | [batch-nodes.md#3d-blur](batch-nodes.md#3d-blur) |
| Action | 3 | - | [batch-nodes.md#action](batch-nodes.md#action) |
| Auto Stabilize | 0 | - | [batch-nodes.md#auto-stabilize](batch-nodes.md#auto-stabilize) |
| Average | 3 | - | [batch-nodes.md#average](batch-nodes.md#average) |
| Blend & Comp | 0 | - | [batch-nodes.md#blend--comp](batch-nodes.md#blend--comp) |
| Blur | 0 | - | [batch-nodes.md#blur](batch-nodes.md#blur) |
| Bump Displace | 0 | - | [batch-nodes.md#bump-displace](batch-nodes.md#bump-displace) |
| Burn-in Letterbox | 3 | - | [batch-nodes.md#burn-in-letterbox](batch-nodes.md#burn-in-letterbox) |
| Burn-in Metadata | 0 | - | [batch-nodes.md#burn-in-metadata](batch-nodes.md#burn-in-metadata) |
| Clamp | 4 | - | [batch-nodes.md#clamp](batch-nodes.md#clamp) |
| Colour Blend | 0 | - | [batch-nodes.md#colour-blend](batch-nodes.md#colour-blend) |
| Colour Correct | 0 | - | [batch-nodes.md#colour-correct](batch-nodes.md#colour-correct) |
| Colour Curves | 0 | - | [batch-nodes.md#colour-curves](batch-nodes.md#colour-curves) |
| Colour Mgmt | 9 | - | [batch-nodes.md#colour-mgmt](batch-nodes.md#colour-mgmt) |
| Colour Source | 0 | - | [batch-nodes.md#colour-source](batch-nodes.md#colour-source) |
| Colour Warper | 0 | - | [batch-nodes.md#colour-warper](batch-nodes.md#colour-warper) |
| Combine | 1 | - | [batch-nodes.md#combine](batch-nodes.md#combine) |
| Comp | 17 | - | [batch-nodes.md#comp](batch-nodes.md#comp) |
| Compass | 3 | `schematic_colour`, `schematic_colour_label` | [batch-nodes.md#compass](batch-nodes.md#compass) |
| Compound | 1 | - | [batch-nodes.md#compound](batch-nodes.md#compound) |
| Cryptomatte | 1 | - | [batch-nodes.md#cryptomatte](batch-nodes.md#cryptomatte) |
| Damage | 0 | - | [batch-nodes.md#damage](batch-nodes.md#damage) |
| Deal | 2 | - | [batch-nodes.md#deal](batch-nodes.md#deal) |
| Deform | 0 | - | [batch-nodes.md#deform](batch-nodes.md#deform) |
| Degrain | 0 | - | [batch-nodes.md#degrain](batch-nodes.md#degrain) |
| DeInterlace | 0 | - | [batch-nodes.md#deinterlace](batch-nodes.md#deinterlace) |
| Denoise | 0 | - | [batch-nodes.md#denoise](batch-nodes.md#denoise) |
| Depth Of Field | 1 | - | [batch-nodes.md#depth-of-field](batch-nodes.md#depth-of-field) |
| Difference Matte | 0 | - | [batch-nodes.md#difference-matte](batch-nodes.md#difference-matte) |
| Dissolve | 0 | - | [batch-nodes.md#dissolve](batch-nodes.md#dissolve) |
| Distort | 0 | - | [batch-nodes.md#distort](batch-nodes.md#distort) |
| Edge Detect | 0 | - | [batch-nodes.md#edge-detect](batch-nodes.md#edge-detect) |
| Exposure | 0 | - | [batch-nodes.md#exposure](batch-nodes.md#exposure) |
| Field Merge | 0 | - | [batch-nodes.md#field-merge](batch-nodes.md#field-merge) |
| Filter | 0 | - | [batch-nodes.md#filter](batch-nodes.md#filter) |
| Flip | 0 | - | [batch-nodes.md#flip](batch-nodes.md#flip) |
| Frequency | 8 | - | [batch-nodes.md#frequency](batch-nodes.md#frequency) |
| Glow | 0 | - | [batch-nodes.md#glow](batch-nodes.md#glow) |
| GMask | 0 | - | [batch-nodes.md#gmask](batch-nodes.md#gmask) |
| GMask Tracer | 3 | - | [batch-nodes.md#gmask-tracer](batch-nodes.md#gmask-tracer) |
| Gradient | 0 | - | [batch-nodes.md#gradient](batch-nodes.md#gradient) |
| HDR | 32 | - | [batch-nodes.md#hdr](batch-nodes.md#hdr) |
| Image | 3 | - | [batch-nodes.md#image](batch-nodes.md#image) |
| Interlace | 0 | - | [batch-nodes.md#interlace](batch-nodes.md#interlace) |
| Keyer 3D | 0 | - | [batch-nodes.md#keyer-3d](batch-nodes.md#keyer-3d) |
| Keyer Channel | 0 | - | [batch-nodes.md#keyer-channel](batch-nodes.md#keyer-channel) |
| Keyer HLS | 0 | - | [batch-nodes.md#keyer-hls](batch-nodes.md#keyer-hls) |
| Keyer Luma | 0 | - | [batch-nodes.md#keyer-luma](batch-nodes.md#keyer-luma) |
| Keyer RGB | 0 | - | [batch-nodes.md#keyer-rgb](batch-nodes.md#keyer-rgb) |
| Keyer RGBCMYL | 0 | - | [batch-nodes.md#keyer-rgbcmyl](batch-nodes.md#keyer-rgbcmyl) |
| Keyer YUV | 0 | - | [batch-nodes.md#keyer-yuv](batch-nodes.md#keyer-yuv) |
| Look | 0 | - | [batch-nodes.md#look](batch-nodes.md#look) |
| Luma Matte | 3 | - | [batch-nodes.md#luma-matte](batch-nodes.md#luma-matte) |
| Map Convert | 0 | - | [batch-nodes.md#map-convert](batch-nodes.md#map-convert) |
| Master Keyer | 0 | - | [batch-nodes.md#master-keyer](batch-nodes.md#master-keyer) |
| Matchbox | 1 | - | [batch-nodes.md#matchbox](batch-nodes.md#matchbox) |
| Matte Blend | 0 | - | [batch-nodes.md#matte-blend](batch-nodes.md#matte-blend) |
| Matte Curves | 0 | - | [batch-nodes.md#matte-curves](batch-nodes.md#matte-curves) |
| Matte Edge | 0 | - | [batch-nodes.md#matte-edge](batch-nodes.md#matte-edge) |
| Modular Keyer | 0 | - | [batch-nodes.md#modular-keyer](batch-nodes.md#modular-keyer) |
| Mono | 0 | - | [batch-nodes.md#mono](batch-nodes.md#mono) |
| Morph | 18 | - | [batch-nodes.md#morph](batch-nodes.md#morph) |
| Motif | 0 | - | [batch-nodes.md#motif](batch-nodes.md#motif) |
| Motion Analysis | 0 | - | [batch-nodes.md#motion-analysis](batch-nodes.md#motion-analysis) |
| Motion Blur | 0 | - | [batch-nodes.md#motion-blur](batch-nodes.md#motion-blur) |
| Motion Convert | 1 | - | [batch-nodes.md#motion-convert](batch-nodes.md#motion-convert) |
| Negative | 0 | - | [batch-nodes.md#negative](batch-nodes.md#negative) |
| OpenFX | 2 | - | [batch-nodes.md#openfx](batch-nodes.md#openfx) |
| Optics | 0 | - | [batch-nodes.md#optics](batch-nodes.md#optics) |
| Paint | 0 | - | [batch-nodes.md#paint](batch-nodes.md#paint) |
| Pixel Spread | 0 | - | [batch-nodes.md#pixel-spread](batch-nodes.md#pixel-spread) |
| Posterize | 0 | - | [batch-nodes.md#posterize](batch-nodes.md#posterize) |
| Pulldown | 0 | - | [batch-nodes.md#pulldown](batch-nodes.md#pulldown) |
| Pybox | 1 | - | [batch-nodes.md#pybox](batch-nodes.md#pybox) |
| Recursive Ops | 0 | - | [batch-nodes.md#recursive-ops](batch-nodes.md#recursive-ops) |
| Regrain | 0 | - | [batch-nodes.md#regrain](batch-nodes.md#regrain) |
| Resize | 0 | - | [batch-nodes.md#resize](batch-nodes.md#resize) |
| Separate | 2 | - | [batch-nodes.md#separate](batch-nodes.md#separate) |
| Stereo Filter | 0 | - | [batch-nodes.md#stereo-filter](batch-nodes.md#stereo-filter) |
| Stereo Toolbox | 1 | - | [batch-nodes.md#stereo-toolbox](batch-nodes.md#stereo-toolbox) |
| STMap | 14 | - | [batch-nodes.md#stmap](batch-nodes.md#stmap) |
| Stylize | 0 | - | [batch-nodes.md#stylize](batch-nodes.md#stylize) |
| Substance Noise | 0 | - | [batch-nodes.md#substance-noise](batch-nodes.md#substance-noise) |
| Substance Splatter | 0 | - | [batch-nodes.md#substance-splatter](batch-nodes.md#substance-splatter) |
| Text | 0 | - | [batch-nodes.md#text](batch-nodes.md#text) |
| Timewarp | 0 | - | [batch-nodes.md#timewarp](batch-nodes.md#timewarp) |
| Note | 1 | - | [batch-nodes.md#note](batch-nodes.md#note) |
| MUX | 11 | - | [batch-nodes.md#mux](batch-nodes.md#mux) |
| Write File | 41 | - | [batch-nodes.md#write-file](batch-nodes.md#write-file) |
| Render | 23 | - | [batch-nodes.md#render](batch-nodes.md#render) |

## Index — Action objects (PyCoNode)

| node | specific attrs | missing common | link |
|---|---|---|---|
| 3D Path | 0 | - | [action-nodes.md#3d-path](action-nodes.md#3d-path) |
| 3D Shape | 1 | - | [action-nodes.md#3d-shape](action-nodes.md#3d-shape) |
| 3D Text | 1 | - | [action-nodes.md#3d-text](action-nodes.md#3d-text) |
| Analyzer | 0 | - | [action-nodes.md#analyzer](action-nodes.md#analyzer) |
| Atomize | 0 | - | [action-nodes.md#atomize](action-nodes.md#atomize) |
| Axis | 5 | - | [action-nodes.md#axis](action-nodes.md#axis) |
| Blooming | 0 | - | [action-nodes.md#blooming](action-nodes.md#blooming) |
| Border FX | 0 | - | [action-nodes.md#border-fx](action-nodes.md#border-fx) |
| Camera | 13 | - | [action-nodes.md#camera](action-nodes.md#camera) |
| Camera 3D | 34 | - | [action-nodes.md#camera-3d](action-nodes.md#camera-3d) |
| Compass | 3 | - | [action-nodes.md#compass](action-nodes.md#compass) |
| Deform Mesh | 0 | - | [action-nodes.md#deform-mesh](action-nodes.md#deform-mesh) |
| Diffuse Map | 0 | - | [action-nodes.md#diffuse-map](action-nodes.md#diffuse-map) |
| Displace Map | 0 | - | [action-nodes.md#displace-map](action-nodes.md#displace-map) |
| Emissive Map | 0 | - | [action-nodes.md#emissive-map](action-nodes.md#emissive-map) |
| Surface | 0 | - | [action-nodes.md#surface](action-nodes.md#surface) |
| Glint Texture | 0 | - | [action-nodes.md#glint-texture](action-nodes.md#glint-texture) |
| Glow Texture | 0 | - | [action-nodes.md#glow-texture](action-nodes.md#glow-texture) |
| GMask | 0 | - | [action-nodes.md#gmask](action-nodes.md#gmask) |
| IBL | 1 | - | [action-nodes.md#ibl](action-nodes.md#ibl) |
| Iris Texture | 0 | - | [action-nodes.md#iris-texture](action-nodes.md#iris-texture) |
| Lens Flare | 0 | - | [action-nodes.md#lens-flare](action-nodes.md#lens-flare) |
| Lens Texture | 0 | - | [action-nodes.md#lens-texture](action-nodes.md#lens-texture) |
| Light | 20 | - | [action-nodes.md#light](action-nodes.md#light) |
| Matchbox | 0 | - | [action-nodes.md#matchbox](action-nodes.md#matchbox) |
| Material | 0 | - | [action-nodes.md#material](action-nodes.md#material) |
| Motion Vectors Map | 0 | - | [action-nodes.md#motion-vectors-map](action-nodes.md#motion-vectors-map) |
| Normal Map | 0 | - | [action-nodes.md#normal-map](action-nodes.md#normal-map) |
| Object ID Map | 0 | - | [action-nodes.md#object-id-map](action-nodes.md#object-id-map) |
| Parallax Map | 0 | - | [action-nodes.md#parallax-map](action-nodes.md#parallax-map) |
| Particle Animator | 5 | - | [action-nodes.md#particle-animator](action-nodes.md#particle-animator) |
| Particle Bouncer | 0 | - | [action-nodes.md#particle-bouncer](action-nodes.md#particle-bouncer) |
| Particle Generator | 0 | - | [action-nodes.md#particle-generator](action-nodes.md#particle-generator) |
| PBS Map | 0 | - | [action-nodes.md#pbs-map](action-nodes.md#pbs-map) |
| Perspective Grid | 5 | - | [action-nodes.md#perspective-grid](action-nodes.md#perspective-grid) |
| Position Map | 0 | - | [action-nodes.md#position-map](action-nodes.md#position-map) |
| Projector | 21 | - | [action-nodes.md#projector](action-nodes.md#projector) |
| Rays | 0 | - | [action-nodes.md#rays](action-nodes.md#rays) |
| Reflection Map | 0 | - | [action-nodes.md#reflection-map](action-nodes.md#reflection-map) |
| Ring Texture | 0 | - | [action-nodes.md#ring-texture](action-nodes.md#ring-texture) |
| Selective | 0 | - | [action-nodes.md#selective](action-nodes.md#selective) |
| Shader | 16 | - | [action-nodes.md#shader](action-nodes.md#shader) |
| Shadow | 0 | - | [action-nodes.md#shadow](action-nodes.md#shadow) |
| Shadow Cast | 0 | - | [action-nodes.md#shadow-cast](action-nodes.md#shadow-cast) |
| Specular Map | 0 | - | [action-nodes.md#specular-map](action-nodes.md#specular-map) |
| Streak Texture | 0 | - | [action-nodes.md#streak-texture](action-nodes.md#streak-texture) |
| UV Map | 0 | - | [action-nodes.md#uv-map](action-nodes.md#uv-map) |
| Z-Depth | 0 | - | [action-nodes.md#z-depth](action-nodes.md#z-depth) |

## Source notes (garbles / oddities, kept or repaired)

- PyNode: Batch Nodes Attributes — repaired: Colour Mgmt.bit_depth: dropped stray line '>' (HTML markup artefact)
- PyNode: Batch Nodes Attributes — repaired: Colour Mgmt.bit_depth: removed stray '<' from bullet '- 32<'
- PyNode: Batch Nodes Attributes — repaired: Write File.version_name: restored '<version>' token stripped by HTML->md conversion
- PyNode: Batch Nodes Attributes — repaired: Write File.add_to_workspace: attr heading not code-formatted in source
- PyNode: Batch Nodes Attributes — repaired: Write File.add_to_workspace: removed wrapping backticks from '`Add the exported clip to the Workspace after the rendering is complete.Value range:`'
- PyNode: Batch Nodes Attributes — repaired: Write File.add_to_workspace: split description glued to 'Value range:'
- PyNode: Batch Nodes Attributes — repaired: Write File.add_to_workspace: removed stray backticks from bullet '- `True`'
- PyNode: Batch Nodes Attributes — repaired: Write File.add_to_workspace: removed stray backticks from bullet '- `False'
- PyNode: Batch Nodes Attributes — repaired: Write File.basic_metadata_input: dropped stray line '`' (HTML markup artefact)
- PyCoNode: Action Nodes Attributes — the `## Axis Attributes` section occurs 5 times (one after Atomize, four more between Streak Texture and UV Map), all byte-identical, also in the HTML original. Deduplicated to one **Axis** entry (raw: 52 sections / 446 attr entries; unique: 48 objects / 406 attrs). The extra copies may stand in for other object types the page fails to document.
- PyCoNode: Action Nodes Attributes — Camera `film_type` description reads "The Focal attribute of the Camera Action node…" (apparent copy-paste error in source; kept verbatim).
- PyCoNode: Action Nodes Attributes — `text` on both 3D Shape and 3D Text has type `unicode` and description "The text string of the 3D Text node." (verbatim).
- PyNode: Batch Nodes Attributes — Compass lists neither `schematic_colour` nor `schematic_colour_label` (all other 91 nodes do).
- PyNode: Batch Nodes Attributes — `current_node` is typed `NoneType` on Action and GMask Tracer but `(class 'flame.PyCoNode')` on Image (verbatim).
- PyNode: Batch Nodes Attributes — `bit_depth` is `int` on Colour Mgmt but `str` on Write File / Render (different value lists; verbatim).
- PyNode: Batch Nodes Attributes — Write File / Render `destination` has no "Value range" in the source; its argument list ("The following arguments can be set:") is shown in the value-range column and stored as `arguments` in the JSON.
- Typos kept verbatim: "The status of the the Stereo option.", "Available only of **blend_type**", "Write File node.." etc.
