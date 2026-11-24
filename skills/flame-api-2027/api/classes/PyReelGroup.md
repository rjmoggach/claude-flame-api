# class `flame.PyReelGroup`(PyArchiveEntry)

Object representing a Reel Group.

**Method resolution order:** PyReelGroup → PyArchiveEntry → PyFlameObject

> Cannot be instantiated from Python (obtained from other API objects).

## Methods

### `clear`

```python
clear( (PyReelGroup)arg1 [, (bool)confirm=True]) -> bool
```

Clear the Reel Group content.

### `create_reel`

```python
create_reel( (PyReelGroup)arg1, (str)name [, (bool)sequence=False]) -> object
```

Create a new Reel inside a Reel Group.

### `save`

```python
save( (PyReelGroup)arg1) -> bool
```

Save the Reel Group to the defined save destination.

## Read-only properties defined here

### `children`

Return a list of the immediate children of the current object.

### `reels`

Return a list of Reel objects that are immediate children of the current object.

## Inherited members

- **Static methods inherited from PyArchiveEntry:** `clear_colour`, `commit`, `get_wiretap_node_id`, `get_wiretap_storage_id`
- **Read-only properties inherited from PyFlameObject:** `attributes`, `parent`

## Attributes (documented values)

Source: "PyReelGroup Attributes" help page. Access via `obj.<attr>`; most return a `PyAttribute` — use `.get_value()` / `.set_value()` (see PyAttribute.md).

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
