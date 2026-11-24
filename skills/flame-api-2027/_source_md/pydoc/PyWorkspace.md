# class `flame.PyWorkspace`(PyArchiveEntry)

Object representing a Workspace.

**Method resolution order:** PyWorkspace → PyArchiveEntry → PyFlameObject

## Methods

> Cannot be instantiated from Python (obtained from other API objects).

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
