# class `flame.PyClrMgmtTimelineFX`(PyTimelineFX)

> **2027 additions not shown below.** Autodesk's published pydoc predates some Flame 2027 API changes. New/renamed/deprecated members for this class (or its bases) are in What's New: [PyTimelineFX](../../guides/whats-new-2027.md#pytimelinefx). Treat those as authoritative where they differ.

Object representing a Colour Management TimelineFX.

**Method resolution order:** PyClrMgmtTimelineFX → PyTimelineFX → PyFlameObject

> Cannot be instantiated from Python (obtained from other API objects).

## Methods

### `get_context_variables`

```python
get_context_variables( (PyClrMgmtTimelineFX)arg1) -> dict
```

Get the context variables in a dictionary.

### `import_transform`

```python
import_transform( (PyClrMgmtTimelineFX)arg1, (str)file_path) -> None
```

Used to import a CDL, CTF, LUT, or 3D LUT form a file.

### `reset_context_variables`

```python
reset_context_variables( (PyClrMgmtTimelineFX)arg1) -> None
```

Reset the context variables to their initial state from the OCIO config.

### `set_context_variable`

```python
set_context_variable( (PyClrMgmtTimelineFX)arg1, (str)name, (str)value) -> None
```

Set the value for the specified context variable.

## Inherited members

- **Static methods inherited from PyTimelineFX:** `clear_maps_cache_media`, `load_setup`, `save_setup`, `slide_keyframes`, `sync_connected_segments`
- **Read-only properties inherited from PyTimelineFX:** `has_maps_cache_media`, `type`
- **Read-only properties inherited from PyFlameObject:** `attributes`, `parent`
