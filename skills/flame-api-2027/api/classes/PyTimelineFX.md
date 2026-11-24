# class `flame.PyTimelineFX`(PyFlameObject)

> **2027 additions not shown below.** Autodesk's published pydoc predates some Flame 2027 API changes. New/renamed/deprecated members for this class (or its bases) are in What's New: [PyTimelineFX](../../guides/whats-new-2027.md#pytimelinefx). Treat those as authoritative where they differ.

Object representing a TimelineFX.

**Method resolution order:** PyTimelineFX → PyFlameObject

> Cannot be instantiated from Python (obtained from other API objects).

## Methods

### `clear_maps_cache_media`

```python
clear_maps_cache_media( (PyTimelineFX)arg1) -> bool
```

Clear the Timeline FX Maps and ML cached media.

### `load_setup`

```python
load_setup( (PyTimelineFX)arg1, (str)file_name) -> bool
```

Load a Node setup. A path and a file name must be defined as arguments.

### `save_setup`

```python
save_setup( (PyTimelineFX)arg1, (str)file_name) -> bool
```

Save a Node setup. A path and a file name must be defined as arguments.

### `slide_keyframes`

```python
slide_keyframes( (PyTimelineFX)arg1, (float)offset) -> None
```

Slide the keyframes the PySegment.

Keywords argument:

offset -- Relative offset to slide the keyframes.

sync -- Enable to perform the same operation on the segments that belong to the same sync group as the current PySegment.

### `sync_connected_segments`

```python
sync_connected_segments( (PyTimelineFX)arg1) -> None
```

Push the Timeline FX to connected segments.

## Read-only properties defined here

### `has_maps_cache_media`

Return whether the Timeline FX has Maps or ML cached media.

### `type`

Return the type of the Timeline FX.

## Inherited members

- **Read-only properties inherited from PyFlameObject:** `attributes`, `parent`

## Attributes (documented values)

Source: "PyTimelineFX Attributes" help page. Access via `obj.<attr>`; most return a `PyAttribute` — use `.get_value()` / `.set_value()` (see PyAttribute.md).

#### `bypass (type 'bool')`

The bypass status of the Timeline FX.

Value range:

- True
- False
