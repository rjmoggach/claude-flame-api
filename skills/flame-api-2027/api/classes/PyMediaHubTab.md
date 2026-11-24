# class `flame.PyMediaHubTab`

This class represents a MediaHub tab.

**Method resolution order:** PyMediaHubTab

> Cannot be instantiated from Python (obtained from other API objects).

## Methods

### `get_path`

```python
get_path( (PyMediaHubTab)arg1) -> str
```

Return the MediaHub tab current path.

### `set_path`

```python
set_path( (PyMediaHubTab)arg1, (str)arg2 [, (bool)allow_partial_success=False]) -> bool
```

Set the MediaHub tab current path. If allow_partial_success is True, the path will be set to the last valid folder in the path.

## Attributes (documented values)

Source: "PyMediaHubTab" help page. Access via `obj.<attr>`; most return a `PyAttribute` — use `.get_value()` / `.set_value()` (see PyAttribute.md).

Base object for manipulating tabs in the **MediaHub** module. This class provides common functionality for navigating and managing different types of **MediaHub** tabs, such as **Files** or **Archives** browser interfaces.

---

### PyMediaHubTab Methods

| Command | Description |
|---|---|
| `get_path` | Retrieve the current file system path or location of the tab. |
| `set_path` | Set the current path of the tab. Returns `True` if successful. |

---

### Examples

#### Set/Get the Path of the Files Tab

Print and change the current path of the **Files** tab of the **MediaHub** module.

`python
import flame
print("Current path is %s" % flame.mediahub.files.get_path())
flame.mediahub.files.set_path("/Volumes/External Storage/")
`

#### Set/Get the Path of the Archives Tab

Print and change the current path of the **Archives** tab of the **MediaHub** module.

`python
import flame
print("Current path is %s" % flame.mediahub.archives.get_path())
flame.mediahub.archives.set_path("/Volumes/External Storage/")
`
