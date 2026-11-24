# class `flame.PyArchiveEntry`(PyFlameObject)

Class derived from PyFlameObject. Base class for any object displayed in the Media Panel.

**Method resolution order:** PyArchiveEntry → PyFlameObject

> Cannot be instantiated from Python (obtained from other API objects).

## Methods

### `clear_colour`

```python
clear_colour( (PyArchiveEntry)arg1) -> None
```

Clear the colour of an object in the Media Panel.

### `commit`

```python
commit( (PyArchiveEntry)arg1) -> None
```

Commit to disk the Media Panel object or its closest container possible.

### `get_wiretap_node_id`

```python
get_wiretap_node_id( (PyArchiveEntry)arg1) -> str
```

Return the Wiretap Node ID of the Flame object, but only if the object is in the Media Panel.

### `get_wiretap_storage_id`

```python
get_wiretap_storage_id( (PyArchiveEntry)arg1) -> str
```

Return the Wiretap server's storage ID for the Flame object, but only if the object is in the Media Panel.

## Inherited members

- **Read-only properties inherited from PyFlameObject:** `attributes`, `parent`
