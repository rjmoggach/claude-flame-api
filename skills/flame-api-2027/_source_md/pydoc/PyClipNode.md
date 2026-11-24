# class `flame.PyClipNode`(PyNode)

Class derived from PyNode. This class represents a Clip node.

**Method resolution order:** PyClipNode → PyNode → PyFlameObject

## Methods

> Cannot be instantiated from Python (obtained from other API objects).

### `set_version_uid`

```python
set_version_uid( (PyClipNode)arg1, (str)version_uid) -> bool
```

Set the clip node's current version unique ID.

Keywords argument:

version_uid -- version unique ID.

## Read-only properties defined here

### `clip`

The associated PyClip or PySequence of the clip node.

### `version_uid`

The clip node's list of available version unique IDs.

### `version_uids`

The clip node's list of available version unique IDs.

### `colour_space`

The clip colour space at current frame for primary output.

## Inherited members

- **Static methods inherited from PyNode:** `delete`, `duplicate`, `load_node_setup`, `save_node_setup`, `set_context`
- **Read-only properties inherited from PyNode:** `input_sockets`, `output_sockets`, `sockets`
- **Read-only properties inherited from PyFlameObject:** `attributes`, `parent`
