<!-- source: Autodesk Flame Family 2027 Help _ PyClip Attributes _ Autodesk.html -->
# PyClip Attributes

### `name (type 'str')`

The name of an object in the Media Panel, resolving tokens if any are present.

Value range: None

### `shot_name (type 'str')`

The shot name of an object in the Media Panel, resolving tokens if any are present.

Value range: None

### `tokenized_shot_name (type 'str')`

The shot name of an object in the Media Panel, including any unresolved tokens, if present.

Value range: None

### `dynamic_shot_name (type 'str')`

The Dynamic attribute of an object in the Media Panel. Automatically disabled when the shot_name attribute is set.

Value range:

- True
- False

### `uid (type 'str')`

The unique identifier of an object in the Media Panel.

Value range: None

### `token_name (type 'str')`

The tokenized name of an object in the Media Panel.

Value range: None

### `expanded (type 'bool')`

The expanded state of an object in the Media Panel. If you're expanding/collapsing a Shared Library, you must have exclusive access if you want this property to be persisted.

Value range:

- True
- False

### `colour (type 'tuple')`

The colour of an object in the Media Panel.

Value range:

- (0.0, 0.0, 0.0)
- (1.0, 1.0, 1.0)

### `colour_label (type 'str')`

The colour label of an object in the Media Panel.

Value range: None

### `selected (type 'bool')`

The PyArchiveEntry is selected in the Media Panel.

Value range:

- True
- False

### `start_time (class 'flame.PyTime')`

The Clip's start time, as a PyTime object.

Value range: None

### `in_mark (type 'NoneType')`

The Clip's In mark. Undefined until set. Set as a timecode, or a frame number relative to the start of the clip (1 based). The mark is exclusive or inclusive, depending on the application Preference.

Value range: None

### `out_mark (type 'NoneType')`

The Clip's out mark. Undefined until set. Set as a timecode, or a frame number relative to the start of the clip (1 based). The mark is exclusive or inclusive, depending on the application Preference.

Value range: None

### `current_time (class 'flame.PyTime')`

The position of the playhead on the Clip.

Value range: None

### `selected_segments (type 'list')`

Return a list of PySegment currently selected.

Value range: None

### `selected_markers (type 'list')`

Return a list of PyMarker currently selected.

Value range: None

### `tags (type 'list')`

The tag list of an object in the Media Panel..

Value range: None

## Related pages

- Autodesk Flame Python: flame module
