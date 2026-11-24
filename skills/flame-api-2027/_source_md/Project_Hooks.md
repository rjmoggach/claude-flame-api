<!-- source: Autodesk Flame Family 2027 Help _ Project Hooks _ Autodesk.html -->
# Project Hooks

All hooks described in this section follow the same pattern: a `pre` and a `post` hook that will be called respectively before and after a given action is done, allowing the implementer to monitor, abort, and react to an event. Some classes of hooks will also have an `init` hook to initialise a new panel or window being shown with parameters different from the default ones.

---

## Project Creation Hooks

| Function | Description |
|---|---|
| `project_init_creation` | Hook called when the Create New Project panel is opened.<br><br>This can be used to fill in information in that panel before the user does. |
| `project_pre_creation` | Hook called before a project is created.<br><br>This can be used to validate information and potentially abort the creation process before it starts. |
| `project_post_creation` | Hook called after a project is created. |

All project creation hooks use a similar `info` dictionary as parameter with some keys only available/modifiable in some hooks.

| Key | Type | Init | Pre | Post | Description |
|---|---|---|---|---|---|
| `project_name` | String | Modifiable | Available | Available | Name of the project. |
| `project_uuid` | String |  |  | Available | Unique identifier of the project. |
| `project_description` | String | Modifiable | Available | Available | Description of the project. |
| `project_nickname` | String | Modifiable | Available | Available | Nickname of the project. |
| `project_home` | String | Modifiable | Available | Available | Path of the project home. |
| `project_setups_dir` | String | Modifiable | Available | Available | Path of the project setups. |
| `project_media_dir` | String | Modifiable | Available | Available | Path of the project media. |
| `abort` | Boolean |  | Modifiable |  | Hook can set this to True if the creation should be aborted. |
| `abort_message` | String |  | Modifiable |  | Error message to be displayed to the user when the creation process has been aborted. |

 Note: Paths support tokens in `project_init_creation`, but tokens will be resolved in `project_pre_creation` and `project_post_creation`. See the Project Folders section for more details.

---

## Project Deletion Hooks

| Function | Description |
|---|---|
| `project_pre_delete` | Hook called before a project is deleted.<br><br>This can be used to validate information and potentially abort the delete process before it starts. |
| `project_post_delete` | Hook called after a project is deleted. |

All project delete hooks use a similar `info` dictionary as parameter with some keys only available/modifiable in some hooks.

| Key | Type | Pre | Post | Description |
|---|---|---|---|---|
| `project_name` | String | Available | Available | Name of the project. |
| `project_uuid` | String | Available | Available | Unique identifier of the project. |
| `abort` | Boolean | Modifiable |  | Hook can set this to True if the delete should be aborted. |
| `abort_message` | String | Modifiable |  | Error message to be displayed to the user when the deletion process has been aborted. |

---

## Project Edition Hooks

| Function | Description |
|---|---|
| `project_pre_edition` | Hook called before a project is edited.<br><br>This can be used to validate information and potentially abort the edition process before it starts. |
| `project_post_edition` | Hook called after a project is edited. |

All project edition hooks use a similar `info` dictionary as parameter with some keys only available/modifiable in some hooks.

| Key | Type | Pre | Post | Description |
|---|---|---|---|---|
| `project_name` | String | Available | Available | Name of the project. |
| `project_uuid` | String | Available | Available | Unique identifier of the project. |
| `project_description` | String | Available | Available | Description of the project. |
| `project_nickname` | String | Available | Available | Nickname of the project. |
| `project_home` | String | Available | Available | Path of the project home. |
| `project_setups_dir` | String | Available | Available | Path of the project setups. |
| `project_media_dir` | String | Available | Available | Path of the project media. |
| `abort` | Boolean | Modifiable |  | Hook can set this to True if the edition should be aborted. |
| `abort_message` | String | Modifiable |  | Error message to be displayed to the user when the edition process has been aborted. |

---

## Project Conversion Hooks

| Function | Description |
|---|---|
| `project_init_conversion` | Hook called when the Convert Legacy Project to Compatible Format window is opened.<br><br>This can be used to fill in information in that window before the user does. |
| `project_pre_conversion` | Hook called before a project is converted.<br><br>This can be used to validate information and potentially abort the conversion process before it starts. |
| `project_post_conversion` | Hook called after a project is converted. |

All project conversion hooks use a similar `info` dictionary as parameter with some keys only available/modifiable in some hooks.

| Key | Type | Init | Pre | Post | Description |
|---|---|---|---|---|---|
| `project_name` | String | Modifiable | Available | Available | Name of the project. |
| `project_uuid` | String |  |  | Available | Unique identifier of the project. |
| `project_description` | String | Modifiable | Available | Available | Description of the project. |
| `project_nickname` | String | Modifiable | Available | Available | Nickname of the project. |
| `project_home` | String | Modifiable | Available | Available | Path of the project home. |
| `project_setups_dir` | String | Modifiable | Available | Available | Path of the project setups. |
| `project_media_dir` | String | Modifiable | Available | Available | Path of the project media. |
| `copy_project` | Boolean | Modifiable | Available | Available | Indicate if the project is copied or converted in-place. |
| `abort` | Boolean |  | Modifiable |  | Hook can set this to True if the conversion should be aborted. |
| `abort_message` | String |  | Modifiable |  | Error message to be displayed to the user when the conversion process has been aborted. |

 Note: Paths support tokens in `project_init_conversion`, but tokens will be resolved in `project_pre_conversion` and `project_post_conversion`. See the Project Folders section for more details.

---

## Project Restore Hooks

| Function | Description |
|---|---|
| `project_init_restore` | Hook called when the Project Restore window is opened.<br><br>This can be used to fill in information in that window before the user does. |
| `project_pre_restore` | Hook called before a project is restored.<br><br>This can be used to validate information and potentially abort the restore process before it starts. |
| `project_post_restore` | Hook called after a project is restored. |

All project restore hooks use a similar `info` dictionary as parameter with some keys only available/modifiable in some hooks.

| Key | Type | Init | Pre | Post | Description |
|---|---|---|---|---|---|
| `project_name` | String | Modifiable | Available | Available | Name of the project. |
| `project_description` | String | Modifiable | Available | Available | Description of the project. |
| `project_nickname` | String | Modifiable | Available | Available | Nickname of the project. |
| `project_home` | String | Modifiable | Available | Available | Path of the project home. |
| `project_setups_dir` | String | Modifiable | Available | Available | Path of the project setups. |
| `project_media_dir` | String | Modifiable | Available | Available | Path of the project media. |
| `abort` | Boolean |  | Modifiable |  | Hook can set this to True if the restore should be aborted. |
| `abort_message` | String |  | Modifiable |  | Error message to be displayed to the user when the restore process has been aborted. |

 Note: Paths support tokens in `project_init_restore`, but tokens will be resolved in `project_pre_restore` and `project_post_restore`. See the Project Folders section for more details.

---

## Project Hooks Examples

Examples are located in `/opt/Autodesk/<PRODUCT>_<VERSION>/python_utilities/examples`.

| File | Description |
|---|---|
| `project_protection.py` | Example of how to use the abort flag to prevent creation, modification, or conversion. |
| `conversion_description.py` | Example of how to initialise the user interface with default values on creation or conversion. |

## Related pages

- Python Hooks Reference
