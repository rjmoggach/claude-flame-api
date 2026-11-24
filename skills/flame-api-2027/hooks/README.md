# Flame 2027 Python Hooks: Overview and Index

> Source: "Python Hooks Reference", plus "Project Hooks", "Batch Hooks", "Tokens Hooks", "Custom User Interface Actions" and "Python Hooks Tips" (Autodesk Flame Family 2027 Help).

Python hooks are "places where external Python code can be injected to monitor, inspect, or change the behaviour of the application". Typical uses: integrating Flame with a shot management system, monitoring archives, and controlling how Batch setups are named. A hook is a **module-level function with a reserved name** in a `.py` file that Flame scans. Flame calls it when the corresponding event happens.

The object API used inside hooks is documented in [../api/index.md](../api/index.md).

## Files in this directory

| File | Contents |
|---|---|
| [project-hooks.md](project-hooks.md) | 13 project lifecycle hooks (`project_init_*`, `project_pre_*`, `project_post_*`): creation, delete, edition, conversion, restore. |
| [batch-hooks.md](batch-hooks.md) | 13 Batch hooks: setup loaded/saved, Batch Group, Batch FX, iteration, render, burn, Write File export. |
| [tokens-hooks.md](tokens-hooks.md) | `get_hook_token_list`, `resolve_hook_token`: custom **Add Token** entries (2027.1+). |
| [custom-ui-actions.md](custom-ui-actions.md) | 7 `get_*_custom_ui_actions` hooks: the menu dict structure and the selection argument. |
| [export-hooks.md](export-hooks.md) | `exportHook.py` call order (`pre_export`, `post_export_asset`, …) and the `PyExporter` hook override. Only partly documented in the sources. |
| [other-hooks.md](other-hooks.md) | `app_initialized`, `render_ended`: hooks that appear only in the Tips examples. |
| [tips-and-gotchas.md](tips-and-gotchas.md) | Environment variables, reloading, threading, Wiretap import, installed example files, and a consolidated gotcha checklist. |

---

## Hook file locations

The Reference page says: "All Python hook files are located in `/opt/Autodesk/<application>/python/`." The **no-op/description files** that Autodesk installs there document each hook's parameters ("The hooks parameters and usage are documented within the Python files located in `/opt/Autodesk/<application>/python/`"). Named files include `custom_actions.py`, `tokens_hook.py` and `exportHook.py` (also spelled `exportHooks.py` elsewhere).

To add your own hooks, put a `.py` file in one of these locations:

| Scope | Path |
|---|---|
| A specific user (Linux) | `/home/<user name>/flame/python` |
| A specific user (macOS) | `/Users/<user name>/Library/Preferences/Autodesk/flame/python` |
| A specific project | `/opt/Autodesk/project/<project name>/python`. The source says "In the future, any python files located there will be copied with the project when the project is converted to a new version." |
| A specific application version | `/opt/Autodesk/<PRODUCT>_<VERSION>/python` |
| Global shared location | `/opt/Autodesk/shared/python`: "Will be used by all users and projects in all versions." |

### `DL_PYTHON_HOOK_PATH`

Setting `DL_PYTHON_HOOK_PATH` makes Flame scan another directory, "other than `/opt/Autodesk/<PRODUCT>_<VERSION>/python`", for `.py` files. Separate multiple paths with `:`. Paths are searched in order: in the Tips example, hooks load from the first path, and the scan continues into later paths only for hooks that are still undefined.

```sh
export DL_PYTHON_HOOK_PATH=/share_1/dev/python_hooks/test:/share_1/dev/python_hooks/production
```

The sources do not say:
- whether the default locations are still scanned when the variable is set;
- the relative precedence of the user, project, version and shared locations.

### Discovery and loading

- "Flame loads modules, searching for supported methods until all supported hooks are found." Hook implementations can therefore be split across several files.
- Debugging: `export DL_DEBUG_PYTHON_HOOKS=1` prints which hooks load from which files, and the data sent to each hook that is triggered.
- **Reloading:** the *Scan for python hooks* keyboard shortcut (default **Ctrl+Shift+P+H**, listed in the Keyboard Shortcuts Editor) rescans the hook files while Flame runs. The Tokens page calls this **Rescan Python Hooks**. Hooks are also scanned when the application launches.

## Naming

- Python does not support two files (modules) with the same name. Hook files must have **unique file names** across all scanned locations.
- Some hooks support **multiple definitions** across files:
  - Hooks that return nothing: **every** definition is called once when the hook point is reached.
  - Hooks that return values: handling "might vary", but "will usually result in the union of the return values". For the `get_*_custom_ui_actions` hooks, outputs are merged in load order, and later definitions may override earlier ones on conflict.

The sources mark multiple definitions as "Allowed" only for the custom UI action hooks. They do not say which other hooks support them.

## Signature conventions

- "Python Hooks are designed to be forward-compatible as much as possible. With that mindset, example hooks are implemented with **variadic arguments as the last parameters** to allow new parameters to be added in future versions. These parameters are meant to be ignored and new parameters should not change the values of previously passed ones."
- The help pages give argument **names** and dict **keys**, but mostly not full `def` lines. The exceptions are:
  - `get_*_custom_ui_actions()`, written with no parameters;
  - `app_initialized(project_name)`;
  - `render_ended(moduleName, sequenceName, elapsedTimeInSeconds)`;
  - the `PyExporter` hook-override methods `(self, info, userData, *args, **kwargs)`.

  For everything else, copy the exact signature from the installed no-op files in `/opt/Autodesk/<PRODUCT>_<VERSION>/python/`.
- Common shapes in the sources:
  - **`info` dict** (project, Batch paired and export hooks). Read keys from it, and change *Modifiable* keys **in place** to alter behaviour or to abort.
  - **`userData` dict**: Batch paired hooks and export hooks. It is filled by the first hook of a pair and carried over to the second.
  - **Event arguments**, such as `setupPath`, `batch_group`, `batch_fx_setup` and `source` (String).
  - **Return-value hooks**: `get_*_custom_ui_actions`, `get_hook_token_list` and `resolve_hook_token`.
- Naming style differs between families. Project, Batch and Tokens hooks are snake_case functions. Batch `info` keys are camelCase (`savePath`, `abortMessage`), while project `info` keys are snake_case (`abort_message`).

> **Agent note:** the defensive pattern, derived from the rule above, is `def hook_name(<documented args>, *args, **kwargs):`. Read optional keys with `info.get(...)`.

## Execution model

- "Hooks are blocking, and relinquish control only once they complete." Long work must run in a thread; see [tips-and-gotchas.md#threading-hooks](tips-and-gotchas.md#threading-hooks).
- `print()` output goes to the Konsole/Terminal from which Flame was started.

## Third-party packages

Flame ships its own Python distribution in `/opt/Autodesk/python/<VERSION>/`, to avoid disrupting the system Python. Install third-party site-packages into it with `/opt/Autodesk/python/<VERSION>/bin/pip`.

---

## Complete hook table

Legend:
- **Args** are the names documented in the sources. "Signature not printed" means the order and the full `def` line must come from the installed file.
- **Return** "—" means no return value is documented; the effect is achieved by mutating `info`.
- **2027.x** marks features flagged as new in an update release.

### Project hooks: [project-hooks.md](project-hooks.md)

| Hook | Fires | Args | Return / effect |
|---|---|---|---|
| `project_init_creation` | Create New Project panel opened | `info` (dict) | —; Modifiable: `project_name`, `project_description`, `project_nickname`, `project_home`, `project_setups_dir`, `project_media_dir` (paths may contain tokens) pre-fill the panel |
| `project_pre_creation` | Before a project is created | `info` | —; set `info["abort"]=True`, `info["abort_message"]` to abort |
| `project_post_creation` | After a project is created | `info` (incl. `project_uuid`) | — |
| `project_pre_delete` | Before a project is deleted | `info` (`project_name`, `project_uuid`, `abort`, `abort_message`) | —; abort via `abort` / `abort_message` |
| `project_post_delete` | After a project is deleted | `info` (`project_name`, `project_uuid`) | — |
| `project_pre_edition` | Before a project is edited | `info` | —; abort via `abort` / `abort_message` |
| `project_post_edition` | After a project is edited | `info` | — |
| `project_init_conversion` | Convert Legacy Project to Compatible Format window opened | `info` (+ `copy_project`) | —; Modifiable keys pre-fill the window |
| `project_pre_conversion` | Before a project is converted | `info` | —; abort via `abort` / `abort_message` |
| `project_post_conversion` | After a project is converted | `info` (incl. `project_uuid`) | — |
| `project_init_restore` | Project Restore window opened | `info` | —; Modifiable keys pre-fill the window |
| `project_pre_restore` | Before a project is restored | `info` | —; abort via `abort` / `abort_message` |
| `project_post_restore` | After a project is restored | `info` (no `project_uuid`) | — |

### Batch hooks: [batch-hooks.md](batch-hooks.md)

| Hook | Fires | Args | Return / effect |
|---|---|---|---|
| `batch_setup_loaded` | A Batch setup is loaded | `setupPath` (str), `source` (str, 2027.2) | — |
| `batch_setup_saved` | A Batch setup is saved | `setupPath` (str) | — |
| `batch_group_created` (2027.2) | A Batch Group is created | `batch_group` (`PyBatch`), `source` (str) | —; e.g. load a template setup into `batch_group` |
| `batch_group_activated` (2027.2) | A Batch Group is set active | `batch_group` (`PyBatch`), `source` (str) | — |
| `batch_fx_created` (2027.2) | A Batch FX is created | `batch_fx_setup` (`PyBatch`), `source` (str) | —; e.g. load a template setup |
| `batch_setup_iterated_pre` | Before a Batch iteration is created | `info`, `userData` | —; Modifiable `savePath`, `setupName`, `abort`, `abortMessage` |
| `batch_setup_iterated_post` | After a Batch iteration is created (not called if `_pre` aborted) | `info`, `userData` | —; `info.get("abort")` is True if the save failed (key absent on success) |
| `batch_render_begin` | Before a render begins | `info`, `userData` | —; Modifiable `backgroundJobName`, `aborted`, `abortMessage` |
| `batch_render_end` | When a render ends (with Burn/Background Reactor: before all frames are done) | `info`, `userData` | —; `backgroundJobId`, `aborted` |
| `batch_burn_begin` | Before a job is sent to Burn / Background Reactor | `info`, `userData` | —; Modifiable `aborted`, `abortMessage` |
| `batch_burn_end` | After a job is sent to Burn / Background Reactor | `info`, `userData` | —; `backgroundJobId`, `aborted` |
| `batch_export_begin` | Before a Write File node starts to export (twice for stereo) | `info`, `userData` | —; Modifiable `exportPath`, `aborted`, `abortMessage` |
| `batch_export_end` | When a Write File node export ends (twice for stereo; with Burn/BG Reactor: before frames are done) | `info`, `userData` | — |

### Tokens hooks (2027.1): [tokens-hooks.md](tokens-hooks.md)

| Hook | Fires | Args | Return / effect |
|---|---|---|---|
| `get_hook_token_list` | To get the tokens available for a context (Add Token drop-downs) | `context` (str, e.g. `"Export"`); signature not printed | Tuple of dicts `{"name": "<tok>", "displayName": "..."}` (`{tok}` in the `Browsing` context) |
| `resolve_hook_token` | To resolve a token to its value (repeatedly when Dynamic) | `token_name` (str), `context_info` (dict-like, keys such as `"<user>"`); signature not printed | Resolved value (a str in every example) |

### Custom UI action hooks: [custom-ui-actions.md](custom-ui-actions.md)

All take no parameters. Each returns a tuple of action-group dicts `{"name", "actions"}` and/or action dicts with the keys `name`, `caption`, `isEnabled`, `isVisible`, `execute`, `minimumVersion`, `maximumVersion`. The callables receive a tuple of selected Flame objects. Multiple definitions are allowed and are merged.

| Hook | Menu |
|---|---|
| `get_main_menu_custom_ui_actions()` | Main menu |
| `get_media_panel_custom_ui_actions()` | Media Panel context menu |
| `get_mediahub_files_custom_ui_actions()` | MediaHub Files context menu |
| `get_mediahub_archives_custom_ui_actions()` | MediaHub Archives context menu |
| `get_timeline_custom_ui_actions()` | Timeline context menu |
| `get_batch_custom_ui_actions()` | Batch context menu |
| `get_action_custom_ui_actions()` | Action context menu |

### Export hooks (`exportHook.py`): [export-hooks.md](export-hooks.md)

Names follow the Tips page text. The sources also use camelCase variants; see the file for details.

| Hook | Fires | Args | Return / effect |
|---|---|---|---|
| `get_custom_export_profiles` / `getCustomExportProfiles` | To populate the context menu with custom export options | Not documented | Not documented (the list of custom export options) |
| `pre_custom_export` | Optional, when a custom export menu item is selected | `info`, `userData` (diagram) | Not documented |
| `pre_export` | Always; as the Export dialog is displayed (regular export) or after `pre_custom_export` (custom export) | `info`, `userData` | Not documented |
| `pre_export_sequence` | Always; before writing the sequence | `info`, `userData` | Not documented |
| `pre_export_asset` | Always; for each asset, all at once in Foreground Export, or as each job is submitted in Background Export | `info`, `userData` | Not documented |
| `post_export_asset` | Always; after an asset is written (possibly in Backburner, per `useBackburnerPostExportAsset`) | `info`, `userData` | Not documented |
| `post_export_sequence` | Always; after `post_export_asset` | `info`, `userData` | Not documented |
| `post_export` | Always; after `post_export_sequence` | `info`, `userData` | Not documented |
| `post_custom_export` | Optional; after `post_export` | `info`, `userData` (diagram) | Not documented |
| `useBackburnerPostExportAsset` | Determines whether `post_export_asset` runs in Backburner; whether it is a hook is not stated | Not documented | Not documented |
| `exportOverwriteFile` | `PyExporter.export(hooks=...)` override object only | `self, path, *args, **kwargs` | `"ask"` or `"overwrite"` |

### Other hooks: [other-hooks.md](other-hooks.md)

| Hook | Fires | Args | Return / effect |
|---|---|---|---|
| `app_initialized` | "whenever the project changes" | `project_name` | — |
| `render_ended` | Not described (example only) | `moduleName`, `sequenceName`, `elapsedTimeInSeconds` | — |

**Count:**
- 46 hook functions are named by the help pages: Project 13, Batch 13, Tokens 2, Custom UI 7, Export 9 (`get_custom_export_profiles` plus 8 pre/post hooks), Other 2.
- Two further export-related names are listed above but are not standard module-level hooks: `useBackburnerPostExportAsset` (nature unclear) and `exportOverwriteFile` (`PyExporter` override only).
