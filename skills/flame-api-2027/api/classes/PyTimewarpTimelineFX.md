# class `flame.PyTimewarpTimelineFX`(PyTimelineFX)

> **2027 additions not shown below.** Autodesk's published pydoc predates some Flame 2027 API changes. New/renamed/deprecated members for this class (or its bases) are in What's New: [PyTimelineFX](../../guides/whats-new-2027.md#pytimelinefx). Treat those as authoritative where they differ.

Object representing a Timewarp TimelineFX.

**Method resolution order:** PyTimewarpTimelineFX → PyTimelineFX → PyFlameObject

> Cannot be instantiated from Python (obtained from other API objects).

## Methods

### `get_duration_timing`

```python
get_duration_timing( (PyTimewarpTimelineFX)arg1, (float)frame) -> float
```

Return the timing value for the current frame while in the duration mode.

### `get_speed`

```python
get_speed( (PyTimewarpTimelineFX)arg1, (float)frame) -> float
```

Return the speed attribute at the requested frame.

### `get_speed_timing`

```python
get_speed_timing( (PyTimewarpTimelineFX)arg1, (float)frame) -> float
```

The timing value for the current frame while in the speed mode.

### `get_timing`

```python
get_timing( (PyTimewarpTimelineFX)arg1, (float)frame) -> float
```

Return the timing value at the requested frame.

### `set_speed`

```python
set_speed( (PyTimewarpTimelineFX)arg1, (float)frame, (float)new_speed) -> None
```

Set the speed at the requested frame.

### `set_timing`

```python
set_timing( (PyTimewarpTimelineFX)arg1, (float)frame, (float)new_timing) -> None
```

Set the timing at the requested frame.

## Inherited members

- **Static methods inherited from PyTimelineFX:** `load_setup`, `save_setup`, `slide_keyframes`, `sync_connected_segments`
- **Read-only properties inherited from PyTimelineFX:** `type`
- **Read-only properties inherited from PyFlameObject:** `attributes`, `parent`
