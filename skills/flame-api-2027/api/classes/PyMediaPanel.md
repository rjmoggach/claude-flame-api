# class `flame.PyMediaPanel`

This class represents the Media Panel.

**Method resolution order:** PyMediaPanel

> Cannot be instantiated from Python (obtained from other API objects).

## Methods

### `copy`

```python
copy( (PyMediaPanel)arg1, (object)source_entries, (object)destination [, (str)duplicate_action='add']) -> object
```

Copy a PyObject or a list of PyObjects from the Media Panel to a destination inside the Media Panel.Return a list of the copied PyObjects.Keyword arguments:

source_entries -- The PyObject or list of PyObjects to copy.

destination -- The PyObject that acts as destination.

duplicate_action -- Action to take when finding an object with the same name (add or replace).

### `move`

```python
move( (PyMediaPanel)arg1, (object)source_entries, (object)destination [, (str)duplicate_action='add']) -> object
```

Move a PyObject or a list of PyObjects from the Media Panel to a destination inside the Media Panel.

Return a list of the moved PyObjects.

Keyword arguments:

source_entries -- The PyObject or list of PyObjects to move.

destination -- The PyObject that acts as destination.

duplicate_action -- Action to take when finding an object with the same name (add or replace).

## Properties (data descriptors)

### `dual`

The dual view status of the Media Panel.

### `full_height`

The full height status of the Media Panel.

### `full_width`

The full width status of the Media Panel.

### `selected_entries`

A list of PyObject currently selected.

### `visible`

The visible status of the Media Panel.
