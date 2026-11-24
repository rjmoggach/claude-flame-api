# Project Hooks (Flame 2027)

> Source: "Project Hooks" (Autodesk Flame Family 2027 Help), with cross-references to "Python Hooks Reference" and "Python Hooks Tips".

13 hooks in 5 groups: creation, deletion, edition, conversion, restore. Overview and discovery rules: [README.md](README.md).

## Pattern

All project hooks follow the same pattern: a `pre` and a `post` hook called respectively **before** and **after** an action, "allowing the implementer to monitor, abort, and react to an event". Some groups also have an `init` hook, called when the corresponding panel/window is shown, to initialise it with values different from the defaults.

Every project hook receives an **`info` dictionary** as parameter. Per key, the tables below say whether the key is:

- **Modifiable** — the hook may change the value (in `init`: pre-fills the UI field; in `pre`: `abort` / `abort_message` control aborting).
- **Available** — present, read-only by intent.
- *(blank)* — not present in that hook.

### Signature

The help page does **not** print Python signatures; it only says each hook takes "a similar `info` dictionary as parameter". The authoritative signatures/docstrings are in the installed no-op hook files in `/opt/Autodesk/<PRODUCT>_<VERSION>/python/` ("The hooks parameters and usage are documented within the Python files located in `/opt/Autodesk/<application>/python/`").

> **Agent note (derived, unverified against the installed file):** a definition compatible with the documented contract and the forward-compatibility rule ("example hooks are implemented with variadic arguments as the last parameters") is:
>
> ```python
> def project_pre_creation(info, *args, **kwargs):
>     ...
> ```
>
> Change values by mutating `info` in place (e.g. `info["abort"] = True`). The source documents **no return value** for any project hook; aborting is done through the `abort` key, not by returning.

### Aborting (pre hooks)

In every `pre` hook, set `info["abort"] = True` to abort the operation and `info["abort_message"]` (String) to the error message displayed to the user. Key names are snake_case here (`abort_message`) — unlike the Batch hooks, which use `abortMessage` / `aborted` (see [batch-hooks.md](batch-hooks.md)).

### Tokens in paths

In `init` hooks, path keys (`project_home`, `project_setups_dir`, `project_media_dir`) support tokens; in the corresponding `pre` and `post` hooks the tokens are already resolved. (Source: "Paths support tokens in `project_init_creation`, but tokens will be resolved in `project_pre_creation` and `project_post_creation`. See the Project Folders section for more details." — same note for conversion and restore. The "Project Folders" section is not part of the hooks pages.) Custom tokens for the Project context can be added with [tokens hooks](tokens-hooks.md) (context `Project`: Project Home, Setups Directory, Media Cache fields).

---

## Project Creation Hooks

| Function | When called |
|---|---|
| `project_init_creation` | When the **Create New Project** panel is opened. Use it to fill in information in that panel before the user does. |
| `project_pre_creation` | Before a project is created. Use it to validate information and potentially abort creation before it starts. |
| `project_post_creation` | After a project is created. |

`info` keys:

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

Note: `project_uuid` only exists in `project_post_creation`.

---

## Project Deletion Hooks

| Function | When called |
|---|---|
| `project_pre_delete` | Before a project is deleted. Use it to validate information and potentially abort deletion before it starts. |
| `project_post_delete` | After a project is deleted. |

No `init` hook. Function names use `delete` (not `deletion`).

`info` keys:

| Key | Type | Pre | Post | Description |
|---|---|---|---|---|
| `project_name` | String | Available | Available | Name of the project. |
| `project_uuid` | String | Available | Available | Unique identifier of the project. |
| `abort` | Boolean | Modifiable |  | Hook can set this to True if the delete should be aborted. |
| `abort_message` | String | Modifiable |  | Error message to be displayed to the user when the deletion process has been aborted. |

---

## Project Edition Hooks

| Function | When called |
|---|---|
| `project_pre_edition` | Before a project is edited. Use it to validate information and potentially abort the edition before it starts. |
| `project_post_edition` | After a project is edited. |

No `init` hook. All non-abort keys are **Available** only (not Modifiable) in both hooks.

`info` keys:

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

Note: the source does not say whether `pre` sees the values before or after the user's edits.

---

## Project Conversion Hooks

| Function | When called |
|---|---|
| `project_init_conversion` | When the **Convert Legacy Project to Compatible Format** window is opened. Use it to fill in information in that window before the user does. |
| `project_pre_conversion` | Before a project is converted. Use it to validate information and potentially abort the conversion before it starts. |
| `project_post_conversion` | After a project is converted. |

`info` keys:

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

`copy_project` exists only in the conversion hooks. Path keys support tokens in `project_init_conversion`; resolved in `project_pre_conversion` / `project_post_conversion`.

---

## Project Restore Hooks

| Function | When called |
|---|---|
| `project_init_restore` | When the **Project Restore** window is opened. Use it to fill in information in that window before the user does. |
| `project_pre_restore` | Before a project is restored. Use it to validate information and potentially abort the restore before it starts. |
| `project_post_restore` | After a project is restored. |

`info` keys:

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

Note: the restore `info` table lists **no `project_uuid` key** (not even in `post`). Path keys support tokens in `project_init_restore`; resolved in `project_pre_restore` / `project_post_restore`.

---

## Key availability matrix (all project hooks)

| Key | creation (init/pre/post) | delete (pre/post) | edition (pre/post) | conversion (init/pre/post) | restore (init/pre/post) |
|---|---|---|---|---|---|
| `project_name` | M / A / A | A / A | A / A | M / A / A | M / A / A |
| `project_uuid` | – / – / A | A / A | A / A | – / – / A | – |
| `project_description` | M / A / A | – | A / A | M / A / A | M / A / A |
| `project_nickname` | M / A / A | – | A / A | M / A / A | M / A / A |
| `project_home` | M / A / A | – | A / A | M / A / A | M / A / A |
| `project_setups_dir` | M / A / A | – | A / A | M / A / A | M / A / A |
| `project_media_dir` | M / A / A | – | A / A | M / A / A | M / A / A |
| `copy_project` | – | – | – | M / A / A | – |
| `abort` | – / M / – | M / – | M / – | – / M / – | – / M / – |
| `abort_message` | – / M / – | M / – | M / – | – / M / – | – / M / – |

M = Modifiable, A = Available, – = not present.

---

## Examples (installed with Flame)

Examples are located in `/opt/Autodesk/<PRODUCT>_<VERSION>/python_utilities/examples`. The help page lists them but does **not** reproduce their code.

| File | Description |
|---|---|
| `project_protection.py` | Example of how to use the abort flag to prevent creation, modification, or conversion. |
| `conversion_description.py` | Example of how to initialise the user interface with default values on creation or conversion. |

(The Tips page describes `conversion_description.py` as "Example of how to use the project conversion hook to edit information in the description of a converted project.")

> **Agent note (derived, unverified against the installed files):** minimal sketch of the abort mechanism using only documented keys:
>
> ```python
> def project_pre_delete(info, *args, **kwargs):
>     if info.get("project_name", "").startswith("PROD_"):
>         info["abort"] = True
>         info["abort_message"] = "Production projects cannot be deleted."
> ```
