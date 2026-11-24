<!-- source: Autodesk Flame Family 2027 Help _ Python API _ Autodesk.html -->
# Python API

The Flame Family Python API is a tool for Flame, Flare, and Flame Assist users looking to script workflows and automate tedious tasks.

The Python API is accessed via the Flame Python Console. This console provides a place to write and execute code while working in Flame.

The Flame module is the core of the Python API. This module contains everything needed to use the Flame Python API.

The Python API uses Python version 3.13.3, starting with Flame Family 2027.

- New to the Flame Python API?
- What's New in 2027

  - Global Functions

    - Examples

  - PyActionFamilyNode

    - Examples

  - PyAudioTrack
  - PyBatch

    - Examples

  - PyClip

    - Example

  - PyClipNode

    - Example

  - PyMarker

    - Examples

  - PyMetadataNode

    - Examples

  - PyMetadataTimelineFX

    - Examples

  - PyNode

    - Examples

  - PyNodeMarker
  - PyRenderNode

    - Examples
    - Deprecated

  - PySegment

    - Examples

  - PyTimelineFX

    - Examples

  - PyTypeNode and PyTypeTimelineFX
  - PyWriteFileNode

    - Examples
    - Deprecated

---

## New to the Flame Python API?

Write Your First Python API Script provides a small and basic example to get started.

The Flame API Code Samples contains code snippets that offer ideas on the structure of the API and how to use it. Examples of scripts can also be found in `/opt/Autodesk/<flame_version>/python_examples`.
 Note: Some functions and attributes may not be available in Flare or Flame Assist.

---

## What's New in 2027

### Global Functions

| Command | Type | Description |
|---|---|---|
| `flame.clear_graphics_memory()` | Function | `flame.flush_graphics_memory()` has been renamed and deprecated. |
| `flame.clear_unreferenced_cache()` | Function | Clear cached media that is no longer referenced by any clip in either the current project or any other project.<br><br>The all_projects parameter can be set to True to clear unreferenced cache in all available projects. |

#### Examples

`python
# Reclaim space used by unreferenced cache in current project (cache of deleted clips)
flame.clear_unreferenced_cache()
python
# Reclaim space used by unreferenced cache in all projects (cache of deleted clips)
flame.clear_unreferenced_cache(all_projects=True)
`

### PyActionFamilyNode

| Command | Type | Description |
|---|---|---|
| `<PyActionFamilyNode>.get_metadata()` | Function | Used to get information about the metadata keys of an Action node or one of its inputs. Three optional arguments can be passed: • socket_name: The socket from which to pull the metadata. The default output is used when no socket name is specified. • key: The name of the key to get the value from. All metadata values are returned when no key name is specified. • frame: The metadata value at a specific frame. If not specified, the current frame is used. |

 Note: The functions listed in the PyNode section are also available on a PyActionFamilyNode object.

#### Examples

`python
# Get all the metadata keys and values of a new PyAction node. If no socket is defined, the Result socket of the current Output is used.
action = flame.batch.create_node("Action")
print(action.get_metadata())
python
# Get all the metadata keys and values of a media layer.
print(action.get_metadata("media1"))
`

### PyAudioTrack

| Command | Type | Description |
|---|---|---|
| `<PyAudioTrack>.stereo_merge()` | Function | Used to convert two mono audio tracks with the same editorial structure into a single stereo audio track. It is mandatory to pass a second PyAudioTrack object as an argument: • right_channel: The PyAudioTrack to be used for the right channel. |

### PyBatch

`<PyBatch>.create_node()` is not new, but serves as a reminder of how to create a Metadata node in Batch.

| Command | Type | Description |
|---|---|---|
| `<PyBatch>.create_node()` | Function | Used to create a Metadata node. |

#### Examples

`python
# Create a Metadata node in the current Batch Group.
flame.batch.create_node("Metadata")
`

### PyClip

| Command | Type | Description |
|---|---|---|
| `<PyClip>.clear_cache_media()` | Function | `<PyClip>.flush_cache_media()` has been renamed and deprecated. |
| `<PyClip>.clear_renders()` | Function | `<PyClip>.flush_renders()` has been renamed and deprecated. |
| `<PyClip>.get_metadata()` | Function | Used to get information about the metadata keys of a Clip. Two optional arguments can be passed: • key: The name of the key to get the value from. All metadata values are returned when no key name is specified. • time: The metadata value at a specific frame. Must be a PyTime. If not specified, the current frame is used. |
| `<PyClip>.tape_name` | Read-Only Property | Used to get the clip's tape name. |
| `<PyClip>.update_sources` | Function | Used to update the clip external sources.<br><br>An optional argument can be passed • version_selection_mode: Change the currently selected version if defined. Possible values are: • PyClip.KEEP_SELECTED_VERSION - Default • PyClip.SELECT_CURRENT_VERSION • PyClip.SELECT_LATEST_VERSION See `<PyClip>.VersionSelectionMode` for more details. |
| `<PyClip>.VersionSelectionMode` | Enumeration | • PyClip.KEEP_SELECTED_VERSION<br><br>Keep the currently selected version. • PyClip.SELECT_CURRENT_VERSION<br><br>Select the version defined in the source file. • PyClip.SELECT_LATEST_VERSION<br><br>Select the latest version available in the source. |
| `<PyClip>.version_uids` | Read-Only Property | Used to list the versions available for a source clip. Only available on single-segment clips. |
| `<PyClip>.version_uid` | Read-Only Property | Used to get the current version of a source clip. Only available on single-segment clips. |

#### Example

`python
# Import a file sequence to a reel

# Define a destination for the import
wksp = flame.projects.current_project.current_workspace
reel_group = wksp.desktop.create_reel_group("Clip Update Sources Test")
reel = reel_group.create_reel("Clips", True)

# Import the clip defined by the scan pattern to the destination reel.
clips = flame.import_clips("/myStorage/myClip.[001-100].dpx", reel)
python
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
`

### PyClipNode

| Command | Type | Description |
|---|---|---|
| `<PyClipNode>.get_metadata()` | Function | Used to get information about the metadata keys of a Clip node. Three optional arguments can be passed: • socket_name: The socket from which to pull the metadata. The default output is used when no socket name is specified. • key: The name of the key to get the value from. All metadata values are returned when no key name is specified. • frame: The metadata value at a specific frame. If not specified, the current frame is used. |
| `<PyClipNode>.get_tokenized_metadata()` | Function | Used to get information about the metadata keys of a Clip without resolving tokens. Two optional arguments can be passed: • key: The name of the key to get the value from. All metadata values are returned when no key name is specified. • frame: The metadata value at a specific frame. If not specified, the current frame is used. |
| `<PyClipNode>.set_metadata_discarded()` | Function | Used to enable or disable the discard status of a key in a Clip node. Two mandatory and one optional arguments must be passed: • socket_name (optional): The socket on which the discarded status of a metadata key must be changed. The default output is used when no socket name is specified. • key (mandatory): The name of the metadata key to be discarded or restored. • discarded (mandatory): • True: Discard the key from the node metadata output. • False: Restore the key. |
| `<PyClipNode>.set_metadata_key()` | Function | Used to set the name of a metadata key in a Clip node. One mandatory and two optional arguments must be passed: • socket_name (optional): The output socket on which to change the name of the key. The default output is used when no socket name is specified. • key (mandatory): The metadata key to rename. • name (optional): The new name for the specified key. If None is specified, the current value will revert to the original value. |
| `<PyClipNode>.set_metadata_value()` | Function | Used to set the value of a metadata key in a Clip node. Two mandatory and one optional arguments must be passed: • socket_name (optional): The output socket on which to set the metadata. The default output is used when no socket name is specified. • key (mandatory): The metadata key to be modified or added. • value (mandatory): The metadata value to be set or edited for the specified key. If None is specified, the current value will revert to the original value. |

 Note: The functions listed in the PyNode section are also available on a PyClipNode object.

#### Example

`python
# Get all the metadata keys and values of a Clip node.
print(<PyClipNode>.get_metadata())
python
# Get all the metadata keys and values for a specific channel of a Multi-Channel Clip node.
print(<PyClipNode>.get_metadata("albedo"))
python
# Get the value for a specific key of a Clip node.
# The first argument is the socket_name, the second one is the key.
print(<PyClipNode>.get_metadata("Default", "focus"))
python
# Edit the name of a metadata key (string) of a Clip node.
# The first argument is the socket_name, the second one is the name of the key, and the third one is the new name for that key.
<PyClipNode>.set_metadata_key("Default", "key name", "modified key name")
python
# Restore the name of a renamed key in a Clip node.
# The first argument is the socket_name, the second one is the key, and the third one is discarded or can be set to None.
<PyClipNode>.set_metadata_key("Default", "key name")

<PyClipNode>.set_metadata_key("Default", "key name", None)
python
# Edit the metadata value (string) of a Clip node.
# The first argument is the socket_name, the second one is the key, and the third one is the value.
<PyClipNode>.set_metadata_value("Default", "focus", "100")
python
# Edit the metadata value (integer) of a Clip node.
# The first argument is the socket_name, the second one is the key, and the third one is the value.
<PyClipNode>.set_metadata_value("Default", "focus", 100)
python
# Edit the metadata value (float) of a Clip node.
# The first argument is the socket_name, the second one is the key, and the third one is the value.
<PyClipNode>.set_metadata_value("Default", "focus", 100.12)
python
# Edit the metadata value in the channel of a Multi-Channel Clip node.
# The first argument is the socket_name, the second one is the key, and the third one is the value.
<PyClipNode>.set_metadata_value("albedo", "CameraFOV", 100.12)
python
# Reset the value of key in Clip node.
# The first argument is the socket_name, the second one is the key, and the third one is the value.
# When value is set to None, the original value is restored.
<PyClipNode>.set_metadata_value("Default", "focus", None)
python
# Add a new key and set its value in the metadata of a Clip node.
# The first argument is the socket_name, the second one is the key, and the third one is the value.
<PyClipNode>.set_metadata_value("Default", "Application", "Flame")
python
# Delete an added key in a Clip node.
# The first argument is the socket_name, the second one is the key, and the third one is the value.
# The value must be set to None for the key to be deleted.
<PyClipNode>.set_metadata_value("Default", "Application", None)
python
# Set the Discard status for a key in a Clip node.
# The first argument is the socket_name, the second one is the key, and the third one is discarded.
<PyClipNode>.set_metadata_discarded("Default", "focus", True)
python
# Restore a discarded key in a Clip node
# The first argument is the socket_name, the second one is the key, and the third one is discarded.
<PyClipNode>.set_metadata_discarded("Default", "focus", False)
`

### PyMarker

| Command | Type | Description |
|---|---|---|
| `<PyMarker>.clear_annotations()` | Function | Used to clear all annotations from a marker. |
| `<PyMarker>.has_annotations` | Read-Only Property | Indicates whether a marker has annotations. |

#### Examples

`python
# Find which Markers have annotations in the current Sequence.
for marker in flame.timeline.clip.markers:
    if marker.has_annotations:
       print(marker.name)
python
# Clear all the annotations in a Sequence.
for marker in flame.timeline.clip.markers:
    if marker.has_annotations:
       marker.clear_annotations()
`

### PyMetadataNode

| Command | Type | Description |
|---|---|---|
| `<PyMetadataNode>.get_metadata()` | Function | Used to get information about the metadata keys of a Metadata node or one of its inputs. Three optional arguments can be passed: • socket_name: The socket from which to pull the metadata. The default output is used when no socket name is specified. • key: The name of the key to get the value from. All metadata values are returned when no key name is specified. • frame: The metadata value at a specific frame. If not specified, the current frame is used. |
| `<PyMetadataNode>.get_tokenized_metadata()` | Function | Used to get information about the metadata keys of a Metadata node or one of its inputs without resolving tokens. Three optional arguments can be passed: • socket_name: The socket from which to pull the metadata. The default output is used when no socket name is specified. • key: The name of the key to get the value from. All metadata values are returned when no key name is specified. • frame: The metadata value at a specific frame. If not specified, the current frame is used. |
| `<PyMetadataNode>.load_node_setup()` | Function | Used to load a setup in the Metadata node.<br><br>The complete path to the setup, including the file name, must be passed as an argument.<br><br>The following arguments can also be set to True or False to apply modifications or discard keys when the setup is loaded. All arguments are set to True by default. • edited_keys • discarded_keys • added_keys • replaced_keys |
| `<PyMetadataNode>.set_metadata_discarded()` | Function | Used to enable or disable the discard status of a key in a Metadata node. Two mandatory arguments must be passed: • key (mandatory): The metadata key to be discarded or restored. • discarded (mandatory): • True: Discard the key from the node metadata output. • False: Restore the key. |
| `<PyMetadataNode>.set_metadata_key()` | Function | Used to set the name of a metadata key in a Metadata node. One mandatory and two optional arguments must be passed: • socket_name (optional): The output socket on which to change the name of the key. • key (mandatory): The metadata key to rename. • name (optional): The new name for the specified key. If None is specified, the current value will revert to the original value. |
| `<PyMetadataNode>.set_metadata_value()` | Function | Used to set the value of a metadata key in a Metadata node. Two mandatory arguments must be passed: • key (mandatory): The metadata key to be modified or added. • value (mandatory): The metadata value to be set or edited for the specified key. If None is specified, the current value will revert to the original value. |

#### Examples

`python
# Get all the metadata keys and values of a Metadata node.
print(<PyMetadataNode>.get_metadata())
python
# Get the value for a specific key in a Metadata node
# The first argument is the socket_name, the second one is the key.
print(<PyMetadataNode>.get_metadata("Default", "focus"))
python
# Edit the name of a metadata key (string) in a Metadata node, without specifying an output socket.
# The first argument is the name of the key and the second one is the new name for that key.
<PyMetadataNode>.set_metadata_key(key="key name", name="new key name")
python
# Restore the name of a renamed key in a Metadata node.
# The first argument is the socket_name (always Result or Default for a Metadata node), the second one is the key, and the third one is discarded or can be set to None.
<PyMetadataNode>.set_metadata_key("Result", "key name")

<PyMetadataNode>.set_metadata_key("Result", "key name", None)
python
# Edit the metadata value (string) of a Metadata node.
# The first argument is the socket_name, the second one is the key, and the third one is the value.
<PyMetadataNode>.set_metadata_value("Default", "focus", "100")
python
# Edit the metadata value (integer) of a Metadata node.
# The first argument is the socket_name, the second one is the key, and the third one is the value.
<PyMetadataNode>.set_metadata_value("Default", "focus", 100)
python
# Edit the metadata value (float) of a Metadata node.
# The first argument is the socket_name, the second one is the key, and the third one is the value.
<PyMetadataNode>.set_metadata_value("Default", "focus", 100.12)
python
# Reset the value of key in a Metadata node.
# The first argument is the socket_name, the second one is the key, and the third one is the value.
# When value is set to None, the original value is restored.
<PyMetadataNode>.set_metadata_value("Default", "focus", None)
python
# Add a new key and set its value in the metadata of a Metadata node.
# The first argument is the socket_name, the second one is the key, and the third one is the value.
<PyMetadataNode>.set_metadata_value("Default", "Application", "Flame")
python
# Delete an added key in a Metadata node.
# The first argument is the socket_name, the second one is the key, and the third one is the value.
# The value must be set to None for the key to be deleted.
<PyMetadataNode>.set_metadata_value("Default", "Application", None)
python
# Set the Discard status for a key in a Metadata node.
# The first argument is the socket_name, the second one is the key, and the third one is discarded.
<PyMetadataNode>.set_metadata_discarded("Default", "focus", True)
python
# Restore a discarded key in a Metadata node.
# The first argument is the socket_name, the second one is the key, and the third one is discarded.
<PyMetadataNode>.set_metadata_discarded("Default", "focus", False)
python
# Load a setup in the Metadata node and only apply the added_keys.
<PyMetadataNode>.load_node_setup('/var/tmp/mysetup.metadata_node', edited_keys=False, discarded_keys=False, added_keys=True, replaced_keys=False)
`

### PyMetadataTimelineFX

| Command | Type | Description |
|---|---|---|
| `<PyMetadataTimelineFX>.get_metadata()` | Function | Used to get information about the metadata keys of a Source Metadata Timeline FX. Two optional arguments can be passed: • key: The name of the key to get the value from. All metadata values are returned when no key name is specified. • frame: The metadata value at a specific frame, relative to the segment's start. If not specified, the current frame is used. |
| `<PyMetadataTimelineFX>.get_tokenized_metadata()` | Function | Used to get information about the metadata keys of a Source Metadata Timeline FX without resolving tokens. Two optional arguments can be passed: • key: The name of the key to get the value from. All metadata values are returned when no key name is specified. • frame: The metadata value at a specific frame, relative to the segment's start. If not specified, the current frame is used. |
| `<PyMetadataTimelineFX>.load_setup()` | Function | Used to load a setup in the Source Metadata Timeline FX.<br><br>The complete path to the setup, including the file name, must be passed as an argument.<br><br>The following arguments can also be set to True or False to apply modifications or discard keys when the setup is loaded. All arguments are set to True by default. • edited_keys • discarded_keys • added_keys |
| `<PyMetadataTimelineFX>.set_metadata_discarded()` | Function | Used to enable or disable the discard status of a key in a Source Metadata Timeline FX. Two mandatory arguments must be passed: • key (mandatory): The metadata key to be discarded or restored. • discarded (mandatory): • True: Discard the key from the node metadata output. • False: Restore the key. |
| `<PyMetadataTimelineFX>.set_metadata_key()` | Function | Used to set the name of a metadata key in a Metadata Timeline FX. One mandatory and one optional arguments must be passed: • key (mandatory): The metadata key to rename. • name (optional): The new name for the specified key. If None is specified, the current value will revert to the original value. |
| `<PyMetadataTimelineFX>.set_metadata_value()` | Function | Used to set the metadata value of a key in a Source Metadata Timeline FX. Two mandatory arguments must be passed: • key: The metadata key to be modified or added. • value: The metadata value to be set or edited for the specified key. If None is specified, the current value will revert to the original value. |

#### Examples

`python
# Get all the metadata keys and values of a Source Metadata Timeline FX.
print(<PyMetadataTimelineFX>.get_metadata())
python
# Get the value for a specific key in a Source Metadata Timeline FX.
# The argument is the key.
print(<PyMetadataTimelineFX>.get_metadata("focus"))
python
# Edit the name of a metadata key (string) in a Source Metadata Timeline FX.
# The first argument is the name of the key and the second one is the new name for that key.
<PyMetadataTimelineFX>.set_metadata_key("key name", "new key name")
python
# Restore the name of a renamed key in a Source Metadata Timeline FX.
# The first argument is the key and the second one is discarded or can be set to None.
<PyMetadataTimelineFX>.set_metadata_key("key name")

<PyMetadataTimelineFX>.set_metadata_key("key name", None)
python
# Edit the metadata value (string) of a Source Metadata Timeline FX.
# The first argument is the key, and the second one is the value.
<PyMetadataTimelineFX>.set_metadata_value("focus", "100")
python
# Edit the metadata value (integer) of a Source Metadata Timeline FX.
# The first argument is the key, and the second one is the value.
<PyMetadataTimelineFX>.set_metadata_value("focus", 100)
python
# Edit the metadata value (float) of a Source Metadata Timeline FX.
# The first argument is the socket_name, the second one is the key, and the third one is the value.
<PyMetadataTimelineFX>.set_metadata_value("focus", 100.12)
python
# Reset the value of key in a Source Metadata Timeline FX.
# The first argument is the key, and the second one is the value.
# When value is set to None, the original value is restored.
<PyMetadataTimelineFX>.set_metadata_value("focus", None)
python
# Add a new key and set its value in the metadata of a Source Metadata Timeline FX.
# The first argument is the key, and the second one is the value.
<PyMetadataTimelineFX>.set_metadata_value("Application", "Flame")
python
# Delete an added key in a Source Metadata Timeline FX.
# The first argument is the key, and the second one is the value.
# The value must be set to None for the key to be deleted.
<PyMetadataTimelineFX>.set_metadata_value("Application", None)
python
# Set the Discard status for a key in a Source Metadata Timeline FX.
# The first argument is the key, and the second one is discarded.
<PyMetadataTimelineFX>.set_metadata_discarded("focus", True)
python
# Restore a discarded key in a Source Metadata Timeline FX.
# The first argument is the key, and the second one is discarded.
<PyMetadataTimelineFX>.set_metadata_discarded("focus", False)
python
# Load a setup in the Metadata Timeline FX and only apply the edited_keys.
<PyMetadataTimelineFX>.load_setup('/var/tmp/mysetup.metadata_node', edited_keys=True, discarded_keys=False, added_keys=False)
`

### PyNode

| Command | Type | Description |
|---|---|---|

| `<PyNode>.create_marker()` | Function | Used to add a Marker to a Node. The following argument must be passed:

- The frame at which the marker will be created. Must be an integer number representing the frame.
 | | `<PyNode>.get_metadata()` | Function | Used to get information about the metadata keys of a node or one of its inputs. Three optional arguments can be passed:

- socket_name: The socket from which to pull the metadata. The default output is used when no socket name is specified.
- key: The name of the key to get the value from. All metadata values are returned when no key name is specified.
- frame: The metadata value at a specific frame. If not specified, the current frame is used.
 | | `<PyNode>.markers` | Read-Only Property | Used to get a list of markers on a node. | | `<PyNode>.output_channel_as_metadata_key()` | Function | Used to output the content of a channel as a metadata key. Two arguments must be passed:

- channel_name: The name of the channel to be exported. The inclusion of the node's name in the string is optional.
- enable: Must be set to True or False.

  - True: The content of the channel is exported as a metadata key.
  - False: The content of the channel is no longer exported.

 | | `<PyNode>.set_expression()` | Function | Used to set an expression on a channel. Two mandatory arguments must be passed:

- channel_name (mandatory): The name of the channel to set the expression on.
- expression (mandatory): The expression to set on the channel.
 | | `<PyNode>.get_expression()` | Function | Used to get the expression set on a channel. One mandatory argument must be passed:

- channel_name (mandatory): The name of the channel to get the expression from.
 | | `<PyNode>.clear_expression()` | Function | Used to clear the expression set on a channel. One mandatory argument must be passed:

- channel_name (mandatory): The name of the channel to clear the expression from.
 | | `<PyNode>.bake_expression()` | Function | Used to bake the expression set on a channel into keyframes. Four mandatory arguments must be passed:

- channel_name (mandatory): The name of the channel to bake the expression from.
- step (mandatory): The step in frames between each baked keyframe.
- start (mandatory): The first frame of the bake range.
- end (mandatory): The last frame of the bake range.
 |

#### Examples

`python
# Get all the metadata keys and values of a new PyNode node. If no socket is defined, the Result socket is used.
flip = flame.batch.create_node("Flip")
print(flip.get_metadata())
python
# Output the content of the X Position channel of a 2D Transform node as a metadata key.
dd = flame.batch.create_node("2D Transform")
dd.output_channel_as_metadata_key("AxisTransform.Position.X", True)
python
# Stop outputting the content of the X Position channel of a 2D Transform node as a metadata key.
flame.batch.current_node.output_channel_as_metadata_key("AxisTransform.Position.X", False)
`

Examples of how the set_expression() and bake_expression() functions can be used to propagate information in the metadata keys of a clip to parameters of a Camera object in an Action node are available in the `propagate_metadata_to_action_camera.py` file, located in `/opt/Autodesk/<application version>/python_utilities/examples`.

### PyNodeMarker

| Command | Type | Description |
|---|---|---|
| `<PyNodeMarker>.clear_annotations()` | Function | Used to clear all annotations from a marker. |
| `<PyNodeMarker>.has_annotations` | Read-Only Property | Indicates whether a marker has annotations. |
| `<PyNodeMarker>.name` | Attribute | Used to get or set the Marker's name. A string must be passed as the argument when the name is set. |
| `<PyNodeMarker>.tokenized_name` | Attribute | Used to get or set the Marker's tokenized name. A string must be passed as the argument when the tokenized name is set. |
| `<PyNodeMarker>.dynamic_name` | Attribute | Used to get or set the status of the Dynamic option for the name. True or False must be passed as an argument when the status is set. |
| `<PyNodeMarker>.comment` | Attribute | Used to get or set the Marker's comment. A string must be passed as the argument when the comment is set. |
| `<PyNodeMarker>.tokenized_comment` | Attribute | Used to get or set the Marker's tokenized comment. A string must be passed as the argument when the tokenized comment is set. |
| `<PyNodeMarker>.dynamic_comment` | Attribute | Used to get or set the status of the Dynamic option for the comment. True or False must be passed as an argument when the status is set. |
| `<PyNodeMarker>.location` | Attribute | Used to get or set the Marker's location. An integer number representing a frame must be passed when the location is set. |
| `<PyNodeMarker>.duration` | Attribute | Used to get or set the Marker's duration. An integer number representing a duration must be passed when the duration is set. |
| `<PyNodeMarker>.colour` | Attribute | Used to get or set the Marker's colour. A tuple containing three float numbers representing the red, green, and blue values must be passed as an argument when the colour is set. |
| `<PyNodeMarker>.colour_label` | Attribute | Used to get or set the Marker's colour label. A string representing the name of a colour label must be passed as an argument when the colour is set. |
| `<PyNodeMarker>.locked_location` | Attribute | Used to get or set the status of the Marker's lock option. True or False must be passed as an argument when the status is set. |
| `<PyNodeMarker>.selected` | Attribute | Used to get or set the selection status of the Marker. True or False must be passed as an argument when the status is set. |

### PyRenderNode

| Command | Type | Description |
|---|---|---|
| `<PyRenderNode>.basic_metadata` | Attribute | Used to get or set the status of the Basic Metadata option.<br><br>One of the following must be passed as the argument when the attribute is set: • Custom Values • Use Input Values |
| `<PyRenderNode>.basic_metadata_input` | Attribute | Used to get or set the status of the Basic Metadata Input option.<br><br>One of the following must be passed as the argument when the attribute is set: • Use Front Input • Use Metadata Input |
| `<PyRenderNode>.get_metadata()` | Function | Used to get information about the metadata keys of a Render node. Three optional arguments can be passed: • socket_name: The socket from which to pull the metadata. The first output channel is used when no socket name is specified. Note that the name of the corresponding channel can be used in place of the socket name. • key: The name of the key to get the value from. All metadata values are returned when no key name is specified. • frame: The metadata value at a specific frame. If not specified, the current frame is used. |
| `<PyRenderNode>.get_tokenized_metadata()` | Function | Used to get information about the metadata keys of a Render node without resolving tokens. Three optional arguments can be passed: • socket_name: The socket from which to pull the metadata. The first output channel is used when no socket name is specified. Note that the name of the corresponding channel can be used in place of the socket name. • key: The name of the key to get the value from. All metadata values are returned when no key name is specified. • frame: The metadata value at a specific frame. If not specified, the current frame is used. |
| `<PyRenderNode>.set_metadata_discarded()` | Function | Used to enable or disable the discard status of a key in a Render node. Two mandatory and one optional arguments must be passed: • socket_name (optional): The channel on which the discarded status of a metadata key must be changed. The first input socket is used when no socket name is specified. • key (mandatory): The metadata key to be discarded or restored. • discarded (mandatory): • True: Discard the key from the node metadata output. • False: Restore the key. |
| `<PyRenderNode>.set_metadata_key()` | Function | Used to set the name of a metadata key in a Render node. One mandatory and one optional arguments must be passed: • socket_name (optional): The output channel on which to change the name of the key. The first channel is used when no channel name is specified. • key (mandatory): The metadata key to rename. • name (optional): The new name for the specified key. If None is specified, the current value will revert to the original value. |
| `<PyRenderNode>.set_metadata_value()` | Function | Used to set the value of a metadata key in a Render node. Two mandatory and one optional arguments must be passed: • socket_name (optional): The output channel on which to set the metadata. The first channel is used when no channel name is specified. • key (mandatory): The metadata key to be modified or added. • value (mandatory): The metadata value to be set or edited for the specified key. If None is specified, the current value will revert to the original value. |

#### Examples

`python
# Get all the metadata keys and values of a Render node.
print(<PyRenderNode>.get_metadata())
python
# Get the value for a specific key in a Render node.
# The first argument is the socket_name, the second one is the key.
print(<PyRenderNode>.get_metadata("Default", "focus"))
python
# Edit the name of a metadata key (string) in a Render node.
# The first argument is the socket_name (a channel name or Default for a Render node), the second one is the key, and the third one is the new name for that key.
<PyRenderNode>.set_metadata_key("channel name", "key name", "new key name")
python
# Restore the name of a renamed key in a Render node.
# The first argument is the socket_name (a channel name for a Render node), the second one is the key, and the third one is discarded or can be set to None.
<PyRenderNode>.set_metadata_key("channel name", "key name")

<PyRenderNode>.set_metadata_key("channel name", "key name", None)
python
# Edit the metadata value (string) of a Render node.
# The first argument is the socket_name, the second one is the key, and the third one is the value.
<PyRenderNode>.set_metadata_value("Default", "focus", 100)
python
# Edit the metadata value (integer) of a Render node.
# The first argument is the socket_name, the second one is the key, and the third one is the value.
<PyRenderNode>.set_metadata_value("Default", "focus", 100)
python
# Edit the metadata value (float) of a Render node.
# The first argument is the socket_name, the second one is the key, and the third one is the value.
<PyRenderNode>.set_metadata_value("Default", "focus", 100.12)
python
# Reset the value of key in a Render node.
# The first argument is the socket_name, the second one is the key, and the third one is the value.
# When value is set to None, the original value is restored.
<PyRenderNode>.set_metadata_value("Default", "focus", None)
python
# Add a new key and set its value in the metadata of a Render node.
# The first argument is the socket_name, the second one is the key, and the third one is the value.
<PyRenderNode>.set_metadata_value("Default", "Application", "Flame")
python
# Delete an added key in a Render node.
# The first argument is the socket_name, the second one is the key, and the third one is the value.
# The value must be set to None for the key to be deleted.
<PyRenderNode>.set_metadata_value("Default", "Application", None)
python
# Set the Discard status for a key in a Render node.
# The first argument is the socket_name, the second one is the key, and the third one is discarded.
<PyRenderNode>.set_metadata_discarded("Default", "focus", True)
python
# Restore a discarded key in a Render node.
# The first argument is the socket_name, the second one is the key, and the third one is discarded.
<PyRenderNode>.set_metadata_discarded("Default", "focus", False)
`

#### Deprecated

The `<PyRenderNode>.format` attribute has been deprecated since its corresponding option inside the **Render** node user interface is no longer available.

### PySegment

`<PySegment>.create_effect()` is not new, but serves as a reminder of how to create a Source Metadata Timeline FX on a Timeline Segment.

| Command | Type | Description |
|---|---|---|
| `<PySegment>.create_effect()` | Function | Used to create a Metadata Source Timeline FX. |
| `<PySegment>.create_unlinked_segment()` | Function | The timewarp_speed argument has been added to create_unlinked_segment function.<br><br>Use the timewarp_speed argument to create a Timewarp Timeline FX on the segment created from a Gap. The speed can be a float or integer value and can be a negative value, zero, or a positive value.<br><br>The head value remains the first frame of the segment with any of the timewarp values. |
| `<PySegment>.get_metadata()` | Function | Used to get information about the metadata keys of a timeline segment. Two optional arguments can be passed: • key: The name of the key to get the value from. All metadata values are returned when no key name is specified. • time: The metadata value at a specific frame. Must be a PyTime. If not specified, the timeline segment's start frame is used. |

#### Examples

`python
# Create a Source Metadata Timeline FX on the selected segment.
flame.timeline.current_segment.create_effect("Source Metadata")
python
# Turn a gap into a timeline segment with a Timewarp Timeline FX of 50% on it.
flame.timeline.current_segment.create_unlinked_segment(timewarp_speed=50.0)
`

### PyTimelineFX

| Command | Type | Description |
|---|---|---|
| `<PyTimelineFX>.clear_maps_cache_media()` | Function | `<PyTimelineFX>.flush_maps_cache_media()` was renamed and deprecated. |
| `<PyTimelineFX>.output_channel_as_metadata_key()` | Function | Used to output the content of a channel as a metadata key. Two arguments must be passed: • channel_name: The name of the channel to be exported. The inclusion of the timeline fx's name in the string is optional. • enable: Must be set to True or False: • True: The content of the channel is exported as a metadata key. • False: The content of the channel is no longer exported. |

 Note: The functions other than `create_marker()` and `get_metadata()` listed in the PyNode section are also available on a PyTimelineFX object.

#### Examples

`python
# Output the content of the X Position channel of a 2D Transform Timeline FX as a metadata key.
dd = flame.timeline.current_segment.create_effect("2D Transform")
dd.output_channel_as_metadata_key("AxisTransform.Position.X", True)
python
# Stop outputting the content of the X Position channel of a 2D Transform Timeline FX as a metadata key.
flame.timeline.current_segment.effects[0].output_channel_as_metadata_key("AxisTransform.Position.X", False)
`

### PyTypeNode and PyTypeTimelineFX

| Command | Type | Description |
|---|---|---|
| `<PyTypeNode>.show_char_axis` | Attribute | Used to get or set the status of Show Axis for the Characters Axis.<br><br>One of the following must be passed as the argument when the attribute is set: • True • False |
| `<PyTypeNode>.show_char_pos` | Attribute | Used to get or set the status of Show Position for the Characters Axis.<br><br>One of the following must be passed as the argument when the attribute is set: • True • False |
| `<PyTypeNode>.show_layer_axis` | Attribute | Used to get or set the status of Show Axis for the Layer Axis.<br><br>One of the following must be passed as the argument when the attribute is set: • True • False |
| `<PyTypeNode>.show_para_axis` | Attribute | Used to get or set the status of Show Axis for the Paragraph Axis.<br><br>One of the following must be passed as the argument when the attribute is set: • True • False |

 Note: The functions other than `create_marker()` and `get_metadata()` listed in the PyNode section are also available on PyTypeNode and PyTypeTimelineFX objects.

### PyWriteFileNode

| Command | Type | Description |
|---|---|---|
| `<PyWriteFileNode>.basic_metadata` | Attribute | Used to get or set the status of the Basic Metadata option.<br><br>One of the following must be passed as the argument when the attribute is set: • Custom Values • Use Input Values |
| `<PyWriteFileNode>.basic_metadata_input` | Attribute | Used to get or set the status of the Basic Metadata Input option.<br><br>One of the following must be passed as the argument when the attribute is set: • Use Front Input • Use Metadata Input |
| `<PyWriteFileNode>.get_metadata()` | Function | Used to get information about the metadata keys of a Write File node. Three optional arguments can be passed: • socket_name: The socket from which to pull the metadata. The first output channel is used when no socket name is specified. Note that the name of the corresponding channel can be used in place of the socket name. • key: The name of the key to get the value from. All metadata values are returned when no key name is specified. • frame: The metadata value at a specific frame. If not specified, the current frame is used. |
| `<PyWriteFileNode>.get_tokenized_metadata()` | Function | Used to get information about the metadata keys of a Write File node without resolving tokens. Three optional arguments can be passed: • socket_name: The socket from which to pull the metadata. The first output channel is used when no socket name is specified. Note that the name of the corresponding channel can be used in place of the socket name. • key: The name of the key to get the value from. All metadata values are returned when no key name is specified. • frame: The metadata value at a specific frame. If not specified, the current frame is used. |
| `<PyWriteFileNode>.set_metadata_discarded()` | Function | Used to enable or disable the discard status of a key in a Write File node. Two mandatory and one optional arguments must be passed: • socket_name (optional): The channel on which the discarded status of a metadata key must be changed. The first channel is used when no socket name is specified. • key (mandatory): The metadata key to be discarded or restored. • discarded (mandatory): • True: Discard the key from the node metadata output. • False: Restore the key. |
| `<PyWriteFileNode>.set_metadata_key()` | Function | Used to set the name of a metadata key in a Write File node. One mandatory and one optional arguments must be passed: • socket_name (optional): The output channel on which to change the name of the key. The first channel is used when no socket name is specified. • key (mandatory): The metadata key to rename. • name (optional): The new name for the specified key. If None is specified, the current value will revert to the original value. |
| `<PyWriteFileNode>.set_metadata_value()` | Function | Used to set the value of a metadata key in a Write File node. Two mandatory and one optional arguments must be passed: • socket_name (optional): The output channel on which to set the metadata. The first channel is used when no socket name is specified. • key (mandatory): The metadata key to be modified or added. • value (mandatory): The metadata value to be set or edited for the specified key. If None is specified, the current value will revert to the original value. |

#### Examples

`python
# Get all the metadata keys and values of a Write file node.
print(<PyWriteFileNode>.get_metadata())
python
# Get the value for a specific key in a Write file node.
# The first argument is the socket_name, the second one is the key.
print(<PyWriteFileNode>.get_metadata("Default", "focus"))
python
# Edit the name of a metadata key (string) in a Write File node.
# The first argument is the socket_name (a channel name or Default for a Write File node), the second one is the key, and the third one is the new name for that key.
<PyWriteFileNode>.set_metadata_key("channel name", "key name", "new key name")
python
# Restore the name of a renamed key in a Write File node.
# The first argument is the socket_name (a channel name for a Write File node), the second one is the key, and the third one is discarded or can be set to None.
<PyWriteFileNode>.set_metadata_key("channel name", "key name")

<PyWriteFileNode>.set_metadata_key("channel name", "key name", None)
python
# Edit the metadata value (string) of a Write file node.
# The first argument is the socket_name, the second one is the key, and the third one is the value.
<PyWriteFileNode>.set_metadata_value("Default", "focus", "100")
python
# Edit the metadata value (integer) of a Write file node.
# The first argument is the socket_name, the second one is the key, and the third one is the value.
<PyWriteFileNode>.set_metadata_value("Default", "focus", 100)
python
# Edit the metadata value (float) of a Write file node.
# The first argument is the socket_name, the second one is the key, and the third one is the value.
<PyWriteFileNode>.set_metadata_value("Default", "focus", 100.12)
python
# Reset the value of key in a Write file node.
# The first argument is the socket_name, the second one is the key, and the third one is the value.
# When value is set to None, the original value is restored.
<PyWriteFileNode>.set_metadata_value("Default", "focus", None)
python
# Add a new key and set its value in the metadata of a Write file node.
# The first argument is the socket_name, the second one is the key, and the third one is the value.
<PyWriteFileNode>.set_metadata_value("Default", "Application", "Flame")
python
# Delete an added key in a Write file node.
# The first argument is the socket_name, the second one is the key, and the third one is the value.
# The value must be set to None for the key to be deleted.
<PyWriteFileNode>.set_metadata_value("Default", "Application", None)
python
# Set the Discard status for a key in a Write file node.
# The first argument is the socket_name, the second one is the key, and the third one is discarded.
<PyWriteFileNode>.set_metadata_discarded("Default", "focus", True)
python
# Restore a discarded key in a Write file node.
# The first argument is the socket_name, the second one is the key, and the third one is discarded.
<PyWriteFileNode>.set_metadata_discarded("Default", "focus", False)
`

#### Deprecated

The `<PyWriteFileNode>.format` attribute has been deprecated since its corresponding option inside the **Write File** node user interface is no longer available.

## Related pages

- Autodesk Flame Python: flame module
- Python Console and how to Execute Scripts
- Write Your First Python API Script
- Python API Examples
- Defines for the flame Module
- What's New in Previous Releases
