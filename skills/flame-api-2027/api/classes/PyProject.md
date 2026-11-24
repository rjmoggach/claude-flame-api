# class `flame.PyProject`(PyArchiveEntry)

Object representing a Project.

**Method resolution order:** PyProject → PyArchiveEntry → PyFlameObject

> Cannot be instantiated from Python (obtained from other API objects).

## Methods

### `create_shared_library`

```python
create_shared_library( (PyProject)arg1, (str)name) -> object
```

Create a new Shared Library in the Project.

### `export_ocio_config`

```python
export_ocio_config( (PyProject)arg1, (str)config_name, [, (str)destination_folder='' [, (bool)overwrite_existing=False [, (bool)export_as_locked=False [, (bool)generate_ocioz=False]]]]) -> bool
```

Export the OCIO config file.

Keyword arguments:

config_name -- Specifies the name that will be written inside the exported OCIO config and used as the parent folder name where the config will be exported. It should not contain the '.ocio' extension. Mandatory.

destination_folder -- Specifies the absolute destination folder for the exported OCIO config. It will use the default colour management shared path if empty.

overwrite_existing -- Specifies if the export should overwrite an existing OCIO config with the same name located in the same destination_folder.

export_as_locked -- Specifies if the exported OCIO config should be locked (the 'LockedPolicy' parameter inside the settings.cfg sidecar file).

generate_ocioz -- Specifies if an OCIOZ archive should be created alongside the exported OCIO config.

### `get_context_variables`

```python
get_context_variables( (PyProject)arg1) -> dict
```

Get the context variables in a dictionary.

### `refresh_shared_libraries`

```python
refresh_shared_libraries( (PyProject)arg1) -> bool
```

Refresh the Shared Libraries list in the Media Panel.

### `reload_ocio_config`

```python
reload_ocio_config( (PyProject)arg1 [, (bool)reset_colour_policy=False]) -> bool
```

Reload the OCIO config file.

Keyword argument:

reset_colour_policy -- Delete the project's custom colour spaces, roles, and rules (false by default).

### `reset_context_variables`

```python
reset_context_variables( (PyProject)arg1) -> None
```

Reset the context variables to their initial state from the OCIO config.

### `set_context_variable`

```python
set_context_variable( (PyProject)arg1, (str)name, (str)value) -> None
```

Set the value for the specified context variable.

## Read-only properties defined here

### `current_workspace`

Return the current Workspace.

### `media_folder`

The path where the project media is located.

### `name`

Return the Project name.

### `nickname`

Return the Project nickname.

### `description`

Return the Project description.

### `project_folder`

The path where the project is located.

### `project_name`

Deprecated / use name instead.

### `setups_folder`

The path where the project setups are located.

### `shared_libraries`

Return a list of Shared Libraries inside the Project.

### `workspaces_count`

Return the amount of Project Workspaces.

## Inherited members

- **Static methods inherited from PyArchiveEntry:** `clear_colour`, `commit`, `get_wiretap_node_id`, `get_wiretap_storage_id`
- **Read-only properties inherited from PyFlameObject:** `attributes`, `parent`

## Attributes (documented values)

Source: "PyProject Attributes" help page. Access via `obj.<attr>`; most return a `PyAttribute` — use `.get_value()` / `.set_value()` (see PyAttribute.md).

#### `shotgrid_project_name (type 'str')`

The name of the linked Flow Production Tracking project.

#### `working_colour_space (type 'str')`

The working colour space of the Project.

#### `action_colour_space (type 'str')`

The colour space used to render in Action.
