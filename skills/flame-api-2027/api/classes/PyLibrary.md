# class `flame.PyLibrary`(PyArchiveEntry)

Class derived from PyArchiveEntry. This class represents a Library.

**Method resolution order:** PyLibrary → PyArchiveEntry → PyFlameObject

> Cannot be instantiated from Python (obtained from other API objects).

## Methods

### `acquire_exclusive_access`

```python
acquire_exclusive_access( (PyLibrary)arg1) -> bool
```

Acquire exclusive access to the Shared Library. Shared Libraries are created locked. Only use with Shared Libraries.

### `clear`

```python
clear( (PyLibrary)arg1 [, (bool)confirm=True]) -> bool
```

Clear the Library's contents.

### `close`

```python
close( (PyLibrary)arg1) -> bool
```

Close a Library to release it from the application memory.

### `create_folder`

```python
create_folder( (PyLibrary)arg1, (str)name) -> object
```

Create a Folder inside a Library.

### `create_reel`

```python
create_reel( (PyLibrary)arg1, (str)name) -> object
```

Create a Reel inside a Library.

### `create_reel_group`

```python
create_reel_group( (PyLibrary)arg1, (str)name) -> object
```

Create a Reel Group inside a Library.

### `create_sequence`

```python
create_sequence( (PyLibrary)arg1 [, (str)name='Untitled Sequence' [, (int)video_tracks=1 [, (bool)video_stereo=False [, (int)width=1920 [, (int)height=1080 [, (float)ratio=1.7777777777777777 [, (int)bit_depth=8 [, (str)scan_mode='P' [, (str)frame_rate='29.97 fps NDF' [, (object)start_at=00:00:00:00 [, (object)duration=00:00:00:01 [, (int)audio_tracks=1 [, (bool)audio_stereo=True]]]]]]]]]]]]]) -> object
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

### `open`

```python
open( (PyLibrary)arg1) -> bool
```

Open a Library and load it in the application memory. Until a Library is open, it cannot be accessed. Libraries are created open.

### `release_exclusive_access`

```python
release_exclusive_access( (PyLibrary)arg1) -> bool
```

Release exclusive access to the Shared Library. Only used for Shared Libraries. Only use with Shared Libraries.

## Read-only properties defined here

### `batch_groups`

Return a list of Batch Group objects that are immediate children of the current object.

### `batch_iterations`

Return a list of Batch Iteration objects that are immediate children of the current object.

### `children`

Return a list of the immediate children of the current object.

### `clips`

Return a list of Clip objects that are immediate children of the current object.

### `desktops`

Return a list Desktop objects that are immediate children of the current object.

### `folders`

Return a list of the Folder objects that are immediate children of the current object.

### `opened`

Return True if the Library is in the open state.

### `reel_groups`

Return a list of Reel Group objects that are immediate children of the current object..

### `reels`

Return a list of Reel objects that are immediate children of the current object.

### `sequences`

Return a list of Sequence objects that are immediate children of the current object.

## Inherited members

- **Static methods inherited from PyArchiveEntry:** `clear_colour`, `commit`, `get_wiretap_node_id`, `get_wiretap_storage_id`
- **Read-only properties inherited from PyFlameObject:** `attributes`, `parent`

## Attributes (documented values)

Source: "PyLibrary Attributes" help page. Access via `obj.<attr>`; most return a `PyAttribute` — use `.get_value()` / `.set_value()` (see PyAttribute.md).

#### `name (type 'str')`

The name of an object in the Media Panel, resolving tokens if any are present.

Value range: None

#### `uid (type 'str')`

The unique identifier of an object in the Media Panel.

Value range: None

#### `token_name (type 'str')`

The tokenized name of an object in the Media Panel.

Value range: None

#### `expanded (type 'bool')`

The expanded state of an object in the Media Panel. If you're expanding/collapsing a Shared Library, you must have exclusive access if you want this property to be persisted.

Value range:

- True
- False

#### `colour (type 'tuple')`

The colour of an object in the Media Panel.

Value range:

- (0.0, 0.0, 0.0)
- (1.0, 1.0, 1.0)

#### `colour_label (type 'str')`

The colour label of an object in the Media Panel.

Value range: None

#### `selected (type 'bool')`

The PyArchiveEntry is selected in the Media Panel.

Value range:

- True
- False

#### `tags (type 'list')`

The tag list of an object in the Media Panel.

Value range: None
