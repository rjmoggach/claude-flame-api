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

<!-- COMMON batch -->

Other attributes that recur with identical definitions on several Batch nodes (still listed in full under each node in
`batch-nodes.md`):

<!-- RECURRING batch -->

## Common Action object attributes

Present with this exact definition on most Action objects. Note: `position` here is the generic definition (±3.4028234663852886e+38);
7 objects (Axis, Camera, Camera 3D, Light, Particle Animator, Perspective Grid, Projector) redefine `position` with a different
description/range — those are flagged "Differs from common definition" in `action-nodes.md`.

<!-- COMMON action -->

Other attributes that recur with identical definitions on several Action objects:

<!-- RECURRING action -->

## Index — Batch nodes

"specific attrs" = rows in `batch-nodes.md` (non-common attributes + common attributes whose definition differs).

<!-- INDEX batch -->

## Index — Action objects (PyCoNode)

<!-- INDEX action -->

## Source notes (garbles / oddities, kept or repaired)

<!-- NOTES -->
