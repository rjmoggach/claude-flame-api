# class `flame.PyBatchIteration`(PyArchiveEntry)

Class derived from PyArchiveEntry. This class represents a Batch Iteration.

**Method resolution order:** PyBatchIteration → PyArchiveEntry → PyFlameObject

> Cannot be instantiated from Python (obtained from other API objects).

## Methods

### `open_as_batch_group`

```python
open_as_batch_group( (PyBatchIteration)arg1 [, (bool)confirm=True]) -> bool
```

Open a Batch Iteration as a new Batch Group, adding it to PyDesktop.batch_groups. Can only be called from a Library.

## Read-only properties defined here

### `iteration_number`

Return the iteration number of the Batch Iteration.

## Inherited members

- **Static methods inherited from PyArchiveEntry:** `clear_colour`, `commit`, `get_wiretap_node_id`, `get_wiretap_storage_id`
- **Read-only properties inherited from PyFlameObject:** `attributes`, `parent`

## Attributes (documented values)

Source: "PyBatchIteration Attributes" help page. Access via `obj.<attr>`; most return a `PyAttribute` — use `.get_value()` / `.set_value()` (see PyAttribute.md).

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

#### `selected (type 'bool')`

The PyArchiveEntry is selected in the Media Panel.

Value range:

- True
- False

#### `tags (type 'list')`

The tag list of an object in the Media Panel.
