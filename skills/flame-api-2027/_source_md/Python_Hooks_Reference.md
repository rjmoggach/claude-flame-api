<!-- source: Autodesk Flame Family 2027 Help _ Python Hooks Reference _ Autodesk.html -->
# Python Hooks Reference

## What are the Python Hooks

Python Hooks in Flame are places where external Python code can be injected to monitor, inspect, or change the behaviour of the application. They are meant to help integrate Flame into a shot management system, monitor archives, or specify how Batch setups are named, as examples.

All Python hook files are located in `/opt/Autodesk/<application>/python/`.

To provide more flexibility in how hook implementations are deployed, Flame loads modules, searching for supported methods until all supported hooks are found. This allows to separate hook implementations into multiple files, making allowance for better organization.
 Note: The hooks parameters and usage are documented within the Python files located in `/opt/Autodesk/<application>/python/`. Samples and example files are located in `/opt/Autodesk/<application>/python_examples/`. Note: Hooks are blocking, and relinquish control only once they complete. To run a hook in its own thread, see Threading Hooks.

---

## Hooks Location

### User, Project, Application, and Shared Locations

Python hooks can be assigned to a given user or project. Add the Python file with the custom hooks in one of the following locations:

-
A specific user:

  - Linux: `/home/<user name>/flame/python`
  - macOS: `/Users/<user name>/Library/Preferences/Autodesk/flame/python`

-
A specific project: `/opt/Autodesk/project/<project name>/python`

  - In the future, any python files located there will be copied with the project when the project is converted to a new version.

-
A specific application version: `/opt/Autodesk/<PRODUCT>_<VERSION>/python`

-
A global, opened and shared location: `/opt/Autodesk/shared/python`

  - Will be used by all users and projects in all versions.

### Other Locations

It is possible to make Flame scan a directory other than `/opt/Autodesk/<PRODUCT>_<VERSION>/python` for `.py` files by setting the `DL_PYTHON_HOOK_PATH` environment variable to the desired path.

Multiple paths can also be used by separating them by `:`.

---

## Naming

Python does not support having two files of the same name. Ensure that files have unique names if they are in more than one location.

Some hooks support multiple definitions:

- For hooks that do not return any values, every hook will be called once when the hook point is reached.
- For hooks that return values, the way to handle multiple definitions might vary, but this will usually result in the union of the return values.

---

## Parameters

Python Hooks are designed to be forward-compatible as much as possible. With that mindset, example hooks are implemented with variadic arguments as the last parameters to allow new parameters to be added in future versions. These parameters are meant to be ignored and new parameters should not change the values of previously passed ones.

---

## Third Party Packages

In order to avoid disruption with the system Python installation, Flame provides its own distribution of Python, located in `/opt/Autodesk/python/<VERSION>/`.

Third-party site-packages can be installed in it. Pip can be used to do so using `/opt/Autodesk/python/<VERSION>/bin/pip`.

## Related pages

- Tokens Hooks
- Custom User Interface Actions
- Batch Hooks
- Project Hooks
- Python Hooks Tips
