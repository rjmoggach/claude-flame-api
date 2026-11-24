# class `flame.PyWriteFileNode`(PyRenderNode)

Class derived from PyRenderNode. This class represents a WriteFile node.

**Method resolution order:** PyWriteFileNode → PyRenderNode → PyNode → PyFlameObject

## Methods

> Cannot be instantiated from Python (obtained from other API objects).

### `get_resolved_media_path`

```python
get_resolved_media_path( (PyWriteFileNode)arg1 [, (bool)show_extension=True [, (bool)translate_path=True [, (object)frame=None]]]) -> object
```

Return the resolved media path.

Keyword arguments:

show_extension -- Set True to display the extension.

translate_path -- Set True to apply the Media Location Path Translation.

frame -- Pass a frame number, between range_start and range_end, to get the path for that frame.

## Inherited members

- **Static methods inherited from PyRenderNode:** `set_channel_name`
- **Read-only properties inherited from PyRenderNode:** `channels`
- **Static methods inherited from PyNode:** `delete`, `duplicate`, `load_node_setup`, `save_node_setup`, `set_context`
- **Read-only properties inherited from PyNode:** `input_sockets`, `output_sockets`, `sockets`
- **Read-only properties inherited from PyFlameObject:** `attributes`, `parent`
