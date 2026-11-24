<!-- source: Autodesk Flame Family 2027 Help _ Flame Python API Code Samples _ Autodesk.html -->
# Flame Python API Code Samples

This pages contains very simple `flame API` recipes. These basic examples should help you in discovering how to use the API automate tasks.

As for bracketed names such as <PyClip>, they are shorthand for objects created from the `flame API`. See Defines for the flame Module

---

## Clip Import

Import a clip into a library:

`flame.import_clips("/usr/tmp/clip.mov", PyLibrary)`

---

## Clip Reformat

Changing the resolution of a clip:

`<PyClip>.reformat( width = 1920, height = 1080, ratio = 1.778)`

---

## Rendering a Clip

Render all the Timeline FX in a clip in proxy resolution using Burn:

`<PyClip>.render(render_mode ="All", render_option = "Burn", render_quality = "Proxy Resolution")`

Render all the Batch FX on a clip:

`<PyClip>.render(effect_type = "Batch FX")`

Get a the render state of a clip:

`print(<PyClip>.is_rendered())`

---

## Switching Views

Switch the top view to Desktop Reels without changing the visible item:

`<PyDesktop>.set_desktop_reels()`

Set a PyBatch as the visible item in the Desktop Reels view:

`<PyDesktop>.set_desktop_reels(<PyBatch>)`

Switch the top view to Freeform without changing the visible item:

`<PyWorkspace>.set_freeform()`

Set a PyBatch as the visible item in the Freeform view:

`<PyWorkspace>.set_freeform(<PyLibrary>)`

---

## Select Segments on the Timeline

Select all segments on the bottom video track of a clip:

`python
for seg in <PyVersion>.tracks[0].segments:
   seg.selected = True
`

Select all segments that are unrendered on a track:

`python
for seg in <PyVersion>.tracks[0].segments:
   if seg.is_rendered() == False:
      seg.selected = True
`

Change the comment of all selected markers on a timeline segment:

`python
for markers in <PySegment>.selected_markers:
   markers.comment = "Need MasterGrade Work"
`

---

## Working with Markers

Print the name of all the markers located on a clip:

`python
for markers in <PyClip>.markers:
   print(markers.name)
`

Create a marker on the 10th frame of a clip:

`<PyClip>.create_marker(10)`

Select all markers of a clip:

`python
for marker in <PyClip>:
   marker.selected = True
`

Select all markers of a segment:

`python
for marker in <PyTrack>.segments[0]:
   marker.selected = True
`

Change the location of a marker on a clip:

`python
marker = <PyClip>.markers[0]
marker.location = 20
`

Move a marker to the middle of a timeline segment:

`python
marker.location = <PySegment>.record_in
+ (<PySegment>.record_duration.frame / 2 )
`

Change the name of a marker located on a timeline segment to the name of that timeline segment:

`python
tlname = <PySegment>.name
marker = <PySegment>.markers[0]
marker.name = tlname
`

Change the name of a comment located on a clip using tokens:

`python
marker = <PyClip>.markers[0]
marker.comment = "<user>_<date>"
`

---

## Using PyTime

Set a PyTime in timecode:

`tc = flame.PyTime("10:00:01:05", "23.976 fps")`

Set a PyTime in relative frame:

`frm = flame.PyTime(10)`

Set a PyTime in absolute frame:

`frm = flame.PyTime(864000, "23.976 fps")`

Get the current time of a clip in frame:

`print(<PyClip>.current_time.frame)`

Get the current time of a clip in relative frame:

`print(<PyClip>.current_time.relative_frame)`

Get the current time of a clip in timecode:

`print(<PyClip>.current_time.timecode)`

---

## Clip Operations

Print a list of clips located in a reel:

`print(<PyReel>.clips)`

Store a clip in a define:

`clip = <PyReel>.clips[0]`

Set an in mark on a clip based on relative frame:

`<PyClip>.in_mark = 20`

Set an in mark on a clip based on a PyTime timecode:

`python
tc = flame.PyTime("10:00:00:20", "23.976 fps")
<PyClip>.in_mark = tc
`

Get the in mark value in frame:

`print(<PyClip>.in_mark.get_value().frame)`

Set an out mark on a clip based on relative frame:

`<PyClip>.out_mark = 30`

Set an out mark on a clip based on a PyTime timecode:

`python
tc = flame.PyTime("10:00:01:05", "23.976 fps")
<PyClip>.out_mark = tc
`

Get the out mark value in frame:

`print(<PyClip>.out_mark.get_value().frame)`

Get the duration of a clip between in and out marks in frame:

`print(<PyClip>.duration.frame)`

Set the current time on a clip based on a timecode value:

`<PyClip>.current_time = "10:00:00:20"`

Set the current time on a clip based on an absolute frame using PyTime:

`python
frm = flame.PyTime(864000, "23.976 fps")
<PyClip>.current_time = frm
`

Get the current time of a clip in frame:

`print(<PyClip>.current_time.frame)`

---

## Segment Operations

Get the name of a timeline segment:

`print(<PyTrack>.segments[0].name)`

Get the name of all segments in a timeline:

`python
for version in flame.timeline.clip.versions:
    for track in version.tracks:
        for segment in track.segments:
            print(segment.name)
`

Get the name of all selected segments in a timeline:

`python
for version in flame.timeline.clip.versions:
    for track in version.tracks:
        for segment in track.selected_segments.get_value():
            print(segment.name)
`

Get the name of the currently selected timeline segment:

`print(flame.timeline.current_segment.name)`

Set the shot name of a timeline segment:

`<PySegment>.shot_name = "sh010"`

Set the comment of a timeline segment:

`<PySegment>.comment = "sh010"`

Get the source file path of a timeline segment:

`print(<PySegment>.file_path)`

Add a Blur Timeline FX to a timeline segment:

`<PySegment>.create_effect("Blur")`

Add a Blur Timeline FX after an existing Image TL FX:

`<PySegment>.create_effect("Blur", "Image")`

Print the TL FX that can be added on a timeline segment:

`print(<PySegment>.effect_types)`

Print the existing PyTimelineFX of a timeline segment:

`print(<PySegment>.effects)`

Store a Timeline FX in a define:

`blur = <PySegment>.effects[0]`

Bypass all Image Timeline FXs in a sequence:

`python
for segments in <PyTrack>.segments:
   for effect in segments.effects:
      if effect.type == "Image"
         effect.bypass = True
`

Get the hidden information of a timeline segment:

`print(<PyTrack>.segments[0].hidden)`

Hide a timeline segment:

`<PyTrack>.segments[0].hidden = True`

Get the colour information of a timeline segment:

`print(<PyTrack>.segments[0].colour)`

Set the colour of a timeline segment to blue:

`python
tl_seg = <PyTrack>.segments[0]
tl_seg.colour = (0.0, 0.0, 1.0)
`

Get the source name of a timeline segment:

`print(<PyTrack>.segments[0].source_name)`

Get the source media time in of a timeline segment:

`print(<PyTrack>.segments[0].source_in)`

Get the source media time out of a timeline segment:

`print(<PyTrack>.segments[0].source_out)`

Get the source media duration of a timeline segment:

`print(<PyTrack>.segments[0].source_duration)`

Get the tape name of a timeline segment:

`print(<PyTrack>.segments[0].tape_name)`

Get the in time of a timeline segment:

`print(<PyTrack>.segments[0].record_in)`

Get the out time of a timeline segment:

`print(<PyTrack>.segments[0].record_out)`

Get the duration of a timeline segment:

`print(<PyTrack>.segments[0].record_duration)`

---

## Timeline FX

Bypass a Timeline FX on a timeline segment:

`<PyTimelineFX>.bypass = True`

Get the Bypass status of a Timeline FX:

`print(<PyTimelineFX>.bypass)`

Print the names of all TL FX existing on a timeline segment:

`python
for tlfx in <PySegment>.effects:
   print(tlfx.type)
`

Bypass all Image Timeline FXs in a sequence:

`python
for segments in <PyTrack>.segments:
   for effect in segments.effects:
      if effect.type == "Image"
         effect.bypass = True
`

Save a Timeline FX setup using the .effects list index:

`<PySegment>.effects[#].save_setup("/usr/tmp/my_timelinefx_setup")`

Save a setup for a particular Timeline FX:

`python
for tlfx in <PySegment>.effects:
  if tlfx.type == "Blur":
        tlfx.save_setup("/usr/tmp/my_timelinefx_setup")
`

Load a Timeline FX setup on a timeline segment:

`python
<PySegment>.create_effect("Blur")
for tlfx in <PySegment>.effects:
    if tlfx.type == "Blur":
        tlfx.load_setup("/usr/tmp/my_timelinefx_setup")
`

Load a setup Timeline FX setup on all selected timeline segments:

`python
for version in flame.timeline.clip.versions:
    for track in version.tracks:
        for segment in track.selected_segments.get_value():
            openfx = segment.create_effect("OpenFX")
            openfx.load_setup("/usr/tmp/my_openfx_setup")
`

---

## Tracks Operations

Set a Track to be the Primary Track:

`python
seq = <PySequence>
track = seq.versions[0].tracks.[0]
seq.primary_track = track
`

Get the name of the Primary Track:

`python
seq = <PySequence>
print(seq.primary_track.get_value().name)
`

Set a Track to be the Secondary Track:

`python
seq = <PySequence>
track = seq.versions[0].tracks.[0]
seq.secondary_track = track
`

Collapse a timeline video version:

`python
version = <PySequence>.version[0]
version.expanded = False
`

Lock a track:

`python
version = <PySequence>.version[0]
version.locked = True
`

Hide a track:

`python
version = <PySequence>.version[0]
version.hidden = True
`

Disable the stereo Link on a stereo video track:

`python
track = <PyVersion>.tracks[0]
track.stereo_linked = False
`

Disable the stereo Link on a stereo audio track:

`python
atrack = <PyAudioTrack>.channels[0]
atrack.stereo_linked = False
`

Print the name of all the segments located on a track:

`python
for segments in <PyVersion>.tracks[0]:
   print(segments.name )
`

Collapse an audio track:

`python
atrack = <PySequence>.audio_tracks[0]
atrack.expanded = False
`

---

## Media Panel Operations

Create a new Reel named "MyReel":

`python
batch = <PyDesktop>.batch_groups[0]
batch.create_reel("MyReel")
`

Create a new Reel named "MyShelfReel":

`python
batch = <PyDesktop>.batch_groups[0]
batch.create_shelf_reel("MyShelfReel")
`

Create a Batch Iteration in a Batch Group:

`python
batch = <PyDesktop>.batch_groups[0]
batch.iterate()
`

Create Batch Iteration 5 in a Batch Group:

`python
batch = <PyDesktop>.batch_groups[0]
batch.iterate(5)
`

Save a Batch Group from the Desktop to a Library:

`python
desk = <PyDesktop>
batch = <PyDesktop>.batch_groups[0]
lib = <PyLibrary>
desk.destination = lib
batch.save()
`

Save the current Batch Iteration from the Desktop to a Library:

`python
desk = <PyDesktop>
batch = <PyDesktop>.batch_groups[0]
lib = <PyLibrary>
desk.destination = lib
batch.save_current_iteration()
`

Print the name of the Batch Groups in a Library:

`python
for batch in <PyLibrary>.batch_groups:
   print(batch.name)
`

Print the name of the Batch Groups in a Folder:

`python
for batch in <PyFolder>.batch_groups:
   print(batch.name)
`

Open a Batch Group located inside a Folder in the Desktop:

`<PyFolder>.batch_groups[0].open_as_batch_group()`

Open a Batch Iteration located inside a Library in the Desktop:

`<PyLibrary>.batch_iterations[0].open_as_batch_group()`

Overwrite a clip in the current Sequence:

`flame.execute_shortcut("Overwrite Edit")`

Select the Desktop in the Workspace:

`python
desk = <pyWorkspace>.desktop
desk.selected = True
`

Move all clips from a Library Folder to a Desktop Reel:

`python
clip = <PyLibrary>.folders[0].clips
reel = <PyDesktop>.reel_groups[0].reels[0]
flame.media_panel.move(clip, reel)
`

Copy all clips from a Library Folder to a Desktop Reel:

`python
clip = <PyLibrary>.folders[0].clips
reel = <PyDesktop>.reel_groups[0].reels[0]
flame.media_panel.copy(clip, reel)
`

Select multiple entries at once:

`flame.media_panel.selected_entries = <PyReel>.clips`

Print the list of selected entries in the Media Panel:

`print(flame.media_panel.selected_entries)`

Hide the Media Panel:

`flame.media_panel.visible = False`

Set the Media Panel to Full Width:

`flame.media_panel.full_width = True`

Set the Media Panel to Full Height:

`flame.media_panel.full_height = True`

Set the Media Panel to Dual mode:

`flame.media_panel.dual = True`

---

## Using the `parent` Property

Get the name of the Sequence hosting the Marker located, through a Python Hook:

`python
def action_1(selection): import flame for marker in selection:
    print(marker.parent.name )
`

Put a Segment Marker in the middle of a segment in a custom action:

`python
def action_1(selection): import flame for marker in selection:
    parent = marker.parent
    marker.location = parent.record_in + (parent.record_duration.frame / 2 )
`

---

## Using a Compass in Action

Set the Compass colour:

`python
compass = action.create_node("Compass")
compass.colour = (50, 50, 50)
`

Set the Compass name:

`python
compass = action.create_node("Compass")
compass.name = "MyCompass"
`

Set the Compass width:

`python
compass = action.create_node("Compass")
compass.width = 250
`

Set the Compass height:

`python
compass = action.create_node("Compass")
compass.height = 250
`

Create a Compass around nodes:

`action.encompass_nodes(["NodeName1", node3, "NodeName2"])`

Get a list of nodes inside a Compass:

`python
compass = encompass_nodes( ["NodeName1", node3, "NodeName2"] )
print(compass.nodes)
`

---

## Working with Nodes in Batch

Specify a shader from the default path when creating a Matchbox:

`flame.batch.create_node("Matchbox","Blur.mx")`

Specify a handler from the default path when creating a Pybox:

`flame.batch.create_node("Pybox","sendmail.py")`

Print the name of the current Matchbox shader:

`python
mx = flame.batch.get_node("Matchbox100")
print(mx.shader_name)
`

Create an OpenFX node and load a plugin in it:

`python
ofx = flame.batch.create_node("OpenFX")
ofx.change_plugin("S_Distort")
`

Print the name of the current OpenFX plugin:

`python
ofx = flame.batch.get_node("OpenFX100")
print(ofx.plugin_name)
`

Bypass a node:

`mux = flame.batch.current_node.get_value() mux.bypass = True`

Set the Before setting of a MUX Range:

`python
mux = flame.batch.current_node.get_value()
mux.before_range = "Repeat First"
`

Set the After setting of a MUX Range:

`python
mux = flame.batch.current_node.get_value()
mux.after_range = "Repeat Last"
`

Freeze the current frame in a MUX node:

`python
frame = flame.batch.current_frame
mux = flame.batch.current_node.get_value()
mux.range_active = True
mux.range_start = frame
mux.range_end = frame
mux.before_range = "Repeat First"
mux.after_range = "Repeat Last"
`

---

## Working with Users

Store the name of the current user:

`user = flame.users.current_user.name`

Print the nickname of the current user:

`print(flame.users.current_user.nickname)`

---

## Working with Tabs

Print the tab currently selected in the software:

`print(flame.get_current_tab())`

Go to the Timeline Tab

`flame.set_current_tab("Timeline")`

## Related pages

- Python API Examples
