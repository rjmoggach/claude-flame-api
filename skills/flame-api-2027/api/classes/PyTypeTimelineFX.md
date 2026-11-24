# class `flame.PyTypeTimelineFX`(PyTimelineFX)

> **2027 additions not shown below.** Autodesk's published pydoc predates some Flame 2027 API changes. New/renamed/deprecated members for this class (or its bases) are in What's New: [PyTypeTimelineFX](../../guides/whats-new-2027.md#pytypenode-and-pytypetimelinefx), [PyTimelineFX](../../guides/whats-new-2027.md#pytimelinefx). Treat those as authoritative where they differ.

Object representing a Type TimelineFX.

**Method resolution order:** PyTypeTimelineFX → PyTimelineFX → PyFlameObject

> Cannot be instantiated from Python (obtained from other API objects).

## Methods

### `add_layer`

```python
add_layer( (PyTypeTimelineFX)arg1, (float)frame) -> float
```

Create a new layer.

Keyword argument:

layer_type -- Must be one of Left, Centre(default), Right, Roll, or Crawl.

### `append_type_setup`

```python
append_type_setup( (PyTypeTimelineFX)arg1, (str)file_name) -> bool
```

Append a setup to the current Type setup.

## Read-only properties defined here

### `layers`

Return the layers list.

## Inherited members

- **Static methods inherited from PyTimelineFX:** `load_setup`, `save_setup`, `slide_keyframes`, `sync_connected_segments`
- **Read-only properties inherited from PyTimelineFX:** `type`
- **Read-only properties inherited from PyFlameObject:** `attributes`, `parent`
