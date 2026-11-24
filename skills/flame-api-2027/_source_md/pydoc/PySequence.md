# class `flame.PySequence`(PyClip)

Object representing a Sequence.

**Method resolution order:** PySequence → PyClip → PyArchiveEntry → PyFlameObject

## Methods

> Cannot be instantiated from Python (obtained from other API objects).

### `copy_selection_to_media_panel`

```python
copy_selection_to_media_panel( (PySequence)arg1, (PyArchiveEntry)destination [, (str)duplicate_action='add']) -> object
```

Create a new clip by copying the currently selected segments.

Return the new PyClip.

Keyword arguments:

destination -- The PyObject that acts as the destination.

duplicate_action -- Action to take when an object with the same name already exists (add or replace).

### `create_audio`

```python
create_audio( (PySequence)arg1 [, (bool)stereo=False]) -> object
```

Add an Audio Track to the Sequence.

### `create_container`

```python
create_container( (PySequence)arg1) -> object
```

Create a container with the selected segments or between the in and out marks.

### `create_group`

```python
create_group( (PySequence)arg1, (str)name) -> object
```

Creates a new PySequenceGroup.

The group name must be supplied as argument.

### `create_subtitle`

```python
create_subtitle( (PySequence)arg1) -> object
```

Add a Subtitle Track to the Sequence.

### `create_version`

```python
create_version( (PySequence)arg1 [, (bool)stereo=False]) -> object
```

Add a Version to the Sequence.

### `extract_selection_to_media_panel`

```python
extract_selection_to_media_panel( (PySequence)arg1 [, (PyArchiveEntry)destination=None [, (str)duplicate_action='add']]) -> object
```

Extract the selection from the sequence.

Return the new PyClip created from the selection when a destination is supplied.

Keyword arguments:

destination -- The PyObject that acts as the destination.

duplicate_action -- Action to take when an object with the same name already exists (add or replace).

### `import_subtitles_file`

```python
import_subtitles_file( (PySequence)arg1, (str)file_name [, (object)file_type=None [, (bool)align_first_event_to_clip_start=False [, (object)convert_from_frame_rate=None]]]) -> object
```

Import a subtitles file into a new Subtitles Track.

Return the new PySubtitleTrack.

Keyword arguments:

file_name -- The path and name of the file to import.

file_type -- The type of subtitle if it is not the file extension (srt or txt).

align_first_event_to_clip_start -- Force the first event to be aligned with the clip start.

convert_from_frame_rate -- frame rate of the imported file (for txt files only).

### `insert`

```python
insert( (PySequence)arg1, (PyClip)source_clip [, (PyTime)insert_time=None [, (PyTrack)destination_track=None]]) -> bool
```

Creates a new PySequenceGroup.

The group name must be supplied as argument.

### `lift_selection_to_media_panel`

```python
lift_selection_to_media_panel( (PySequence)arg1 [, (PyArchiveEntry)destination=None [, (str)duplicate_action='add']]) -> object
```

Lift the selection from the sequence.

Return the new PyClip created from the selection when a destination is supplied.

Keyword arguments:

destination -- The PyObject that acts as the destination.

duplicate_action -- Action to take when an object with the same name already exists (add or replace).

### `open`

```python
open( (PySequence)arg1) -> bool
```

Open the Sequence.

### `overwrite`

```python
overwrite( (PySequence)arg1, (PyClip)source_clip [, (PyTime)overwrite_time=None [, (PyTrack)destination_track=None]]) -> bool
```

Creates a new PySequenceGroup.

The group name must be supplied as argument.

## Read-only properties defined here

### `groups`

Return a list of the sequence's PySequenceGroups.

## Inherited members

- **Static methods inherited from PyClip:** `cache_media`, `change_dominance`, `change_start_frame`, `close_container`, `create_marker`, `cut`, `clear_cache_media`, `clear_renders`, `get_colour_space`, `is_rendered`, `open_as_sequence`, `open_container`, `reformat`, `render`, `save`
- **Read-only properties inherited from PyClip:** `archive_date`, `archive_error`, `audio_tracks`, `bit_depth`, `cached`, `colour_primaries`, `creation_date`, `duration`, `essence_uid`, `frame_rate`, `has_deliverables`, `has_history`, `height`, `markers`, `matrix_coefficients`, `original_source_uid`, `proxy_resolution`, `ratio`, `sample_rate`, `scan_mode`, `source_uid`, `start_frame`, `subtitles`, `transfer_characteristics`, `unlinked`, `versions`, `width`
- **Static methods inherited from PyArchiveEntry:** `clear_colour`, `commit`, `get_wiretap_node_id`, `get_wiretap_storage_id`
- **Read-only properties inherited from PyFlameObject:** `attributes`, `parent`
