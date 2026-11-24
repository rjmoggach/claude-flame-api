# class `flame.PyClip`(PyArchiveEntry)

Class derived from PyArchiveEntry. This class represents a Clip.

**Method resolution order:** PyClip → PyArchiveEntry → PyFlameObject

## Methods

> Cannot be instantiated from Python (obtained from other API objects).

### `cache_media`

```python
cache_media( (PyClip)arg1 [, (str)mode='current']) -> bool
```

Cache the Clip's linked media.

Keyword argument:

mode -- Determine the version to cache (currently selected or all versions). All Versions is only useful with to multi-version clips (Current, All Versions)

### `change_dominance`

```python
change_dominance( (PyClip)arg1, (str)scan_mode) -> None
```

Change the Clip's dominance. Changes only the clip's metadata.

Keyword argument:

scan_mode -- Field dominance. (P, F1, F2)

### `change_start_frame`

```python
change_start_frame( (PyClip)arg1, (int)start_frame [, (bool)use_segment_connections=True]) -> None
```

Modify the start frame of a source Clip.

Keywords argument:

start_frame -- New start frame of the clip.

use_segment_connections -- Sync the start frame of connected segments.

### `close_container`

```python
close_container( (PyClip)arg1) -> None
```

Close the container timeline if the Clip is inside a container.

### `create_marker`

```python
create_marker( (PyClip)arg1, (object)location) -> object
```

Add a Marker to the Clip.Keyword argument:

location -- The frame where the marker gets created.

### `cut`

```python
cut( (PyClip)arg1, (PyTime)cut_time) -> None
```

Cut all tracks of the Clip.

### `clear_cache_media`

```python
clear_cache_media( (PyClip)arg1 [, (str)mode='current']) -> bool
```

Clear the Clip's media cache.

Keyword argument:

mode -- Determine the version's cache to clear. (Current, All Versions, All But Current)

### `clear_renders`

```python
clear_renders( (PyClip)arg1) -> None
```

Clear the Clip's TimelineFX renders.

### `get_colour_space`

```python
get_colour_space( (PyClip)arg1 [, (PyTime)time=None]) -> str
```

Return the colour space at the requested time. Use current_time when no time is supplied.

### `is_rendered`

```python
is_rendered( (PyClip)arg1 [, (bool)top_only=False [, (str)render_quality='Full Resolution']]) -> bool
```

Return if a Clip is rendered.

The following attributes can be defined: top_only, render_quality.

### `open_as_sequence`

```python
open_as_sequence( (PyClip)arg1) -> object
```

Open the Clip as a Sequence. Mutates the PyClip object into a PySequence object.

### `open_container`

```python
open_container( (PyClip)arg1) -> bool
```

Open the container timeline if the Clip is inside a container.

### `reformat`

```python
reformat( (PyClip)arg1 [, (int)width=0 [, (int)height=0 [, (float)ratio=0.0 [, (int)bit_depth=0 [, (str)scan_mode='' [, (str)frame_rate='' [, (str)resize_mode='Letterbox']]]]]]]) -> None
```

Reformat the Clip to the specified format.

Keywords arguments:

width -- Integer between 24 and 16384.

height -- Integer between 24 and 16384.

ratio -- Frame aspect ratio. Float between 0.01 and 100.

bit_depth -- Bit depth. (8, 10, 12, 16 or 32)

scan_mode -- Scan mode of the sequence. (F1, F2, P)

frame_rate -- Frame rate. (60 fps, 59.54 NDF, 59.94 DF, 50 fps, 30 fps, 29.97 NDF, 29.97 DF, 25 fps, 24 fps, 23.976 fps)

resize_mode -- Resize mode. (Letterbox, Crop Edges, Fill, Centre)

### `render`

```python
render( (PyClip)arg1 [, (str)render_mode='All' [, (str)render_option='Foreground' [, (str)render_quality='Full Resolution' [, (str)effect_type='' [, (str)effect_caching_mode='Current' [, (bool)include_handles=False]]]]]]) -> bool
```

Trigger a render of the Clip

The following attributes can be defined: render_mode, render_option, render_quality, effect_type, effect_caching_mode and include_handles.

### `save`

```python
save( (PyClip)arg1) -> bool
```

Save the Clip to the defined save destination.

### `update-sources`

```python
update-sources( (PyClip)version_selection_mode) -> VersionSelectionMode
```

Update the sources of the Clip.

Keywords arguments:

version_selection_mode -- Specify which version should be selected after the update.

None -- Current Version Kept

PyClip.KEEP_SELECTED_VERSION -- Do not change currently selected version.

PyClip.SELECT_CURRENT_VERSION -- Current version as specified in external Open Clip.

PyClip.SELECT_LATEST_VERSION -- Latest version available.

## Read-only properties defined here

### `archive_date`

Return the Clip's last archive date.

### `archive_error`

Return the Clip's last archive error.

### `audio_tracks`

Return a list of the Clip's Audio Tracks.

### `bit_depth`

Return the Clip's bit depth.

### `cached`

Return the Clip's cache status.

### `colour_primaries`

Deduce the Clip's 'colour primaries' export attribute.

### `creation_date`

Return the Clip's creation date.

### `duration`

Return the Clip's duration.

### `essence_uid`

Return the Clip's essence uid.

### `frame_rate`

Return the Clip's frame rate.

### `has_deliverables`

Return the existence of deliverables on the Clip.

### `has_history`

Return the existence of history inside the Clip.

### `height`

Return the Clip's height.

### `markers`

Return a list of the Clip's Markers.

### `matrix_coefficients`

Deduce the Clip's 'matrix coefficients' export attribute.

### `original_source_uid`

Return the Clip's original source UID.

### `proxy_resolution`

Return the Clip's proxy resolution if it has proxies.

### `ratio`

Return the Clip's frame ratio.

### `sample_rate`

Return the Clip's audio sample rate.

### `scan_mode`

Return the Clip's scan mode.

### `source_uid`

Return the Clip's source uid.

### `start_frame`

Return the Clip's start frame.

### `subtitles`

Return a list of the Clip's Subtitles Tracks.

### `tape_name`

Return the Clip's tape name.

### `transfer_characteristics`

Deduce the Clip's 'transfer characteristics' export attribute.

### `unlinked`

Return the Clip's unlinked status.

### `versions`

Return a list of the Clip's versions.

### `version_uids`

Return a list of the Clip's source UIDs. Only available on single segment clips.

### `version_uid`

Return the currently selected source UID of the Clip. Only available on single segment clips.

### `width`

Return the Clip's width.

## Inherited members

- **Static methods inherited from PyArchiveEntry:** `clear_colour`, `commit`, `get_wiretap_node_id`, `get_wiretap_storage_id`
- **Read-only properties inherited from PyFlameObject:** `attributes`, `parent`
