# class `flame.PyReel`(PyArchiveEntry)

Object representing a Reel.

**Method resolution order:** PyReel → PyArchiveEntry → PyFlameObject

## Methods

> Cannot be instantiated from Python (obtained from other API objects).

### `clear`

```python
clear( (PyReel)arg1 [, (bool)confirm=True]) -> bool
```

Clear the Reel content.

### `create_sequence`

```python
create_sequence( (PyReel)arg1 [, (str)name='Untitled Sequence' [, (int)video_tracks=1 [, (bool)video_stereo=False [, (int)width=1920 [, (int)height=1080 [, (float)ratio=1.7777777777777777 [, (int)bit_depth=8 [, (str)scan_mode='P' [, (str)frame_rate='29.97 fps NDF' [, (object)start_at=00:00:00:00 [, (object)duration=00:00:00:01 [, (int)audio_tracks=1 [, (bool)audio_stereo=True]]]]]]]]]]]]]) -> object
```

Create a Sequence in a PyReel, PyLibrary, PyFolder.

Keywords arguments:

video_tracks -- Number of video tracks. Integer between 1 and 8.

video_stereo -- Stereoscopy. False for mono, True for stereo.

width -- Integer between 24 and 16384.

height -- Integer between 24 and 16384.

ratio -- Frame aspect ratio. Float between 0.01 and 100.

scan_mode -- Scan mode of the sequence. (F1, F2, P)

frame_rate -- Frame rate. (60 fps, 59.54 NDF, 59.94 DF, 50 fps, 30 fps, 29.97 NDF, 29.97 DF, 25 fps, 24 fps, 23.976 fps)

start_at -- Start timecode. The timecode format must be of the format specified by *frame_rate*.

duration -- Can be an end timecode or an integer. If an end timecode, format must be of the format specified by *frame_rate*. If an integer, it represents a number of frames.

audio_tracks -- Number of audio tracks. (0, 1, 2, 4, 8, 12, 16)

audio_stereo -- Stereophony, apply to all *audio_tracks*. False for mono tracks, True for stereo.

### `save`

```python
save( (PyReel)arg1) -> bool
```

Save the Reel to the defined save destination.

## Read-only properties defined here

### `children`

Return a list of the immediate children of the current object.

### `clips`

Return a list of Clip objects that are immediate children of the current object.

### `sequences`

Return a list of Sequence objects that are immediate children of the current object.

### `type`

Return the Reel type (Reel, Schematic, Sequences, Shelf).

## Inherited members

- **Static methods inherited from PyArchiveEntry:** `clear_colour`, `commit`, `get_wiretap_node_id`, `get_wiretap_storage_id`
- **Read-only properties inherited from PyFlameObject:** `attributes`, `parent`
