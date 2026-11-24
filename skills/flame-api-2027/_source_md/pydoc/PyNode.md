# class `flame.PyNode`(PyFlameObject)

Object representing a Node.

**Method resolution order:** PyNode → PyFlameObject

## Methods

> Cannot be instantiated from Python (obtained from other API objects).

### `cache_range`

```python
cache_range( (PyFlameObject)arg1 [, (object)start=None [, (object)end=None]]) -> int
```

Cache the Node result.

Keyword arguments:

start -- The first frame of the cache range. The current Batch start frame is used when not specified.

end -- The last frame of the cache range. The current Batch end frame is used when not specified.

### `clear_schematic_colour`

```python
clear_schematic_colour( (PyFlameObject)arg1) -> None
```

Clear the schematic colour of the Node.

### `delete`

```python
delete( (PyFlameObject)arg1 [, (bool)confirm=True]) -> bool
```

Delete the node.

### `duplicate`

```python
duplicate( (PyNode)arg1 [, (bool)keep_node_connections=False]) -> object
```

Duplicate the node.

### `load_node_setup`

```python
load_node_setup( (PyNode)arg1, (str)file_name) -> bool
```

Load a Node setup. A path and a file name must be defined as arguments.

### `save_node_setup`

```python
save_node_setup( (PyNode)arg1, (str)file_name) -> bool
```

Save a Node setup. A path and a file name must be defined as arguments.

### `set_context`

```python
set_context( (PyNode)arg1, (int)index [, (str)socket_name='Default']) -> bool
```

Set a Context view on a Node socket. An index and a socket name must be defined as arguments.

### `clear_schematic_colour`

```python
clear_schematic_colour( (PyNode)arg1) -> None
```

Clear the schematic colour of the Node.

## Read-only properties defined here

### `colour_space`

The colour space at current frame for primary output..

### `input_sockets`

Return a list of the node input sockets names.

### `output_sockets`

Return a list of the node output sockets names.

### `sockets`

Return a dictionary of the input/output sockets names and their connections.

## Inherited members

- **Read-only properties inherited from PyFlameObject:** `attributes`, `parent`
