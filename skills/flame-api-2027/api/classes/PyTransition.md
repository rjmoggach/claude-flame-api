# class `flame.PyTransition`(PyFlameObject)

Object representing a Transition.

**Method resolution order:** PyTransition → PyFlameObject

> Cannot be instantiated from Python (obtained from other API objects).

## Methods

### `set_dissolve_to_from_colour`

```python
set_dissolve_to_from_colour( (PyTransition)arg1 [, (float)r=0.0 [, (float)g=0.0 [, (float)b=0.0]]]) -> None
```

Make a dissolve transition dissolve to/from a colour.

### `set_fade_to_from_silence`

```python
set_fade_to_from_silence( (PyTransition)arg1) -> None
```

Make a fade dip to/from silence.

### `set_transition`

```python
set_transition( (PyTransition)arg1, (str)type [, (int)duration=10 [, (str)alignment='Centred' [, (int)in_offset=0]]]) -> object
```

Replace the Transition with another type of Transition.

Returns the new PyTransition if successful.

Keywords argument:

type -- Type of the new Transition.

duration -- Duration of the new Transition in frames.

alignment -- Alignment of the new Transition.

in_offset -- Number of frames on left side of the cut in custom alignment.

### `slide`

```python
slide( (PyTransition)arg1, (int)offset [, (bool)sync=False]) -> bool
```

Slide the Transition.

Keywords argument:

offset -- Amount of frames to slide the Transition with.

sync -- Enable to perform the same operation on transitions that belong to the same sync group as the current PyTransition.

## Read-only properties defined here

### `in_offset`

Return the in offset of the Transition.

### `record_time`

Return the record time of Transition focus.

### `type`

Return the Transition type.

## Inherited members

- **Read-only properties inherited from PyFlameObject:** `attributes`, `parent`
