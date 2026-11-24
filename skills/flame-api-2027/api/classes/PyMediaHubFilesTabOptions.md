# class `flame.PyMediaHubFilesTabOptions`

This class represents the MediaHub Files tab options.

**Method resolution order:** PyMediaHubFilesTabOptions

> Cannot be instantiated from Python (obtained from other API objects).

## Methods

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

## Attributes (documented values)

Source: "PyMediaHubFilesTabOptions" help page. Access via `obj.<attr>`; most return a `PyAttribute` — use `.get_value()` / `.set_value()` (see PyAttribute.md).

Object allowing manipulation of current options of the **Files** tab of the **MediaHub** module. These options control how media files are imported and processed when brought into the project.

---

### PyMediaHubFileTabOptions Attributes

| Property | Type | Description |
|---|---|---|
| `multi_channel_mode` | string | Multi-Channel Mode. |
| `sequence_mode` | bool | Enable or disable sequence mode. |
| `cache_mode` | bool | Enable or disable cache mode. |
| `proxies_mode` | bool | Enable or disable proxies mode. |
| `cache_and_proxies_all_versions` | bool | Generate cache and proxies for all versions. |
| `resize_mode` | string | Resize mode. |
| `resize_filter` | string | Resize filter. |
| `resolution` | string | Resolution. |
| `width` | int | Width in pixels. |
| `height` | int | Height in pixels. |
| `scaling_presets_value` | float | Scaling preset value. |
| `frame_ratio` | float | Frame ratio. |
| `bit_depth` | int | Bit depth. |
| `scan_mode` | string | Scan mode. |
| `pixel_ratio` | float | Pixel ratio. |
| `tagged_colour_space` | string | Tagged colour space name. |
| `colour_mgmt_mode` | string | Colour Management mode. |
| `colour_mgmt_display` | string | Colour Management display name. |
| `colour_mgmt_invert` | bool | Enable or disable the Colour Management invert option. |
| `colour_mgmt_view` | string | Colour Management view name. |
| `colour_mgmt_working_space` | string | Colour Management working space name. |

---

### PyMediaHubFileTabOptions Methods

| Function | Description |
|---|---|
| `import_transform()` | Import a transform in `Use LUT` Colour Management mode. One mandatory argument must be passed: • file_path: Path to the transform file. |

See PyMediaHubFilesTab for inherited methods.

---

### Enumeration Values

#### Multi-Channel Modes

| Values |
|---|
| `Multi-Channel Clip` |
| `Include Alpha Clip` |
| `Ignore Alpha Channel` |
| `Create Matte Container` |
| `Matte Container With Comp` |
| `Matte Container (Full)` |

#### Resize Modes

| Values |
|---|
| `Centre` |
| `Letterbox` |
| `Crop Edges` |
| `Fill` |
| `Fill Pan` |
| `Fill Pixel` |
| `Fill All Pixel` |

#### Resize Filters

| Values |
|---|
| `lanczos` |
| `draft` |
| `bicubic` |
| `mitchell` |
| `triangle` |
| `impulse` |
| `shannon` |
| `quadratic` |
| `gaussian` |

#### Bit Depths

| Values |
|---|
| `From Source` |
| `From LUT` |
| `8` |
| `10` |
| `12` |
| `16` |

#### Scan Modes

| Values |
|---|
| `From Source` |
| `P` |
| `F1` |
| `F2` |

#### Colour Management Modes

| Values |
|---|
| `Tag Only` |
| `Auto Convert` |
| `View Transform` |
| `Use LUT` |
