<!-- source: Autodesk Flame Family 2027 Help _ Custom User Interface Actions _ Autodesk.html -->
# Custom User Interface Actions

Custom user interface actions are additional actions that can be added to context menus or drop-down buttons in various application contexts.

A keyboard shortcut is created for each custom action and is available from the Shortcut Editor.

---

## Custom User Interface Actions Hook Definition

Each hook returns a tuple of group dictionaries, where each dictionary represents a group of related actions. These groups are organised hierarchically to form a tree structure, allowing actions to be added to the standard Flame menus in a nested and organised manner.

Actions can be returned directly or inside a group which will add a sub section in the menu.

Actions and groups are dictionaries.

### Action Dictionary

| Key | Type | Optional | Description |
|---|---|---|---|
| `name` | String | No | Name of the action. Will also be used as the caption if no caption is defined. Intended to be unique. |
| `caption` | String | Yes | Caption of the menu item. Defaults to `name` if not defined. |
| `isEnabled` | Boolean/Callable | Yes | Boolean or callable object to enable/disable an action. Defaults to `True` if not defined. The callable takes a tuple of selected Flame objects as a parameter. |
| `isVisible` | Boolean/Callable | Yes | Boolean or callable object to show/hide an action. Defaults to `True` if not defined. The callable takes a tuple of selected Flame objects as a parameter. |
| `execute` | Callable | Yes | Action to execute upon selection. The callable takes a tuple of selected Flame objects as a parameter. |
| `minimumVersion` | String | Yes | Minimum application version (inclusive) that can use the action. If the application is older, the action will not be visible. |
| `maximumVersion` | String | Yes | Maximum application version (inclusive) that can use the action. If the application is newer, the action will not be visible. |

A callable is any Python object implementing the `__call__` function. See Python documentation for details.

### Action Group Dictionary

| Key | Type | Optional | Description |
|---|---|---|---|
| `name` | String | No | Name of the action group that will be created in the menu. |
| `actions` | Tuple | No | Tuple of action dictionaries. Each dictionary defines a menu item to be created in the group. |

---

## Available Custom User Interface Actions Hooks

The no-op hook implementation and full description are located in `/opt/Autodesk/<PRODUCT>_<VERSION>/python/custom_actions.py`.

| Function | Description | Multiple definitions |
|---|---|---|
| `get_main_menu_custom_ui_actions()` | Defines custom actions for the main menu. | Allowed |
| `get_media_panel_custom_ui_actions()` | Defines custom actions for the Media Panel context menu. | Allowed |
| `get_mediahub_files_custom_ui_actions()` | Defines custom actions for the MediaHub Files context menu. | Allowed |
| `get_mediahub_archives_custom_ui_actions()` | Defines custom actions for the MediaHub Archives context menu. | Allowed |
| `get_timeline_custom_ui_actions()` | Defines custom actions for the Timeline context menu. | Allowed |
| `get_batch_custom_ui_actions()` | Defines custom actions for the Batch context menu. | Allowed |
| `get_action_custom_ui_actions()` | Defines custom actions for the Action context menu. | Allowed |

 Note: Multiple definitions of the hooks functions can be implemented in multiple Python modules/files, and the output of all of them will be combined. The combination process merges the outputs in the order they are loaded, with later definitions potentially overriding earlier ones in case of conflicts.

---

## Custom User Interface Actions Examples

Examples are located in `/opt/Autodesk/<PRODUCT>_<VERSION>/python_utilities/examples`.

| File | Description |
|---|---|
| `custom_action_object.py` | Example of how custom actions can be any callable Python object. |
| `custom_menu_structure.py` | Examples of how two different menu structures can be defined for the same custom actions. |
| `version_scoping_hooks.py` | Examples of how custom actions can be limited to appear in some application versions only. |

## Related pages

- Python Hooks Reference
