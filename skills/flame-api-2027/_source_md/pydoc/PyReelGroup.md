# class `flame.PyReelGroup`(PyArchiveEntry)

Object representing a Reel Group.

**Method resolution order:** PyReelGroup → PyArchiveEntry → PyFlameObject

## Methods

> Cannot be instantiated from Python (obtained from other API objects).

### `clear`

```python
clear( (PyReelGroup)arg1 [, (bool)confirm=True]) -> bool
```

Clear the Reel Group content.

### `create_reel`

```python
create_reel( (PyReelGroup)arg1, (str)name [, (bool)sequence=False]) -> object
```

Create a new Reel inside a Reel Group.

### `save`

```python
save( (PyReelGroup)arg1) -> bool
```

Save the Reel Group to the defined save destination.

## Read-only properties defined here

### `children`

Return a list of the immediate children of the current object.

### `reels`

Return a list of Reel objects that are immediate children of the current object.

## Inherited members

- **Static methods inherited from PyArchiveEntry:** `clear_colour`, `commit`, `get_wiretap_node_id`, `get_wiretap_storage_id`
- **Read-only properties inherited from PyFlameObject:** `attributes`, `parent`
