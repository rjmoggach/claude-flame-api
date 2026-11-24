> Source: Flame Python API Code Samples (sections: Select Segments on the Timeline, Working with Markers, Segment Operations, Timeline FX, Tracks Operations, Using the `parent` Property) — Autodesk Flame Family 2027 Help

# Examples — Timeline: Segments, Markers, Timeline FX, Tracks

Notation: `<PyClip>`, `<PySequence>`, `<PyVersion>`, `<PyTrack>`, `<PySegment>`, `<PyTimelineFX>`, `<PyAudioTrack>` are placeholders (see [../guides/constants.md](../guides/constants.md)). Code is verbatim from the source, **including several source bugs** flagged in "Source issue" notes; a corrected form is given only where the intent is unambiguous, and is labelled as such.

Class references: [PySequence](../api/classes/PySequence.md), [PyVersion](../api/classes/PyVersion.md), [PyTrack](../api/classes/PyTrack.md), [PySegment](../api/classes/PySegment.md), [PyMarker](../api/classes/PyMarker.md), [PyTimelineFX](../api/classes/PyTimelineFX.md), [PyAudioTrack](../api/classes/PyAudioTrack.md), [PyTimeline](../api/classes/PyTimeline.md).

Hierarchy used throughout (from the samples): `PySequence.versions[#]` → `PyVersion.tracks[#]` → `PyTrack.segments[#]` → `PySegment.effects[#]` / `PySegment.markers[#]`. The open timeline is `flame.timeline.clip`; the selected segment is `flame.timeline.current_segment`.

## Select Segments on the Timeline

### Select all segments on the bottom video track of a clip
API: `PyVersion.tracks`, `PyTrack.segments`, `PySegment.selected`.

```python
for seg in <PyVersion>.tracks[0].segments:
   seg.selected = True
```

### Select all segments that are unrendered on a track
API: `PySegment.is_rendered()`, `PySegment.selected`.

```python
for seg in <PyVersion>.tracks[0].segments:
   if seg.is_rendered() == False:
      seg.selected = True
```

### Change the comment of all selected markers on a timeline segment
API: `PySegment.selected_markers`, `PyMarker.comment`.

```python
for markers in <PySegment>.selected_markers:
   markers.comment = "Need MasterGrade Work"
```

## Working with Markers

### Print the name of all the markers located on a clip
API: `PyClip.markers`, `PyMarker.name`.

```python
for markers in <PyClip>.markers:
   print(markers.name)
```

### Create a marker on the 10th frame of a clip
API: `PyClip.create_marker(frame)`.

```python
<PyClip>.create_marker(10)
```

### Select all markers of a clip
API: `PyMarker.selected`.

```python
for marker in <PyClip>:
   marker.selected = True
```

> Source issue: iterates over `<PyClip>` itself; every other sample iterates `<PyClip>.markers`. Likely intended (unverified): `for marker in <PyClip>.markers:`.

### Select all markers of a segment
```python
for marker in <PyTrack>.segments[0]:
   marker.selected = True
```

> Source issue: iterates over a segment object; likely intended (unverified): `for marker in <PyTrack>.segments[0].markers:`.

### Change the location of a marker on a clip
API: `PyMarker.location`.

```python
marker = <PyClip>.markers[0]
marker.location = 20
```

### Move a marker to the middle of a timeline segment
API: `PySegment.record_in`, `PySegment.record_duration`, `PyMarker.location`.

```python
marker.location = <PySegment>.record_in
+ (<PySegment>.record_duration.frame / 2 )
```

> Source issue: the expression is split over two lines without parentheses or a backslash. As written, Python executes `marker.location = <PySegment>.record_in` and then evaluates `+ (...)` as a separate, discarded statement. Single-line form (matches the `parent` sample further below): `marker.location = <PySegment>.record_in + (<PySegment>.record_duration.frame / 2 )`.

### Rename a marker on a segment to the segment's name
API: `PySegment.name`, `PySegment.markers`, `PyMarker.name`.

```python
tlname = <PySegment>.name
marker = <PySegment>.markers[0]
marker.name = tlname
```

### Change the comment of a marker on a clip using tokens
API: `PyMarker.comment` (accepts tokens such as `<user>`, `<date>`).

```python
marker = <PyClip>.markers[0]
marker.comment = "<user>_<date>"
```

(2027 marker additions — `PyMarker.has_annotations`, `clear_annotations()`, node markers — are in [../guides/whats-new-2027.md](../guides/whats-new-2027.md#pymarker).)

## Segment Operations

### Get the name of a timeline segment
```python
print(<PyTrack>.segments[0].name)
```

### Get the name of all segments in a timeline
API: `flame.timeline.clip.versions`, `PyVersion.tracks`, `PyTrack.segments`.

```python
for version in flame.timeline.clip.versions:
    for track in version.tracks:
        for segment in track.segments:
            print(segment.name)
```

### Get the name of all selected segments in a timeline
API: `PyTrack.selected_segments` (a `PyAttribute`; `.get_value()` returns the list).

```python
for version in flame.timeline.clip.versions:
    for track in version.tracks:
        for segment in track.selected_segments.get_value():
            print(segment.name)
```

### Get the name of the currently selected timeline segment
API: `flame.timeline.current_segment`.

```python
print(flame.timeline.current_segment.name)
```

### Set the shot name of a timeline segment
```python
<PySegment>.shot_name = "sh010"
```

### Set the comment of a timeline segment
```python
<PySegment>.comment = "sh010"
```

### Get the source file path of a timeline segment
```python
print(<PySegment>.file_path)
```

### Add a Blur Timeline FX to a timeline segment
API: `PySegment.create_effect(type)`.

```python
<PySegment>.create_effect("Blur")
```

### Add a Blur Timeline FX after an existing Image TL FX
API: `PySegment.create_effect(type, after_type)`.

```python
<PySegment>.create_effect("Blur", "Image")
```

### Print the TL FX that can be added on a timeline segment
```python
print(<PySegment>.effect_types)
```

### Print the existing PyTimelineFX of a timeline segment
```python
print(<PySegment>.effects)
```

### Store a Timeline FX in a define
```python
blur = <PySegment>.effects[0]
```

### Bypass all Image Timeline FXs in a sequence
API: `PySegment.effects`, `PyTimelineFX.type`, `PyTimelineFX.bypass`.

```python
for segments in <PyTrack>.segments:
   for effect in segments.effects:
      if effect.type == "Image"
         effect.bypass = True
```

> Source issue: missing `:` after `if effect.type == "Image"` (SyntaxError as written). Same sample appears again under Timeline FX.

### Get the hidden information of a timeline segment
```python
print(<PyTrack>.segments[0].hidden)
```

### Hide a timeline segment
```python
<PyTrack>.segments[0].hidden = True
```

### Get the colour information of a timeline segment
```python
print(<PyTrack>.segments[0].colour)
```

### Set the colour of a timeline segment to blue
API: `PySegment.colour` (RGB float tuple).

```python
tl_seg = <PyTrack>.segments[0]
tl_seg.colour = (0.0, 0.0, 1.0)
```

### Get source information of a timeline segment
`source_name`, `source_in`, `source_out`, `source_duration`, `tape_name`:

```python
print(<PyTrack>.segments[0].source_name)
```

```python
print(<PyTrack>.segments[0].source_in)
```

```python
print(<PyTrack>.segments[0].source_out)
```

```python
print(<PyTrack>.segments[0].source_duration)
```

```python
print(<PyTrack>.segments[0].tape_name)
```

### Get record in / out / duration of a timeline segment
```python
print(<PyTrack>.segments[0].record_in)
```

```python
print(<PyTrack>.segments[0].record_out)
```

```python
print(<PyTrack>.segments[0].record_duration)
```

## Timeline FX

### Bypass a Timeline FX on a timeline segment
```python
<PyTimelineFX>.bypass = True
```

### Get the Bypass status of a Timeline FX
```python
print(<PyTimelineFX>.bypass)
```

### Print the names of all TL FX existing on a timeline segment
API: `PyTimelineFX.type`.

```python
for tlfx in <PySegment>.effects:
   print(tlfx.type)
```

### Bypass all Image Timeline FXs in a sequence (repeat of the sample above)
```python
for segments in <PyTrack>.segments:
   for effect in segments.effects:
      if effect.type == "Image"
         effect.bypass = True
```

> Source issue: missing `:` after the `if` condition.

### Save a Timeline FX setup using the .effects list index
API: `PyTimelineFX.save_setup(path)`. `#` is a placeholder for an index.

```python
<PySegment>.effects[#].save_setup("/usr/tmp/my_timelinefx_setup")
```

### Save a setup for a particular Timeline FX
```python
for tlfx in <PySegment>.effects:
  if tlfx.type == "Blur":
        tlfx.save_setup("/usr/tmp/my_timelinefx_setup")
```

### Load a Timeline FX setup on a timeline segment
API: `PySegment.create_effect`, `PyTimelineFX.load_setup(path)`.

```python
<PySegment>.create_effect("Blur")
for tlfx in <PySegment>.effects:
    if tlfx.type == "Blur":
        tlfx.load_setup("/usr/tmp/my_timelinefx_setup")
```

### Load a Timeline FX setup on all selected timeline segments
API: `PyTrack.selected_segments.get_value()`, `PySegment.create_effect("OpenFX")` (returns the new effect), `load_setup`.

```python
for version in flame.timeline.clip.versions:
    for track in version.tracks:
        for segment in track.selected_segments.get_value():
            openfx = segment.create_effect("OpenFX")
            openfx.load_setup("/usr/tmp/my_openfx_setup")
```

## Tracks Operations

### Set a Track to be the Primary Track
API: `PySequence.primary_track`.

```python
seq = <PySequence>
track = seq.versions[0].tracks.[0]
seq.primary_track = track
```

> Source issue: `tracks.[0]` is a SyntaxError; intended `tracks[0]`.

### Get the name of the Primary Track
API: `PySequence.primary_track` (a `PyAttribute`; `.get_value()`).

```python
seq = <PySequence>
print(seq.primary_track.get_value().name)
```

### Set a Track to be the Secondary Track
```python
seq = <PySequence>
track = seq.versions[0].tracks.[0]
seq.secondary_track = track
```

> Source issue: `tracks.[0]` → `tracks[0]`.

### Collapse a timeline video version
API: `PyVersion.expanded`.

```python
version = <PySequence>.version[0]
version.expanded = False
```

> Source issue: `<PySequence>.version[0]`; the attribute documented elsewhere (Defines page, class reference) is `versions`.

### Lock a track
```python
version = <PySequence>.version[0]
version.locked = True
```

### Hide a track
```python
version = <PySequence>.version[0]
version.hidden = True
```

> Source issue (both samples above): titled "track" but the code sets `locked` / `hidden` on a version object obtained via `<PySequence>.version[0]`. In the class reference, `locked` and `hidden` are attributes of [PyTrack](../api/classes/PyTrack.md) (and `hidden` of PySegment). For a track, likely intended (unverified): `track = <PySequence>.versions[0].tracks[0]` then `track.locked = True`.

### Disable the stereo Link on a stereo video track
API: `PyTrack.stereo_linked`.

```python
track = <PyVersion>.tracks[0]
track.stereo_linked = False
```

### Disable the stereo Link on a stereo audio track
API: `PyAudioTrack.channels`, `stereo_linked`.

```python
atrack = <PyAudioTrack>.channels[0]
atrack.stereo_linked = False
```

### Print the name of all the segments located on a track
```python
for segments in <PyVersion>.tracks[0]:
   print(segments.name )
```

> Source issue: iterates the track object directly; other samples use `<PyVersion>.tracks[0].segments`.

### Collapse an audio track
API: `PySequence.audio_tracks`, `PyAudioTrack.expanded`.

```python
atrack = <PySequence>.audio_tracks[0]
atrack.expanded = False
```

(2027: `PyAudioTrack.stereo_merge(right_channel)` — see [../guides/whats-new-2027.md](../guides/whats-new-2027.md#pyaudiotrack).)

## Using the `parent` Property

### Get the name of the Sequence hosting a Marker, through a Python Hook
API: `PyMarker.parent`. Intended as a custom-action hook callback receiving `selection`.

```python
def action_1(selection): import flame for marker in selection:
    print(marker.parent.name )
```

### Put a Segment Marker in the middle of a segment in a custom action
API: `PyMarker.parent` (the segment), `PySegment.record_in`, `record_duration`, `PyMarker.location`.

```python
def action_1(selection): import flame for marker in selection:
    parent = marker.parent
    marker.location = parent.record_in + (parent.record_duration.frame / 2 )
```

> Source issue (garbled in the official HTML itself): in both samples the first three lines were collapsed into one (`def action_1(selection): import flame for marker in selection:`), which is not valid Python. Line-restored form of the second sample (only line breaks/indentation added, labelled reconstruction):
>
> ```python
> def action_1(selection):
>     import flame
>     for marker in selection:
>         parent = marker.parent
>         marker.location = parent.record_in + (parent.record_duration.frame / 2 )
> ```
>
> The first sample restores the same way, with `print(marker.parent.name )` as the loop body. How `action_1` is registered as a custom action is not shown on this page (see the Python hooks documentation).
