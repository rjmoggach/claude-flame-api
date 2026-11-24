# class `flame.PyTimewarpNode`(PyNode)

Object representing a Timewarp node.

**Method resolution order:** PyTimewarpNode → PyNode → PyFlameObject

## Methods

> Cannot be instantiated from Python (obtained from other API objects).

### `get_duration_timing`

```python
get_duration_timing( (PyTimewarpNodearg1, (float)frame) -> float
```

Return the timing value for the current frame while in the duration mode.

### `get_speed`

```python
get_speed( (PyTimewarpNodearg1, (float)frame) -> float
```

Return the speed attribute at the requested frame.

### `get_timing`

```python
get_timing( (PyTimewarpNodearg1, (float)frame) -> float
```

Return the timing value at the requested frame.

### `get_speed_timing`

```python
get_speed_timing( (PyTimewarpNodearg1, (float)frame) -> float
```

The timing value for the current frame while in the speed mode.

### `set_speed`

```python
set_speed( (PyTimewarpNodearg1, (float)frame, (float)new_speed) -> None
```

Set the speed at the requested frame.

### `set_timing`

```python
set_timing( (PyTimewarpNodearg1, (float)frame, (float)new_timing) -> None
```

Set the timing at the requested frame.

## Inherited members

- **Static methods inherited from PyNode:** `delete`, `duplicate`, `load_node_setup`, `save_node_setup`, `set_context`
- **Read-only properties inherited from PyNode:** `input_sockets`, `output_sockets`, `sockets`
- **Read-only properties inherited from PyFlameObject:** `attributes`, `parent`
