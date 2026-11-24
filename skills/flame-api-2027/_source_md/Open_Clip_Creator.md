<!-- source: Autodesk Flame Family 2027 Help _ Open Clip Creator _ Autodesk.html -->
# Open Clip Creator

The Open Clip XML is a .xml wrapper, native to Autodesk Flame, that points to single or multiple video and/or audio sources and wraps them in a single entity. The Open Clip XML is built to reflect the structure of a complex clip, with the most atomic portions, Spans (paths to the media) at the bottom of the hierarchy, moving up to Feeds (track versions) and Tracks (the sum of information about a single channel), and finally to the Clip as the topmost entity. Open Clips have a .clip file extension.

Open Clip Creator is used to create Single Version, Multi-Version, Multi-Channel, Stereo 3D, or Patterned .clip files. The three-tabbed user interface simplifies the assembly of these Open Clips. The File tab is used to select individual media files as the sources for the .clip file. The Pattern tab uses tokens for folder and media file detection. The Metadata tab allows overriding of the default metadata values.

Open Clip Creator is installed automatically with Flame. It can also be downloaded from the Autodesk App Store as a standalone application, without requiring a Flame installation.

In the Flame MediaHub, the Create Open Clip option is available in the context menu when one or more clips are selected. Selecting this option launches Open Clip Creator. Launching the standalone application also opens Open Clip Creator. The user interface comprises the following options:

#### Open Clip Type

- Type: Select the type of Open Clip(s) to create:

  - Single-Version: Selected content creates single-version Open Clips. The name of the clip as seen in MediaHub is used to name the Open Clip files.
  - Multi-Version: Selected content is consolidated in a multi-version Open Clip. The order of the selection defines the version order.
  - Multi-Channel: Selected content is consolidated in a multi-channel Open Clip.
  - Stereo 3D: Selected content is consolidated in a Stereo 3D Open Clip. The order of the selection defines the polarity (Left/Right).
  - Pattern: Select this option to create Open Clips based on tokens. See the Patterns section.

#### The Files Tab

-
File(s) tab: Displays the selected media files used to create the Open Clip(s).

-
Sort input files: Offers various sorting modes for the selected files:

  - Sort by name: The list of files is sorted by name (default order is based on selection order).
  - Expand file sequence: Applies only to file sequences. Displays all the frames instead of the grouped sequences.
  - Find file sequence: This mode groups files with the same base name into a continuous sequence, even if there are gaps in the sequence numbering. The resulting clips will display a checkerboard for frames with missing media.
  - Find gap-defined file sequences: This mode groups files with the same base name into a continuous sequence. But where the Find file sequence mode ignores gaps, this mode uses these same gaps in numbering to define the start and end of clips.

#### The Metadata Tab

-
Metadata tab: While the following values are automatically written based on the selected clips, defaults can be overridden using the following fields:

  - Name: The name of the clip as seen in MediaHub. By default, Tape Name is inherited from the selected media files, according to the configured Format Specific Option and Metadata Option. Format Specific Options can differ by supported media format.
  - Source Name: Tape/Source/Reel name is inherited from the media files, but this field allows custom Source names to be defined. This is especially useful for file formats that do not support Source names, or when the Source name is incorrect.
  - Comment: This field accepts a comment that can be seen in Batch as a Note.

#### The Pattern Tab

- Pattern tab: Defines tokens for folder and media file detection.

The following tokens are available:

-
`{name}`: The name of the Open Clip file is used to fill this token.

-
`{version}`: The version ID of the media file name. If the version token is next to another token, it needs to be a numerical value only. For example, in `{name}_{version}.{ext}` version can be alphanumeric but in `{name}{version}.{ext}` it needs to be numerical.

-
`{frame}`: This token is used for file sequence content. The frame token is always numerical only.

Frame padding in Open Clips can be specified by adding # after the frame token to define the padding. For example: {frame####} to restrict the padding to four digits.

-
`{track}`: This token is used for track identification. Track in this context will usually map to a layer or a channel group.

-
`{polarity}`: This token is used to identify Left and Right tracks. Creates a stereo Open Clip.

-
`{ext}/{extension}`: The file extension of the media file must be entered at the end of the pattern.

#### Output Settings

- Output File Name: Sets the resulting Open Clip name in single-clip creation mode.

In multi Open Clip creation mode, the names of the selected clips are used. Do not enter the .clip file extension, because it is added automatically when Open Clips are created.

- Output Folder: Where Open Clips will be created. To avoid possible confusion or multiple matches in Conform, do not create Open Clips at the location of the media files.

---

## Using Open Clip Creator Outside of Flame

Open Clip Creator is also available outside of Flame, as a command-line tool or as a standalone application.

-
The application can be started by using the following commands:

  - On macOS: `/Applications/Autodesk/Open\ Clip\ Creator.app`
  - On Linux: `/usr/local/bin/openclip_creator`

-
The tool can also be used directly on the command line. Use help for more details on using the tool without a graphical interface:

  - On macOS: `/Applications/Autodesk/Open Clip Creator.app/Contents/MacOS/openclip_creator --help`
  - On Linux: `/usr/local/bin/openclip_creator --help`

Examples of command-line usage:

-
Create a stereo open clip file (newStereo.clip) from multiple clips (1 frame each), without displaying the UI:

`./openclip_creator -m Stereo -o /tmp/newStereo.clip -n "Stereo Clip Name" -noui channel1.LEFT.exr channel2.RIGHT.exr`

-
Create a multi-version open clip (newMultiVersion.clip) from the files matching the pattern in the folder, using the graphical user interface:

`./openclip_creator -m Multi-Version -o /tmp/newMultiVersion.clip /storage/versions/A020_C003_0729FX*`

Notes:

-
The "m" option defines the structure of the Open Clip.

-
Only one structure setting can be specified; the tool cannot be used to create a multi-channel multi-version Open Clip.

-
When creating a stereo Open Clip, the first listed file corresponds to the left eye and the second to the right eye.

---

## Pattern Based Open Clips

An Open Clip can be created based on patterns and tokens. This allows Open Clip versions in Flame Family products to be updated when content matching the pattern is added to the destination location. Supported tokens are:

-
{name}: the name of the Open Clip and the base name of the media files.

  -
For a movie file named A002_0222_0202.mov, A002_0222_0202 is the base name.

  -
For a file sequence named A002_0222_0202.86400.dpx to A002_0222_0202.89000.dpx, A002_0222_0202 is the base name.

-
{frame}: the file sequence index

  - For a file sequence named A002_0222_0202.86400.dpx, 86400 is the index.

-
{version}: the version ID

  -
For a movie file named A002_0222_0202_001.mov, 001 is the version ID.

  -
For a file sequence named A002_0222_0202_v001.86400.dpx, v001 is the version ID.

 Note: Do not use <name>, <frame>, or <version> as tokens. Use {name}, {frame}, and {version}.

Absolute or relative media location can be defined in the Open Clip.

Broken file sequences with the same base name are supported; the first and last frames available define the duration, and missing frames appear as black. If the duration of the clip is updated (for example, by changing the starting frame or extending the last frame), the clip must be updated using Source Version  Update Source Option (context menu).

---

## Pattern Based Multi-Channel Open Clips

It is also possible to create patterned Open Clips with Multi-Channel OpenEXR media files. This enables a versioning workflow with media files with a variable number of channels coming from CG rendering and Desktop Compositing products.

---

## Sample Open Clips with Pattern Tokens

### Example 1: No Version File Sequence

A DPX file sequence named TEST.86400.dpx to 89000.dpx, located in the MEDIA folder.

`python
<clip>
    <handler>
        <name>MIO Clip</name>
        <options>
            <ScanPattern type="string">MEDIA/{name}.{frame}.dpx</ScanPattern>
        </options>
    </handler>
</clip>
`

### Example 2: Multi-Version File Sequence

OpenEXR file sequences named TEST_001.86400.exr to 89000.exr, TEST_002.86500.exr to 88000.exr, and TEST_003.87000.exr to 87500.exr, located in the `/usr/tmp` folder. The start and end frames are defined based on the available media in all versions, and a No Media slate is shown for versions where media is not available.

If the OpenEXR file sequence is multi-layer or multi-part, tracks are created automatically. It is assumed that part/layer identifiers are consistent between versions.

`python
<clip>
    <handler>
        <name>MIO Clip</name>
        <options>
            <ScanPattern type="string">/usr/tmp/{name}.{version}.{frame}.exr</ScanPattern>
        </options>
    </handler>
</clip>
`

### Example 3: Multi-Version Movie File

`python
<clip>
    <handler>
        <name>MIO Clip</name>
        <options>
            <ScanPattern type="string">/usr/tmp/{name}.v{version}.mov</ScanPattern>
        </options>
    </handler>
</clip>
`
