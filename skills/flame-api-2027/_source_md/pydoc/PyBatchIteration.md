# class `flame.PyBatchIteration`(PyArchiveEntry)

Class derived from PyArchiveEntry. This class represents a Batch Iteration.

**Method resolution order:** PyBatchIteration → PyArchiveEntry → PyFlameObject

## Methods

> Cannot be instantiated from Python (obtained from other API objects).

### `open_as_batch_group`

```python
open_as_batch_group( (PyBatchIteration)arg1 [, (bool)confirm=True]) -> bool
```

Open a Batch Iteration as a new Batch Group, adding it to PyDesktop.batch_groups. Can only be called from a Library.

## Read-only properties defined here

### `iteration_number`

Return the iteration number of the Batch Iteration.

## Inherited members

- **Static methods inherited from PyArchiveEntry:** `clear_colour`, `commit`, `get_wiretap_node_id`, `get_wiretap_storage_id`
- **Read-only properties inherited from PyFlameObject:** `attributes`, `parent`
