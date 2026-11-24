# class `flame.PySubtitleTrack`(PyTrack)

Object representing a Subtitle Track.

**Method resolution order:** PySubtitleTrack → PyTrack → PyFlameObject

> Cannot be instantiated from Python (obtained from other API objects).

## Methods

### `export_as_avid_txt_file`

```python
export_as_avid_txt_file( (PySubtitleTrack)arg1, (str)file_name [, (str)start_timecode='Same as Clip']) -> None
```

Export the Subtitle Track as a Avid Caption (txt) file.Keyword arguments:

file_name -- The path and name of the file to write.

start_timecode -- Specify the timecode mode, Same As Clip or, Relative to Clip Start.

### `export_as_srt_file`

```python
export_as_srt_file( (PySubtitleTrack)arg1, (str)file_name [, (bool)character_based_attributes=True [, (bool)export_colours=False [, (str)exclude_colour='' [, (bool)use_original_colours=False [, (bool)use_original_alignment=False [, (bool)export_alignments=False [, (str)alignment_type='an' [, (str)exclude_alignment='' [, (str)start_timecode='Same as Clip']]]]]]]]]) -> None
```

Export the Subtitles Track as a SubRip (srt) file.Keyword arguments:

file_name -- The path and name of the file to write.

character_based_attributes -- Export the bold, italic, and underline attributes.

export_colours -- Export colours.

exclude_colour -- Specify a colour, in hexadecimal or CSS colour name, to ignore.

use_original_colours -- Reuse hexadecimal or CSS colour names from the imported file.

use_original_alignment -- Reuse alignment tokens from the imported file .

export_alignments -- Export alignments.

alignment_type -- Set to a or an alignment style tokens.

exclude_alignment -- Specify an alignment to ignore.

start_timecode -- Specify the timecode mode, Same as Clip or, Relative to Clip Start.

## Inherited members

- **Static methods inherited from PyTrack:** `copy_to_media_panel`, `cut`, `insert_transition`
- **Read-only properties inherited from PyTrack:** `segments`, `transitions`
- **Read-only properties inherited from PyFlameObject:** `attributes`, `parent`
