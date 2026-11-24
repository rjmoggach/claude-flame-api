# Batch Hooks (Flame 2027)

> Source: "Batch Hooks" (Autodesk Flame Family 2027 Help), with cross-references to "Python Hooks Tips".

13 hooks in 7 groups: setup, Batch Group, Batch FX, iteration, render, burn, export (Write File node). Overview and discovery rules: [README.md](README.md).

Items marked **[New in 2027.2]** carry a "NEW IN 2027.2 UPDATE" badge in the source HTML: the `source` argument of `batch_setup_loaded` (and its values table), the Batch Group Hooks section, and the Batch FX Hooks section. Do not rely on them in earlier releases.

## Two patterns

1. **Event hooks** — called once an event *has occurred* (setup loaded, Batch Group created, …). They receive the setup path or the Python object concerned and, "for most of them", a `source` argument (String) indicating how the event was triggered.
   Hooks: `batch_setup_loaded`, `batch_setup_saved`, `batch_group_created`, `batch_group_activated`, `batch_fx_created`.
2. **Paired hooks** — a `pre`/`post` or `begin`/`end` pair called before and after an action, to monitor, abort and react. **Both hooks of a pair receive an `info` dictionary and a `userData` dictionary.** The `userData` dictionary filled by the first hook is carried over into the second one, so it can pass data between the two.
   Pairs: `batch_setup_iterated_pre`/`_post`, `batch_render_begin`/`_end`, `batch_burn_begin`/`_end`, `batch_export_begin`/`_end`.

### Signatures

The help page names the arguments (`setupPath`, `source`, `batch_group`, `batch_fx_setup`, `info`, `userData`) but does **not** print full Python signatures or positional order. Authoritative signatures are in the installed hook files in `/opt/Autodesk/<PRODUCT>_<VERSION>/python/`.

> **Agent note (derived, unverified):** following the documented argument names, the order in which the source tables list them, and the forward-compatibility rule (variadic trailing parameters, see [README.md](README.md#signature-conventions)), defensive definitions look like:
>
> ```python
> def batch_setup_loaded(setupPath, *args, **kwargs): ...   # `source` arrives in args or kwargs: verify
> def batch_group_created(batch_group, *args, **kwargs): ... # `source` likewise
> def batch_render_begin(info, userData, *args, **kwargs): ...
> ```
>
> Whether `source` is passed positionally or by keyword is **not documented**; check the installed file before relying on either. Paired hooks change behaviour by mutating `info` in place; no return value is documented for any Batch hook.

### Abort-key naming differs between groups (gotcha)

| Group | Abort flag key | Message key |
|---|---|---|
| Iteration (`batch_setup_iterated_*`) | `abort` | `abortMessage` |
| Render / Burn / Export (`batch_render_*`, `batch_burn_*`, `batch_export_*`) | `aborted` | `abortMessage` |
| Project hooks (for comparison) | `abort` | `abort_message` |

---

## Batch Setup Hooks

| Function | When called |
|---|---|
| `batch_setup_loaded` | When a Batch setup is loaded. |
| `batch_setup_saved` | When a Batch setup is saved. |

Arguments:

| Argument | Type | Loaded | Saved | Description |
|---|---|---|---|---|
| `setupPath` | String | Available | Available | File path of the setup being loaded or saved. |
| `source` | String | Available **[New in 2027.2]** |  | How the setup was loaded. |

`batch_setup_saved` does **not** receive `source`.

`source` values for `batch_setup_loaded` **[New in 2027.2]**:

| Value | Description |
|---|---|
| `file_browser` | A setup loaded from the **Load Batch** file browser. |
| `open_as_batch_group` | A setup loaded when a Batch Group is opened, including with the **Open as Batch Group** option of an open clip that contains a Batch setup. |
| `load_iteration` | A setup loaded from an iteration other than the current one. |
| `startup` | A setup loaded with the execute batch setup (`-b`) switch when the application is started from a command line. |
| `create_new_version` | A setup loaded with the **Create New Version** option of an open clip that contains a Batch setup. |
| `promote_to_batch_fx` | A setup loaded with the **Promote to Batch FX** option of an open clip that contains a Batch setup. |

---

## Batch Group Hooks **[New in 2027.2]**

| Function | When called |
|---|---|
| `batch_group_created` | When a Batch Group is created. Use this hook to load a template setup upon creation. |
| `batch_group_activated` | When a Batch Group is set active. |

Arguments (same for both):

| Argument | Type | Created | Activated | Description |
|---|---|---|---|---|
| `batch_group` | `PyBatch` ([class ref](../api/classes/PyBatch.md)) | Available | Available | The Batch Group Python object. |
| `source` | String | Available | Available | How the Batch Group was created or set active. |

> **Source note:** Edit a new Batch Group through the `batch_group` argument rather than through `flame.batch`. For a Batch Group published to a Library, the Batch Group is loaded in memory and written back to its setup, and `flame.batch` does not point to it.

`source` values for `batch_group_created`:

| Value | Description |
|---|---|
| `media_panel` | A Batch Group created with the **Batch Group** option of the **New** submenu, in the context menu of a Media Panel item such as a Desktop. |
| `batch_new` | A Batch Group created with the **New** button in the Batch environment. |
| `timeline` | A Batch Group created with the **Create Batch Group** option in the context menu of a Timeline segment. |
| `timeline_convert_fx` | A Batch Group created with the **Create Batch Group (Convert TL FX)** option in the context menu of a Timeline segment. The Timeline FX are converted in the Batch Group. |
| `conform` | A Batch Group created with the **Create Batch Group** button in the Conform environment. |
| `shot_publish` | A Batch Group created during a Shot Publish operation, with the **Create Open Clip** and **Create Batch** options of the Shot Publish presets in Media Export. |
| `auto_replace` | A Batch Group created automatically when the last Batch Group of a Desktop is deleted. |

`source` values for `batch_group_activated`:

| Value | Description |
|---|---|
| `media_panel` | A Batch Group set active by clicking its icon in the Media Panel. |
| `desktop_reels` | A Batch Group set active by selecting it in a Desktop Reels drop-down. |

---

## Batch FX Hooks **[New in 2027.2]**

| Function | When called |
|---|---|
| `batch_fx_created` | When a Batch FX is created. Use this hook to load a template setup upon creation. |

Arguments:

| Argument | Type | Description |
|---|---|---|
| `batch_fx_setup` | `PyBatch` ([class ref](../api/classes/PyBatch.md)) | The newly created Batch FX setup. |
| `source` | String | How the Batch FX was created. |

`source` values for `batch_fx_created`:

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

| Function | When called |
|---|---|
| `batch_setup_iterated_pre` | Before a Batch iteration is created. Use it to change where the iteration is saved, or to validate information and potentially abort the iteration before it is saved. |
| `batch_setup_iterated_post` | After a Batch iteration is created. |

Arguments: `info` (dict), `userData` (dict, carried from `pre` to `post`).

`info` keys:

| Key | Type | Pre | Post | Description |
|---|---|---|---|---|
| `savePath` | String | Modifiable | Available | Path to which the Batch setup file of the iteration is saved on disk. |
| `setupName` | String | Modifiable | Available | Name of the Batch setup file of the iteration saved on disk. |
| `abort` | Boolean | Modifiable | Available | Hook can set this to True if the iteration should be aborted. In `batch_setup_iterated_post`, True if the save failed. |
| `abortMessage` | String | Modifiable | Available | Error message describing why the iteration was aborted. A generic message is used if left blank. |

> **Source note:** When `batch_setup_iterated_pre` aborts the iteration, `batch_setup_iterated_post` is not called. The `abort` key of `batch_setup_iterated_post` therefore only indicates an actual error, and **is not defined when the save succeeds**.
>
> **Agent note:** read it with `info.get("abort", False)` in `batch_setup_iterated_post` — indexing `info["abort"]` would raise `KeyError` on success.

---

## Batch Render Hooks

| Function | When called |
|---|---|
| `batch_render_begin` | Before a render begins. Use it to change the Backburner job name, or to validate information and potentially abort the render before it starts. |
| `batch_render_end` | When a render ends. |

Arguments: `info` (dict), `userData` (dict, carried from `begin` to `end`).

`info` keys:

| Key | Type | Begin | End | Description |
|---|---|---|---|---|
| `backgroundJobName` | String | Modifiable | Available | Job name as shown in Backburner. |
| `backgroundJobId` | String |  | Available | Identifier of the background job given by the Backburner Manager upon submission. |
| `aborted` | Boolean | Modifiable | Available | Hook can set this to True if the render should be aborted. In `batch_render_end`, True if the render was aborted by the user or by a render error. |
| `abortMessage` | String | Modifiable | Available | Error message describing why the render was aborted. A generic message is used if left blank. |

> **Source note:** When the render is done with Burn or Background Reactor, `batch_render_end` is called **before** the rendering of all frames is completed.

---

## Batch Burn Hooks

| Function | When called |
|---|---|
| `batch_burn_begin` | Before a job is sent to Burn or Background Reactor. Use it to validate information and potentially abort the job before it is sent. |
| `batch_burn_end` | After a job is sent to Burn or Background Reactor. |

Arguments: `info` (dict), `userData` (dict, carried from `begin` to `end`).

`info` keys:

| Key | Type | Begin | End | Description |
|---|---|---|---|---|
| `backgroundJobId` | String |  | Available | Identifier of the background job given by the Backburner Manager upon submission. |
| `aborted` | Boolean | Modifiable | Available | Hook can set this to True if the job should be aborted. In `batch_burn_end`, True if the job was aborted by the user or by an error. |
| `abortMessage` | String | Modifiable | Available | Error message describing why the job was aborted. A generic message is used if left blank. |

Note: `batch_burn_end` fires after the job is *sent*, not after it finishes rendering.

---

## Batch Export Hooks (Write File node)

| Function | When called |
|---|---|
| `batch_export_begin` | Before a Write File node starts to export. Use it to change where the files are written, or to validate information and potentially abort the export before it starts. |
| `batch_export_end` | When a Write File node ends the export. |

> **Source note:** For stereo exports, both hooks are called **twice**, once for each channel: left first, and right second.

Arguments: `info` (dict), `userData` (dict, carried from `begin` to `end`).

`info` keys:

| Key | Type | Begin | End | Description |
|---|---|---|---|---|
| `nodeName` | String | Available | Available | Name of the Write File node. |
| `exportPath` | String | Modifiable | Available | Export path as entered in the user interface. Hook can modify it to change where the files are written. |
| `namePattern` | String | Available | Available | List of optional naming tokens as entered in the user interface. |
| `resolvedPath` | String | Available | Available | Full file pattern exported, with all the tokens resolved. |
| `firstFrame` | Integer | Available | Available | Frame number of the first frame exported. |
| `lastFrame` | Integer | Available | Available | Frame number of the last frame exported. |
| `versionName` | String | Available | Available | Current version name of the export. Empty if unversioned. |
| `versionNumber` | Integer | Available | Available | Current version number of the export. 0 if unversioned. |
| `shotName` | String | Available | Available | Current shot name of the export. |
| `openClipNamePattern` | String | Available | Available | List of optional naming tokens pointing to the open clip created, if any, as entered in the user interface. Only available if versioning is enabled. |
| `openClipResolvedPath` | String | Available | Available | Full path to the open clip created, if any, with all the tokens resolved. Only available if versioning is enabled. |
| `setupNamePattern` | String | Available | Available | List of optional naming tokens pointing to the setup created, if any, as entered in the user interface. Only available if versioning is enabled. |
| `setupResolvedPath` | String | Available | Available | Full path to the setup created, if any, with all the tokens resolved. Only available if versioning is enabled. |
| `width` | Long | Available | Available | Frame width of the exported media. |
| `height` | Long | Available | Available | Frame height of the exported media. |
| `aspectRatio` | Double | Available | Available | Frame aspect ratio of the exported media. |
| `depth` | String | Available | Available | Frame depth of the exported media: `8-bits`, `10-bits`, `12-bits`, or `16 fp`. |
| `scanFormat` | String | Available | Available | Scan format of the exported media: `FIELD_1`, `FIELD_2`, or `PROGRESSIVE`. |
| `colourSpace` | String | Available |  | Colour space of the exported media. **Begin only.** |
| `fps` | Double | Available | Available | Frame rate of the exported media. |
| `backgroundJobId` | String |  | Available | Identifier of the background job given by the Backburner Manager upon submission. Empty if the export is done in the foreground. |
| `aborted` | Boolean | Modifiable | Available | Hook can set this to True if the export should be aborted. In `batch_export_end`, True if the export was aborted by the user or by a render error. |
| `abortMessage` | String | Modifiable | Available | Error message describing why the export was aborted. A generic message is used if left blank. |

Notes:
- Only `exportPath`, `aborted`, `abortMessage` are Modifiable (in `batch_export_begin`).
- `namePattern`, `openClipNamePattern`, `setupNamePattern` are typed String although described as a "List of optional naming tokens" — the source does not clarify the format (presumably the pattern string as typed in the UI).
- "Long"/"Double"/"Integer" are the source's type names; in Python these are `int`/`float`.

> **Source note:** When the export is done with Burn or Background Reactor, `batch_export_end` is called **before** the rendering of all frames is completed.

Custom tokens for the Write File node Pattern / Create Open Clip / Include Setup fields: [tokens-hooks.md](tokens-hooks.md) (context `Export`).

---

## Examples (installed with Flame)

Located in `/opt/Autodesk/<product>_<version>/python_utilities/scripts`. The help page lists them but does **not** reproduce their code.

| File | Description |
|---|---|
| `batch_write_file_quicktime.py` | Example of how to use `batch_export_end` to transcode the media exported by a Write File node to a QuickTime file. |
| `inject_metadata_write_file_exr.py` | Example of how to use `batch_export_begin` to inject custom metadata in the OpenEXR files written by a Write File node. (Marked "NEW IN 2027" on the Tips page.) |
