# flame module-level functions

Called as `flame.<function>(...)`.

### `delete`

```python
delete( (PyFlameObject)object [, (bool)confirm=True]) -> bool
```

Delete the target object.

### `dump`

```python
dump() -> None
```

### `duplicate`

```python
duplicate( (PyFlameObject)object [, (bool)keep_node_connections=False]) -> object
```

Duplicate the target object.

### `duplicate_many`

```python
duplicate_many( (list)object_list [, (bool)keep_node_connections=False]) -> list
```

Duplicate the target objects.

### `execute_command`

```python
execute_command( (str)command [, (bool)blocking=True [, (bool)shell=False [, (bool)capture_stdout=False [, (bool)capture_stderr=False]]]]) -> tuple
```

Execute command line through the Autodesk Flame Multi-Purpose Daemon.

This way of starting new processes is better since any native python

subprocess command (os.system, subprocess, Popen, etc.) will call fork()

which will duplicate the process memory before calling exec().

This can be costly especially for a process like Flame.

command -- Command line to execute.

blocking -- If True, will not return until the command line has completed.

shell -- Should the command be executed in a sh shell.

WARNING Using shell=True can be a security hazard.

capture_stdout -- If True, stdout of the command will be captured and

returned instead of forwarded to the application stdout.

Requires blocking=True

capture_stderr -- If True, stdout of the command will be captured and

returned instead of forwarded to the application stderr.

Requires blocking=True

Note: Environment variables will not be forwarded to the executed command.

### `execute_shortcut`

```python
execute_shortcut( (str)description [, (bool)update_list=True]) -> bool
```

Execute the Flame shortcut.

description -- The description in the Keyboard Shortcut editor.

### `exit`

```python
exit() -> None
```

Exit the application.

### `find_by_name`

```python
find_by_name( (str)name [, (object)parent=None]) -> list
```

Find a Flame object in the Media Panel by name.

### `find_by_uid`

```python
find_by_uid( (str)uid) -> object
```

Find a Flame object in the Media Panel by UID.

### `find_by_wiretap_node_id`

```python
find_by_wiretap_node_id( (str)node_id) -> object
```

Find a Flame object in the Media Panel by Wiretap Node ID.

### `get_current_tab`

```python
get_current_tab() -> str
```

Get the current tab name.

### `get_home_directory`

```python
get_home_directory() -> str
```

Get the application home directory.

### `get_init_cfg_path`

```python
get_init_cfg_path() -> str
```

Get the application init configuration file.

### `get_selected_segment`

```python
get_selected_segment() -> object
```

### `get_selected_version`

```python
get_selected_version() -> object
```

### `get_version`

```python
get_version() -> str
```

Get the application version.

### `get_version_major`

```python
get_version_major() -> str
```

Get the application major version.

### `get_version_minor`

```python
get_version_minor() -> str
```

Get the application minor version.

### `get_version_patch`

```python
get_version_patch() -> str
```

Get the application patch version.

### `get_version_stamp`

```python
get_version_stamp() -> str
```

Get the application version stamp.

### `go_to`

```python
go_to( (str)tab) -> bool
```

Deprecated / use set_current_tab() instead.

### `import_clips`

```python
import_clips( (object)path [, (object)destination=None]) -> list
```

Import one or many clips from a path.

Keyword arguments:

path -- The path to the media can be:

- A path to a single media file.

- A path to a sequence of media files (ie "/dir/clip.[100-2000].dpx").

- A folder containing media files.

- A pattern to media files (ie "/dir/{name}_v{version}.{frame}.{extension}").

- A list of paths.

destination -- Flame object containing a clip like a reel or a folder object.

### `press_button`

```python
press_button( (str)name [, (float)param=0]) -> bool
```

Press the Flame button or assign a given value to it's variable.

name -- The unique name of the menu item.

param -- An optional value to be assigned to the button's variable.

### `schedule_idle_event`

```python
schedule_idle_event( (object)function [, (int)delay=0]) -> None
```

Register a function callback that will be called eventually when the application is idle. The function must not block and be quick since it will be executed in the main application thread.

Keyword arguments:

function -- Callable object to be called.

delay -- Minimum time (in seconds) to wait before calling function.

### `set_current_tab`

```python
set_current_tab( (str)arg1) -> bool
```

Set the given tab as the active environment.

Keyword arguments:

tab -- The tab to set active (MediaHub, Conform, Timeline, Effects, Batch, Tools)

### `set_render_option`

```python
set_render_option( (str)render_option [, (str)render_context='']) -> bool
```

Set the default render option.

Keyword arguments:

render_option -- Defines the rendering method used. (Foreground, Background Reactor, Background Reactor (Auto), Burn)

render_context -- Defines the rendering context. (Timeline, Conform, Effects, BFX, Batch). None for all of them.

Note: Batch does not support Background Reactor (Auto) and will

default to Background Reactor if (Auto) is passed.

