<!-- source: Autodesk Flame Family 2027 Help _ PyBatch Attributes _ Autodesk.html -->
# PyBatch Attributes

### `name (type 'str')`

The name of an object in the Media Panel, resolving tokens if any are present.

### `uid (type 'str')`

The unique identifier of an object in the Media Panel.

### `token_name (type 'str')`

The tokenized name of an object in the Media Panel.

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

### `selected (type 'bool')`

The PyArchiveEntry is selected in the Media Panel.

Value range:

- True
- False

### `selected_nodes (type 'list')`

The list of Batch object nodes that are currently selected in the Batch schematic.

### `current_node (class 'flame.PyActionNode')`

Return the Batch node currently selected in the Batch schematic. Use current_node to capture the node selected by the user. In the case of a multi-selection, return the primary selection (yellow ring).

### `duration (type 'int')`

The duration of Batch Group.

### `start_frame (type 'int')`

The start frame of the Batch Group.

### `auto_key (type 'bool')`

The Auto Key status of the Batch Group.

### `current_frame (type 'int')`

The current frame of the Batch Group.

### `tags (type 'list')`

The tag list of an object in the Media Panel.

## Related pages

- Autodesk Flame Python: flame module
