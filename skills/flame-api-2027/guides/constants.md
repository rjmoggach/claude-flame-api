> Source: Defines for the flame Module (plus enumeration / string values from Python API "What's New in 2027", Colour Management API and Flame Python API Code Samples) — Autodesk Flame Family 2027 Help

# Defines, Enumerations and Option Values for the `flame` Module

## 1. Defines for the `flame` module (verbatim)

"Defines can be set for objects supported in the Python API. The following are just a subset of what's possible."

> **Note (source):** `flame.project` was changed to `flame.projects` in the 2020.1 Update version. Both syntaxes are supported for compatibility reasons, but we encourage the use of the latter instead of the former.

A "define" is the access path that yields an object of the given class. In the code samples, `<PyClip>`, `<PyBatch>`, etc. stand for an object obtained this way. `[#]` means "an index into the list".

| Object | Define (access path) | Class reference |
|---|---|---|
| PyProject | `<PyProject> ---> flame.projects.current_project` | [PyProject](../api/classes/PyProject.md) |
| PyWorkspace | `<PyWorkspace ---> flame.projects.current_project.current_workspace`<br>or<br>`PyProject.current_workspace` | [PyWorkspace](../api/classes/PyWorkspace.md) |
| PyDesktop | `<PyDesktop> ---> flame.projects.current_project.current_workspace.desktop`<br>or<br>`PyWorkspace.desktop` | [PyDesktop](../api/classes/PyDesktop.md) |
| PyBatch | `<PyBatch> ---> flame.projects.current_project.current_workspace.desktop.batch_groups[#]`<br>`<PyBatch> ---> flame.batch (current batch)` | [PyBatch](../api/classes/PyBatch.md) |
| PyNode | `<PyNode> ---> flame.projects.current_project.current_workspace.desktop.batch_groups[#].nodes[#]`<br>`<PyNode> ---> flame.projects.current_project.current_workspace.desktop.batch_groups[#].current_node`<br>`<PyNode> ---> flame.projects.current_project.current_workspace.desktop.batch_groups[#].get_node("name")`<br>`<PyNode> ---> flame.projects.current_project.current_workspace.desktop.batch_groups[#].create_node("type")` | [PyNode](../api/classes/PyNode.md) |
| PyReelGroup | `<PyReelGroup> ---> flame.projects.current_project.libraries[#].reel_groups[#]`<br>`<PyReelGroup> ---> flame.projects.current_project.current_workspace.desktop.reel_groups[#]` | [PyReelGroup](../api/classes/PyReelGroup.md) |
| PyReel | `<PyReel> ---> flame.projects.current_project.current_workspace.libraries[#].reel_groups[#].reels[#]`<br>`<PyReel> ---> flame.projects.current_project.current_workspace.desktop.reel_groups[#].reels[#]` | [PyReel](../api/classes/PyReel.md) |
| PyLibrary | `<PyLibrary> ---> flame.projects.current_project.current_workspace.libraries[#]` | [PyLibrary](../api/classes/PyLibrary.md) |
| PyFolder | `<PyFolder> ---> flame.projects.current_project.current_workspace.libraries[#].folders[#]`<br>`<PyFolder> ---> flame.projects.current_project.current_workspace.libraries[#].folders[#].folders[#]` | [PyFolder](../api/classes/PyFolder.md) |
| PyBatchIteration | `<PyBatchIteration> ---> flame.projects.current_project.current_workspace.desktop.batch_groups[#].batch_iterations[#]` | [PyBatchIteration](../api/classes/PyBatchIteration.md) |
| PyClip | `<PyClip> ---> flame.projects.current_project.current_workspace.libraries[#].clips[#]`<br>`flame.projects.current_project.current_workspace.desktop.reel_groups[#].reels[#].clips[#]` | [PyClip](../api/classes/PyClip.md) |
| PySequence | `<PySequence> ---> flame.projects.current_project.current_workspace.libraries[#].sequences[#]`<br>`flame.projects.current_project.current_workspace.desktop.reel_groups[#].reels[#].sequences[#]` | [PySequence](../api/classes/PySequence.md) |
| PyVersion | `<PyVersion> ---> PySequence.versions[#]` | [PyVersion](../api/classes/PyVersion.md) |
| PyTimelineFX | `<PyTimelineFX> ---> PyReel.sequences[#].versions[#].tracks[#].segments[#].effects[#]` | [PyTimelineFX](../api/classes/PyTimelineFX.md) |
| PyTrack | `<PyTrack> ---> PyReel.sequences[#].versions[#].tracks[#]` | [PyTrack](../api/classes/PyTrack.md) |
| PyMarker | `<PyMarker> ---> PyReel.sequences[#].versions[#].tracks[#].segments[#].markers[#]`<br>`PyReel.sequences[#].markers[#]` | [PyMarker](../api/classes/PyMarker.md) |
| PyAudioTrack | `<PyAudioTrack> ---> PyReel.sequences[#].audio_tracks[#]` | [PyAudioTrack](../api/classes/PyAudioTrack.md) |
| PySegment | `<PySegment> ---> PyReel.sequences[#].versions[#].tracks[#].segments[#]` | [PySegment](../api/classes/PySegment.md) |

Source quirks (kept verbatim above):
- `<PyWorkspace` is missing its closing `>` in the source.
- PyReelGroup's first path omits `current_workspace` (`flame.projects.current_project.libraries[#]`), whereas PyLibrary / PyReel / PyFolder use `flame.projects.current_project.current_workspace.libraries[#]`. Which is correct is not stated; the PyLibrary path is the one repeated most often.
- Second paths for PyClip, PySequence and PyMarker lack the `<PyXxx> --->` prefix.

> Agent note: `flame.batch`, `flame.projects`, `flame.timeline`, `flame.media_panel`, `flame.mediahub`, `flame.users` etc. are pre-instantiated module objects; see [../api/flame-module-data.md](../api/flame-module-data.md).

---

## 2. Enumerations

### `PyClip.VersionSelectionMode` (new in 2027)

Used by `<PyClip>.update_sources(version_selection_mode)`. Source: Python API → What's New in 2027 → PyClip. Class reference: [PyClip](../api/classes/PyClip.md).

| Constant | Meaning |
|---|---|
| `PyClip.KEEP_SELECTED_VERSION` | Keep the currently selected version. **Default.** |
| `PyClip.SELECT_CURRENT_VERSION` | Select the version defined in the source file. |
| `PyClip.SELECT_LATEST_VERSION` | Select the latest version available in the source. |

### Enumerations documented elsewhere in this library

Not part of the pages covered here; listed so they can be found:
- `PyExporter` preset enums `PresetType`, `PresetVisibility` — [../api/classes/PyExporter.md](../api/classes/PyExporter.md)
- "Enumeration Values" section — [../api/classes/PyMediaHubFilesTabOptions.md](../api/classes/PyMediaHubFilesTabOptions.md)

---

## 3. String option values that appear in these sources

Agent note: the API takes many options as UI-label strings. These are the exact strings used in the official samples / tables covered by this library. They are not exhaustive lists unless marked "(complete per source)".

### Node / effect type names

| Context | Strings seen |
|---|---|
| `PyBatch.create_node(type)` | `"Comp"`, `"Write File"`, `"Action"`, `"Metadata"`, `"Flip"`, `"2D Transform"`, `"Colour Mgmt"`, `"Colour Source"`, `"Matchbox"` (+ shader `"Blur.mx"`), `"Pybox"` (+ handler `"sendmail.py"`), `"OpenFX"` |
| `PyActionNode.create_node(type)` | `"Compass"`, `"IBL"` |
| `PySegment.create_effect(type)` / `PySequence.create_effect(type)` | `"Blur"`, `"OpenFX"`, `"Source Metadata"`, `"2D Transform"`, `"Source Colour Mgmt"`, `"Colour Mgmt"`; `create_effect("Blur", "Image")` adds Blur after an existing Image TL FX |
| `PyNode.type` values compared in samples | `"Action Media"`, `"Comp"` |
| `PyTimelineFX.type` values compared in samples | `"Image"`, `"Blur"`, `"Source Colour Mgmt"`, `"Colour Mgmt"` |

### Colour Mgmt (`PyClrMgmtNode` / `PyClrMgmtTimelineFX`) `mode` values

| Value | Notes |
|---|---|
| `"Tag Only"` | Set `tagged_colour_space`. |
| `"Input Transform"` | `tagged_colour_space` sets the Input Colour Space; also `working_space`. |
| `"View Transform"` | `display`, `view`, `tagged_colour_space`, `invert`. |
| `"Colour Transform"` | Selected automatically by `import_transform(path)` (CTF / LUT). |
| Auto Convert, etc. | Mentioned as existing in MediaHub but "not currently available via Python" there. |

### Other attribute values

| Attribute | Values seen | Source |
|---|---|---|
| `<PyRenderNode>.basic_metadata`, `<PyWriteFileNode>.basic_metadata` | `Custom Values`, `Use Input Values` (complete per source) | What's New 2027 |
| `<PyRenderNode>.basic_metadata_input`, `<PyWriteFileNode>.basic_metadata_input` | `Use Front Input`, `Use Metadata Input` (complete per source) | What's New 2027 |
| `<PyClip>.render(...)` | `render_mode="All"`, `render_option="Burn"`, `render_quality="Proxy Resolution"`, `effect_type="Batch FX"` | Code Samples |
| Comp node `flame_blend_mode` | `"Add"`, `"Screen"` | Looping by Node Type, Render Passes |
| MUX node `before_range` / `after_range` | `"Repeat First"`, `"Repeat Last"` | Code Samples |
| `flame.PyTime(timecode, rate)` frame rate | `"23.976 fps"` | Code Samples |
| `flame.set_current_tab(name)` | `"Timeline"` | Code Samples |
| `flame.execute_shortcut(name)` | `"Overwrite Edit"` | Code Samples |
| Clip node output socket (for `connect_nodes`) | `"BGR"`; multi-channel clips expose one socket per channel name (e.g. `"robot_direct_diffuse"`) | Render Passes, Multi-Channel |
| Input / output sockets used with `connect_nodes` | `"Result"`, `"Front"`, `"Back"`, `"output1 [ Comp ]"` (Action) | Examples |
| Metadata `socket_name` | `"Default"`, `"Result"` (Metadata node: "always Result or Default"), channel names for Render / Write File nodes | What's New 2027 |
| `flame.mediahub.files.options.set_tagged_colour_space(...)` special value | `"From File or Rules"` | Colour Management API |
