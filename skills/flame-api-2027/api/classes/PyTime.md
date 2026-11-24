# class `flame.PyTime`

Object representing a time unit

PyTime(timecode, frame_rate)

PyTime(relative_frame)

PyTime(absolute_frame, frame_rate)

**Method resolution order:** PyTime

## Methods

### `__add__`

```python
__add__( (PyTime)arg1, (PyTime)arg2) -> object
```

__add__( (PyTime)arg1, (int)arg2) -> object

### `__eq__`

```python
__eq__( (PyTime)arg1, (PyTime)arg2) -> bool
```

### `__iadd__`

```python
__iadd__( (object)arg1, (PyTime)arg2) -> object
```

__iadd__( (object)arg1, (int)arg2) -> object

### `__init__`

```python
__init__( (object)arg1, (str)arg2, (str)arg3) -> None
```

__init__( (object)arg1, (int)arg2) -> None

__init__( (object)arg1, (int)arg2, (str)arg3) -> None

### `__isub__`

```python
__isub__( (object)arg1, (PyTime)arg2) -> object
```

__isub__( (object)arg1, (int)arg2) -> object

### `__ne__`

```python
__ne__( (PyTime)arg1, (PyTime)arg2) -> bool
```

### `__repr__`

```python
__repr__( (PyTime)arg1) -> object
```

### `__str__`

```python
__str__( (PyTime)arg1) -> str
```

### `__sub__`

```python
__sub__( (PyTime)arg1, (PyTime)arg2) -> object
```

__sub__( (PyTime)arg1, (int)arg2) -> object

## Read-only properties defined here

### `frame`

Return the absolute frame number.

### `frame_rate`

Return the object frame rate.

### `relative_frame`

Return the relative frame number.

### `timecode`

Return the timecode.

## Data and other attributes defined here

### `__instance_size__`

`__instance_size__ = 72`
