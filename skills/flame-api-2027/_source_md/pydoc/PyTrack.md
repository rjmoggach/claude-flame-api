# class `flame.PyTrack`(PyFlameObject)

Object representing a Track.

**Method resolution order:** PyTrack → PyFlameObject

## Methods

> Cannot be instantiated from Python (obtained from other API objects).

### `copy_to_media_panel`

```python
copy_to_media_panel( (PyTrack)arg1, (PyArchiveEntry)destination [, (str)duplicate_action='add']) -> object
```

Create a new clip with a copy of the PyObject.

### `cut`

```python
cut( (PyTrack)arg1, (PyTime)cut_time [, (bool)sync=False]) -> None
```

Cut the Track.

### `insert_transition`

```python
insert_transition( (PyTrack)arg1, (PyTime)record_time, (str)type [, (int)duration=10 [, (str)alignment='Centred' [, (int)in_offset=0 [, (bool)sync=False]]]]) -> object
```

Insert a Transition on the Track.

Returns the new PyTransition if successful.

Keywords argument:

record_time -- Time at which the Transition is inserted.

type -- Type of the new Transition.

duration -- Duration of the new Transition in frames.

alignment -- Alignment of the new Transition.

in_offset -- Number of frames on left side of the cut in custom alignment.

sync -- Perform the operation on all Tracks part of the sync group.

## Read-only properties defined here

### `segments`

Return a list of the Track's segments.

### `transitions`

Return a list of the Track's transitions.

## Inherited members

- **Read-only properties inherited from PyFlameObject:** `attributes`, `parent`
