# class `flame.PyCoCameraAnalysis`(PyCoNode)

Class derived from PyCoNode. This class represents the camera analysis node in the Action schematic.

**Method resolution order:** PyCoCameraAnalysis → PyCoNode → PyFlameObject

## Methods

> Cannot be instantiated from Python (obtained from other API objects).

### `analyseRange`

```python
analyseRange( (PyCoCameraAnalysis)arg1, (object)arg2, (object)start) -> bool
```

Run the analysis for the given frame range using the first frame as a reference if none has been already set.

### `resetAnalysis`

```python
resetAnalysis( (PyCoCameraAnalysis)arg1) -> bool
```

Reset the current analysis.

## Inherited members

- **Static methods inherited from PyCoNode:** `add_reference`, `assign_media`, `cache_range`, `children`, `parents`
- **Read-only properties inherited from PyCoNode:** `type`
- **Read-only properties inherited from PyFlameObject:** `attributes`, `parent`
