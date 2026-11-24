# Flame object model — how to reach things

> Source: derived from the per-class reference in [classes/](classes/) (pydoc + "Py* Attributes" pages) and code samples in the 2027 help. Every property/method named here exists in the linked class file.

## 1. Entry points: module singletons

`import flame` exposes pre-built singleton objects (see [flame-module-data.md](flame-module-data.md)):

| Singleton | Class | Use |
|---|---|---|
| `flame.projects` / `flame.project` | [`PyProjectSelector`](classes/PyProjectSelector.md) | `.current_project` → `PyProject` |
| `flame.batch` | [`PyBatch`](classes/PyBatch.md) | The current Batch Group (schematic, nodes, render) |
| `flame.media_panel` | [`PyMediaPanel`](classes/PyMediaPanel.md) | `.selected_entries`, panel visibility, copy/move |
| `flame.timeline` | [`PyTimeline`](classes/PyTimeline.md) | `.clip`, `.current_segment`, `.current_effect`, `.current_marker`, `.current_transition`, `.type` |
| `flame.mediahub` | [`PyMediaHub`](classes/PyMediaHub.md) | MediaHub tabs (files / projects / archives) |
| `flame.browser` | [`PyBrowser`](classes/PyBrowser.md) | File browser (`.show(...)`, `.selection`) |
| `flame.messages` | [`PyMessages`](classes/PyMessages.md) | Message bar in the UI |
| `flame.search` | [`PySearch`](classes/PySearch.md) | Search |
| `flame.users` | [`PyUsers`](classes/PyUsers.md) | `.current_user` → `PyUser` |

Module-level functions (`flame.find_by_name`, `flame.find_by_uid`, `flame.import_clips`, `flame.delete`, `flame.duplicate`, `flame.execute_command`, `flame.execute_shortcut`, `flame.schedule_idle_event`, `flame.set_current_tab`, `flame.get_version`, …): [flame-module-functions.md](flame-module-functions.md).

## 2. Containment tree (Media Panel)

```
flame.projects.current_project                         PyProject
 ├─ .current_workspace                                 PyWorkspace
 │   ├─ .desktop                                       PyDesktop
 │   │   ├─ .reel_groups[]                             PyReelGroup
 │   │   │   └─ .reels[]                               PyReel  (.type: Reel | Schematic | Sequences | Shelf)
 │   │   │       ├─ .clips[]                           PyClip
 │   │   │       └─ .sequences[]                       PySequence (subclass of PyClip)
 │   │   └─ .batch_groups[]                            PyBatch
 │   └─ .libraries[]                                   PyLibrary
 │       └─ .folders[] / .reel_groups[] / .reels[] / .clips[] / .sequences[]
 │          .batch_groups[] / .batch_iterations[] / .desktops[]   (PyFolder has the same set)
 └─ .shared_libraries[]                                PyLibrary
```
Every container also has `.children` (all immediate children) and every `PyFlameObject` has `.parent`.

## 3. Clip / sequence internals

```
PyClip / PySequence
 ├─ .versions[]                 PyVersion
 │   └─ .tracks[]               PyTrack            (PySubtitleTrack derives from PyTrack)
 │       ├─ .segments[]         PySegment          (.effects[] → PyTimelineFX subclasses, .markers[])
 │       └─ .transitions[]      PyTransition
 ├─ .audio_tracks[]             PyAudioTrack
 ├─ .subtitles[]                PySubtitleTrack
 ├─ .markers[]                  PyMarker
 └─ PySequence only: .groups[]  PySequenceGroup
```
Segment timing: `record_in`, `record_out`, `record_duration`, `source_in`, `source_out`, `source_duration`, `head`, `tail` (values are `PyTime`). Source media info: `file_path`, `source_name`, `source_uid`, `tape_name`, `source_*` format properties.

## 4. Batch

```
flame.batch                      PyBatch (current Batch Group)
 ├─ .nodes[]                     PyNode and subclasses (PyActionNode, PyClipNode, PyWriteFileNode, PyOFXNode, …)
 ├─ .node_types                  list[str] usable with create_node()
 ├─ .batch_iterations[] / .current_iteration / .current_iteration_number
 ├─ .reels[] (schematic reels) / .shelf_reels[]
 └─ .contexts / .cursor_position / .opened
PyNode: .input_sockets, .output_sockets, .sockets (dict of connections), .colour_space
PyActionFamilyNode (Action / Image / GMaskTracer): own schematic of PyCoNode objects
   create_node(), get_node(), connect_nodes(), disconnect_nodes(), clear_schematic()
```
Per-node-type attributes: [../nodes/](../nodes/).

## 5. Values: `PyAttribute`, `PyTime`, `PyResolution`

- Attribute access on Flame objects (`clip.name`, `node.bypass`, `seg.record_in`, …) usually returns a [`PyAttribute`](classes/PyAttribute.md) wrapper, not the raw Python value. Use `.get_value()` to unwrap and `.set_value(v)` (returns `bool`) to write; `.values` lists possible values/range. Plain assignment (`node.bypass = True`) also works via `__setattr__`. The wrapper supports arithmetic/comparison operators and `str()`.
  - Samples in the help do exactly this: `<PyClip>.in_mark.get_value().frame`, `track.selected_segments.get_value()`, `seq.primary_track.get_value().name`, `flame.batch.current_node.get_value()`.
  - Agent note: when you need a real Python `str`/`int`/`list` (comparisons, `json.dumps`, string formatting into paths), call `.get_value()` explicitly.
- `obj.attributes` (on every `PyFlameObject`) lists the attribute names available on that instance — useful for discovery at runtime.
- Only three classes are constructible from Python:
  - [`PyTime`](classes/PyTime.md): `flame.PyTime(timecode, frame_rate)` (str, str), `flame.PyTime(relative_frame)` (int), `flame.PyTime(absolute_frame, frame_rate)` (int, str); properties `frame`, `relative_frame`, `timecode`, `frame_rate`.
  - [`PyResolution`](classes/PyResolution.md): `PyResolution()`, `PyResolution(width, height, bit_depth, frame_ratio, scan_format)` (int, int, int, float, str); pydoc also lists a single-`str` overload (undocumented — presumably a resolution preset name, cf. the `resolution` property "based on its name in the UI"; verify at runtime).
  - [`PyExporter`](classes/PyExporter.md): `flame.PyExporter()` — export settings + `export(...)`; preset enums `PresetType`, `PresetVisibility`.
  Everything else raises if instantiated; obtain it by navigation or creation methods (`create_reel`, `create_folder`, `create_sequence`, `create_node`, `create_library`, `create_batch_group`, …).

## 6. Media Panel objects (`PyArchiveEntry`)

`PyArchiveEntry` subclasses (Project, Workspace, Library, Folder, Desktop, ReelGroup, Reel, Clip, Sequence, BatchIteration, MediaHub entries) all have methods `commit()`, `clear_colour()`, `get_wiretap_node_id()`, `get_wiretap_storage_id()`. Media Panel entries (Workspace, Library, Folder, Desktop, ReelGroup, Reel, Clip, …; not PyProject) also document `name`, `uid`, `colour`, `colour_label`, `selected`, `expanded`, `tags` — check each class's Attributes section. Look up by `flame.find_by_uid(uid)`, `flame.find_by_name(name, parent=None)`, `flame.find_by_wiretap_node_id(id)`.

## 7. Threading & processes (documented constraints)

- Python hooks are blocking — they hold the application until they return (see [../hooks/](../hooks/) for the threading-hook pattern).
- `flame.schedule_idle_event(function, delay=0)` runs a callback later on the main application thread; it must be quick and non-blocking.
- Prefer `flame.execute_command(command, blocking=True, shell=False, capture_stdout=False, capture_stderr=False)` over `subprocess`/`os.system`: native Python subprocess forks the (large) Flame process. Environment variables are **not** forwarded to the executed command.
