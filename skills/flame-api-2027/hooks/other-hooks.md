# Other Hooks Mentioned in the Sources (Flame 2027)

> Source: "Python Hooks Tips" (sections "Passing the Project Name Between Hooks" and "Threading Hooks").

These hooks appear only incidentally (inside tips/examples). The help pages give their signature through example code but no full reference. Their files/modules are not named. Overview: [README.md](README.md).

## `app_initialized`

```python
def app_initialized(project_name): ...
```

- **When:** "This hook is called whenever the project changes." (The name suggests application start-up too; the source only states project changes.)
- **Arguments:** `project_name` — the project name.
- **Return:** none documented.
- **Use (source):** pass the project name between hooks by storing it in a module-level global readable by other hooks.

Source example (verbatim):

```python
global_project_name = ""

def app_initialized(project_name):
    global global_project_name
    global_project_name = project_name
```

> **Agent note:** a global is only visible to hooks in the **same module**. The source does not say how to share it across hook files. Inside a running session the current project is also reachable through the `flame` module (see [../api/flame-module-data.md](../api/flame-module-data.md)).

## `render_ended`

```python
def render_ended(moduleName, sequenceName, elapsedTimeInSeconds): ...
```

- **When:** not described beyond its name. The example comment calls it "the actual hook called by the application, with its standard moduleName, sequenceName, and elapsedTimeInSeconds parameters".
- **Arguments:** `moduleName`, `sequenceName`, `elapsedTimeInSeconds`. Types and meanings are not documented.
- **Return:** none documented.
- Shown only as the subject of the threading example: see [tips-and-gotchas.md#threading-hooks](tips-and-gotchas.md#threading-hooks).

Ambiguity: `render_ended` does not appear on the Batch Hooks page, which documents `batch_render_begin` / `batch_render_end` for Batch renders. The sources do not say how `render_ended` relates to them, or whether it is still current in 2027. Also note the example signature has **no** trailing `*args, **kwargs`, unlike the forward-compatibility recommendation.

## Hooks referred to by installed examples only

The Tips page describes these example files without naming their hook functions:
- `wait_cursor.py` — "Example of a Python hook overriding the default wait cursor while running to enable use of another GUI."
- `create_user_shared_library.py` (scripts) — "how a Python hook can be used to fetch the current user for later use in custom actions."
- `watch_folder.py` — uses "the Idle event callback" (see `flame.schedule_idle_event` in [../api/flame-module-functions.md](../api/flame-module-functions.md)) — not a hook.
- `context_variables.py` — utility methods for OCIO Context Variables. The Colour Management page describes it as "an example script provided to create Python hooks that set context variables based on selected Batch nodes or Timeline segments".
