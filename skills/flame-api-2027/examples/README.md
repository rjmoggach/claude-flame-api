> Source: Flame Python API Code Samples; Python API Examples; Looping by Node Type; Render Passes with the Python API; Importing Multi-Channel Clip; Colour Management API; Write Your First Python API Script; Python API (What's New in 2027) — Autodesk Flame Family 2027 Help

# Flame 2027 Python API — Examples Index

Every official code sample from the pages above, indexed. Code in all linked files is verbatim from the official HTML (checked against `HTML_DOWNLOAD/`); source bugs are kept and flagged in "Source issue" notes next to the sample.

Conventions:
- `<PyClip>`, `<PySegment>`, ... are placeholders for objects of that class, not valid Python — see [../guides/constants.md](../guides/constants.md) for how to obtain each one.
- "APIs used" lists the classes/members the sample touches (from the sample's description, or extracted from its code when the source gives no description).
- Class reference: [../api/classes/](../api/classes/); module functions: [../api/flame-module-functions.md](../api/flame-module-functions.md).

## Files

| File | Contents | Source page(s) |
|---|---|---|
| [clips.md](clips.md) | Clip import, reformat, render, `PyTime`, in/out marks, current time | Flame Python API Code Samples |
| [timeline.md](timeline.md) | Segment selection, markers, segment properties, Timeline FX, tracks, `parent` in custom actions | Flame Python API Code Samples |
| [batch.md](batch.md) | Batch nodes (Matchbox, Pybox, OpenFX, MUX), Action compasses, looping by node type, render-pass comp, multi-channel clip import | Flame Python API Code Samples; Looping by Node Type; Render Passes with the Python API; Importing Multi-Channel Clip |
| [media-panel-and-ui.md](media-panel-and-ui.md) | Desktop/Freeform views, reels, batch groups & iterations, media panel, users, tabs | Flame Python API Code Samples |
| [../guides/getting-started.md](../guides/getting-started.md) | First script (5 progressive blocks), catching exceptions | Write Your First Python API Script; Python API Examples |
| [../guides/colour-management.md](../guides/colour-management.md) | All 12 Colour Management API samples | Colour Management API |
| [../guides/whats-new-2027.md](../guides/whats-new-2027.md) | All 80 "What's New in 2027" samples (metadata API, update_sources, markers, expressions, timewarp gap fill, cache clearing) | Python API |

## Example index

### [clips.md](clips.md)

| Example | Section | APIs used |
|---|---|---|
| [Import a clip into a library](clips.md#import-a-clip-into-a-library) | Clip Import | `flame.import_clips()` |
| [Change the resolution of a clip](clips.md#change-the-resolution-of-a-clip) | Clip Reformat | `PyClip.reformat(width, height, ratio)` |
| [Render all Timeline FX in proxy resolution using Burn](clips.md#render-all-timeline-fx-in-proxy-resolution-using-burn) | Rendering a Clip | `PyClip.render(render_mode, render_option, render_quality)` |
| [Render all the Batch FX on a clip](clips.md#render-all-the-batch-fx-on-a-clip) | Rendering a Clip | `PyClip.render(effect_type)` |
| [Get the render state of a clip](clips.md#get-the-render-state-of-a-clip) | Rendering a Clip | `PyClip.is_rendered()` |
| [Set a PyTime in timecode](clips.md#set-a-pytime-in-timecode) | Using PyTime | `flame.PyTime(timecode_str, frame_rate_str)` |
| [Set a PyTime in relative frame](clips.md#set-a-pytime-in-relative-frame) | Using PyTime | `flame.PyTime(int)` |
| [Set a PyTime in absolute frame](clips.md#set-a-pytime-in-absolute-frame) | Using PyTime | `flame.PyTime(int, frame_rate_str)` |
| [Get the current time of a clip in frame](clips.md#get-the-current-time-of-a-clip-in-frame) | Using PyTime | `PyClip.current_time`, `PyTime.frame` |
| [Get the current time of a clip in relative frame](clips.md#get-the-current-time-of-a-clip-in-relative-frame) | Using PyTime | `PyTime.relative_frame` |
| [Get the current time of a clip in timecode](clips.md#get-the-current-time-of-a-clip-in-timecode) | Using PyTime | `PyTime.timecode` |
| [Print a list of clips located in a reel](clips.md#print-a-list-of-clips-located-in-a-reel) | Clip Operations | `PyReel.clips` |
| [Store a clip in a define](clips.md#store-a-clip-in-a-define) | Clip Operations | `.clips` |
| [Set an in mark on a clip based on relative frame](clips.md#set-an-in-mark-on-a-clip-based-on-relative-frame) | Clip Operations | `PyClip.in_mark` (accepts an int) |
| [Set an in mark on a clip based on a PyTime timecode](clips.md#set-an-in-mark-on-a-clip-based-on-a-pytime-timecode) | Clip Operations | `PyClip.in_mark` (accepts a `PyTime`) |
| [Get the in mark value in frame](clips.md#get-the-in-mark-value-in-frame) | Clip Operations | `PyClip.in_mark` is a `PyAttribute`; `.get_value()` returns the `PyTime` |
| [Set an out mark on a clip based on relative frame](clips.md#set-an-out-mark-on-a-clip-based-on-relative-frame) | Clip Operations | `.out_mark` |
| [Set an out mark on a clip based on a PyTime timecode](clips.md#set-an-out-mark-on-a-clip-based-on-a-pytime-timecode) | Clip Operations | `flame.PyTime()`, `.out_mark` |
| [Get the out mark value in frame](clips.md#get-the-out-mark-value-in-frame) | Clip Operations | `.out_mark`, `.get_value()`, `.frame` |
| [Get the duration of a clip between in and out marks in frame](clips.md#get-the-duration-of-a-clip-between-in-and-out-marks-in-frame) | Clip Operations | `PyClip.duration` |
| [Set the current time on a clip based on a timecode value](clips.md#set-the-current-time-on-a-clip-based-on-a-timecode-value) | Clip Operations | `PyClip.current_time` (accepts a timecode string) |
| [Set the current time on a clip based on an absolute frame using PyTime](clips.md#set-the-current-time-on-a-clip-based-on-an-absolute-frame-using-pytime) | Clip Operations | `flame.PyTime()`, `.current_time` |
| [Get the current time of a clip in frame (Clip Operations repeat)](clips.md#get-the-current-time-of-a-clip-in-frame-clip-operations-repeat) | Clip Operations | `.current_time`, `.frame` |

### [timeline.md](timeline.md)

| Example | Section | APIs used |
|---|---|---|
| [Select all segments on the bottom video track of a clip](timeline.md#select-all-segments-on-the-bottom-video-track-of-a-clip) | Select Segments on the Timeline | `PyVersion.tracks`, `PyTrack.segments`, `PySegment.selected` |
| [Select all segments that are unrendered on a track](timeline.md#select-all-segments-that-are-unrendered-on-a-track) | Select Segments on the Timeline | `PySegment.is_rendered()`, `PySegment.selected` |
| [Change the comment of all selected markers on a timeline segment](timeline.md#change-the-comment-of-all-selected-markers-on-a-timeline-segment) | Select Segments on the Timeline | `PySegment.selected_markers`, `PyMarker.comment` |
| [Print the name of all the markers located on a clip](timeline.md#print-the-name-of-all-the-markers-located-on-a-clip) | Working with Markers | `PyClip.markers`, `PyMarker.name` |
| [Create a marker on the 10th frame of a clip](timeline.md#create-a-marker-on-the-10th-frame-of-a-clip) | Working with Markers | `PyClip.create_marker(frame)` |
| [Select all markers of a clip](timeline.md#select-all-markers-of-a-clip) | Working with Markers | `PyMarker.selected` |
| [Select all markers of a segment](timeline.md#select-all-markers-of-a-segment) | Working with Markers | `.segments`, `.selected` |
| [Change the location of a marker on a clip](timeline.md#change-the-location-of-a-marker-on-a-clip) | Working with Markers | `PyMarker.location` |
| [Move a marker to the middle of a timeline segment](timeline.md#move-a-marker-to-the-middle-of-a-timeline-segment) | Working with Markers | `PySegment.record_in`, `PySegment.record_duration`, `PyMarker.location` |
| [Rename a marker on a segment to the segment's name](timeline.md#rename-a-marker-on-a-segment-to-the-segments-name) | Working with Markers | `PySegment.name`, `PySegment.markers`, `PyMarker.name` |
| [Change the comment of a marker on a clip using tokens](timeline.md#change-the-comment-of-a-marker-on-a-clip-using-tokens) | Working with Markers | `PyMarker.comment` (accepts tokens such as `<user>`, `<date>`) |
| [Get the name of a timeline segment](timeline.md#get-the-name-of-a-timeline-segment) | Segment Operations | `.segments`, `.name` |
| [Get the name of all segments in a timeline](timeline.md#get-the-name-of-all-segments-in-a-timeline) | Segment Operations | `flame.timeline.clip.versions`, `PyVersion.tracks`, `PyTrack.segments` |
| [Get the name of all selected segments in a timeline](timeline.md#get-the-name-of-all-selected-segments-in-a-timeline) | Segment Operations | `PyTrack.selected_segments` (a `PyAttribute`; `.get_value()` returns the list) |
| [Get the name of the currently selected timeline segment](timeline.md#get-the-name-of-the-currently-selected-timeline-segment) | Segment Operations | `flame.timeline.current_segment` |
| [Set the shot name of a timeline segment](timeline.md#set-the-shot-name-of-a-timeline-segment) | Segment Operations | `.shot_name` |
| [Set the comment of a timeline segment](timeline.md#set-the-comment-of-a-timeline-segment) | Segment Operations | `.comment` |
| [Get the source file path of a timeline segment](timeline.md#get-the-source-file-path-of-a-timeline-segment) | Segment Operations | `.file_path` |
| [Add a Blur Timeline FX to a timeline segment](timeline.md#add-a-blur-timeline-fx-to-a-timeline-segment) | Segment Operations | `PySegment.create_effect(type)` |
| [Add a Blur Timeline FX after an existing Image TL FX](timeline.md#add-a-blur-timeline-fx-after-an-existing-image-tl-fx) | Segment Operations | `PySegment.create_effect(type, after_type)` |
| [Print the TL FX that can be added on a timeline segment](timeline.md#print-the-tl-fx-that-can-be-added-on-a-timeline-segment) | Segment Operations | `.effect_types` |
| [Print the existing PyTimelineFX of a timeline segment](timeline.md#print-the-existing-pytimelinefx-of-a-timeline-segment) | Segment Operations | `.effects` |
| [Store a Timeline FX in a define](timeline.md#store-a-timeline-fx-in-a-define) | Segment Operations | `.effects` |
| [Bypass all Image Timeline FXs in a sequence](timeline.md#bypass-all-image-timeline-fxs-in-a-sequence) | Segment Operations | `PySegment.effects`, `PyTimelineFX.type`, `PyTimelineFX.bypass` |
| [Get the hidden information of a timeline segment](timeline.md#get-the-hidden-information-of-a-timeline-segment) | Segment Operations | `.segments`, `.hidden` |
| [Hide a timeline segment](timeline.md#hide-a-timeline-segment) | Segment Operations | `.segments`, `.hidden` |
| [Get the colour information of a timeline segment](timeline.md#get-the-colour-information-of-a-timeline-segment) | Segment Operations | `.segments`, `.colour` |
| [Set the colour of a timeline segment to blue](timeline.md#set-the-colour-of-a-timeline-segment-to-blue) | Segment Operations | `PySegment.colour` (RGB float tuple) |
| [Get source information of a timeline segment](timeline.md#get-source-information-of-a-timeline-segment) | Segment Operations | `.segments`, `.source_name`, `.source_in`, `.source_out`, `.source_duration`, `.tape_name` |
| [Get record in / out / duration of a timeline segment](timeline.md#get-record-in--out--duration-of-a-timeline-segment) | Segment Operations | `.segments`, `.record_in`, `.record_out`, `.record_duration` |
| [Bypass a Timeline FX on a timeline segment](timeline.md#bypass-a-timeline-fx-on-a-timeline-segment) | Timeline FX | `.bypass` |
| [Get the Bypass status of a Timeline FX](timeline.md#get-the-bypass-status-of-a-timeline-fx) | Timeline FX | `.bypass` |
| [Print the names of all TL FX existing on a timeline segment](timeline.md#print-the-names-of-all-tl-fx-existing-on-a-timeline-segment) | Timeline FX | `PyTimelineFX.type` |
| [Bypass all Image Timeline FXs in a sequence (repeat of the sample above)](timeline.md#bypass-all-image-timeline-fxs-in-a-sequence-repeat-of-the-sample-above) | Timeline FX | `.segments`, `.effects`, `.type`, `.bypass` |
| [Save a Timeline FX setup using the .effects list index](timeline.md#save-a-timeline-fx-setup-using-the-effects-list-index) | Timeline FX | `PyTimelineFX.save_setup(path)`. `#` is a placeholder for an index |
| [Save a setup for a particular Timeline FX](timeline.md#save-a-setup-for-a-particular-timeline-fx) | Timeline FX | `.effects`, `.type`, `.save_setup()` |
| [Load a Timeline FX setup on a timeline segment](timeline.md#load-a-timeline-fx-setup-on-a-timeline-segment) | Timeline FX | `PySegment.create_effect`, `PyTimelineFX.load_setup(path)` |
| [Load a Timeline FX setup on all selected timeline segments](timeline.md#load-a-timeline-fx-setup-on-all-selected-timeline-segments) | Timeline FX | `PyTrack.selected_segments.get_value()`, `PySegment.create_effect("OpenFX")` (returns the new effect), `load_setup` |
| [Set a Track to be the Primary Track](timeline.md#set-a-track-to-be-the-primary-track) | Tracks Operations | `PySequence.primary_track` |
| [Get the name of the Primary Track](timeline.md#get-the-name-of-the-primary-track) | Tracks Operations | `PySequence.primary_track` (a `PyAttribute`; `.get_value()`) |
| [Set a Track to be the Secondary Track](timeline.md#set-a-track-to-be-the-secondary-track) | Tracks Operations | `.versions`, `.tracks`, `.secondary_track` |
| [Collapse a timeline video version](timeline.md#collapse-a-timeline-video-version) | Tracks Operations | `PyVersion.expanded` |
| [Lock a track](timeline.md#lock-a-track) | Tracks Operations | `.version`, `.locked` |
| [Hide a track](timeline.md#hide-a-track) | Tracks Operations | `.version`, `.hidden` |
| [Disable the stereo Link on a stereo video track](timeline.md#disable-the-stereo-link-on-a-stereo-video-track) | Tracks Operations | `PyTrack.stereo_linked` |
| [Disable the stereo Link on a stereo audio track](timeline.md#disable-the-stereo-link-on-a-stereo-audio-track) | Tracks Operations | `PyAudioTrack.channels`, `stereo_linked` |
| [Print the name of all the segments located on a track](timeline.md#print-the-name-of-all-the-segments-located-on-a-track) | Tracks Operations | `.tracks`, `.name` |
| [Collapse an audio track](timeline.md#collapse-an-audio-track) | Tracks Operations | `PySequence.audio_tracks`, `PyAudioTrack.expanded` |
| [Get the name of the Sequence hosting a Marker, through a Python Hook](timeline.md#get-the-name-of-the-sequence-hosting-a-marker-through-a-python-hook) | Using the `parent` Property | `PyMarker.parent`. Intended as a custom-action hook callback receiving `selection` |
| [Put a Segment Marker in the middle of a segment in a custom action](timeline.md#put-a-segment-marker-in-the-middle-of-a-segment-in-a-custom-action) | Using the `parent` Property | `PyMarker.parent` (the segment), `PySegment.record_in`, `record_duration`, `PyMarker.location` |

### [batch.md](batch.md)

| Example | Section | APIs used |
|---|---|---|
| [Specify a shader from the default path when creating a Matchbox](batch.md#specify-a-shader-from-the-default-path-when-creating-a-matchbox) | Working with Nodes in Batch | `PyBatch.create_node(type, file)` |
| [Specify a handler from the default path when creating a Pybox](batch.md#specify-a-handler-from-the-default-path-when-creating-a-pybox) | Working with Nodes in Batch | `flame.batch.create_node()` |
| [Print the name of the current Matchbox shader](batch.md#print-the-name-of-the-current-matchbox-shader) | Working with Nodes in Batch | `PyBatch.get_node(name)`, Matchbox `shader_name` |
| [Create an OpenFX node and load a plugin in it](batch.md#create-an-openfx-node-and-load-a-plugin-in-it) | Working with Nodes in Batch | `PyOFXNode.change_plugin(name)` |
| [Print the name of the current OpenFX plugin](batch.md#print-the-name-of-the-current-openfx-plugin) | Working with Nodes in Batch | `PyOFXNode.plugin_name` |
| [Bypass a node](batch.md#bypass-a-node) | Working with Nodes in Batch | `PyBatch.current_node`, `PyNode.bypass` |
| [Set the Before setting of a MUX Range](batch.md#set-the-before-setting-of-a-mux-range) | Working with Nodes in Batch | `flame.batch.current_node.get_value()`, `.before_range` |
| [Set the After setting of a MUX Range](batch.md#set-the-after-setting-of-a-mux-range) | Working with Nodes in Batch | `flame.batch.current_node.get_value()`, `.after_range` |
| [Freeze the current frame in a MUX node](batch.md#freeze-the-current-frame-in-a-mux-node) | Working with Nodes in Batch | `PyBatch.current_frame`; MUX `range_active`, `range_start`, `range_end`, `before_range`, `after_range` |
| [Set the Compass colour](batch.md#set-the-compass-colour) | Using a Compass in Action | `PyActionNode.create_node("Compass")`, `PyCompassNode.colour` |
| [Set the Compass name](batch.md#set-the-compass-name) | Using a Compass in Action | `.create_node()`, `.name` |
| [Set the Compass width](batch.md#set-the-compass-width) | Using a Compass in Action | `.create_node()`, `.width` |
| [Set the Compass height](batch.md#set-the-compass-height) | Using a Compass in Action | `.create_node()`, `.height` |
| [Create a Compass around nodes](batch.md#create-a-compass-around-nodes) | Using a Compass in Action | `PyActionNode.encompass_nodes(list)` — list items can be node names or node objects |
| [Get a list of nodes inside a Compass](batch.md#get-a-list-of-nodes-inside-a-compass) | Using a Compass in Action | `encompass_nodes` returns the compass; `PyCompassNode.nodes` |
| [Move Action Media nodes](batch.md#move-action-media-nodes) | Looping by Node Type | `flame.batch.nodes`, `.type`, `.pos_y` |
| [Set all Comp nodes to Add blend mode](batch.md#set-all-comp-nodes-to-add-blend-mode) | Looping by Node Type | `flame.batch.nodes`, `PyNode.type`, Comp `flame_blend_mode` |
| [Render Passes with the Python API](batch.md#render-passes-with-the-python-api) | Render Passes with the Python API | `create_batch_group`, `go_to`, `import_clip`, `create_node`, `connect_nodes`, `organize`; Comp `flame_blend_mode`; clip output socket `"BGR"` |
| [Importing Multi-Channel Clip](batch.md#importing-multi-channel-clip) | Importing Multi-Channel Clip | `import_clip`, `create_node("Action")`, `PyActionNode.add_media()`, `connect_nodes`, `organize` |

### [media-panel-and-ui.md](media-panel-and-ui.md)

| Example | Section | APIs used |
|---|---|---|
| [Switch the top view to Desktop Reels without changing the visible item](media-panel-and-ui.md#switch-the-top-view-to-desktop-reels-without-changing-the-visible-item) | Switching Views | `.set_desktop_reels()` |
| [Set a PyBatch as the visible item in the Desktop Reels view](media-panel-and-ui.md#set-a-pybatch-as-the-visible-item-in-the-desktop-reels-view) | Switching Views | `.set_desktop_reels()` |
| [Switch the top view to Freeform without changing the visible item](media-panel-and-ui.md#switch-the-top-view-to-freeform-without-changing-the-visible-item) | Switching Views | `PyWorkspace.set_freeform()` |
| [Set an item as the visible item in the Freeform view](media-panel-and-ui.md#set-an-item-as-the-visible-item-in-the-freeform-view) | Switching Views | `.set_freeform()` |
| [Create a new Reel named "MyReel" in a Batch group](media-panel-and-ui.md#create-a-new-reel-named-myreel-in-a-batch-group) | Media Panel Operations | `PyDesktop.batch_groups`, `PyBatch.create_reel(name)` |
| [Create a new Shelf Reel named "MyShelfReel"](media-panel-and-ui.md#create-a-new-shelf-reel-named-myshelfreel) | Media Panel Operations | `PyBatch.create_shelf_reel(name)` |
| [Create a Batch Iteration in a Batch Group](media-panel-and-ui.md#create-a-batch-iteration-in-a-batch-group) | Media Panel Operations | `PyBatch.iterate()` |
| [Create Batch Iteration 5 in a Batch Group](media-panel-and-ui.md#create-batch-iteration-5-in-a-batch-group) | Media Panel Operations | `PyBatch.iterate(index)` |
| [Save a Batch Group from the Desktop to a Library](media-panel-and-ui.md#save-a-batch-group-from-the-desktop-to-a-library) | Media Panel Operations | `PyDesktop.destination` (target library), `PyBatch.save()` |
| [Save the current Batch Iteration from the Desktop to a Library](media-panel-and-ui.md#save-the-current-batch-iteration-from-the-desktop-to-a-library) | Media Panel Operations | `PyDesktop.destination`, `PyBatch.save_current_iteration()` |
| [Print the name of the Batch Groups in a Library](media-panel-and-ui.md#print-the-name-of-the-batch-groups-in-a-library) | Media Panel Operations | `.batch_groups`, `.name` |
| [Print the name of the Batch Groups in a Folder](media-panel-and-ui.md#print-the-name-of-the-batch-groups-in-a-folder) | Media Panel Operations | `.batch_groups`, `.name` |
| [Open a Batch Group located inside a Folder in the Desktop](media-panel-and-ui.md#open-a-batch-group-located-inside-a-folder-in-the-desktop) | Media Panel Operations | `open_as_batch_group()` |
| [Open a Batch Iteration located inside a Library in the Desktop](media-panel-and-ui.md#open-a-batch-iteration-located-inside-a-library-in-the-desktop) | Media Panel Operations | `.batch_iterations`, `.open_as_batch_group()` |
| [Overwrite a clip in the current Sequence](media-panel-and-ui.md#overwrite-a-clip-in-the-current-sequence) | Media Panel Operations | `flame.execute_shortcut(name)` — triggers a keyboard-shortcut action by name |
| [Select the Desktop in the Workspace](media-panel-and-ui.md#select-the-desktop-in-the-workspace) | Media Panel Operations | `PyWorkspace.desktop`, `PyDesktop.selected` |
| [Move all clips from a Library Folder to a Desktop Reel](media-panel-and-ui.md#move-all-clips-from-a-library-folder-to-a-desktop-reel) | Media Panel Operations | `flame.media_panel.move(entries, destination)` |
| [Copy all clips from a Library Folder to a Desktop Reel](media-panel-and-ui.md#copy-all-clips-from-a-library-folder-to-a-desktop-reel) | Media Panel Operations | `flame.media_panel.copy(entries, destination)` |
| [Select multiple entries at once](media-panel-and-ui.md#select-multiple-entries-at-once) | Media Panel Operations | `flame.media_panel.selected_entries` (settable with a list) |
| [Print the list of selected entries in the Media Panel](media-panel-and-ui.md#print-the-list-of-selected-entries-in-the-media-panel) | Media Panel Operations | `flame.media_panel.selected_entries` |
| [Hide the Media Panel](media-panel-and-ui.md#hide-the-media-panel) | Media Panel Operations | `flame.media_panel.visible` |
| [Set the Media Panel to Full Width](media-panel-and-ui.md#set-the-media-panel-to-full-width) | Media Panel Operations | `flame.media_panel.full_width` |
| [Set the Media Panel to Full Height](media-panel-and-ui.md#set-the-media-panel-to-full-height) | Media Panel Operations | `flame.media_panel.full_height` |
| [Set the Media Panel to Dual mode](media-panel-and-ui.md#set-the-media-panel-to-dual-mode) | Media Panel Operations | `flame.media_panel.dual` |
| [Store the name of the current user](media-panel-and-ui.md#store-the-name-of-the-current-user) | Working with Users | `flame.users.current_user` (`PyUser`) |
| [Print the nickname of the current user](media-panel-and-ui.md#print-the-nickname-of-the-current-user) | Working with Users | `flame.users.current_user.nickname` |
| [Print the tab currently selected in the software](media-panel-and-ui.md#print-the-tab-currently-selected-in-the-software) | Working with Tabs | `flame.get_current_tab()` |
| [Go to the Timeline Tab](media-panel-and-ui.md#go-to-the-timeline-tab) | Working with Tabs | `flame.set_current_tab(name)` |

### [../guides/getting-started.md](../guides/getting-started.md)

| Example | Section | APIs used |
|---|---|---|
| [Write your first script (5 progressive blocks; complete script in Step 5)](../guides/getting-started.md#write-your-first-script-walkthrough) | Write Your First Python API Script | `flame.batch.create_batch_group(name, start_frame, duration, reels, shelf_reels)`, `flame.batch.go_to()`, `flame.batch.create_node("Comp")` / `("Write File")`, `flame.batch.connect_nodes()`, `flame.batch.organize()` |
| [Catching exceptions](../guides/getting-started.md#catching-exceptions) | Python API Examples | `from flame import batch`, `batch.import_clip()`, `try` / `except Exception` |

### [../guides/colour-management.md](../guides/colour-management.md)

| Example | Section | APIs used |
|---|---|---|
| [Get/set colour space in Batch](../guides/colour-management.md#in-batch) | Getting and Setting the Colour Space | `PyNode.colour_space`, Colour Source `colour_space`, Colour Mgmt `mode = "Tag Only"`, `tagged_colour_space` |
| [Get/set colour space on the Timeline](../guides/colour-management.md#on-the-timeline) | Getting and Setting the Colour Space | `flame.find_by_name()`, `PySequence.get_colour_space(PyTime)`, `PySegment.create_effect("Source Colour Mgmt")` |
| [Colour space in Action](../guides/colour-management.md#in-action) | Getting and Setting the Colour Space | `PyProject.action_colour_space`, `PyActionNode.create_node(node_type="IBL", file_path, input_colour_space)`, `PyActionNode.import_fbx(file_path, input_colour_space)` |
| [Colour space in MediaHub](../guides/colour-management.md#in-mediahub) | Getting and Setting the Colour Space | `flame.mediahub.files.options.set_tagged_colour_space()` |
| [Convert in Batch (Input / View / Colour Transform)](../guides/colour-management.md#in-batch-1) | Converting the Colour Space | Colour Mgmt `mode`, `tagged_colour_space`, `working_space`, `bit_depth`, `display`, `view`, `invert`, `import_transform()` |
| [Convert on the Timeline](../guides/colour-management.md#on-the-timeline-1) | Converting the Colour Space | `PySequence.create_effect("Source Colour Mgmt")`, `PySegment.create_effect("Colour Mgmt")`, same attributes (no `bit_depth`) |
| [Context variables in Project Preferences](../guides/colour-management.md#in-project-preferences) | Using Context Variables | `PyProject.get_context_variables()`, `set_context_variable()`, `reset_context_variables()` |
| [Context variables in Batch](../guides/colour-management.md#in-batch-2) | Using Context Variables | `PyBatch.get_node()`, Colour Mgmt `get_context_variables()`, `context_variables_from_project`, `set_context_variable()`, `reset_context_variables()` |
| [Context variables on the Timeline](../guides/colour-management.md#on-the-timeline-2) | Using Context Variables | `flame.timeline.current_segment`, `PySegment.effects`, `PyTimelineFX.type`, Colour Mgmt TL FX context-variable methods |
| [Reload / export an OCIO config](../guides/colour-management.md#reloading-or-exporting-an-ocio-config) | Reloading or Exporting an OCIO Config | `PyProject.reload_ocio_config()`, `PyProject.export_ocio_config()` |
| [Modify project colour preferences](../guides/colour-management.md#modifying-project-preferences) | Modifying Project Preferences | `PyProject.working_colour_space`, `PyProject.action_colour_space` |
| [Use the OCIO Python binding](../guides/colour-management.md#using-the-ocio-python-binding) | Using the OCIO Python Binding | `PyProject.setups_folder`, `PyOpenColorIO` (`Config.CreateFromFile`, `getColorSpace`, `getViews`, `ColorSpaceTransform`, `getProcessor`) |

### [../guides/whats-new-2027.md](../guides/whats-new-2027.md)

| Example group | # samples | APIs used |
|---|---|---|
| [Global functions](../guides/whats-new-2027.md#global-functions-flame-module) | 2 | `flame.clear_unreferenced_cache()`, `all_projects=True` |
| [PyActionFamilyNode](../guides/whats-new-2027.md#pyactionfamilynode) | 2 | `PyActionFamilyNode.get_metadata([socket])` |
| [PyBatch](../guides/whats-new-2027.md#pybatch) | 1 | `flame.batch.create_node("Metadata")` |
| [PyClip](../guides/whats-new-2027.md#pyclip) | 2 | `flame.import_clips()`, `PyDesktop.create_reel_group()`, `PyReelGroup.create_reel()`, `PyClip.update_sources()`, `PyClip.SELECT_LATEST_VERSION` / `SELECT_CURRENT_VERSION` |
| [PyClipNode](../guides/whats-new-2027.md#pyclipnode) | 14 | `get_metadata`, `set_metadata_key`, `set_metadata_value`, `set_metadata_discarded` (incl. multi-channel socket `"albedo"`) |
| [PyMarker](../guides/whats-new-2027.md#pymarker) | 2 | `flame.timeline.clip.markers`, `PyMarker.has_annotations`, `clear_annotations()` |
| [PyMetadataNode](../guides/whats-new-2027.md#pymetadatanode) | 13 | metadata get/set/discard, `load_node_setup(path, edited_keys, discarded_keys, added_keys, replaced_keys)` |
| [PyMetadataTimelineFX](../guides/whats-new-2027.md#pymetadatatimelinefx) | 13 | metadata get/set/discard (no socket), `load_setup(path, edited_keys, discarded_keys, added_keys)` |
| [PyNode](../guides/whats-new-2027.md#pynode) | 3 | `PyNode.get_metadata()`, `output_channel_as_metadata_key(channel, bool)` |
| [PyRenderNode](../guides/whats-new-2027.md#pyrendernode) | 12 | metadata get/set/discard with channel-name sockets |
| [PySegment](../guides/whats-new-2027.md#pysegment) | 2 | `create_effect("Source Metadata")`, `create_unlinked_segment(timewarp_speed=50.0)` |
| [PyTimelineFX](../guides/whats-new-2027.md#pytimelinefx) | 2 | `PyTimelineFX.output_channel_as_metadata_key()` |
| [PyWriteFileNode](../guides/whats-new-2027.md#pywritefilenode) | 12 | metadata get/set/discard with channel-name sockets |

## Sample counts

| Source page | Code samples |
|---|---|
| Flame Python API Code Samples | 122 (56 multi-line blocks + 66 one-liners) |
| Python API (What's New in 2027) | 80 |
| Colour Management API | 12 |
| Write Your First Python API Script | 5 |
| Looping by Node Type | 2 |
| Render Passes with the Python API | 1 |
| Importing Multi-Channel Clip | 1 |
| Python API Examples (Catching Exceptions) | 1 |
| **Total** | **224** |

## Source issues found in samples (summary)

Details are next to each sample. Kept verbatim; do not copy these patterns:
- `def action_1(selection): import flame for marker in selection:` — three lines collapsed into one in the official HTML ([timeline.md](timeline.md#using-the-parent-property)).
- `mux = flame.batch.current_node.get_value() mux.bypass = True` — two statements on one line ([batch.md](batch.md#bypass-a-node)).
- `if effect.type == "Image"` missing `:` (twice) ([timeline.md](timeline.md#bypass-all-image-timeline-fxs-in-a-sequence)).
- `seq.versions[0].tracks.[0]` (twice) — invalid syntax.
- `<PySequence>.version[0]` — attribute is `versions`; and "Lock/Hide a track" samples set `locked`/`hidden` on a version, while these are `PyTrack` attributes in the class reference.
- `for marker in <PyClip>:` / `for marker in <PyTrack>.segments[0]:` / `for segments in <PyVersion>.tracks[0]:` — iterate the object instead of its `.markers` / `.segments` list.
- Marker "middle of segment" sample split across two lines so the `+ (...)` part is a discarded statement.
- `<PyDesktop>.set_desktop_reels(...)` — `set_desktop_reels` is a `PyWorkspace` method in the class reference.
- `encompass_nodes(...)` called without `action.`.
- Colour Management context-variables timeline sample uses a bare module-level `return`.
