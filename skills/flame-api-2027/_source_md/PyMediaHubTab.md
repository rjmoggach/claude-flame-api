<!-- source: Autodesk Flame Family 2027 Help _ PyMediaHubTab _ Autodesk.html -->
# PyMediaHubTab

Base object for manipulating tabs in the **MediaHub** module. This class provides common functionality for navigating and managing different types of **MediaHub** tabs, such as **Files** or **Archives** browser interfaces.

---

## PyMediaHubTab Methods

| Command | Description |
|---|---|
| `get_path` | Retrieve the current file system path or location of the tab. |
| `set_path` | Set the current path of the tab. Returns `True` if successful. |

---

## Examples

### Set/Get the Path of the Files Tab

Print and change the current path of the **Files** tab of the **MediaHub** module.

`python
import flame
print("Current path is %s" % flame.mediahub.files.get_path())
flame.mediahub.files.set_path("/Volumes/External Storage/")
`

### Set/Get the Path of the Archives Tab

Print and change the current path of the **Archives** tab of the **MediaHub** module.

`python
import flame
print("Current path is %s" % flame.mediahub.archives.get_path())
flame.mediahub.archives.set_path("/Volumes/External Storage/")
`

## Related pages

- Autodesk Flame Python: flame module
- PyMediaHub Attributes
- PyMediaHubFilesTab
