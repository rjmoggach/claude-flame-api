# class `flame.PyDesktop`(PyArchiveEntry)

Class derived from PyArchiveEntry. This class represents a Desktop.

**Method resolution order:** PyDesktop → PyArchiveEntry → PyFlameObject

## Methods

> Cannot be instantiated from Python (obtained from other API objects).

### `clear`

```python
clear( (PyDesktop)arg1) -> bool
```

Clear the Desktop.

### `create_batch_group`

```python
create_batch_group( (PyDesktop)arg1, (str)name [, (int)nb_reels=4 [, (int)nb_shelf_reels=1 [, (list)reels=[] [, (list)shelf_reels=[] [, (int)start_frame=1 [, (object)duration=None]]]]]]) -> object
```

Create a new Batch Group object in the Desktop catalogue.

Keyword arguments:

name -- Name of the Batch Group.

nb_reels -- Number of reels created. *reels* overrides *nb_reels*.

nb_shelf_reels -- Number of shelf reels. The first shelf reel created is named Batch Renders. *shelf_reels* overrides *nb_shelf_reels*.

reels -- A list of reel names. Overrides *nb_reels*.

shelf_reels -- A list of shelf reel names. Overrides *nb_shelf_reels*.

start_frame -- The Batch Group's start frame. No timecodes, only a frame value.

duration -- The number of frames. Sets the Duration field in the Batch UI. Will be set to the first clip duration when not specified.

### `create_reel_group`

```python
create_reel_group( (PyDesktop)arg1, (str)name) -> object
```

Create a new Reel Group object in the Desktop catalogue.

### `save`

```python
save( (PyDesktop)arg1) -> bool
```

Save the Desktop to the location defined by the *destination* attribute.

## Read-only properties defined here

### `batch_groups`

Return a list of Batch Group objects that are immediate children of the current object.

### `children`

Return a list of the immediate children of the current object.

### `reel_groups`

Return a list of Reel Group objects that are immediate children of the current object..

## Inherited members

- **Static methods inherited from PyArchiveEntry:** `clear_colour`, `commit`, `get_wiretap_node_id`, `get_wiretap_storage_id`
- **Read-only properties inherited from PyFlameObject:** `attributes`, `parent`
