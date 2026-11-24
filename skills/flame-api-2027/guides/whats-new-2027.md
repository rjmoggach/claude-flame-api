> Source: Python API (section "What's New in 2027") — Autodesk Flame Family 2027 Help

# What's New in the Flame 2027 Python API

Every addition, rename, deprecation and reminder listed under "What's New in 2027" on the Python API page, organised by class. Descriptions are carried over from the source; argument lists were turned into bullets. Code examples are verbatim.

Notation: `<PyClip>` etc. is the source's shorthand for "an instance of that class" (see [constants.md](constants.md) for how to obtain each object). It is not valid Python; replace it with a real object.

> **Agent note — coverage gap in the class reference.** Most members on this page are **not** present in the generated class reference under `../api/classes/` (which was built from the `flame` module page). Absent there at time of writing: `flame.clear_graphics_memory`, `flame.clear_unreferenced_cache`, every `get_metadata` / `get_tokenized_metadata` / `set_metadata_*` method, `PyAudioTrack.stereo_merge`, `PyMarker.clear_annotations` / `has_annotations`, all of the `PyNode` members below, `PyRenderNode` / `PyWriteFileNode` `basic_metadata*`, the `timewarp_speed` argument of `PySegment.create_unlinked_segment`, `PyTimelineFX.output_channel_as_metadata_key`, and there are no class files at all for `PyMetadataNode`, `PyMetadataTimelineFX` or `PyNodeMarker`. Treat this page as the only source for those. Members that *are* in the class reference are marked "(in class ref)".

## Contents

- [Summary of changes](#summary-of-changes)
- [Global functions (`flame` module)](#global-functions-flame-module)
- [PyActionFamilyNode](#pyactionfamilynode)
- [PyAudioTrack](#pyaudiotrack)
- [PyBatch](#pybatch)
- [PyClip](#pyclip)
- [PyClipNode](#pyclipnode)
- [PyMarker](#pymarker)
- [PyMetadataNode](#pymetadatanode)
- [PyMetadataTimelineFX](#pymetadatatimelinefx)
- [PyNode](#pynode)
- [PyNodeMarker](#pynodemarker)
- [PyRenderNode](#pyrendernode)
- [PySegment](#pysegment)
- [PyTimelineFX](#pytimelinefx)
- [PyTypeNode and PyTypeTimelineFX](#pytypenode-and-pytypetimelinefx)
- [PyWriteFileNode](#pywritefilenode)
- [The metadata API in 2027](#the-metadata-api-in-2027-cross-class-agent-notes)
- [Source ambiguities](#source-ambiguities)

## Summary of changes

### Renamed (old name deprecated)

| New name | Old (deprecated) name |
|---|---|
| `flame.clear_graphics_memory()` | `flame.flush_graphics_memory()` |
| `<PyClip>.clear_cache_media()` | `<PyClip>.flush_cache_media()` |
| `<PyClip>.clear_renders()` | `<PyClip>.flush_renders()` |
| `<PyTimelineFX>.clear_maps_cache_media()` | `<PyTimelineFX>.flush_maps_cache_media()` |

### Deprecated (no replacement)

| Member | Reason given |
|---|---|
| `<PyRenderNode>.format` | Corresponding option no longer available in the **Render** node UI. |
| `<PyWriteFileNode>.format` | Corresponding option no longer available in the **Write File** node UI. |

### New / changed members (one line each)

| Class | Member | Kind |
|---|---|---|
| `flame` | `clear_unreferenced_cache()` | Function (new) |
| `PyActionFamilyNode` | `get_metadata()` | Function |
| `PyAudioTrack` | `stereo_merge()` | Function |
| `PyBatch` | `create_node("Metadata")` | Reminder (not new) |
| `PyClip` | `get_metadata()`, `update_sources()` | Function |
| `PyClip` | `tape_name`, `version_uids`, `version_uid` | Read-only property |
| `PyClip` | `VersionSelectionMode` (`KEEP_SELECTED_VERSION`, `SELECT_CURRENT_VERSION`, `SELECT_LATEST_VERSION`) | Enumeration |
| `PyClipNode` | `get_metadata()`, `get_tokenized_metadata()`, `set_metadata_discarded()`, `set_metadata_key()`, `set_metadata_value()` | Function |
| `PyMarker` | `clear_annotations()` | Function |
| `PyMarker` | `has_annotations` | Read-only property |
| `PyMetadataNode` | `get_metadata()`, `get_tokenized_metadata()`, `load_node_setup()`, `set_metadata_discarded()`, `set_metadata_key()`, `set_metadata_value()` | Function |
| `PyMetadataTimelineFX` | `get_metadata()`, `get_tokenized_metadata()`, `load_setup()`, `set_metadata_discarded()`, `set_metadata_key()`, `set_metadata_value()` | Function |
| `PyNode` | `create_marker()`, `get_metadata()`, `output_channel_as_metadata_key()`, `set_expression()`, `get_expression()`, `clear_expression()`, `bake_expression()` | Function |
| `PyNode` | `markers` | Read-only property |
| `PyNodeMarker` | `clear_annotations()` | Function |
| `PyNodeMarker` | `has_annotations` | Read-only property |
| `PyNodeMarker` | `name`, `tokenized_name`, `dynamic_name`, `comment`, `tokenized_comment`, `dynamic_comment`, `location`, `duration`, `colour`, `colour_label`, `locked_location`, `selected` | Attribute |
| `PyRenderNode` | `basic_metadata`, `basic_metadata_input` | Attribute |
| `PyRenderNode` | `get_metadata()`, `get_tokenized_metadata()`, `set_metadata_discarded()`, `set_metadata_key()`, `set_metadata_value()` | Function |
| `PySegment` | `create_effect("Source Metadata")` | Reminder (not new) |
| `PySegment` | `create_unlinked_segment(timewarp_speed=...)` | New argument |
| `PySegment` | `get_metadata()` | Function |
| `PyTimelineFX` | `output_channel_as_metadata_key()` | Function |
| `PyTypeNode` / `PyTypeTimelineFX` | `show_char_axis`, `show_char_pos`, `show_layer_axis`, `show_para_axis` | Attribute |
| `PyWriteFileNode` | `basic_metadata`, `basic_metadata_input` | Attribute |
| `PyWriteFileNode` | `get_metadata()`, `get_tokenized_metadata()`, `set_metadata_discarded()`, `set_metadata_key()`, `set_metadata_value()` | Function |

---

## Global functions (`flame` module)

Reference: [../api/flame-module-functions.md](../api/flame-module-functions.md) (neither function below is listed there).

| Command | Type | Description |
|---|---|---|
| `flame.clear_graphics_memory()` | Function | `flame.flush_graphics_memory()` has been renamed and deprecated. |
| `flame.clear_unreferenced_cache()` | Function | Clear cached media that is no longer referenced by any clip in either the current project or any other project. The `all_projects` parameter can be set to `True` to clear unreferenced cache in all available projects. |

### Examples

```python
# Reclaim space used by unreferenced cache in current project (cache of deleted clips)
flame.clear_unreferenced_cache()
```

```python
# Reclaim space used by unreferenced cache in all projects (cache of deleted clips)
flame.clear_unreferenced_cache(all_projects=True)
```

---

## PyActionFamilyNode

Class reference: [../api/classes/PyActionFamilyNode.md](../api/classes/PyActionFamilyNode.md)

| Command | Type | Description |
|---|---|---|
| `<PyActionFamilyNode>.get_metadata()` | Function | Used to get information about the metadata keys of an Action node or one of its inputs. |

Three optional arguments can be passed:
- `socket_name`: The socket from which to pull the metadata. The default output is used when no socket name is specified.
- `key`: The name of the key to get the value from. All metadata values are returned when no key name is specified.
- `frame`: The metadata value at a specific frame. If not specified, the current frame is used.

Note (source): The functions listed in the [PyNode](#pynode) section are also available on a `PyActionFamilyNode` object.

### Examples

```python
# Get all the metadata keys and values of a new PyAction node. If no socket is defined, the Result socket of the current Output is used.
action = flame.batch.create_node("Action")
print(action.get_metadata())
```

```python
# Get all the metadata keys and values of a media layer.
print(action.get_metadata("media1"))
```

(The second example reuses the `action` variable from the first.)

---

## PyAudioTrack

Class reference: [../api/classes/PyAudioTrack.md](../api/classes/PyAudioTrack.md)

| Command | Type | Description |
|---|---|---|
| `<PyAudioTrack>.stereo_merge()` | Function | Used to convert two mono audio tracks with the same editorial structure into a single stereo audio track. |

It is mandatory to pass a second `PyAudioTrack` object as an argument:
- `right_channel`: The `PyAudioTrack` to be used for the right channel.

No example is given in the source.

---

## PyBatch

Class reference: [../api/classes/PyBatch.md](../api/classes/PyBatch.md)

`<PyBatch>.create_node()` is not new, but serves as a reminder of how to create a Metadata node in Batch.

| Command | Type | Description |
|---|---|---|
| `<PyBatch>.create_node()` (in class ref) | Function | Used to create a Metadata node. |

### Examples

```python
# Create a Metadata node in the current Batch Group.
flame.batch.create_node("Metadata")
```

---

## PyClip

Class reference: [../api/classes/PyClip.md](../api/classes/PyClip.md)

| Command | Type | Description |
|---|---|---|
| `<PyClip>.clear_cache_media()` (in class ref) | Function | `<PyClip>.flush_cache_media()` has been renamed and deprecated. |
| `<PyClip>.clear_renders()` (in class ref) | Function | `<PyClip>.flush_renders()` has been renamed and deprecated. |
| `<PyClip>.get_metadata()` | Function | Used to get information about the metadata keys of a Clip. See arguments below. |
| `<PyClip>.tape_name` (in class ref) | Read-Only Property | Used to get the clip's tape name. |
| `<PyClip>.update_sources` | Function | Used to update the clip external sources. See arguments below. |
| `<PyClip>.VersionSelectionMode` (in class ref) | Enumeration | See values below. |
| `<PyClip>.version_uids` (in class ref) | Read-Only Property | Used to list the versions available for a source clip. Only available on single-segment clips. |
| `<PyClip>.version_uid` (in class ref) | Read-Only Property | Used to get the current version of a source clip. Only available on single-segment clips. |

`<PyClip>.get_metadata()` — two optional arguments can be passed:
- `key`: The name of the key to get the value from. All metadata values are returned when no key name is specified.
- `time`: The metadata value at a specific frame. Must be a `PyTime`. If not specified, the current frame is used.

`<PyClip>.update_sources()` — an optional argument can be passed:
- `version_selection_mode`: Change the currently selected version if defined. Possible values are:
  - `PyClip.KEEP_SELECTED_VERSION` — Default
  - `PyClip.SELECT_CURRENT_VERSION`
  - `PyClip.SELECT_LATEST_VERSION`

  See `<PyClip>.VersionSelectionMode` for more details.

`<PyClip>.VersionSelectionMode` (Enumeration):

| Value | Meaning |
|---|---|
| `PyClip.KEEP_SELECTED_VERSION` | Keep the currently selected version. |
| `PyClip.SELECT_CURRENT_VERSION` | Select the version defined in the source file. |
| `PyClip.SELECT_LATEST_VERSION` | Select the latest version available in the source. |

> Agent note: the class reference lists this method under the heading `update-sources` (with a hyphen) and signature `update-sources( (PyClip)version_selection_mode) -> VersionSelectionMode`; the Python identifier used in every example on this page is `update_sources`. A hyphen is not valid in a Python identifier, so use `update_sources`. The example below uses bare `PyClip.SELECT_LATEST_VERSION`, which assumes `PyClip` is in scope (e.g. `from flame import PyClip`); with only `import flame`, write `flame.PyClip.SELECT_LATEST_VERSION`. The source does not show either import.

### Example

```python
# Import a file sequence to a reel

# Define a destination for the import
wksp = flame.projects.current_project.current_workspace
reel_group = wksp.desktop.create_reel_group("Clip Update Sources Test")
reel = reel_group.create_reel("Clips", True)

# Import the clip defined by the scan pattern to the destination reel.
clips = flame.import_clips("/myStorage/myClip.[001-100].dpx", reel)
```

```python
# Import a clip based on browsing pattern and refresh its versions.

# In this example, the clip would have the following media files:
#
#  /myStorage/MyClipName_V01.001.dpx ... /myStorage/MyClipName_V01.010.dpx
#  /myStorage/MyClipName_V02.001.dpx ... /myStorage/MyClipName_V02.010.dpx
#
# Thus, a clip with 2 versions of 10 frames each.
media_path = "/myStorage/"
scan_pattern = "{name}_V{version}.{frame}.{extension}"

# Define a destination for the import
wksp = flame.projects.current_project.current_workspace
reel_group = wksp.desktop.create_reel_group("Clip Update Sources Test")
reel = reel_group.create_reel("Clips", True)

# Import the clip defined by the scan pattern to the destination reel.
clips = flame.import_clips(media_path + "/" + scan_pattern, reel)

# The pattern, as defined, could match multiple clips since {name} is
# not bounded; only keep the first one.
clip = clips[0]

# If a new version were to be added under the following files:
#
#  /myStorage/MyClipName_V03.001.dpx ... /myStorage/MyClipName_V03.010.dpx
#
# The clip can be updated to show the new version.
clip.update_sources()

# The currently selected version would be kept, but a new Version 3 would
# be available. To automatically select the newest version, an
# optional argument can be specified.
clip.update_sources(PyClip.SELECT_LATEST_VERSION)

# When pointing to an Open Clip instead of a pattern browsed clip, the
# current version, as specified in the Open Clip, can be selected.
clip.update_sources(PyClip.SELECT_CURRENT_VERSION)
```

---

## PyClipNode

Class reference: [../api/classes/PyClipNode.md](../api/classes/PyClipNode.md)

| Command | Type | Description |
|---|---|---|
| `<PyClipNode>.get_metadata()` | Function | Used to get information about the metadata keys of a Clip node. |
| `<PyClipNode>.get_tokenized_metadata()` | Function | Used to get information about the metadata keys of a Clip without resolving tokens. |
| `<PyClipNode>.set_metadata_discarded()` | Function | Used to enable or disable the discard status of a key in a Clip node. |
| `<PyClipNode>.set_metadata_key()` | Function | Used to set the name of a metadata key in a Clip node. |
| `<PyClipNode>.set_metadata_value()` | Function | Used to set the value of a metadata key in a Clip node. |

Arguments:

- `get_metadata()` — three optional arguments:
  - `socket_name`: The socket from which to pull the metadata. The default output is used when no socket name is specified.
  - `key`: The name of the key to get the value from. All metadata values are returned when no key name is specified.
  - `frame`: The metadata value at a specific frame. If not specified, the current frame is used.
- `get_tokenized_metadata()` — two optional arguments (as listed in the source; note `socket_name` is not listed here although `get_metadata()` has it):
  - `key`: The name of the key to get the value from. All metadata values are returned when no key name is specified.
  - `frame`: The metadata value at a specific frame. If not specified, the current frame is used.
- `set_metadata_discarded()` — two mandatory and one optional arguments:
  - `socket_name` (optional): The socket on which the discarded status of a metadata key must be changed. The default output is used when no socket name is specified.
  - `key` (mandatory): The name of the metadata key to be discarded or restored.
  - `discarded` (mandatory): `True`: Discard the key from the node metadata output. `False`: Restore the key.
- `set_metadata_key()` — one mandatory and two optional arguments:
  - `socket_name` (optional): The output socket on which to change the name of the key. The default output is used when no socket name is specified.
  - `key` (mandatory): The metadata key to rename.
  - `name` (optional): The new name for the specified key. If `None` is specified, the current value will revert to the original value.
- `set_metadata_value()` — two mandatory and one optional arguments:
  - `socket_name` (optional): The output socket on which to set the metadata. The default output is used when no socket name is specified.
  - `key` (mandatory): The metadata key to be modified or added.
  - `value` (mandatory): The metadata value to be set or edited for the specified key. If `None` is specified, the current value will revert to the original value.

Note (source): The functions listed in the [PyNode](#pynode) section are also available on a `PyClipNode` object.

### Example

```python
# Get all the metadata keys and values of a Clip node.
print(<PyClipNode>.get_metadata())
```

```python
# Get all the metadata keys and values for a specific channel of a Multi-Channel Clip node.
print(<PyClipNode>.get_metadata("albedo"))
```

```python
# Get the value for a specific key of a Clip node.
# The first argument is the socket_name, the second one is the key.
print(<PyClipNode>.get_metadata("Default", "focus"))
```

```python
# Edit the name of a metadata key (string) of a Clip node.
# The first argument is the socket_name, the second one is the name of the key, and the third one is the new name for that key.
<PyClipNode>.set_metadata_key("Default", "key name", "modified key name")
```

```python
# Restore the name of a renamed key in a Clip node.
# The first argument is the socket_name, the second one is the key, and the third one is discarded or can be set to None.
<PyClipNode>.set_metadata_key("Default", "key name")

<PyClipNode>.set_metadata_key("Default", "key name", None)
```

```python
# Edit the metadata value (string) of a Clip node.
# The first argument is the socket_name, the second one is the key, and the third one is the value.
<PyClipNode>.set_metadata_value("Default", "focus", "100")
```

```python
# Edit the metadata value (integer) of a Clip node.
# The first argument is the socket_name, the second one is the key, and the third one is the value.
<PyClipNode>.set_metadata_value("Default", "focus", 100)
```

```python
# Edit the metadata value (float) of a Clip node.
# The first argument is the socket_name, the second one is the key, and the third one is the value.
<PyClipNode>.set_metadata_value("Default", "focus", 100.12)
```

```python
# Edit the metadata value in the channel of a Multi-Channel Clip node.
# The first argument is the socket_name, the second one is the key, and the third one is the value.
<PyClipNode>.set_metadata_value("albedo", "CameraFOV", 100.12)
```

```python
# Reset the value of key in Clip node.
# The first argument is the socket_name, the second one is the key, and the third one is the value.
# When value is set to None, the original value is restored.
<PyClipNode>.set_metadata_value("Default", "focus", None)
```

```python
# Add a new key and set its value in the metadata of a Clip node.
# The first argument is the socket_name, the second one is the key, and the third one is the value.
<PyClipNode>.set_metadata_value("Default", "Application", "Flame")
```

```python
# Delete an added key in a Clip node.
# The first argument is the socket_name, the second one is the key, and the third one is the value.
# The value must be set to None for the key to be deleted.
<PyClipNode>.set_metadata_value("Default", "Application", None)
```

```python
# Set the Discard status for a key in a Clip node.
# The first argument is the socket_name, the second one is the key, and the third one is discarded.
<PyClipNode>.set_metadata_discarded("Default", "focus", True)
```

```python
# Restore a discarded key in a Clip node
# The first argument is the socket_name, the second one is the key, and the third one is discarded.
<PyClipNode>.set_metadata_discarded("Default", "focus", False)
```

---

## PyMarker

Class reference: [../api/classes/PyMarker.md](../api/classes/PyMarker.md)

| Command | Type | Description |
|---|---|---|
| `<PyMarker>.clear_annotations()` | Function | Used to clear all annotations from a marker. |
| `<PyMarker>.has_annotations` | Read-Only Property | Indicates whether a marker has annotations. |

### Examples

```python
# Find which Markers have annotations in the current Sequence.
for marker in flame.timeline.clip.markers:
    if marker.has_annotations:
       print(marker.name)
```

```python
# Clear all the annotations in a Sequence.
for marker in flame.timeline.clip.markers:
    if marker.has_annotations:
       marker.clear_annotations()
```

---

## PyMetadataNode

Class reference: none — there is no `PyMetadataNode.md` in `../api/classes/`. A Metadata node is created with `flame.batch.create_node("Metadata")` (see [PyBatch](#pybatch)).

| Command | Type | Description |
|---|---|---|
| `<PyMetadataNode>.get_metadata()` | Function | Used to get information about the metadata keys of a Metadata node or one of its inputs. |
| `<PyMetadataNode>.get_tokenized_metadata()` | Function | Used to get information about the metadata keys of a Metadata node or one of its inputs without resolving tokens. |
| `<PyMetadataNode>.load_node_setup()` | Function | Used to load a setup in the Metadata node. |
| `<PyMetadataNode>.set_metadata_discarded()` | Function | Used to enable or disable the discard status of a key in a Metadata node. |
| `<PyMetadataNode>.set_metadata_key()` | Function | Used to set the name of a metadata key in a Metadata node. |
| `<PyMetadataNode>.set_metadata_value()` | Function | Used to set the value of a metadata key in a Metadata node. |

Arguments:

- `get_metadata()` and `get_tokenized_metadata()` — three optional arguments:
  - `socket_name`: The socket from which to pull the metadata. The default output is used when no socket name is specified.
  - `key`: The name of the key to get the value from. All metadata values are returned when no key name is specified.
  - `frame`: The metadata value at a specific frame. If not specified, the current frame is used.
- `load_node_setup()` — the complete path to the setup, including the file name, must be passed as an argument. The following arguments can also be set to `True` or `False` to apply modifications or discard keys when the setup is loaded. All arguments are set to `True` by default:
  - `edited_keys`
  - `discarded_keys`
  - `added_keys`
  - `replaced_keys`
- `set_metadata_discarded()` — two mandatory arguments:
  - `key` (mandatory): The metadata key to be discarded or restored.
  - `discarded` (mandatory): `True`: Discard the key from the node metadata output. `False`: Restore the key.
- `set_metadata_key()` — one mandatory and two optional arguments:
  - `socket_name` (optional): The output socket on which to change the name of the key.
  - `key` (mandatory): The metadata key to rename.
  - `name` (optional): The new name for the specified key. If `None` is specified, the current value will revert to the original value.
- `set_metadata_value()` — two mandatory arguments:
  - `key` (mandatory): The metadata key to be modified or added.
  - `value` (mandatory): The metadata value to be set or edited for the specified key. If `None` is specified, the current value will revert to the original value.

> Agent note (ambiguity): the table lists only `key`/`value` (and `key`/`discarded`) for `set_metadata_value()` / `set_metadata_discarded()`, but the examples below pass a socket name first (`"Default"`), e.g. `set_metadata_value("Default", "focus", "100")`. The example for `set_metadata_key` states the socket_name is "always Result or Default for a Metadata node". Using keyword arguments (`key=...`, `value=...`), as in the `set_metadata_key(key=..., name=...)` example, avoids depending on positional order.

### Examples

```python
# Get all the metadata keys and values of a Metadata node.
print(<PyMetadataNode>.get_metadata())
```

```python
# Get the value for a specific key in a Metadata node
# The first argument is the socket_name, the second one is the key.
print(<PyMetadataNode>.get_metadata("Default", "focus"))
```

```python
# Edit the name of a metadata key (string) in a Metadata node, without specifying an output socket.
# The first argument is the name of the key and the second one is the new name for that key.
<PyMetadataNode>.set_metadata_key(key="key name", name="new key name")
```

```python
# Restore the name of a renamed key in a Metadata node.
# The first argument is the socket_name (always Result or Default for a Metadata node), the second one is the key, and the third one is discarded or can be set to None.
<PyMetadataNode>.set_metadata_key("Result", "key name")

<PyMetadataNode>.set_metadata_key("Result", "key name", None)
```

```python
# Edit the metadata value (string) of a Metadata node.
# The first argument is the socket_name, the second one is the key, and the third one is the value.
<PyMetadataNode>.set_metadata_value("Default", "focus", "100")
```

```python
# Edit the metadata value (integer) of a Metadata node.
# The first argument is the socket_name, the second one is the key, and the third one is the value.
<PyMetadataNode>.set_metadata_value("Default", "focus", 100)
```

```python
# Edit the metadata value (float) of a Metadata node.
# The first argument is the socket_name, the second one is the key, and the third one is the value.
<PyMetadataNode>.set_metadata_value("Default", "focus", 100.12)
```

```python
# Reset the value of key in a Metadata node.
# The first argument is the socket_name, the second one is the key, and the third one is the value.
# When value is set to None, the original value is restored.
<PyMetadataNode>.set_metadata_value("Default", "focus", None)
```

```python
# Add a new key and set its value in the metadata of a Metadata node.
# The first argument is the socket_name, the second one is the key, and the third one is the value.
<PyMetadataNode>.set_metadata_value("Default", "Application", "Flame")
```

```python
# Delete an added key in a Metadata node.
# The first argument is the socket_name, the second one is the key, and the third one is the value.
# The value must be set to None for the key to be deleted.
<PyMetadataNode>.set_metadata_value("Default", "Application", None)
```

```python
# Set the Discard status for a key in a Metadata node.
# The first argument is the socket_name, the second one is the key, and the third one is discarded.
<PyMetadataNode>.set_metadata_discarded("Default", "focus", True)
```

```python
# Restore a discarded key in a Metadata node.
# The first argument is the socket_name, the second one is the key, and the third one is discarded.
<PyMetadataNode>.set_metadata_discarded("Default", "focus", False)
```

```python
# Load a setup in the Metadata node and only apply the added_keys.
<PyMetadataNode>.load_node_setup('/var/tmp/mysetup.metadata_node', edited_keys=False, discarded_keys=False, added_keys=True, replaced_keys=False)
```

---

## PyMetadataTimelineFX

Class reference: none — there is no `PyMetadataTimelineFX.md` in `../api/classes/`. Created on a segment with `<PySegment>.create_effect("Source Metadata")` (see [PySegment](#pysegment)). Related: [../api/classes/PyTimelineFX.md](../api/classes/PyTimelineFX.md).

| Command | Type | Description |
|---|---|---|
| `<PyMetadataTimelineFX>.get_metadata()` | Function | Used to get information about the metadata keys of a Source Metadata Timeline FX. |
| `<PyMetadataTimelineFX>.get_tokenized_metadata()` | Function | Used to get information about the metadata keys of a Source Metadata Timeline FX without resolving tokens. |
| `<PyMetadataTimelineFX>.load_setup()` | Function | Used to load a setup in the Source Metadata Timeline FX. |
| `<PyMetadataTimelineFX>.set_metadata_discarded()` | Function | Used to enable or disable the discard status of a key in a Source Metadata Timeline FX. |
| `<PyMetadataTimelineFX>.set_metadata_key()` | Function | Used to set the name of a metadata key in a Metadata Timeline FX. |
| `<PyMetadataTimelineFX>.set_metadata_value()` | Function | Used to set the metadata value of a key in a Source Metadata Timeline FX. |

Arguments (no `socket_name` on this class):

- `get_metadata()` and `get_tokenized_metadata()` — two optional arguments:
  - `key`: The name of the key to get the value from. All metadata values are returned when no key name is specified.
  - `frame`: The metadata value at a specific frame, **relative to the segment's start**. If not specified, the current frame is used.
- `load_setup()` — the complete path to the setup, including the file name, must be passed as an argument. The following arguments can also be set to `True` or `False` to apply modifications or discard keys when the setup is loaded. All arguments are set to `True` by default:
  - `edited_keys`
  - `discarded_keys`
  - `added_keys`
  (no `replaced_keys`, unlike `PyMetadataNode.load_node_setup()`)
- `set_metadata_discarded()` — two mandatory arguments:
  - `key` (mandatory): The metadata key to be discarded or restored.
  - `discarded` (mandatory): `True`: Discard the key from the node metadata output. `False`: Restore the key.
- `set_metadata_key()` — one mandatory and one optional arguments:
  - `key` (mandatory): The metadata key to rename.
  - `name` (optional): The new name for the specified key. If `None` is specified, the current value will revert to the original value.
- `set_metadata_value()` — two mandatory arguments:
  - `key`: The metadata key to be modified or added.
  - `value`: The metadata value to be set or edited for the specified key. If `None` is specified, the current value will revert to the original value.

### Examples

```python
# Get all the metadata keys and values of a Source Metadata Timeline FX.
print(<PyMetadataTimelineFX>.get_metadata())
```

```python
# Get the value for a specific key in a Source Metadata Timeline FX.
# The argument is the key.
print(<PyMetadataTimelineFX>.get_metadata("focus"))
```

```python
# Edit the name of a metadata key (string) in a Source Metadata Timeline FX.
# The first argument is the name of the key and the second one is the new name for that key.
<PyMetadataTimelineFX>.set_metadata_key("key name", "new key name")
```

```python
# Restore the name of a renamed key in a Source Metadata Timeline FX.
# The first argument is the key and the second one is discarded or can be set to None.
<PyMetadataTimelineFX>.set_metadata_key("key name")

<PyMetadataTimelineFX>.set_metadata_key("key name", None)
```

```python
# Edit the metadata value (string) of a Source Metadata Timeline FX.
# The first argument is the key, and the second one is the value.
<PyMetadataTimelineFX>.set_metadata_value("focus", "100")
```

```python
# Edit the metadata value (integer) of a Source Metadata Timeline FX.
# The first argument is the key, and the second one is the value.
<PyMetadataTimelineFX>.set_metadata_value("focus", 100)
```

```python
# Edit the metadata value (float) of a Source Metadata Timeline FX.
# The first argument is the socket_name, the second one is the key, and the third one is the value.
<PyMetadataTimelineFX>.set_metadata_value("focus", 100.12)
```

(The comment in the float example above mentions `socket_name` and three arguments, but the call takes two — copied verbatim from the source.)

```python
# Reset the value of key in a Source Metadata Timeline FX.
# The first argument is the key, and the second one is the value.
# When value is set to None, the original value is restored.
<PyMetadataTimelineFX>.set_metadata_value("focus", None)
```

```python
# Add a new key and set its value in the metadata of a Source Metadata Timeline FX.
# The first argument is the key, and the second one is the value.
<PyMetadataTimelineFX>.set_metadata_value("Application", "Flame")
```

```python
# Delete an added key in a Source Metadata Timeline FX.
# The first argument is the key, and the second one is the value.
# The value must be set to None for the key to be deleted.
<PyMetadataTimelineFX>.set_metadata_value("Application", None)
```

```python
# Set the Discard status for a key in a Source Metadata Timeline FX.
# The first argument is the key, and the second one is discarded.
<PyMetadataTimelineFX>.set_metadata_discarded("focus", True)
```

```python
# Restore a discarded key in a Source Metadata Timeline FX.
# The first argument is the key, and the second one is discarded.
<PyMetadataTimelineFX>.set_metadata_discarded("focus", False)
```

```python
# Load a setup in the Metadata Timeline FX and only apply the edited_keys.
<PyMetadataTimelineFX>.load_setup('/var/tmp/mysetup.metadata_node', edited_keys=True, discarded_keys=False, added_keys=False)
```

---

## PyNode

Class reference: [../api/classes/PyNode.md](../api/classes/PyNode.md)

(The source HTML table for this section is malformed; it is reconstructed here without changing any text.)

| Command | Type | Description |
|---|---|---|
| `<PyNode>.create_marker()` | Function | Used to add a Marker to a Node. |
| `<PyNode>.get_metadata()` | Function | Used to get information about the metadata keys of a node or one of its inputs. |
| `<PyNode>.markers` | Read-Only Property | Used to get a list of markers on a node. |
| `<PyNode>.output_channel_as_metadata_key()` | Function | Used to output the content of a channel as a metadata key. |
| `<PyNode>.set_expression()` | Function | Used to set an expression on a channel. |
| `<PyNode>.get_expression()` | Function | Used to get the expression set on a channel. |
| `<PyNode>.clear_expression()` | Function | Used to clear the expression set on a channel. |
| `<PyNode>.bake_expression()` | Function | Used to bake the expression set on a channel into keyframes. |

Arguments:

- `create_marker()` — the following argument must be passed:
  - The frame at which the marker will be created. Must be an integer number representing the frame.
- `get_metadata()` — three optional arguments:
  - `socket_name`: The socket from which to pull the metadata. The default output is used when no socket name is specified.
  - `key`: The name of the key to get the value from. All metadata values are returned when no key name is specified.
  - `frame`: The metadata value at a specific frame. If not specified, the current frame is used.
- `output_channel_as_metadata_key()` — two arguments must be passed:
  - `channel_name`: The name of the channel to be exported. The inclusion of the node's name in the string is optional.
  - `enable`: Must be set to `True` or `False`. `True`: The content of the channel is exported as a metadata key. `False`: The content of the channel is no longer exported.
- `set_expression()` — two mandatory arguments:
  - `channel_name` (mandatory): The name of the channel to set the expression on.
  - `expression` (mandatory): The expression to set on the channel.
- `get_expression()` — one mandatory argument:
  - `channel_name` (mandatory): The name of the channel to get the expression from.
- `clear_expression()` — one mandatory argument:
  - `channel_name` (mandatory): The name of the channel to clear the expression from.
- `bake_expression()` — four mandatory arguments:
  - `channel_name` (mandatory): The name of the channel to bake the expression from.
  - `step` (mandatory): The step in frames between each baked keyframe.
  - `start` (mandatory): The first frame of the bake range.
  - `end` (mandatory): The last frame of the bake range.

`<PyNode>.markers` returns markers on a node; their attributes are listed under [PyNodeMarker](#pynodemarker) (the source does not explicitly state that `markers` returns `PyNodeMarker` objects, but this is the only node-marker class documented).

### Examples

```python
# Get all the metadata keys and values of a new PyNode node. If no socket is defined, the Result socket is used.
flip = flame.batch.create_node("Flip")
print(flip.get_metadata())
```

```python
# Output the content of the X Position channel of a 2D Transform node as a metadata key.
dd = flame.batch.create_node("2D Transform")
dd.output_channel_as_metadata_key("AxisTransform.Position.X", True)
```

```python
# Stop outputting the content of the X Position channel of a 2D Transform node as a metadata key.
flame.batch.current_node.output_channel_as_metadata_key("AxisTransform.Position.X", False)
```

Examples of how the `set_expression()` and `bake_expression()` functions can be used to propagate information in the metadata keys of a clip to parameters of a Camera object in an Action node are available in the `propagate_metadata_to_action_camera.py` file, located in `/opt/Autodesk/<application version>/python_utilities/examples`. (No expression example is given on the page itself.)

---

## PyNodeMarker

Class reference: none — there is no `PyNodeMarker.md` in `../api/classes/`.

| Command | Type | Description |
|---|---|---|
| `<PyNodeMarker>.clear_annotations()` | Function | Used to clear all annotations from a marker. |
| `<PyNodeMarker>.has_annotations` | Read-Only Property | Indicates whether a marker has annotations. |
| `<PyNodeMarker>.name` | Attribute | Used to get or set the Marker's name. A string must be passed as the argument when the name is set. |
| `<PyNodeMarker>.tokenized_name` | Attribute | Used to get or set the Marker's tokenized name. A string must be passed as the argument when the tokenized name is set. |
| `<PyNodeMarker>.dynamic_name` | Attribute | Used to get or set the status of the Dynamic option for the name. `True` or `False` must be passed as an argument when the status is set. |
| `<PyNodeMarker>.comment` | Attribute | Used to get or set the Marker's comment. A string must be passed as the argument when the comment is set. |
| `<PyNodeMarker>.tokenized_comment` | Attribute | Used to get or set the Marker's tokenized comment. A string must be passed as the argument when the tokenized comment is set. |
| `<PyNodeMarker>.dynamic_comment` | Attribute | Used to get or set the status of the Dynamic option for the comment. `True` or `False` must be passed as an argument when the status is set. |
| `<PyNodeMarker>.location` | Attribute | Used to get or set the Marker's location. An integer number representing a frame must be passed when the location is set. |
| `<PyNodeMarker>.duration` | Attribute | Used to get or set the Marker's duration. An integer number representing a duration must be passed when the duration is set. |
| `<PyNodeMarker>.colour` | Attribute | Used to get or set the Marker's colour. A tuple containing three float numbers representing the red, green, and blue values must be passed as an argument when the colour is set. |
| `<PyNodeMarker>.colour_label` | Attribute | Used to get or set the Marker's colour label. A string representing the name of a colour label must be passed as an argument when the colour is set. |
| `<PyNodeMarker>.locked_location` | Attribute | Used to get or set the status of the Marker's lock option. `True` or `False` must be passed as an argument when the status is set. |
| `<PyNodeMarker>.selected` | Attribute | Used to get or set the selection status of the Marker. `True` or `False` must be passed as an argument when the status is set. |

No example is given in the source.

---

## PyRenderNode

Class reference: [../api/classes/PyRenderNode.md](../api/classes/PyRenderNode.md)

| Command | Type | Description |
|---|---|---|
| `<PyRenderNode>.basic_metadata` | Attribute | Used to get or set the status of the Basic Metadata option. One of the following must be passed as the argument when the attribute is set: `Custom Values`, `Use Input Values`. |
| `<PyRenderNode>.basic_metadata_input` | Attribute | Used to get or set the status of the Basic Metadata Input option. One of the following must be passed as the argument when the attribute is set: `Use Front Input`, `Use Metadata Input`. |
| `<PyRenderNode>.get_metadata()` | Function | Used to get information about the metadata keys of a Render node. |
| `<PyRenderNode>.get_tokenized_metadata()` | Function | Used to get information about the metadata keys of a Render node without resolving tokens. |
| `<PyRenderNode>.set_metadata_discarded()` | Function | Used to enable or disable the discard status of a key in a Render node. |
| `<PyRenderNode>.set_metadata_key()` | Function | Used to set the name of a metadata key in a Render node. |
| `<PyRenderNode>.set_metadata_value()` | Function | Used to set the value of a metadata key in a Render node. |

> Agent note: the `basic_metadata` / `basic_metadata_input` values are given in the source as plain text (e.g. Custom Values); the source does not show quoting, but they are presumably passed as Python strings (`"Custom Values"`) like other UI option values in this API. Unverified.

Arguments:

- `get_metadata()` and `get_tokenized_metadata()` — three optional arguments:
  - `socket_name`: The socket from which to pull the metadata. The first output channel is used when no socket name is specified. Note that the name of the corresponding channel can be used in place of the socket name.
  - `key`: The name of the key to get the value from. All metadata values are returned when no key name is specified.
  - `frame`: The metadata value at a specific frame. If not specified, the current frame is used.
- `set_metadata_discarded()` — two mandatory and one optional arguments:
  - `socket_name` (optional): The channel on which the discarded status of a metadata key must be changed. The first input socket is used when no socket name is specified.
  - `key` (mandatory): The metadata key to be discarded or restored.
  - `discarded` (mandatory): `True`: Discard the key from the node metadata output. `False`: Restore the key.
- `set_metadata_key()` — one mandatory and one optional arguments (as stated; three parameters are listed):
  - `socket_name` (optional): The output channel on which to change the name of the key. The first channel is used when no channel name is specified.
  - `key` (mandatory): The metadata key to rename.
  - `name` (optional): The new name for the specified key. If `None` is specified, the current value will revert to the original value.
- `set_metadata_value()` — two mandatory and one optional arguments:
  - `socket_name` (optional): The output channel on which to set the metadata. The first channel is used when no channel name is specified.
  - `key` (mandatory): The metadata key to be modified or added.
  - `value` (mandatory): The metadata value to be set or edited for the specified key. If `None` is specified, the current value will revert to the original value.

### Examples

```python
# Get all the metadata keys and values of a Render node.
print(<PyRenderNode>.get_metadata())
```

```python
# Get the value for a specific key in a Render node.
# The first argument is the socket_name, the second one is the key.
print(<PyRenderNode>.get_metadata("Default", "focus"))
```

```python
# Edit the name of a metadata key (string) in a Render node.
# The first argument is the socket_name (a channel name or Default for a Render node), the second one is the key, and the third one is the new name for that key.
<PyRenderNode>.set_metadata_key("channel name", "key name", "new key name")
```

```python
# Restore the name of a renamed key in a Render node.
# The first argument is the socket_name (a channel name for a Render node), the second one is the key, and the third one is discarded or can be set to None.
<PyRenderNode>.set_metadata_key("channel name", "key name")

<PyRenderNode>.set_metadata_key("channel name", "key name", None)
```

```python
# Edit the metadata value (string) of a Render node.
# The first argument is the socket_name, the second one is the key, and the third one is the value.
<PyRenderNode>.set_metadata_value("Default", "focus", 100)
```

(Verbatim from source: the "(string)" example above passes the integer `100`; the Clip node / Metadata node / Write File node equivalents pass the string `"100"`.)

```python
# Edit the metadata value (integer) of a Render node.
# The first argument is the socket_name, the second one is the key, and the third one is the value.
<PyRenderNode>.set_metadata_value("Default", "focus", 100)
```

```python
# Edit the metadata value (float) of a Render node.
# The first argument is the socket_name, the second one is the key, and the third one is the value.
<PyRenderNode>.set_metadata_value("Default", "focus", 100.12)
```

```python
# Reset the value of key in a Render node.
# The first argument is the socket_name, the second one is the key, and the third one is the value.
# When value is set to None, the original value is restored.
<PyRenderNode>.set_metadata_value("Default", "focus", None)
```

```python
# Add a new key and set its value in the metadata of a Render node.
# The first argument is the socket_name, the second one is the key, and the third one is the value.
<PyRenderNode>.set_metadata_value("Default", "Application", "Flame")
```

```python
# Delete an added key in a Render node.
# The first argument is the socket_name, the second one is the key, and the third one is the value.
# The value must be set to None for the key to be deleted.
<PyRenderNode>.set_metadata_value("Default", "Application", None)
```

```python
# Set the Discard status for a key in a Render node.
# The first argument is the socket_name, the second one is the key, and the third one is discarded.
<PyRenderNode>.set_metadata_discarded("Default", "focus", True)
```

```python
# Restore a discarded key in a Render node.
# The first argument is the socket_name, the second one is the key, and the third one is discarded.
<PyRenderNode>.set_metadata_discarded("Default", "focus", False)
```

### Deprecated

The `<PyRenderNode>.format` attribute has been deprecated since its corresponding option inside the **Render** node user interface is no longer available.

---

## PySegment

Class reference: [../api/classes/PySegment.md](../api/classes/PySegment.md)

`<PySegment>.create_effect()` is not new, but serves as a reminder of how to create a Source Metadata Timeline FX on a Timeline Segment.

| Command | Type | Description |
|---|---|---|
| `<PySegment>.create_effect()` (in class ref) | Function | Used to create a Metadata Source Timeline FX. |
| `<PySegment>.create_unlinked_segment()` (in class ref, without the new argument) | Function | The `timewarp_speed` argument has been added to `create_unlinked_segment` function. Use the `timewarp_speed` argument to create a Timewarp Timeline FX on the segment created from a Gap. The speed can be a float or integer value and can be a negative value, zero, or a positive value. The head value remains the first frame of the segment with any of the timewarp values. |
| `<PySegment>.get_metadata()` | Function | Used to get information about the metadata keys of a timeline segment. |

`<PySegment>.get_metadata()` — two optional arguments:
- `key`: The name of the key to get the value from. All metadata values are returned when no key name is specified.
- `time`: The metadata value at a specific frame. Must be a `PyTime`. If not specified, the timeline segment's start frame is used.

> Agent note: the effect type string used in the example is `"Source Metadata"` (the table calls it "Metadata Source Timeline FX"; use the string from the code). `create_unlinked_segment()` replaces a **gap** segment (class reference: "Replace the gap with an unlinked source media segment"), so `flame.timeline.current_segment` must be a gap in the example below. The example `timewarp_speed=50.0` is commented as "50%", i.e. the value is a percentage.

### Examples

```python
# Create a Source Metadata Timeline FX on the selected segment.
flame.timeline.current_segment.create_effect("Source Metadata")
```

```python
# Turn a gap into a timeline segment with a Timewarp Timeline FX of 50% on it.
flame.timeline.current_segment.create_unlinked_segment(timewarp_speed=50.0)
```

---

## PyTimelineFX

Class reference: [../api/classes/PyTimelineFX.md](../api/classes/PyTimelineFX.md)

| Command | Type | Description |
|---|---|---|
| `<PyTimelineFX>.clear_maps_cache_media()` (in class ref) | Function | `<PyTimelineFX>.flush_maps_cache_media()` was renamed and deprecated. |
| `<PyTimelineFX>.output_channel_as_metadata_key()` | Function | Used to output the content of a channel as a metadata key. |

`output_channel_as_metadata_key()` — two arguments must be passed:
- `channel_name`: The name of the channel to be exported. The inclusion of the timeline fx's name in the string is optional.
- `enable`: Must be set to `True` or `False`. `True`: The content of the channel is exported as a metadata key. `False`: The content of the channel is no longer exported.

Note (source): The functions other than `create_marker()` and `get_metadata()` listed in the [PyNode](#pynode) section are also available on a `PyTimelineFX` object (i.e. `output_channel_as_metadata_key()`, `set_expression()`, `get_expression()`, `clear_expression()`, `bake_expression()`; `markers` is a property, and the note does not say whether it is included).

### Examples

```python
# Output the content of the X Position channel of a 2D Transform Timeline FX as a metadata key.
dd = flame.timeline.current_segment.create_effect("2D Transform")
dd.output_channel_as_metadata_key("AxisTransform.Position.X", True)
```

```python
# Stop outputting the content of the X Position channel of a 2D Transform Timeline FX as a metadata key.
flame.timeline.current_segment.effects[0].output_channel_as_metadata_key("AxisTransform.Position.X", False)
```

---

## PyTypeNode and PyTypeTimelineFX

Class references: [../api/classes/PyTypeNode.md](../api/classes/PyTypeNode.md), [../api/classes/PyTypeTimelineFX.md](../api/classes/PyTypeTimelineFX.md)

| Command | Type | Description |
|---|---|---|
| `<PyTypeNode>.show_char_axis` | Attribute | Used to get or set the status of Show Axis for the Characters Axis. One of the following must be passed as the argument when the attribute is set: `True`, `False`. |
| `<PyTypeNode>.show_char_pos` | Attribute | Used to get or set the status of Show Position for the Characters Axis. One of the following must be passed as the argument when the attribute is set: `True`, `False`. |
| `<PyTypeNode>.show_layer_axis` | Attribute | Used to get or set the status of Show Axis for the Layer Axis. One of the following must be passed as the argument when the attribute is set: `True`, `False`. |
| `<PyTypeNode>.show_para_axis` | Attribute | Used to get or set the status of Show Axis for the Paragraph Axis. One of the following must be passed as the argument when the attribute is set: `True`, `False`. |

Note (source): The functions other than `create_marker()` and `get_metadata()` listed in the [PyNode](#pynode) section are also available on `PyTypeNode` and `PyTypeTimelineFX` objects.

> Agent note: the heading covers both classes, but the table only shows `<PyTypeNode>.` prefixes; the source implies the same attributes exist on `PyTypeTimelineFX`. The four attributes appear in `PyTypeNode.md` in the class reference.

No example is given in the source.

---

## PyWriteFileNode

Class reference: [../api/classes/PyWriteFileNode.md](../api/classes/PyWriteFileNode.md) (`PyWriteFileNode` derives from `PyRenderNode`).

| Command | Type | Description |
|---|---|---|
| `<PyWriteFileNode>.basic_metadata` | Attribute | Used to get or set the status of the Basic Metadata option. One of the following must be passed as the argument when the attribute is set: `Custom Values`, `Use Input Values`. |
| `<PyWriteFileNode>.basic_metadata_input` | Attribute | Used to get or set the status of the Basic Metadata Input option. One of the following must be passed as the argument when the attribute is set: `Use Front Input`, `Use Metadata Input`. |
| `<PyWriteFileNode>.get_metadata()` | Function | Used to get information about the metadata keys of a Write File node. |
| `<PyWriteFileNode>.get_tokenized_metadata()` | Function | Used to get information about the metadata keys of a Write File node without resolving tokens. |
| `<PyWriteFileNode>.set_metadata_discarded()` | Function | Used to enable or disable the discard status of a key in a Write File node. |
| `<PyWriteFileNode>.set_metadata_key()` | Function | Used to set the name of a metadata key in a Write File node. |
| `<PyWriteFileNode>.set_metadata_value()` | Function | Used to set the value of a metadata key in a Write File node. |

Arguments:

- `get_metadata()` and `get_tokenized_metadata()` — three optional arguments:
  - `socket_name`: The socket from which to pull the metadata. The first output channel is used when no socket name is specified. Note that the name of the corresponding channel can be used in place of the socket name.
  - `key`: The name of the key to get the value from. All metadata values are returned when no key name is specified.
  - `frame`: The metadata value at a specific frame. If not specified, the current frame is used.
- `set_metadata_discarded()` — two mandatory and one optional arguments:
  - `socket_name` (optional): The channel on which the discarded status of a metadata key must be changed. The first channel is used when no socket name is specified.
  - `key` (mandatory): The metadata key to be discarded or restored.
  - `discarded` (mandatory): `True`: Discard the key from the node metadata output. `False`: Restore the key.
- `set_metadata_key()` — one mandatory and one optional arguments (as stated; three parameters are listed):
  - `socket_name` (optional): The output channel on which to change the name of the key. The first channel is used when no socket name is specified.
  - `key` (mandatory): The metadata key to rename.
  - `name` (optional): The new name for the specified key. If `None` is specified, the current value will revert to the original value.
- `set_metadata_value()` — two mandatory and one optional arguments:
  - `socket_name` (optional): The output channel on which to set the metadata. The first channel is used when no channel name is specified.
  - `key` (mandatory): The metadata key to be modified or added.
  - `value` (mandatory): The metadata value to be set or edited for the specified key. If `None` is specified, the current value will revert to the original value.

### Examples

```python
# Get all the metadata keys and values of a Write file node.
print(<PyWriteFileNode>.get_metadata())
```

```python
# Get the value for a specific key in a Write file node.
# The first argument is the socket_name, the second one is the key.
print(<PyWriteFileNode>.get_metadata("Default", "focus"))
```

```python
# Edit the name of a metadata key (string) in a Write File node.
# The first argument is the socket_name (a channel name or Default for a Write File node), the second one is the key, and the third one is the new name for that key.
<PyWriteFileNode>.set_metadata_key("channel name", "key name", "new key name")
```

```python
# Restore the name of a renamed key in a Write File node.
# The first argument is the socket_name (a channel name for a Write File node), the second one is the key, and the third one is discarded or can be set to None.
<PyWriteFileNode>.set_metadata_key("channel name", "key name")

<PyWriteFileNode>.set_metadata_key("channel name", "key name", None)
```

```python
# Edit the metadata value (string) of a Write file node.
# The first argument is the socket_name, the second one is the key, and the third one is the value.
<PyWriteFileNode>.set_metadata_value("Default", "focus", "100")
```

```python
# Edit the metadata value (integer) of a Write file node.
# The first argument is the socket_name, the second one is the key, and the third one is the value.
<PyWriteFileNode>.set_metadata_value("Default", "focus", 100)
```

```python
# Edit the metadata value (float) of a Write file node.
# The first argument is the socket_name, the second one is the key, and the third one is the value.
<PyWriteFileNode>.set_metadata_value("Default", "focus", 100.12)
```

```python
# Reset the value of key in a Write file node.
# The first argument is the socket_name, the second one is the key, and the third one is the value.
# When value is set to None, the original value is restored.
<PyWriteFileNode>.set_metadata_value("Default", "focus", None)
```

```python
# Add a new key and set its value in the metadata of a Write file node.
# The first argument is the socket_name, the second one is the key, and the third one is the value.
<PyWriteFileNode>.set_metadata_value("Default", "Application", "Flame")
```

```python
# Delete an added key in a Write file node.
# The first argument is the socket_name, the second one is the key, and the third one is the value.
# The value must be set to None for the key to be deleted.
<PyWriteFileNode>.set_metadata_value("Default", "Application", None)
```

```python
# Set the Discard status for a key in a Write file node.
# The first argument is the socket_name, the second one is the key, and the third one is discarded.
<PyWriteFileNode>.set_metadata_discarded("Default", "focus", True)
```

```python
# Restore a discarded key in a Write file node.
# The first argument is the socket_name, the second one is the key, and the third one is discarded.
<PyWriteFileNode>.set_metadata_discarded("Default", "focus", False)
```

### Deprecated

The `<PyWriteFileNode>.format` attribute has been deprecated since its corresponding option inside the **Write File** node user interface is no longer available.

---

## The metadata API in 2027 (cross-class agent notes)

Derived only from the sections above.

| Class | `get_metadata` args | Default when no socket | Has `get_tokenized_metadata` | Has `set_metadata_*` | Setup loader |
|---|---|---|---|---|---|
| `PyNode` (any node) | `socket_name`, `key`, `frame` | default output (Result socket per example) | no | no | — |
| `PyActionFamilyNode` | `socket_name`, `key`, `frame` | default output (Result socket of current Output per example) | no | no | — |
| `PyClipNode` | `socket_name`, `key`, `frame` | default output | yes (`key`, `frame`) | yes (`socket_name` optional first) | — |
| `PyMetadataNode` | `socket_name`, `key`, `frame` | default output | yes | yes | `load_node_setup(path, edited_keys, discarded_keys, added_keys, replaced_keys)` |
| `PyRenderNode` | `socket_name`, `key`, `frame` | first output channel | yes | yes (`socket_name` = channel name) | — |
| `PyWriteFileNode` | `socket_name`, `key`, `frame` | first output channel | yes | yes (`socket_name` = channel name) | — |
| `PyClip` | `key`, `time` (`PyTime`) | — | no | no | — |
| `PySegment` | `key`, `time` (`PyTime`) | — (default time = segment start frame) | no | no | — |
| `PyMetadataTimelineFX` | `key`, `frame` (relative to segment start) | — | yes | yes (no `socket_name`) | `load_setup(path, edited_keys, discarded_keys, added_keys)` |

Common semantics (as stated in the source):
- Omitting `key` returns all metadata values.
- `set_metadata_value(..., key, None)` restores an edited key's original value, and deletes a key that was added.
- `set_metadata_key(..., key)` or `set_metadata_key(..., key, None)` restores a renamed key's original name.
- `set_metadata_discarded(..., key, True)` discards the key from the node's metadata output; `False` restores it.
- Values can be strings, integers or floats (examples show `"100"`, `100`, `100.12`).
- Channels can be exposed as metadata keys with `output_channel_as_metadata_key(channel_name, enable)` on nodes and Timeline FX; channel names use dotted paths such as `"AxisTransform.Position.X"`.
- The return type of `get_metadata()` is not documented on this page (examples only `print()` it).

## Source ambiguities

- `PyNode` table is malformed in the source HTML (raw pipe text inside a `<p>`); reconstructed above with text unchanged.
- `PyMetadataNode.set_metadata_value()` / `set_metadata_discarded()` are described with two mandatory args (no `socket_name`) but every example passes a socket name first.
- `PyClipNode.get_tokenized_metadata()` lists only `key` and `frame` although its description mirrors `get_metadata()` which also takes `socket_name`.
- `PyRenderNode` "Edit the metadata value (string)" example passes integer `100`.
- `PyMetadataTimelineFX` float example comment refers to a `socket_name` argument that this class does not take.
- `PyRenderNode.set_metadata_discarded()` says the "first input socket" is the default, while other `PyRenderNode` methods say "first output channel"/"first channel".
- `PyClip.update_sources` appears without `()` in the table; the class reference spells it `update-sources`.
- The example using `PyClip.SELECT_LATEST_VERSION` does not show how `PyClip` was imported.
