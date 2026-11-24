# class `flame.PyWorkspace`(PyArchiveEntry)

Object representing a Workspace.

**Method resolution order:** PyWorkspace → PyArchiveEntry → PyFlameObject

> Cannot be instantiated from Python (obtained from other API objects).

## Methods

### `create_library`

```python
create_library( (PyWorkspace)arg1, (str)name) -> object
```

Create a new Library in a Workspace.

### `replace_desktop`

```python
replace_desktop( (PyWorkspace)arg1, (PyDesktop)desktop) -> bool
```

Replace the Workspace active Desktop with another one.

### `set_desktop_reels`

```python
set_desktop_reels( (PyWorkspace)arg1 [, (object)group=None]) -> bool
```

Set the Desktop Reels view mode.

### `set_freeform`

```python
set_freeform( (PyWorkspace)arg1 [, (object)reel=None]) -> bool
```

Set the Freeform view mode.

## Read-only properties defined here

### `desktop`

Return the current Desktop.

### `libraries`

Return the Workspace Libraries.

## Inherited members

- **Static methods inherited from PyArchiveEntry:** `clear_colour`, `commit`, `get_wiretap_node_id`, `get_wiretap_storage_id`
- **Read-only properties inherited from PyFlameObject:** `attributes`, `parent`

## Attributes (documented values)

Source: "PyWorkspace Attributes" help page. Access via `obj.<attr>`; most return a `PyAttribute` — use `.get_value()` / `.set_value()` (see PyAttribute.md).

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

#### `current_reel_group (class 'flame.PyReelGroup')`

The Workspace current Reel Group (PyReelGroup).

Value range: None

#### `tags (type 'list')`

The tag list of an object in the Media Panel.

Value range: None
