> Source: Flame Python API Code Samples (sections: Clip Import, Clip Reformat, Rendering a Clip, Using PyTime, Clip Operations) — Autodesk Flame Family 2027 Help

# Examples — Clips, Rendering and PyTime

Notation: `<PyClip>`, `<PyReel>`, `<PyLibrary>` are placeholders for objects obtained via the paths in [../guides/constants.md](../guides/constants.md). Code is verbatim from the source. Class references: [PyClip](../api/classes/PyClip.md), [PyTime](../api/classes/PyTime.md), [PyReel](../api/classes/PyReel.md), [PyAttribute](../api/classes/PyAttribute.md), [module functions](../api/flame-module-functions.md).

## Clip Import

### Import a clip into a library
Imports a movie file into a library. API: `flame.import_clips(path, destination)`.

```python
flame.import_clips("/usr/tmp/clip.mov", PyLibrary)
```

> Agent note: `PyLibrary` here stands for a library object (source omits the `< >` placeholder brackets). See also the 2027 `import_clips` + `update_sources` example in [../guides/whats-new-2027.md](../guides/whats-new-2027.md#pyclip).

## Clip Reformat

### Change the resolution of a clip
API: `PyClip.reformat(width, height, ratio)`.

```python
<PyClip>.reformat( width = 1920, height = 1080, ratio = 1.778)
```

## Rendering a Clip

### Render all Timeline FX in proxy resolution using Burn
API: `PyClip.render(render_mode, render_option, render_quality)`.

```python
<PyClip>.render(render_mode ="All", render_option = "Burn", render_quality = "Proxy Resolution")
```

### Render all the Batch FX on a clip
API: `PyClip.render(effect_type)`.

```python
<PyClip>.render(effect_type = "Batch FX")
```

### Get the render state of a clip
API: `PyClip.is_rendered()`.

```python
print(<PyClip>.is_rendered())
```

## Using PyTime

### Set a PyTime in timecode
API: `flame.PyTime(timecode_str, frame_rate_str)`.

```python
tc = flame.PyTime("10:00:01:05", "23.976 fps")
```

### Set a PyTime in relative frame
API: `flame.PyTime(int)`.

```python
frm = flame.PyTime(10)
```

### Set a PyTime in absolute frame
API: `flame.PyTime(int, frame_rate_str)`.

```python
frm = flame.PyTime(864000, "23.976 fps")
```

### Get the current time of a clip in frame
API: `PyClip.current_time`, `PyTime.frame`.

```python
print(<PyClip>.current_time.frame)
```

### Get the current time of a clip in relative frame
API: `PyTime.relative_frame`.

```python
print(<PyClip>.current_time.relative_frame)
```

### Get the current time of a clip in timecode
API: `PyTime.timecode`.

```python
print(<PyClip>.current_time.timecode)
```

## Clip Operations

### Print a list of clips located in a reel
API: `PyReel.clips`.

```python
print(<PyReel>.clips)
```

### Store a clip in a define
```python
clip = <PyReel>.clips[0]
```

### Set an in mark on a clip based on relative frame
API: `PyClip.in_mark` (accepts an int).

```python
<PyClip>.in_mark = 20
```

### Set an in mark on a clip based on a PyTime timecode
API: `PyClip.in_mark` (accepts a `PyTime`).

```python
tc = flame.PyTime("10:00:00:20", "23.976 fps")
<PyClip>.in_mark = tc
```

### Get the in mark value in frame
API: `PyClip.in_mark` is a `PyAttribute`; `.get_value()` returns the `PyTime`.

```python
print(<PyClip>.in_mark.get_value().frame)
```

### Set an out mark on a clip based on relative frame
```python
<PyClip>.out_mark = 30
```

### Set an out mark on a clip based on a PyTime timecode
```python
tc = flame.PyTime("10:00:01:05", "23.976 fps")
<PyClip>.out_mark = tc
```

### Get the out mark value in frame
```python
print(<PyClip>.out_mark.get_value().frame)
```

### Get the duration of a clip between in and out marks in frame
API: `PyClip.duration`.

```python
print(<PyClip>.duration.frame)
```

### Set the current time on a clip based on a timecode value
API: `PyClip.current_time` (accepts a timecode string).

```python
<PyClip>.current_time = "10:00:00:20"
```

### Set the current time on a clip based on an absolute frame using PyTime
```python
frm = flame.PyTime(864000, "23.976 fps")
<PyClip>.current_time = frm
```

### Get the current time of a clip in frame (Clip Operations repeat)
```python
print(<PyClip>.current_time.frame)
```

> Agent note: in these samples `in_mark` / `out_mark` are read with `.get_value()` (they are `PyAttribute` wrappers), whereas `current_time` and `duration` are read directly (`.frame`). Follow the pattern shown for each attribute.
