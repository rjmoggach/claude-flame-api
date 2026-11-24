> Source: Colour Management API — Autodesk Flame Family 2027 Help

# Colour Management API

The Python API allows you to access the tagged colour space of a clip and create Colour Mgmt tools as nodes in Batch or as Timeline FX. You may also control OCIO context variables at both the project and Colour Mgmt tool level. In addition, you may use the OCIO Python binding (`PyOpenColorIO`), which is installed with the application.

Class references: [PyClrMgmtNode](../api/classes/PyClrMgmtNode.md), [PyClrMgmtTimelineFX](../api/classes/PyClrMgmtTimelineFX.md), [PyProject](../api/classes/PyProject.md), [PyNode](../api/classes/PyNode.md) (`colour_space`), [PyClip](../api/classes/PyClip.md) / [PySequence](../api/classes/PySequence.md) / [PySegment](../api/classes/PySegment.md) (`get_colour_space`), [PyActionNode](../api/classes/PyActionNode.md) (`input_colour_space`), [PyMediaHubFilesTabOptions](../api/classes/PyMediaHubFilesTabOptions.md) (`set_tagged_colour_space`).

> Agent note: the Colour Mgmt node/effect settings used below (`mode`, `tagged_colour_space`, `working_space`, `bit_depth`, `display`, `view`, `invert`, `context_variables_from_project`) are node attributes that are **not** listed in the PyClrMgmtNode / PyClrMgmtTimelineFX class reference files; this page is their source. Likewise `PySequence.create_effect(...)`, used in the "Converting the colour space → On the Timeline" sample, is not listed in [PySequence](../api/classes/PySequence.md) (only `PySegment.create_effect` is).

## Quick reference

| Task | Batch | Timeline | Project |
|---|---|---|---|
| Read tagged colour space | `<PyNode>.colour_space` (read-only, main output) | `<PySequence/PyClip/PySegment>.get_colour_space(PyTime)` (current frame if omitted) | — |
| Set (tag) colour space | `create_node("Colour Mgmt")`, `mode = "Tag Only"`, `tagged_colour_space = ...` | `create_effect("Source Colour Mgmt")` (source effect) or `"Colour Mgmt"` (non-source), `mode = "Tag Only"` | — |
| Colour Source node colour space | `create_node("Colour Source").colour_space = ...` (get or set) | — | — |
| Action read nodes | `action.create_node(node_type="IBL", file_path=..., input_colour_space=...)`, `action.import_fbx(..., input_colour_space=...)`; `read_fbx()` and `import_psd()` also take `input_colour_space` | — | `prj.action_colour_space` (default Action rendering colour space; cannot be set per Action node via Python) |
| MediaHub import tagging | `flame.mediahub.files.options.set_tagged_colour_space(name)` (forces "Tag Only"), or `"From File or Rules"` | | |
| Convert | `mode = "Input Transform"` / `"View Transform"`; `import_transform(path)` → `"Colour Transform"` | same, except no `bit_depth` | — |
| OCIO context variables | `node.get_context_variables()` (dict), `context_variables_from_project = False`, `set_context_variable(name, value)`, `reset_context_variables()` | same on the Colour Mgmt Timeline FX | `prj.get_context_variables()`, `set_context_variable`, `reset_context_variables()` |
| Config | — | — | `prj.reload_ocio_config([True])`, `prj.export_ocio_config(config_name, dest_folder, locked, overwrite, gen_ocioz)`; `prj.working_colour_space` (scene_linear role), `prj.action_colour_space` (rendering role) |

Rules stated by the source:
- An exception will be raised if you try to set a value that does not exist, for example a colour space name or a display name that is not in the config.
- You may use one of a colour space's **alias** names instead of its canonical name.
- For **View Transform**, you must set `view` to an option that exists for the `display` you set — this is **not validated** by the setter.
- In **Input Transform** mode, `tagged_colour_space` actually sets the Input Colour Space.
- `bit_depth` takes a number, not a string (Batch only; not available on the Timeline FX).
- Each timeline frame is tagged and could potentially be a different colour space, hence `get_colour_space()` takes a `PyTime`.
- The Flame binding spells "colour" with a "u"; the OCIO binding spells it "color".

---

## Getting and setting the colour space

### In Batch

Batch nodes have a `colour_space` read-only property that provides the tagged colour space of the main output. If you need to set the colour space, use **Tag Only** mode on a Colour Mgmt node:

```python
import flame

# Get the output colour space from any Batch node.
cs_name = flame.batch.get_node("import1").colour_space

# Get or set the colour space of a Colour Source node.
colour = flame.batch.create_node("Colour Source")
colour.colour_space = "ACEScg"

# Create a Batch node to set the colour space.
tag_it = flame.batch.create_node("Colour Mgmt")
tag_it.mode = "Tag Only"
tag_it.tagged_colour_space = "ACEScct"
# Now connect this node to the output of the node you want to tag ...
```

### On the Timeline

You may get the tagged colour space from a `PySequence`, `PyClip`, or `PySegment`. Each frame is tagged and potentially could be a different colour space (for example, if the user has made edits at the frame level). Therefore, the `get_colour_space` function takes a `PyTime` as an argument to identify the frame. If no time is provided, it returns the colour space of the current frame.

```python
import flame

# Get a sequence.
seq = flame.find_by_name("My Sequence")[0]
# Get the colour space at a given time.
cs_name = seq.get_colour_space(flame.PyTime(0))

# Create a Timeline FX to set the colour space. This creates a source effect.
# Use just "Colour Mgmt" to create a non-source effect.
tag_it = flame.timeline.current_segment.create_effect("Source Colour Mgmt")
tag_it.mode = "Tag Only"
tag_it.tagged_colour_space = "ACEScct"
```

### In Action

In Action, various read nodes allow you to specify the colour space of the file. The colour space of each imported element will be converted to the Action rendering colour space. The default rendering colour space for Action is set at the project level.

```python
import flame

# Set the default rendering colour space used by Action at the project level.
# Currently, this may not be set on individual Action nodes via Python.
prj = flame.projects.current_project
prj.action_colour_space = "ACEScg"

# Set the colour space of an IBL node.
action = flame.batch.create_node("Action")
action.create_node(
    node_type="IBL",
    file_path="/my/ibl.exr",
    input_colour_space="ACES2065-1"
)

# Set the colour space of an FBX scene, including any incorporated textures.
action2 = flame.batch.create_node("Action")
action2.import_fbx(
    file_path="/my/fbx.fbx",
    input_colour_space="sRGB Encoded Rec.709 (sRGB)"
)
# The read_fbx() and import_psd() also have an input_colour_space parameter.
```

### In MediaHub

In the MediaHub, you may set the General Colour Management options to `Tag Only` mode and set the colour space. The other Colour Management modes (Auto Convert, etc.) are not currently available via Python, though you may apply them with a Colour Mgmt Timeline FX.

```python
import flame

opt = flame.mediahub.files.options
# Note that invoking this command will switch the mode to "Tag Only", regardless
# of what mode it was currently in.
opt.set_tagged_colour_space("ACES2065-1")
# You may also enable "From File or Rules" mode.
opt.set_tagged_colour_space("From File or Rules")
```

---

## Converting the colour space

You may use a Colour Mgmt node or Colour Mgmt Timeline FX to convert the colour space using the **Input Transform** or **View Transform** modes, or you may use **Tag Only** mode, as shown above.

The **Colour Transform** mode may be used to load a CTF or LUT from a file (this is equivalent to an OCIO FileTransform).

An exception will be raised if you try to set a value that does not exist, for example, if you use a colour space name or a display name that is not in the config. You may also use one of a colour space's alias names instead of its canonical name.

However, in the case of **View Transform** you must be careful to set the `view` to an option that exists for the `display` that you set, since this is not validated by the setter.

### In Batch

```python
import flame

# Create an Input Transform.
clr1 = flame.batch.create_node("Colour Mgmt")
clr1.mode = "Input Transform"
# Note: The tagged_colour_space actually sets the Input Colour Space, in this case.
clr1.tagged_colour_space = "ACEScct"
clr1.working_space = "ACEScg"
# Set the bit depth of the output. Note that the argument is a number, not a string.
clr1.bit_depth = 32

# Create a View Transform.
clr2 = flame.batch.create_node("Colour Mgmt")
clr2.mode = "View Transform"
clr2.display = "sRGB - Display"
clr2.view = "ACES 2.0 - SDR 100 nits (Rec.709)"
clr2.tagged_colour_space = "ACEScg"
# Enable invert mode, to convert from the display back to the tagged colour space.
clr2.invert = True

# Load a CTF file as a Colour Transform.
clr3 = flame.batch.create_node("Colour Mgmt")
# (Using the import_transform function automatically selects Colour Transform mode.)
clr3.import_transform("/opt/Autodesk/colour_mgmt/configs/legacy_configs/syncolor_ctfs/misc/green-channel-only.ctf")
```

### On the Timeline

The Timeline FX supports the same options as the Batch effect, with the exception of the `bit_depth` attribute.

```python
import flame

# Get a sequence by name.
sequence = flame.find_by_name("My Sequence")[0]

# Create a Source Timeline FX.
clr1 = sequence.create_effect("Source Colour Mgmt")

# Create an Input Transform.
clr1.mode = "Input Transform"
# Note: The tagged_colour_space actually sets the Input Colour Space, in this case.
clr1.tagged_colour_space = "ACEScct"
clr1.working_space = "ACEScg"

# Get the current segment.
segment = flame.timeline.current_segment

# Create a (non-source) Timeline FX.
clr2 = segment.create_effect("Colour Mgmt")

# Create a View Transform.
clr2.mode = "View Transform"
clr2.display = "sRGB - Display"
clr2.view = "ACES 2.0 - SDR 100 nits (Rec.709)"
clr2.tagged_colour_space = "ACEScg"
# Enable invert mode, to convert from the display back to the tagged colour space.
clr2.invert = True

# Load a CTF file as a Colour Transform.
# (Using the import_transform function automatically selects Colour Transform mode.)
clr2.import_transform("/opt/Autodesk/colour_mgmt/configs/legacy_configs/syncolor_ctfs/misc/green-channel-only.ctf")
```

---

## Using context variables

You may get and set OCIO context variables either at the project level or on individual Colour Mgmt Batch nodes or Timeline FX.

This allows you to write a script that sets the context variables for each segment on a timeline based on metadata such as the shot name.

You may find the "Context Var. Example" config preset installed with the application to be useful for experimentation.

An example script that creates Python hooks to set context variables based on selected Batch nodes or Timeline segments is installed at: `/opt/Autodesk/<flame_version>/python_utilities/examples/context_variables.py`.

For more, see the help page "OCIO Context Variables" (not part of this library).

### In Project Preferences

```python
import flame

# Get the current project.
prj = flame.projects.current_project

# Get the context variables, as a dictionary.
cv = prj.get_context_variables()

# Get the current value of variable "CCC_ID".
val = cv["CCC_ID"]

# Set the value of the variable "CCC_ID" to a new value.
prj.set_context_variable("CCC_ID", "0002")

# Reset the context variables based on the config's environment section.
prj.reset_context_variables()
```

### In Batch

```python
import flame

# Get a Batch node by name.
node = flame.batch.get_node("clrmgmt10")

# Get the context variables, as a dictionary.
cv = node.get_context_variables()

# Get the current value of variable "CCC_ID".
val = cv["CCC_ID"]

# Turn off "From Project" mode to allow use of custom context variables.
node.context_variables_from_project = False

# Set the value of the variable "CCC_ID" to a new value.
node.set_context_variable("CCC_ID", "0002")

# Reset the context variables to the current values set at the project level.
node.reset_context_variables()
```

### On the Timeline

```python
import flame

# Get the current segment.
segment = flame.timeline.current_segment

# Look for a "Colour Mgmt" effect on this segment, if it exists.
colour_mgmt_effect = None
for fx in segment.effects:
    if fx.type == "Source Colour Mgmt":
        colour_mgmt_effect = fx
        break
    elif fx.type == "Colour Mgmt":
        colour_mgmt_effect = fx
        break

# The following examples obviously won't work if there is no Colour Mgmt effect.
if colour_mgmt_effect is None:
    return

# Get the context variables, as a dictionary.
cv = colour_mgmt_effect.get_context_variables()

# Get the current value of variable "CCC_ID".
val = cv["CCC_ID"]

# Turn off "From Project" mode to allow use of custom context variables.
colour_mgmt_effect.context_variables_from_project = False

# Set the value of the variable "CCC_ID" to a new value.
colour_mgmt_effect.set_context_variable("CCC_ID", "0002")

# Reset the context variables to the current values set at the project level.
colour_mgmt_effect.reset_context_variables()
```

> Agent note: this sample contains a bare `return` at module level (`if colour_mgmt_effect is None: return`), which is a `SyntaxError` if run as a top-level script in the Python Console. It is verbatim from the source; wrap the code in a function (or replace `return` with another guard) when using it.

---

## Reloading or exporting an OCIO config

`reload_ocio_config(True)` also deletes all project overrides (custom colour spaces, views, file rules, and context variables). `export_ocio_config(config_name, dest_folder, locked, overwrite, gen_ocioz)` — defaults per comments: `dest_folder` = OCIO configs shared path, `locked=False`, `overwrite=False`, `gen_ocioz=False`.

```python
import flame

# Get the current project.
prj = flame.projects.current_project

# Reload the config.
prj.reload_ocio_config()

# Reload the config and delete all project overrides such as
# custom colour spaces, views, file rules, and context variables.
prj.reload_ocio_config(True)

# Export the config.

# Set the config name shown in the Project Management panel.
config_name = "my customized config"
# Set the location for the export (default: OCIO configs shared path).
dest_folder = "/Volumes/server1/shared_configs"
# Whether users will be able to override settings in new projects (default: False).
locked = False
# Overwrite any existing exported config of that name (default: False).
overwrite = True
# Generate an OCIOZ archive file alongside the exported config (default: False).
gen_ocioz = True

prj.export_ocio_config( config_name, dest_folder, locked, overwrite, gen_ocioz )
```

---

## Modifying project preferences

`working_colour_space` is the **scene_linear** role in the config; `action_colour_space` is the **rendering** role.

```python
import flame

# Get the current project.
prj = flame.projects.current_project

# Get or set the Working Colour Space for the project.
# This is the scene_linear role in the config.
prj.working_colour_space = "ACEScg"

# Get or set the Action Colour Space for the project.
# This is the rendering role in the config.
prj.action_colour_space = "ACEScg"
```

---

## Using the OCIO Python binding

The application has the OCIO Python binding installed and you may use it in connection with the Flame colour management API. (The Flame binding spells "colour" with a "u", while the OCIO binding spells it "color".)

The following example assumes that no user overrides have been made to the config. If you want to load a config that contains any overrides, you could export the config as shown in a previous example and load that instead.

> Note (source): You should not make modifications to a config in an open project. The application would not pick up any changes unless you wrote out the modified config and then used `reload_ocio_config` as shown in a previous example.

The project's config is at `os.path.join(prj.setups_folder, "colour_mgmt", "config.ocio")`, usually a soft-link; resolve it with `os.path.realpath` before using anything that depends on the config's search path.

For more about OCIO, see the help page "OpenColorIO in Flame" (not part of this library).

```python
import flame
import PyOpenColorIO as ocio
import os.path

# Start by getting the path to the OCIO config used by the project.
prj = flame.projects.current_project
config_path = os.path.join(prj.setups_folder, "colour_mgmt", "config.ocio")

# In most cases, the above config_path will be a soft-link to the actual config.
# If you need to do anything that involves the config's search path, such as
# loading the transforms for a colour space, it's important to de-reference the
# soft-link to the real path. Otherwise the search paths won't work since they
# will be relative to the soft-link rather than the real path.
config_path = os.path.realpath(config_path)

# Load the OCIO config for the project.
cfg = ocio.Config.CreateFromFile(config_path)

# Now you may use any of the features of the OCIO API. Here are some examples:

# Inspect properties of a colour space.
cs = cfg.getColorSpace("ACES2065-1")
print( list(cs.getAliases()) )

# Get the views for a display.
views = cfg.getViews("sRGB - Display")
print( list(views) )

# Convert an RGB value.
cst = ocio.ColorSpaceTransform("ACES2065-1", "ACEScg")
cpu = cfg.getProcessor(cst).getDefaultCPUProcessor()
rgb = cpu.applyRGB([0.5, 0.4, 0.3])
```
