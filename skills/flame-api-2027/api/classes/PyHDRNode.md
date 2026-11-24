# class `flame.PyHDRNode`(PyNode)

> **2027 additions not shown below.** Autodesk's published pydoc predates some Flame 2027 API changes. New/renamed/deprecated members for this class (or its bases) are in What's New: [PyNode](../../guides/whats-new-2027.md#pynode). Treat those as authoritative where they differ.

Object representing a HDR node.

**Method resolution order:** PyHDRNode → PyNode → PyFlameObject

> Cannot be instantiated from Python (obtained from other API objects).

## Methods

### `analyze`

```python
analyze( (PyHDRNode)arg1 [, (str)analyze_mode='Current Shot']) -> None
```

Perform HDR analysis.

### `export_DolbyVision_xml`

```python
export_DolbyVision_xml( (PyHDRNode)arg1, (str)file_name [, (str)comment='']) -> None
```

Export the current HDR to a Dolby Vision XML file.

### `has_trim`

```python
has_trim( (PyHDRNode)arg1, (int)target_display_id) -> bool
```

Returns True if the given Target Display ID has trims.

### `import_DolbyVision_xml`

```python
import_DolbyVision_xml( (PyHDRNode)arg1, (str)file_name [, (str)mode='Include Frame Based Transitions Trims' [, (int)shot_idx=0]]) -> None
```

Import the current HDR from a Dolby Vision XML file.

### `interpolate_trims`

```python
interpolate_trims( (PyHDRNode)arg1) -> None
```

Interpolate the current HDR trims.

### `keep_analysis`

```python
keep_analysis( (PyHDRNode)arg1) -> None
```

Remove the dirty flag from the HDR analysis.

### `l2_from_l8`

```python
l2_from_l8( (PyHDRNode)arg1) -> object
```

Dictionary containing the L2 values based on L8 values. Not valid in Dolby Vision 2.9.

### `reset_analysis`

```python
reset_analysis( (PyHDRNode)arg1) -> None
```

Reset the current HDR analysis.

### `reset_trims`

```python
reset_trims( (PyHDRNode)arg1) -> None
```

Reset the current HDR trims.

## Read-only properties defined here

### `analysis_status`

Return the current state of the HDR analysis.

### `mastering_display_ids`

List of available Mastering Display Ids.

### `mastering_display_info`

Dictionary containing Mastering Display information. Returned object is a copy.

### `target_display_ids`

List of available Target Display Ids.

### `target_display_info`

Dictionary containing Target Display information. Returned object is a copy.

## Inherited members

- **Static methods inherited from PyNode:** `delete`, `duplicate`, `load_node_setup`, `save_node_setup`, `set_context`
- **Read-only properties inherited from PyNode:** `input_sockets`, `output_sockets`, `sockets`
- **Read-only properties inherited from PyFlameObject:** `attributes`, `parent`
