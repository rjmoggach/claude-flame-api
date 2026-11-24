<!-- source: Autodesk Flame Family 2027 Help _ PySegment Attributes _ Autodesk.html -->
# PySegment Attributes

### `name (type 'str')`

The name of the Segment.

### `tokenized_name (type 'str')`

The name of the Segment, including any unresolved tokens, if present.

### `dynamic_name (type 'bool')`

The Dynamic attribute of a Segment's name. Automatically disabled when the name attribute is set.

Value range:

- True
- False

### `shot_name (type 'str')`

The shot name of the Segment.

### `tokenized_shot_name (type 'str')`

The shot name of the Segment, including any unresolved tokens, if present.

### `dynamic_shot_name (type 'bool')`

The Dynamic attribute of a Segment's shot name. Automatically disabled when the shot_name attribute is set.

Value range:

- True
- False

### `comment (type 'str')`

The comment of the Segment.

### `tokenized_comment (type 'str')`

The comment of the Segment, including any unresolved tokens, if present.

### `dynamic_comment (type 'bool')`

The Dynamic attribute of a Segment's comment. Automatically disabled when the comment attribute is set.

Value range:

- True
- False

### `hidden (type 'bool')`

The hidden status of the Segment.

Value range:

- True
- False

### `colour (type 'tuple')`

The colour of the Segment.

Value range:

- (0.0, 0.0, 0.0)
- (1.0, 1.0, 1.0)

### `colour_label (type 'str')`

The colour label of the Segment.

Value range: None

### `selected (type 'bool')`

Select a segment on the Clip.

Value range:

- True
- False

### `selected_markers (type 'list')`

Return a list of PyMarker currently selected.

### `tags (type 'list')`

The tag list of the Segment.

Value range: None

## Related pages

- Autodesk Flame Python: flame module
