# class `flame.PyMediaHubFilesTabOptions`

This class represents the MediaHub Files tab options.

**Method resolution order:** PyMediaHubFilesTabOptions

## Methods

> Cannot be instantiated from Python (obtained from other API objects).

### `set_tagged_colour_space`

```python
set_tagged_colour_space( (PyMediaHubFilesTabOptions)arg1, (str)colour_space) -> None
```

Import pixel ratio value. Returns None when resolution is not set to Same As Source.

## Properties (data descriptors)

### `bit_depth`

Import bit depth value. Possible values are 8, 10, 12, 16, 32, and From Source.

### `cache_and_proxies_all_versions`

Generate caches and proxies for all versions instead of the current one on import.

### `cache_mode`

Cache media on import.

### `frame_ratio`

Import frame ratio value. Returns None when resolution mode is not set to Resolution List.

### `height`

Import height value. Returns None when resolution is set to Same as Source, Scaling Presets or Adaptive when based on width.

### `multi_channel_mode`

Multi-Channel Mode to use upon import.

### `pixel_ratio`

Import pixel ratio value. Returns None when resolution is not set to Same As Source.

### `proxies_mode`

Generate proxies on import.

### `resize_filter`

Import resizing filter value. Possible values are Lanczos, Shannon, Gaussian, Quadratic, Bicubic, Mitchell, Triangle, and Impulse.

### `resize_mode`

Import resizing mode value. Possible values are Letterbox, Crop Edges, Fill, and Centre.

### `resolution`

Set the resolution based on the name. Possible values are Custom Resolution, Project Res, Adaptive, Scaling Presets, Same as Source or a resolution with this format: HD 720 16:9 (1280 x 720)

### `scaling_presets_value`

Import scaling presets value. Returns None when the resolution selector is not Scaling Presets.

### `scan_mode`

Import scan mode value. Possible values are P, F1, F2, and From Source.

### `sequence_mode`

Use the sequence mode to import a range of files.

### `width`

Import width value. Returns None when resolution is set to Same as Source, Scaling Presets or Adaptive when based on height.
