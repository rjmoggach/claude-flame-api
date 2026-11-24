# Python Hooks: Tips and Gotchas (Flame 2027)

> Source: "Python Hooks Tips", plus notes and warnings from "Python Hooks Reference", "Project Hooks", "Batch Hooks", "Tokens Hooks" and "Custom User Interface Actions" (Autodesk Flame Family 2027 Help).

The hooks themselves are documented in the `.py` files in `/opt/Autodesk/<PRODUCT>_<VERSION>/python/`.

## Gotcha checklist (all pages)

1. **Hooks block the application.** "Hooks are blocking, and relinquish control only once they complete." Move slow work to a thread ([Threading Hooks](#threading-hooks)).
2. **Unique file names.** Python does not support two files (modules) of the same name. If you use more than one hook location, give every file a unique name.
3. **Forward compatibility.** Example hooks put variadic parameters last so that Flame can add parameters in future versions. Your hooks should do the same and ignore extra parameters. New parameters should not change the values of the ones already passed.
4. **Multiple definitions.** Hooks without a return value: every definition is called once. Hooks with a return value: handling varies, "usually" the union of the return values. Custom UI action outputs are merged in load order, and later definitions may override earlier ones on conflict.
5. **Abort key names differ:**
   - Project hooks: `abort` / `abort_message`.
   - Batch iteration hooks: `abort` / `abortMessage`.
   - Batch render, burn and export hooks: `aborted` / `abortMessage`.

   A misspelt key silently does nothing (agent inference: the hook only mutates a dict).
6. **`batch_setup_iterated_post`:** `abort` is **not defined** when the save succeeds. Use `info.get("abort")`. If `batch_setup_iterated_pre` aborts, `_post` is not called.
7. **Burn / Background Reactor:** `batch_render_end` and `batch_export_end` are called **before** all frames are rendered. Do not assume the files are complete in the `_end` hook.
8. **Stereo Write File exports:** `batch_export_begin` and `batch_export_end` are each called **twice**, left channel first, then right.
9. **`colourSpace`** is only in `batch_export_begin`, not in `_end`. `backgroundJobId` is empty for foreground exports.
10. **Batch Group created from a Library:** edit it through the `batch_group` argument, not `flame.batch`. For a Batch Group published to a Library, `flame.batch` does not point to it.
11. **Project path tokens:** tokens appear unresolved in `project_init_*` and are already resolved in `project_pre_*` and `project_post_*`.
12. **`project_uuid` availability:** present in both delete hooks, both edition hooks, `project_post_creation` and `project_post_conversion` only. It is absent from all `init`/`pre` creation and conversion hooks and from **all restore hooks**.
13. **Tokens:** the Browsing context uses `{name}`, all other contexts use `<name>`. Resolving a token takes more than 0.05 s → warning printed to the terminal and to the app log. **Dynamic** tokens re-run constantly and Flame has no caching, so add your own cache.
14. **Locked Shared Libraries:** export hooks in the context menu for Shared Libraries are always accessible, regardless of lock status. If the library is locked when the export hook is called, and the selected preset re-imports the exported material with the source clip in the library, the **re-import fails silently**.
15. **New-version features:**
   - The Tokens hooks are new in 2027.1.
   - New in 2027.2: `batch_setup_loaded`'s `source` argument, `batch_group_created`, `batch_group_activated` and `batch_fx_created`.

   Guard with version checks if your tool targets older releases. For custom UI actions, `minimumVersion` / `maximumVersion` exist.
16. **Wiretap import path:** use `from adsk import libwiretapPythonClientAPI` ([below](#libwiretappythonclientapiso)).

---

## Installed examples and scripts

**Examples** are in `/opt/Autodesk/<PRODUCT>_<VERSION>/python_utilities/examples/`. They are "simple, incomplete solution snippets that demonstrate and explain code concepts rather than complete implementations."

| Filename | Description |
|---|---|
| `context_variables.py` | Simple samples of utility methods used to manage OCIO Context Variables. |
| `conversion_description.py` | Example of how to use the project conversion hook to edit information in the description of a converted project. |
| `custom_action_object.py` | Example of how custom actions can be any callable Python object. |
| `custom_menu_structure.py` | Examples demonstrating how to define two different menu structures for the same custom actions. |
| `import_file_using_custom_dialog.py` | Demonstrates how a clip can be imported in Batch Group using a Qt File Dialog or a Flame Browser through a custom action scoped to the Batch Schematic background. |
| `object_scoping.py` | Example demonstrating how to scope custom actions to specific areas or objects. |
| `post_export_asset_after_snapshot.py` | Example demonstrating how to scope the post_export_asset hook to be called only after a snapshot operation. |
| `post_export_dependency.py` | Examples of custom actions that use the Python export API (PyExporter). |
| `project_protection.py` | Example demonstrating how to use the project hooks abort mechanism to prevent modification of a project. |
| `propagate_metadata_to_action_camera.py` | Example of custom actions used to propagate information in the metadata keys of a clip to parameters of a Camera object in an Action node. (NEW IN 2027) |
| `show_messages.py` | Example of messages presented in the message bar/console or a dialog window via a custom action. |
| `version_scoping_hooks.py` | Example demonstrating how custom actions can be limited to appear in specific software versions only. |
| `wait_cursor.py` | Example of a Python hook overriding the default wait cursor while running to enable use of another GUI. |
| `watch_folder.py` | Example on how to leverage the Idle event callback to perform operations during Flame's user interface idle time. |

**Scripts** are more complete solutions, in `/opt/Autodesk/<PRODUCT>_<VERSION>/python_utilities/scripts/`.

| Filename | Description |
|---|---|
| `batch_write_file_quicktime.py` | Example of a hook that transcodes exported media from a Batch Write File node to a QuickTime file as a post-export process. |
| `cache_motion_vectors.py` | Script that creates Motion Vector Maps for a Clip node located in the Batch Schematic. |
| `clean_batch_iteration.py` | Script that adds a Clean Batch Iterations custom action to different Media Panel objects. When selected, the content of a Batch Group's Iterations folder is emptied. |
| `create_user_shared_library.py` | Example demonstrating how a Python hook can be used to fetch the current user for later use in custom actions. |
| `export_current_frame.py` | Example of a custom action that exports the current frame of each selected clip in a selection. |
| `export_selection.py` | Example of a custom user interface action that exports a thumbnail and a movie for all clips in a selection. |
| `inject_metadata_write_file_exr.py` | Example of a hook injecting metadata into OpenEXR files written by the Write File node in Batch. (NEW IN 2027) |
| `manage_archived_clips.py` | Example of a custom action that removes archived clips from a clip selection. |
| `path_of_selected_clips.py` | Example of a simple custom action that can be run on a MediaHub Files object. |

Also referenced on other pages: `custom_tokens.py` in `.../python_utilities/examples`, which defines and resolves custom tokens and shows a caching strategy.

Path inconsistency: the Python Hooks Reference page says "Samples and example files are located in `/opt/Autodesk/<application>/python_examples/`". Every other page uses `/opt/Autodesk/<PRODUCT>_<VERSION>/python_utilities/examples/` (and `.../scripts/`). The `python_utilities` paths are the more specific and more frequently cited ones.

---

## Passing the Project Name Between Hooks

Use the `app_initialized` hook, which "is called whenever the project changes". Assign the project name it receives to a global variable that other hooks can read.

```python
global_project_name = ""

def app_initialized(project_name):
    global global_project_name
    global_project_name = project_name
```

---

## Environment Variables

### `DL_PYTHON_HOOK_PATH`

Sets the path to the Python hook files. It behaves like other PATH variables: separate multiple paths with `:`.

```sh
export DL_PYTHON_HOOK_PATH=/share_1/dev/python_hooks/test:/share_1/dev/python_hooks/production
```

In this example Flame loads the hooks from `test` first. For any hooks still undefined, it continues to scan `production`.

The Reference page says this variable makes Flame "scan a directory other than `/opt/Autodesk/<PRODUCT>_<VERSION>/python`". Neither page says whether the default locations are still scanned when it is set.

### `DL_DEBUG_PYTHON_HOOKS`

Enables verbose output from hooks, which simplifies debugging. It writes to the shell:
- which hooks are loaded from which files;
- the data sent to each hook that is triggered.

```sh
export DL_DEBUG_PYTHON_HOOKS=1
```

---

## Reloading Hooks from Within the Application

A keyboard shortcut re-scans the hook files while the application is running, which helps when testing changes. Its default mapping is **Ctrl+Shift+P+H**. In the Keyboard Shortcuts Editor it is named *Scan for python hooks*. The Tokens page calls the same feature the **Rescan Python Hooks** function. Rescanning also re-resolves tokens.

> **Agent note:** to trigger it from code, `flame.execute_shortcut` exists ([../api/flame-module-functions.md](../api/flame-module-functions.md)). The sources do not confirm that the shortcut name *Scan for python hooks* works as its argument.

---

## Threading Hooks

Python hooks block the application until they finish. To avoid this, run the hook's work in its own thread. The source example runs `render_ended()` in a separate thread:

```python
from threading import Thread
import atexit

#threads is a list used to keep track of all the threads created
threads = []

def wait_for_threads_at_exit():
    global threads
    if len(threads) > 0:
        for thread in threads:
            print("Waiting for %s" % thread.name)
            # join() waits for the thread to finish before relinquishing
            # control, ensuring everything is done before exit.
            thread.join()
    threads = []

# Clean up by Python on exit
atexit.register(wait_for_threads_at_exit)

# The actual code to execute in a thread.
def async_callback(param1, param2):
    print("async_callback(%s, %s)\n" % (str(param1), str(param2)))

# render_ended is the actual hook called by the application,
# with its standard moduleName, sequenceName, and elapsedTimeInSeconds
# parameters.
def render_ended(moduleName, sequenceName, elapsedTimeInSeconds):
    # Creates the separate thread
    thread = Thread(
        target=async_callback,
        name="async callback",
        args=(moduleName, sequenceName, ))
    thread.start()

    # Add to threads[] the just-created thread to keep track and
    # clean up on exit.
    threads.append(thread)
```

> **Agent note:** the API reference documents `flame.schedule_idle_event(function, delay=0)`, which runs a callback later on the main application thread and must be quick and non-blocking ([../api/object-model.md](../api/object-model.md), [../api/flame-module-functions.md](../api/flame-module-functions.md)). The sources do not say whether Flame objects may be accessed from worker threads, and the threading example only prints. The conservative pattern is to do slow non-Flame work (I/O, network) in the thread and hand results back with `schedule_idle_event`.

---

## Hooks and Locked Shared Libraries

Export hooks in the context menu for Shared Libraries are always accessible, regardless of lock status. However, if the shared library is locked when the export hook is called, and if the selected preset re-imports the exported material with the source clip in the library, the re-import fails silently.

---

## `libwiretapPythonClientAPI.so`

`libwiretapPythonClientAPI.so` is located in `/opt/Autodesk/python/<VERSION>/lib/python<PYTHON_VERSION>/site-packages/adsk/`, so it is in the right folder for Python hooks to make Wiretap calls.

A symlink to it also exists in `/opt/Autodesk/<PRODUCT>_<VERSION>/python/`, so older code keeps working. **However**, hooks should be updated to use the site-package version:

```python
# old
import libwiretapPythonClientAPI
# new
from adsk import libwiretapPythonClientAPI
```

---

## Export hooks call order

Moved to [export-hooks.md](export-hooks.md). In summary: `pre_custom_export` (optional) → `pre_export` → `pre_export_sequence` → `pre_export_asset` → `post_export_asset` (per asset) → `post_export_sequence` → `post_export` → `post_custom_export` (optional). The sources spell these names inconsistently; see that file.

---

## Other notes from the hook pages

- **Third-party packages (Reference):** Flame ships its own Python in `/opt/Autodesk/python/<VERSION>/`. Install packages into it with `/opt/Autodesk/python/<VERSION>/bin/pip` rather than into the system Python.
- **Project location (Reference):** for hooks in `/opt/Autodesk/project/<project name>/python`, "In the future, any python files located there will be copied with the project when the project is converted to a new version." This is stated as future behaviour, so do not rely on it in 2027.
- **Tokens printing (Tokens):** `print()` output from hooks goes to the Konsole/Terminal from which Flame was started.
- **Custom UI actions (Custom UI):** a keyboard shortcut is created automatically for each custom action and is listed in the Shortcut Editor.
