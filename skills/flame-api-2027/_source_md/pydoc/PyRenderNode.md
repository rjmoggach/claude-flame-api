# class `flame.PyRenderNode`(PyNode)

Class derived from PyNode. This class represents a Render node.

**Method resolution order:** PyRenderNode → PyNode → PyFlameObject

## Methods

> Cannot be instantiated from Python (obtained from other API objects).

### `set_channel_name`

```python
set_channel_name( (PyRenderNode)arg1, (object)channel, (object)name) -> None
```

Rename a channel, using its index or front channel name as the index key.

Keyword arguments:

channel -- The channel to rename. Can be the channel index or the current name of the channel's front socket.

name -- The new name of the channel. The type is either a string or a tuple. A Write File node always takes a string. A Render node takes a string or a tuple.

In a Render node, a string only sets the name of the channel's front socket; the function creates the name of the matte socket by appending '_alpha' to 'name'. In the UI, the channel is flagged 'Sync'. A Write File node has only one socket per channel, and requires only a string to set a socket name.

In a Render node, a tuple sets the names of the front and matte sockets. In the UI, the channel is not flagged 'Sync'. A Write File node does not accept a tuple.

## Read-only properties defined here

### `channels`

The channels attribute is a list of tuples, where each tuple is made of a socket name and its channel name.

## Inherited members

- **Static methods inherited from PyNode:** `delete`, `duplicate`, `load_node_setup`, `save_node_setup`, `set_context`
- **Read-only properties inherited from PyNode:** `input_sockets`, `output_sockets`, `sockets`
- **Read-only properties inherited from PyFlameObject:** `attributes`, `parent`
