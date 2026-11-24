> Source: Python API; Write Your First Python API Script; Python Console and how to Execute Scripts; Python API Examples — Autodesk Flame Family 2027 Help

# Getting Started with the Flame 2027 Python API

## Environment facts (as documented)

| Fact | Value / detail |
|---|---|
| Python version | **Python 3.13.3**, starting with Flame Family 2027. |
| Products | Flame, Flare and Flame Assist. Note (source): "Some functions and attributes may not be available in Flare or Flame Assist." |
| Entry point | The `flame` module: "The Flame module is the core of the Python API. This module contains everything needed to use the Flame Python API." |
| Where code runs | The Flame Python Console (opened from the Flame menu), or a script passed at startup with `startApplication -s`. |
| Example scripts shipped with Flame | `/opt/Autodesk/<flame_version>/python_examples` |
| Utility example scripts | `/opt/Autodesk/<flame_version>/python_utilities/examples/` — e.g. `context_variables.py` (OCIO context-variable hooks, see [colour-management.md](colour-management.md)) and `propagate_metadata_to_action_camera.py` (`set_expression()` / `bake_expression()` usage, see [whats-new-2027.md](whats-new-2027.md#pynode)) |
| Startup launcher | `/opt/Autodesk/<version>/bin/startApplication` |
| OCIO binding | `PyOpenColorIO` is installed with the application (see [colour-management.md](colour-management.md#using-the-ocio-python-binding)). |

> Agent note: threading, UI-thread, Qt or idle-event caveats are **not** described in any of the source pages this guide was built from. Do not assume them from here; check the hooks / module-function references (e.g. `flame.schedule_idle_event` in [../api/flame-module-functions.md](../api/flame-module-functions.md)).

Further reading in this library:
- [python-api-overview.md](python-api-overview.md) — map of the documentation.
- [whats-new-2027.md](whats-new-2027.md) — all 2027 changes.
- [constants.md](constants.md) — how to reach each object (`flame.projects.current_project...`) and the `<PyXxx>` placeholder convention.
- [../examples/README.md](../examples/README.md) — all code samples.
- [../api/classes/](../api/classes/) — class reference.

---

## The Python Console

Accessible from the Flame menu, the Flame Python Console is your main tool when using the Python API. It allows you to write, edit, and run code, while being able to view the console output.

Console windows:

- **Terminal Window**: This is where any output from your code will be shown. The terminal is useful when debugging an error, you will get a detailed report of the error within the console (in a red font). This is also the place where any `print()` command or any calls to the `help()` function will be output.
- **Editor Window**: A simple text editor used to write or edit your Python scripts. The editor can have multiple tabs of Python Script files; you can access the multiple tabs underneath the editor's window. To create a new tab, click the plus (`+`) sign in the bottom right corner of the Python Console.

| Icon | Name | Description |
|---|---|---|
| Eraser (terminal) | Eraser | Clears all output in the terminal window |
| Sound Wave | Sound Wave | Choose whether the Python code that is executed will be displayed within the terminal (Will output when icon is Blue) |
| Play Button | Play Button | Executes all code within the current tab of the editor window or selected code segments |
| Save | Save | Prompts user to save the script in the current tab of the editor |
| Load | Load | Prompts user to load a Script which will become a new tab in the editor |
| Eraser (editor) | Eraser | Clears all code within the current tab of the editor |
| Line Number Indicator | Line Number Indicator | Toggling this button will show or hide line numbers within the editor (Line numbers will be visible when icon is blue) |

(The source lists two icons named "Eraser"; the first clears the terminal output, the second clears the editor tab.)

---

## Executing scripts

There are two ways to execute Python API scripts in Flame: at startup from the command line, or from the Python Console.

### Running a script at startup

The Python API allows a user to run a script when the project is loaded by defining what script should be run when starting Flame from the command line.

1. Launch Flame from the command line with `/opt/Autodesk/<version>/bin/startApplication`
2. To define a script to be run at startup, append the `-s` argument to the `startApplication` command and then include a valid path to a valid Python script.

```bash
/opt/Autodesk/<version>/bin/startApplication -s /home/user/scripts/onStart.py
```

> Note (source): A valid Python script must start with `import flame` otherwise the script will not work.

### Running code from the console

- **By Script**: Clicking the Play button within the Python Console will run the entire script (start to finish) that is open in the current tab of the Editor.
- **By Selection**: With a section of the script highlighted, the Play button will only execute the selected parts of the code.

> Important (source): When working in the Python Console, the `import flame` command must only be declared once per tab. Once declared, a single line can be highlighted and executed without the need of another `import flame` command.

---

## Write your first script (walkthrough)

Goal: create a Batch group, switch to Batch, create a Comp node and a Write File node, connect them, and tidy the schematic. APIs: `flame.batch.create_batch_group`, `flame.batch.go_to`, `flame.batch.create_node`, `flame.batch.connect_nodes`, `flame.batch.organize` (see [../api/classes/PyBatch.md](../api/classes/PyBatch.md)).

### Step 1 — import the module

The first thing in any Python API script is the declaration of the Python module. This sets up your environment to use the Flame module functions; without it your code will not run.

```python
import flame
```

### Step 2 — create a Batch group

To create the Batch group we need the names of the reels and the desired start frame and duration values.

```python
import flame

schematicReels = [ 'SchematicReel1', ' SchematicReel2', 'SchematicReel3', 'SchematicReel4' ] #create/name schematic reels
shelfReels = [ 'ShelfReel1', 'ShelfReel2', 'ShelfReel3' ] #create/name shelf reels

#Create batch group with name, start_frame value, duration value, set of schematic reel names, set of shelf reel names
flame.batch.create_batch_group( 'BatchGroupName',
start_frame = 1,
duration = 99,
reels = schematicReels,
shelf_reels = shelfReels )
```

### Step 3 — switch to the Batch tab

`flame.batch.go_to()` switches Flame into the Batch tab. (The source prose writes it as "Flame.batch.go_to()"; the code uses lowercase `flame`.)

```python
import flame

schematicReels = [ 'SchematicReel1', ' SchematicReel2', 'SchematicReel3', 'SchematicReel4' ] #create/name schematic reels
shelfReels = [ 'ShelfReel1', 'ShelfReel2', 'ShelfReel3' ] #create/name shelf reels

#Create batch group with name, start_frame value, duration value, set of schematic reel names, set of shelf reel names
flame.batch.create_batch_group( 'TheName',
start_frame = 1,
duration = 99,
reels = schematicReels,
shelf_reels = shelfReels )

#use this command to switch to the batch tab
flame.batch.go_to()
```

### Step 4 — create and connect nodes

A node created in a script can be stored in a variable for further operations. `flame.batch.connect_nodes(node1, "socket1", node2, "socket2")` connects an output socket to an input socket.

```python
import flame

schematicReels = [ 'SchematicReel1', ' SchematicReel2', 'SchematicReel3', 'SchematicReel4' ] #create/name schematic reels
shelfReels = [ 'ShelfReel1', 'ShelfReel2', 'ShelfReel3' ] #create/name shelf reels

#Create batch group with name, start_frame value, duration value, set of schematic reel names, set of shelf reel names
flame.batch.create_batch_group( 'TheName',
start_frame = 1,
duration = 99,
reels = schematicReels,
shelf_reels = shelfReels )

#use this command to switch to the batch tab
flame.batch.go_to()

#create a comp and writefile node
comp = flame.batch.create_node("Comp") #store the newly created node in a variable called comp
writeFile = flame.batch.create_node("Write File") #store the newly created node in a variable called writeFile

#Connect nodes: flame.batch.connect_nodes(nodename1, "socketname1", nodename2, "socketname2")
flame.batch.connect_nodes(comp, "Result", writeFile, "Front")
#Error msg: Invalid socket name(<type 'exceptions.RuntimeError'>) can occur if the socket name is not exactly what is presented within Flame, the name is case sensitive.
```

Socket names are case sensitive and must match exactly what Flame shows; otherwise an "Invalid socket name" `RuntimeError` is raised (per the comment in the code).

### Step 5 — organise the schematic (complete script)

The Python API creates new nodes in the same position, which leads to overlapping nodes in the Batch Schematic. Two ways to fix this:
1. `flame.batch.organize()` automatically separates and positions all the nodes in the Batch based on connection.
2. Assign positions manually through each node's `pos_x` and `pos_y` attributes.

Using the first method, the completed script:

```python
import flame

schematicReels = [ 'SchematicReel1', ' SchematicReel2', 'SchematicReel3', 'SchematicReel4' ] #create/name schematic reels
shelfReels = [ 'ShelfReel1', 'ShelfReel2', 'ShelfReel3' ] #create/name shelf reels

#Create batch group with name, start_frame value, duration value, set of schematic reel names, set of shelf reel names
flame.batch.create_batch_group( 'TheName',
start_frame = 1,
duration = 99,
reels = schematicReels,
shelf_reels = shelfReels )

#use this command to switch to the batch tab
flame.batch.go_to()

#create a comp and writefile node
comp = flame.batch.create_node("Comp") #store the newly created node in a variable called comp
writeFile = flame.batch.create_node("Write File") #store the newly created node in a variable called writeFile

#Connect nodes: flame.batch.connect_nodes(nodename1, "socketname1", nodename2, "socketname2")
flame.batch.connect_nodes(comp, "Result", writeFile, "Front")
#Error msg: Invalid socket name(<type 'exceptions.RuntimeError'>) can occur if the socket name is not exactly what is presented within Flame, the name is case sensitive.

#by default, all created nodes are placed at the centre (0,0) on top of each other
#organize automatically sets the position of all nodes in the batch group to avoid overlap
flame.batch.organize()
```

Run it with the Play button in the Python Console. To run it at startup instead, save it (Save icon) and pass its path to `startApplication -s` (see [Running a script at startup](#running-a-script-at-startup)), e.g. `/opt/Autodesk/<version>/bin/startApplication -s /home/user/scripts/onStart.py`.

> Agent note: the reel list in the source contains `' SchematicReel2'` with a leading space; this is verbatim from the source (likely a typo) and would produce a reel name starting with a space. The walkthrough first names the group `'BatchGroupName'` and later `'TheName'`.

---

## Catching exceptions

You can catch exceptions in a Python script. The following will throw an exception, catch it, and display it in the console:

```python
from flame import batch
try:
   batch.import_clip("bad_path", "bad_reel_name")
except Exception as e:
   print(str(e))
```

> Agent note: this shows that API failures (here a bad path / reel name passed to `PyBatch.import_clip`) surface as Python exceptions, and that `from flame import batch` is a valid alternative to `import flame` + `flame.batch`.
