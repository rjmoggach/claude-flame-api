<!-- source: Autodesk Flame Family 2027 Help _ Batch Hooks _ Autodesk.html -->
# Batch Hooks

The hooks described in this section follow one of two patterns:

- Event hooks are called once an event has occurred, such as a Batch setup being loaded or a Batch Group being created. They receive the setup path or the Python object concerned by the event and, for most of them, a `source` argument indicating how the event was triggered.
- Paired hooks are a `pre` and a `post` hook, or a `begin` and an `end` hook, that will be called respectively before and after a given action is done, allowing the implementer to monitor, abort, and react to an event. Both hooks of a pair receive an `info` dictionary and a `userData` dictionary. The `userData` dictionary filled by the first hook is carried over into the second one, so it can be used to pass data between the two hooks.

---

## Batch Setup Hooks

| Function | Description |
|---|---|
| `batch_setup_loaded` | Hook called when a Batch setup is loaded. |
| `batch_setup_saved` | Hook called when a Batch setup is saved. |

Both Batch setup hooks use similar arguments, with some arguments only available in some hooks.

| Argument | Type | Loaded | Saved | Description |
|---|---|---|---|---|
| `setupPath` | String | Available | Available | File path of the setup being loaded or saved. |
| `source` | String | Available |  | How the setup was loaded. |

The `source` argument of `batch_setup_loaded` is one of the following values:

| Value | Description |
|---|---|
| `file_browser` | A setup loaded from the **Load Batch** file browser. |
| `open_as_batch_group` | A setup loaded when a Batch Group is opened, including with the **Open as Batch Group** option of an open clip that contains a Batch setup. |
| `load_iteration` | A setup loaded from an iteration other than the current one. |
| `startup` | A setup loaded with the execute batch setup (`-b`) switch when the application is started from a command line. |
| `create_new_version` | A setup loaded with the **Create New Version** option of an open clip that contains a Batch setup. |
| `promote_to_batch_fx` | A setup loaded with the **Promote to Batch FX** option of an open clip that contains a Batch setup. |

---

## Batch Group Hooks

| Function | Description |
|---|---|
| `batch_group_created` | Hook called when a Batch Group is created.<br><br>Use this hook to load a template setup upon creation. |
| `batch_group_activated` | Hook called when a Batch Group is set active. |

Both Batch Group hooks use the same arguments.

| Argument | Type | Created | Activated | Description |
|---|---|---|---|---|
| `batch_group` | PyBatch | Available | Available | The Batch Group Python object. |
| `source` | String | Available | Available | How the Batch Group was created or set active. |

 Note: Edit a new Batch Group through the `batch_group` argument rather than through `flame.batch`. For a Batch Group published to a Library, the Batch Group is loaded in memory and written back to its setup, and `flame.batch` does not point to it.

The `source` argument of `batch_group_created` is one of the following values:

| Value | Description |
|---|---|
| `media_panel` | A Batch Group created with the **Batch Group** option of the **New** submenu, in the context menu of a Media Panel item such as a Desktop. |
| `batch_new` | A Batch Group created with the **New** button in the Batch environment. |
| `timeline` | A Batch Group created with the **Create Batch Group** option in the context menu of a Timeline segment. |
| `timeline_convert_fx` | A Batch Group created with the **Create Batch Group (Convert TL FX)** option in the context menu of a Timeline segment. The Timeline FX are converted in the Batch Group. |
| `conform` | A Batch Group created with the **Create Batch Group** button in the Conform environment. |
| `shot_publish` | A Batch Group created during a Shot Publish operation, with the **Create Open Clip** and **Create Batch** options of the Shot Publish presets in Media Export. |
| `auto_replace` | A Batch Group created automatically when the last Batch Group of a Desktop is deleted. |

The `source` argument of `batch_group_activated` is one of the following values:

| Value | Description |
|---|---|
| `media_panel` | A Batch Group set active by clicking its icon in the Media Panel. |
| `desktop_reels` | A Batch Group set active by selecting it in a Desktop Reels drop-down. |

---

## Batch FX Hooks

| Function | Description |
|---|---|
| `batch_fx_created` | Hook called when a Batch FX is created.<br><br>Use this hook to load a template setup upon creation. |

| Argument | Type | Description |
|---|---|---|
| `batch_fx_setup` | PyBatch | The newly created Batch FX setup. |
| `source` | String | How the Batch FX was created. |

The `source` argument of `batch_fx_created` is one of the following values:

| Value | Description |
|---|---|
| `batch_schematic` | A Batch FX created with the **Create BFX** operation in the Batch Schematic. |
| `timeline` | A Batch FX created on a single Timeline segment, with no option selected. |
| `gap` | A Batch FX created on a gap segment or with the **Add Adjustment Segment** option. |
| `clip` | A Batch FX created with the **Selection as Clip** option. |
| `flowgraph` | A Batch FX created with the **Selection as Flowgraph** option. |
| `comp_3d` | A Batch FX created with the **Selection as 3D Comp** option. |

---

## Batch Iteration Hooks

| Function | Description |
|---|---|
| `batch_setup_iterated_pre` | Hook called before a Batch iteration is created.<br><br>This can be used to change where the iteration is saved, or to validate information and potentially abort the iteration before it is saved. |
| `batch_setup_iterated_post` | Hook called after a Batch iteration is created. |

Both Batch iteration hooks use a similar `info` dictionary as parameter with some keys only modifiable in some hooks.

| Key | Type | Pre | Post | Description |
|---|---|---|---|---|
| `savePath` | String | Modifiable | Available | Path to which the Batch setup file of the iteration is saved on disk. |
| `setupName` | String | Modifiable | Available | Name of the Batch setup file of the iteration saved on disk. |
| `abort` | Boolean | Modifiable | Available | Hook can set this to True if the iteration should be aborted.<br><br>In `batch_setup_iterated_post`, True if the save failed. |
| `abortMessage` | String | Modifiable | Available | Error message describing why the iteration was aborted.<br><br>A generic message is used if left blank. |

 Note: When `batch_setup_iterated_pre` aborts the iteration, `batch_setup_iterated_post` is not called. The `abort` key of `batch_setup_iterated_post` therefore only indicates an actual error, and is not defined when the save succeeds.

---

## Batch Render Hooks

| Function | Description |
|---|---|
| `batch_render_begin` | Hook called before a render begins.<br><br>This can be used to change the Backburner job name, or to validate information and potentially abort the render before it starts. |
| `batch_render_end` | Hook called when a render ends. |

Both Batch render hooks use a similar `info` dictionary as parameter with some keys only available/modifiable in some hooks.

| Key | Type | Begin | End | Description |
|---|---|---|---|---|
| `backgroundJobName` | String | Modifiable | Available | Job name as shown in Backburner. |
| `backgroundJobId` | String |  | Available | Identifier of the background job given by the Backburner Manager upon submission. |
| `aborted` | Boolean | Modifiable | Available | Hook can set this to True if the render should be aborted.<br><br>In `batch_render_end`, True if the render was aborted by the user or by a render error. |
| `abortMessage` | String | Modifiable | Available | Error message describing why the render was aborted.<br><br>A generic message is used if left blank. |

 Note: When the render is done with Burn or Background Reactor, `batch_render_end` is called before the rendering of all frames is completed.

---

## Batch Burn Hooks

| Function | Description |
|---|---|
| `batch_burn_begin` | Hook called before a job is sent to Burn or Background Reactor.<br><br>This can be used to validate information and potentially abort the job before it is sent. |
| `batch_burn_end` | Hook called after a job is sent to Burn or Background Reactor. |

Both Batch burn hooks use a similar `info` dictionary as parameter with some keys only available/modifiable in some hooks.

| Key | Type | Begin | End | Description |
|---|---|---|---|---|
| `backgroundJobId` | String |  | Available | Identifier of the background job given by the Backburner Manager upon submission. |
| `aborted` | Boolean | Modifiable | Available | Hook can set this to True if the job should be aborted.<br><br>In `batch_burn_end`, True if the job was aborted by the user or by an error. |
| `abortMessage` | String | Modifiable | Available | Error message describing why the job was aborted.<br><br>A generic message is used if left blank. |

---

## Batch Export Hooks

| Function | Description |
|---|---|
| `batch_export_begin` | Hook called before a Write File node starts to export.<br><br>This can be used to change where the files are written, or to validate information and potentially abort the export before it starts. |
| `batch_export_end` | Hook called when a Write File node ends the export. |

 Note: For stereo exports, both hooks are called twice, once for each channel: left first, and right second.

Both Batch export hooks use a similar `info` dictionary as parameter with some keys only available/modifiable in some hooks.

| Key | Type | Begin | End | Description |
|---|---|---|---|---|
| `nodeName` | String | Available | Available | Name of the Write File node. |
| `exportPath` | String | Modifiable | Available | Export path as entered in the user interface.<br><br>Hook can modify it to change where the files are written. |
| `namePattern` | String | Available | Available | List of optional naming tokens as entered in the user interface. |
| `resolvedPath` | String | Available | Available | Full file pattern exported, with all the tokens resolved. |
| `firstFrame` | Integer | Available | Available | Frame number of the first frame exported. |
| `lastFrame` | Integer | Available | Available | Frame number of the last frame exported. |
| `versionName` | String | Available | Available | Current version name of the export.<br><br>Empty if unversioned. |
| `versionNumber` | Integer | Available | Available | Current version number of the export.<br><br>0 if unversioned. |
| `shotName` | String | Available | Available | Current shot name of the export. |
| `openClipNamePattern` | String | Available | Available | List of optional naming tokens pointing to the open clip created, if any, as entered in the user interface.<br><br>Only available if versioning is enabled. |
| `openClipResolvedPath` | String | Available | Available | Full path to the open clip created, if any, with all the tokens resolved.<br><br>Only available if versioning is enabled. |
| `setupNamePattern` | String | Available | Available | List of optional naming tokens pointing to the setup created, if any, as entered in the user interface.<br><br>Only available if versioning is enabled. |
| `setupResolvedPath` | String | Available | Available | Full path to the setup created, if any, with all the tokens resolved.<br><br>Only available if versioning is enabled. |
| `width` | Long | Available | Available | Frame width of the exported media. |
| `height` | Long | Available | Available | Frame height of the exported media. |
| `aspectRatio` | Double | Available | Available | Frame aspect ratio of the exported media. |
| `depth` | String | Available | Available | Frame depth of the exported media: `8-bits`, `10-bits`, `12-bits`, or `16 fp`. |
| `scanFormat` | String | Available | Available | Scan format of the exported media: `FIELD_1`, `FIELD_2`, or `PROGRESSIVE`. |
| `colourSpace` | String | Available |  | Colour space of the exported media. |
| `fps` | Double | Available | Available | Frame rate of the exported media. |
| `backgroundJobId` | String |  | Available | Identifier of the background job given by the Backburner Manager upon submission.<br><br>Empty if the export is done in the foreground. |
| `aborted` | Boolean | Modifiable | Available | Hook can set this to True if the export should be aborted.<br><br>In `batch_export_end`, True if the export was aborted by the user or by a render error. |
| `abortMessage` | String | Modifiable | Available | Error message describing why the export was aborted.<br><br>A generic message is used if left blank. |

 Note: When the export is done with Burn or Background Reactor, `batch_export_end` is called before the rendering of all frames is completed.

---

## Batch Hooks Examples

Examples are located in `/opt/Autodesk/<product>_<version>/python_utilities/scripts`.

| File | Description |
|---|---|
| `batch_write_file_quicktime.py` | Example of how to use `batch_export_end` to transcode the media exported by a Write File node to a QuickTime file. |
| `inject_metadata_write_file_exr.py` | Example of how to use `batch_export_begin` to inject custom metadata in the OpenEXR files written by a Write File node. |

## Related pages

- Python Hooks Reference
