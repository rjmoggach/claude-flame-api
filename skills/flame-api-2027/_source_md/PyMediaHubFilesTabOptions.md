<!-- source: Autodesk Flame Family 2027 Help _ PyMediaHubFilesTabOptions _ Autodesk.html -->
# PyMediaHubFilesTabOptions

Object allowing manipulation of current options of the **Files** tab of the **MediaHub** module. These options control how media files are imported and processed when brought into the project.

---

## PyMediaHubFileTabOptions Attributes

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

## PyMediaHubFileTabOptions Methods

| Function | Description |
|---|---|
| `import_transform()` | Import a transform in `Use LUT` Colour Management mode. One mandatory argument must be passed: • file_path: Path to the transform file. |

See PyMediaHubFilesTab for inherited methods.

---

## Enumeration Values

### Multi-Channel Modes

| Values |
|---|
| `Multi-Channel Clip` |
| `Include Alpha Clip` |
| `Ignore Alpha Channel` |
| `Create Matte Container` |
| `Matte Container With Comp` |
| `Matte Container (Full)` |

### Resize Modes

| Values |
|---|
| `Centre` |
| `Letterbox` |
| `Crop Edges` |
| `Fill` |
| `Fill Pan` |
| `Fill Pixel` |
| `Fill All Pixel` |

### Resize Filters

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

### Bit Depths

| Values |
|---|
| `From Source` |
| `From LUT` |
| `8` |
| `10` |
| `12` |
| `16` |

### Scan Modes

| Values |
|---|
| `From Source` |
| `P` |
| `F1` |
| `F2` |

### Colour Management Modes

| Values |
|---|
| `Tag Only` |
| `Auto Convert` |
| `View Transform` |
| `Use LUT` |

## Related pages

- Autodesk Flame Python: flame module
- PyMediaHubFilesTab
