# Custom User Interface Actions (Flame 2027)

> Source: "Custom User Interface Actions" (Autodesk Flame Family 2027 Help), with cross-references to "Python Hooks Reference", "Python Hooks Tips" and "Flame Python API Code Samples".

Custom UI actions are additional actions added to **context menus or drop-down buttons** in various application contexts. Each `get_*_custom_ui_actions` hook returns a description of menu entries; Flame builds the menu and calls your callables. A **keyboard shortcut is created for each custom action** and is available from the Shortcut Editor.

The no-op hook implementation and full description are located in `/opt/Autodesk/<PRODUCT>_<VERSION>/python/custom_actions.py`. Overview and discovery rules: [README.md](README.md).

## The 7 hooks

| Function (as written in source) | Menu | Multiple definitions |
|---|---|---|
| `get_main_menu_custom_ui_actions()` | Main menu. | Allowed |
| `get_media_panel_custom_ui_actions()` | Media Panel context menu. | Allowed |
| `get_mediahub_files_custom_ui_actions()` | MediaHub Files context menu. | Allowed |
| `get_mediahub_archives_custom_ui_actions()` | MediaHub Archives context menu. | Allowed |
| `get_timeline_custom_ui_actions()` | Timeline context menu. | Allowed |
| `get_batch_custom_ui_actions()` | Batch context menu. | Allowed |
| `get_action_custom_ui_actions()` | Action context menu. | Allowed |

- Signature: the source writes each hook with an **empty parameter list** `()`. It takes no documented arguments; the selection is passed later to your callables, not to the hook.
- When called: the source does not state *when* (or how often) Flame calls these hooks (e.g. once at scan time vs. each time a menu opens). Do not rely on either; keep the hook body cheap and side-effect free, and put dynamic logic in `isVisible` / `isEnabled` callables.
- Return: a **tuple** of group dictionaries and/or action dictionaries (see below).

### Multiple definitions (merging)

> **Source note:** Multiple definitions of the hooks functions can be implemented in multiple Python modules/files, and the output of all of them will be combined. The combination process merges the outputs in the order they are loaded, with later definitions potentially overriding earlier ones in case of conflicts.

What counts as a "conflict" is not defined (presumably identical names; not stated). Files must still have unique module names (see [README.md#naming](README.md#naming)).

---

## Return structure

> "Each hook returns a tuple of group dictionaries, where each dictionary represents a group of related actions. These groups are organised hierarchically to form a tree structure, allowing actions to be added to the standard Flame menus in a nested and organised manner."
>
> "Actions can be returned directly or inside a group which will add a sub section in the menu."
>
> "Actions and groups are dictionaries."

So the returned tuple may contain:
- **Action group dictionaries** → each creates a sub-section in the menu containing its `actions`.
- **Action dictionaries** returned directly (not inside a group).

```
return (                                   # tuple
    {"name": <group name>,                 # Action Group Dictionary
     "actions": (                          # tuple of Action Dictionaries
         {"name": ..., "execute": ...},
         ...,
     )},
    {"name": ..., "execute": ...},         # Action Dictionary returned directly
)
```

### Action Group Dictionary — every documented key

| Key | Type | Optional | Description |
|---|---|---|---|
| `name` | String | No | Name of the action group that will be created in the menu. |
| `actions` | Tuple | No | Tuple of action dictionaries. Each dictionary defines a menu item to be created in the group. |

### Action Dictionary — every documented key

| Key | Type | Optional | Default | Description |
|---|---|---|---|---|
| `name` | String | No | — | Name of the action. Also used as the caption if no `caption` is defined. Intended to be unique. |
| `caption` | String | Yes | value of `name` | Caption of the menu item. |
| `isEnabled` | Boolean / Callable | Yes | `True` | Boolean or callable object to enable/disable an action. The callable takes a tuple of selected Flame objects as a parameter. |
| `isVisible` | Boolean / Callable | Yes | `True` | Boolean or callable object to show/hide an action. The callable takes a tuple of selected Flame objects as a parameter. |
| `execute` | Callable | Yes | — | Action to execute upon selection. The callable takes a tuple of selected Flame objects as a parameter. |
| `minimumVersion` | String | Yes | — | Minimum application version (**inclusive**) that can use the action. If the application is older, the action will not be visible. |
| `maximumVersion` | String | Yes | — | Maximum application version (**inclusive**) that can use the action. If the application is newer, the action will not be visible. |

"A callable is any Python object implementing the `__call__` function." (So functions, lambdas, bound methods and instances of classes defining `__call__` are all valid — see installed example `custom_action_object.py`.)

### Keys that are NOT documented

The 2027 help page documents **only** the keys above. It does **not** document any of: `separator`, `hierarchy`, `order`, `waitCursor`, icons, tooltips, submenu nesting keys, or sorting/ordering controls. Do not use such keys based on this reference; if you see them in older code or in the installed `custom_actions.py`, treat them as unverified by this documentation set. (The Tips page lists an example `custom_menu_structure.py` — "two different menu structures … for the same custom actions" — and `wait_cursor.py` — "a Python hook overriding the default wait cursor" — without saying which keys they use. Read those installed files before using any extra key.)

Ambiguities:
- Whether a group's `actions` tuple may itself contain nested groups is **not** stated: the intro speaks of a hierarchical "tree structure", but the group table only says `actions` is a "Tuple of action dictionaries".
- The format of the version string for `minimumVersion` / `maximumVersion` is not specified (installed example: `version_scoping_hooks.py`).
- Whether `execute`'s return value is used is not stated; none is documented.

---

## The `selection` argument

All three callables (`isEnabled`, `isVisible`, `execute`) receive **one parameter: a tuple of selected Flame objects**.

What the tuple contains **per menu context is not documented** on the Custom UI Actions page. Evidence elsewhere in the sources (indirect, not a specification):

| Context | Evidence from sources | Likely object classes (see class reference) |
|---|---|---|
| Media Panel | `clean_batch_iteration.py`: "adds a … custom action to different Media Panel objects"; `manage_archived_clips.py`: action on "a clip selection"; `export_current_frame.py` / `export_selection.py`: "each selected clip in a selection". | Media Panel objects, e.g. [`PyClip`](../api/classes/PyClip.md), [`PyBatch`](../api/classes/PyBatch.md), [`PyFolder`](../api/classes/PyFolder.md), [`PyDesktop`](../api/classes/PyDesktop.md), [`PyLibrary`](../api/classes/PyLibrary.md), [`PyReel`](../api/classes/PyReel.md) … |
| MediaHub Files | `path_of_selected_clips.py`: "a simple custom action that can be run on a MediaHub Files object". | [`PyMediaHubFilesEntry`](../api/classes/PyMediaHubFilesEntry.md), [`PyMediaHubFilesFolder`](../api/classes/PyMediaHubFilesFolder.md) |
| Timeline | "Flame Python API Code Samples" page: a custom action `def action_1(selection)` iterates `for marker in selection` and uses `marker.parent` (code is garbled in the source). | [`PyMarker`](../api/classes/PyMarker.md), [`PySegment`](../api/classes/PySegment.md) … |
| Batch | `import_file_using_custom_dialog.py`: "a custom action scoped to the Batch Schematic background". | Batch nodes ([`PyNode`](../api/classes/PyNode.md) subclasses); background case not described |
| Action | `propagate_metadata_to_action_camera.py`: custom actions acting on "a Camera object in an Action node". | Action nodes ([`PyCoNode`](../api/classes/PyCoNode.md)) |
| MediaHub Archives, Main menu | Nothing in the sources. | Unknown |

> **Agent note:** because the contents are not specified, write `isVisible`/`isEnabled` callables that **type-check** the selection (e.g. `all(isinstance(o, flame.PyClip) for o in selection)`) — this is also the pattern the installed `object_scoping.py` is described as demonstrating ("how to scope custom actions to specific areas or objects"). Class names: [`../api/index.md`](../api/index.md).

---

## Examples (installed with Flame)

Located in `/opt/Autodesk/<PRODUCT>_<VERSION>/python_utilities/examples`. The help page provides **no inline code** for custom UI actions.

| File | Description |
|---|---|
| `custom_action_object.py` | Example of how custom actions can be any callable Python object. |
| `custom_menu_structure.py` | Examples of how two different menu structures can be defined for the same custom actions. |
| `version_scoping_hooks.py` | Examples of how custom actions can be limited to appear in some application versions only. |

Other installed files described on the Tips page as custom-action examples: `object_scoping.py`, `import_file_using_custom_dialog.py`, `post_export_dependency.py` (custom actions using `PyExporter`), `propagate_metadata_to_action_camera.py`, `show_messages.py`, `wait_cursor.py` (in `examples/`); `clean_batch_iteration.py`, `create_user_shared_library.py`, `export_current_frame.py`, `export_selection.py`, `manage_archived_clips.py`, `path_of_selected_clips.py` (in `scripts/`). See [tips-and-gotchas.md](tips-and-gotchas.md#installed-examples-and-scripts).

### Agent skeleton (derived from the documented keys only — not Autodesk code)

```python
import flame

def _is_clip_selection(selection):
    return len(selection) > 0 and all(isinstance(o, flame.PyClip) for o in selection)

def _print_names(selection):
    for item in selection:
        print(item.name)

def get_media_panel_custom_ui_actions():
    return (
        {
            "name": "My Studio Tools",              # group -> sub-section in the menu
            "actions": (
                {
                    "name": "Print Clip Names",     # required, intended unique
                    "caption": "Print Clip Names",  # optional, defaults to name
                    "isVisible": _is_clip_selection,  # bool or callable(selection)
                    "isEnabled": True,
                    "execute": _print_names,        # callable(selection)
                    "minimumVersion": "2027",       # inclusive; string format not specified by source
                },
            ),
        },
    )
```

Remember hooks block the UI while running ([README.md](README.md#execution-model)); long work in `execute` should use a thread or `flame.schedule_idle_event` (see [tips-and-gotchas.md](tips-and-gotchas.md#threading-hooks)).
