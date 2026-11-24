<!-- source: Autodesk Flame Family 2027 Help _ PyMediaHubFilesTab _ Autodesk.html -->
# PyMediaHubFilesTab

Object allowing manipulation of the **Files** tab of the **MediaHub** module. This class provides access to file system browsing capabilities and import/export options within the MediaHub interface.

---

## PyMediaHubFilesTab Attributes

| Property | Type | Description |
|---|---|---|
| `options` | PyMediaHubFilesTabOptions | Import options currently in use in the **Files** tab of the **MediaHub** module. |

See PyMediaHubTab for more attributes.

---

## PyMediaHubFilesTab Methods

See PyMediaHubTab for inherited methods.

---

## Examples

### Set/Get the Path of the Files Tab

Print and change the current path of the **Files** tab of the **MediaHub** module.

`python
import flame
print("Current path is %s" % flame.mediahub.files.get_path())
flame.mediahub.files.set_path("/Volumes/External Storage/")
`

### Enable Cache and Proxy

This will enable cache and proxy on import for the following imports done either through the application or by the Python API.

`python
import flame
flame.mediahub.files.options.cache_mode = True
flame.mediahub.files.options.proxy_mode = True
`

## Related pages

- Autodesk Flame Python: flame module
- PyMediaHub Attributes
- PyMediaHubTab
- PyMediaHubFilesTabOptions
