> Source: Flame Python API Code Samples (sections: Switching Views, Media Panel Operations, Working with Users, Working with Tabs) — Autodesk Flame Family 2027 Help

# Examples — Media Panel, Desktop, Batch Groups, Views, Users and Tabs

Notation: `<PyDesktop>`, `<PyWorkspace>`, `<PyLibrary>`, `<PyFolder>`, `<PyReel>`, `<PyBatch>` are placeholders (see [../guides/constants.md](../guides/constants.md)). Code is verbatim from the source.

Class references: [PyWorkspace](../api/classes/PyWorkspace.md), [PyDesktop](../api/classes/PyDesktop.md), [PyBatch](../api/classes/PyBatch.md), [PyBatchIteration](../api/classes/PyBatchIteration.md), [PyLibrary](../api/classes/PyLibrary.md), [PyFolder](../api/classes/PyFolder.md), [PyMediaPanel](../api/classes/PyMediaPanel.md), [PyUsers](../api/classes/PyUsers.md), [PyUser](../api/classes/PyUser.md), [module functions](../api/flame-module-functions.md).

## Switching Views

### Switch the top view to Desktop Reels without changing the visible item
```python
<PyDesktop>.set_desktop_reels()
```

### Set a PyBatch as the visible item in the Desktop Reels view
```python
<PyDesktop>.set_desktop_reels(<PyBatch>)
```

> Source issue: these two samples call `set_desktop_reels` on `<PyDesktop>`, but in the class reference `set_desktop_reels( (PyWorkspace)arg1 [, (object)group=None])` is a method of [PyWorkspace](../api/classes/PyWorkspace.md) (alongside `set_freeform`), and PyDesktop has no such method. Prefer `<PyWorkspace>.set_desktop_reels(...)`.

### Switch the top view to Freeform without changing the visible item
API: `PyWorkspace.set_freeform()`.

```python
<PyWorkspace>.set_freeform()
```

### Set an item as the visible item in the Freeform view
```python
<PyWorkspace>.set_freeform(<PyLibrary>)
```

(The source title says "Set a PyBatch as the visible item in the Freeform view" but the code passes `<PyLibrary>`.)

## Media Panel Operations

### Create a new Reel named "MyReel" in a Batch group
API: `PyDesktop.batch_groups`, `PyBatch.create_reel(name)`.

```python
batch = <PyDesktop>.batch_groups[0]
batch.create_reel("MyReel")
```

### Create a new Shelf Reel named "MyShelfReel"
API: `PyBatch.create_shelf_reel(name)`.

```python
batch = <PyDesktop>.batch_groups[0]
batch.create_shelf_reel("MyShelfReel")
```

### Create a Batch Iteration in a Batch Group
API: `PyBatch.iterate()`.

```python
batch = <PyDesktop>.batch_groups[0]
batch.iterate()
```

### Create Batch Iteration 5 in a Batch Group
API: `PyBatch.iterate(index)`.

```python
batch = <PyDesktop>.batch_groups[0]
batch.iterate(5)
```

### Save a Batch Group from the Desktop to a Library
API: `PyDesktop.destination` (target library), `PyBatch.save()`.

```python
desk = <PyDesktop>
batch = <PyDesktop>.batch_groups[0]
lib = <PyLibrary>
desk.destination = lib
batch.save()
```

### Save the current Batch Iteration from the Desktop to a Library
API: `PyDesktop.destination`, `PyBatch.save_current_iteration()`.

```python
desk = <PyDesktop>
batch = <PyDesktop>.batch_groups[0]
lib = <PyLibrary>
desk.destination = lib
batch.save_current_iteration()
```

### Print the name of the Batch Groups in a Library
```python
for batch in <PyLibrary>.batch_groups:
   print(batch.name)
```

### Print the name of the Batch Groups in a Folder
```python
for batch in <PyFolder>.batch_groups:
   print(batch.name)
```

### Open a Batch Group located inside a Folder in the Desktop
API: `open_as_batch_group()`.

```python
<PyFolder>.batch_groups[0].open_as_batch_group()
```

### Open a Batch Iteration located inside a Library in the Desktop
```python
<PyLibrary>.batch_iterations[0].open_as_batch_group()
```

### Overwrite a clip in the current Sequence
API: `flame.execute_shortcut(name)` — triggers a keyboard-shortcut action by name.

```python
flame.execute_shortcut("Overwrite Edit")
```

### Select the Desktop in the Workspace
API: `PyWorkspace.desktop`, `PyDesktop.selected`.

```python
desk = <pyWorkspace>.desktop
desk.selected = True
```

(`<pyWorkspace>` lowercase `p` is verbatim; it is the same placeholder as `<PyWorkspace>`.)

### Move all clips from a Library Folder to a Desktop Reel
API: `flame.media_panel.move(entries, destination)`.

```python
clip = <PyLibrary>.folders[0].clips
reel = <PyDesktop>.reel_groups[0].reels[0]
flame.media_panel.move(clip, reel)
```

### Copy all clips from a Library Folder to a Desktop Reel
API: `flame.media_panel.copy(entries, destination)`.

```python
clip = <PyLibrary>.folders[0].clips
reel = <PyDesktop>.reel_groups[0].reels[0]
flame.media_panel.copy(clip, reel)
```

### Select multiple entries at once
API: `flame.media_panel.selected_entries` (settable with a list).

```python
flame.media_panel.selected_entries = <PyReel>.clips
```

### Print the list of selected entries in the Media Panel
```python
print(flame.media_panel.selected_entries)
```

### Hide the Media Panel
```python
flame.media_panel.visible = False
```

### Set the Media Panel to Full Width
```python
flame.media_panel.full_width = True
```

### Set the Media Panel to Full Height
```python
flame.media_panel.full_height = True
```

### Set the Media Panel to Dual mode
```python
flame.media_panel.dual = True
```

## Working with Users

### Store the name of the current user
API: `flame.users.current_user` (`PyUser`).

```python
user = flame.users.current_user.name
```

### Print the nickname of the current user
```python
print(flame.users.current_user.nickname)
```

## Working with Tabs

### Print the tab currently selected in the software
API: `flame.get_current_tab()`.

```python
print(flame.get_current_tab())
```

### Go to the Timeline Tab
API: `flame.set_current_tab(name)`.

```python
flame.set_current_tab("Timeline")
```
