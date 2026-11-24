# class `flame.PyResolution`

Object representing a resolution

PyResolution()

PyResolution(width, height, bit_depth, frame_ratio, scan_format)

**Method resolution order:** PyResolution

## Methods

### `__init__`

```python
__init__( (object)arg1) -> None
```

__init__( (object)arg1, (int)arg2, (int)arg3, (int)arg4, (float)arg5, (str)arg6) -> None

__init__( (object)arg1, (str)arg2) -> None

## Properties (data descriptors)

### `bit_depth`

Return the resolution bit depth.

### `frame_ratio`

Return the resolution frame ratio.

### `height`

Return the resolution height.

### `resolution`

Set the resolution based on its name in the UI.

Possible values are:

Custom Resolution

Project Res

Project Resolution

A resolution, in the format used by the Resolution List in the UI. Example: HD 720 16:9 (1280 x 720)

### `scan_mode`

Return the resolution scan mode.

### `width`

Return the resolution width.

## Data and other attributes defined here

### `__instance_size__`

`__instance_size__ = 80`
