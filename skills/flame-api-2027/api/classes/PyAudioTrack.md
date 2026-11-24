# class `flame.PyAudioTrack`(PyFlameObject)

> **2027 additions not shown below.** Autodesk's published pydoc predates some Flame 2027 API changes. New/renamed/deprecated members for this class (or its bases) are in What's New: [PyAudioTrack](../../guides/whats-new-2027.md#pyaudiotrack). Treat those as authoritative where they differ.

Object representing an Audio Track.

**Method resolution order:** PyAudioTrack → PyFlameObject

> Cannot be instantiated from Python (obtained from other API objects).

## Methods

### `copy_to_media_panel`

```python
copy_to_media_panel( (PyAudioTrack)arg1, (PyArchiveEntry)destination [, (str)duplicate_action='add']) -> object
```

Create a new clip with a copy of the PyObject.

## Read-only properties defined here

### `channels`

Return a list of the Audio Track's channels.

### `stereo`

Return whether or not the Audio Track is stereo.

## Inherited members

- **Read-only properties inherited from PyFlameObject:** `attributes`, `parent`

## Attributes (documented values)

Source: "PyAudioTrack Attributes" help page. Access via `obj.<attr>`; most return a `PyAttribute` — use `.get_value()` / `.set_value()` (see PyAttribute.md).

#### `expanded (type 'bool')`

The expanded status of the Version or Audio Track.

Value range:

- True
- False

#### `selected_segments (type 'list')`

Return a list of PySegment currently selected.

#### `solo (type 'bool')`

The solo status of the Track.

Value range:

- True
- False

#### `mute (type 'bool')`

The transparency attribute of the Front input of the Comp node.

Value range:

- True
- False
