# class `flame.PyLensDistortionNode`(PyNode)

Object representing a Lens Distortion node.

**Method resolution order:** PyLensDistortionNode → PyNode → PyFlameObject

## Methods

> Cannot be instantiated from Python (obtained from other API objects).

### `calculate`

```python
calculate( (PyLensDistortionNodearg1) -> None
```

Calculate the amount of distortion based on the position of vertices.

### `import_lens_distortion`

```python
import_lens_distortion( (PyLensDistortionNode(str)filename) -> None
```

Import a Lens Distortion file.

## Inherited members

- **Static methods inherited from PyNode:** `delete`, `duplicate`, `load_node_setup`, `save_node_setup`, `set_context`
- **Read-only properties inherited from PyNode:** `input_sockets`, `output_sockets`, `sockets`
- **Read-only properties inherited from PyFlameObject:** `attributes`, `parent`
