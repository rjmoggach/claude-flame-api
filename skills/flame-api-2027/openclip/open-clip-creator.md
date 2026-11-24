# Open Clip Creator (`openclip_creator`) — Flame 2027

> Source: "Open Clip Creator" (Autodesk Flame Family 2027 Help); `ScanPattern` cross-reference from "Handler".

Open Clip Creator creates **Single Version, Multi-Version, Multi-Channel, Stereo 3D, or Patterned** `.clip` files (Open Clip XML; see [README.md](README.md)). It can infer structure and assist in the creation process.

- Installed automatically with Flame. Also downloadable from the Autodesk App Store as a standalone application (no Flame installation required).
- In Flame **MediaHub**: select one or more clips → context menu **Create Open Clip** → launches Open Clip Creator.
- Three-tab UI: **Files** (select media files), **Pattern** (tokens for folder/media detection), **Metadata** (override default metadata values).

## UI options

### Open Clip Type

`Type` — the type of Open Clip(s) to create:

| Type | Behaviour |
|---|---|
| Single-Version | Selected content creates single-version Open Clips. The clip name as seen in MediaHub names the Open Clip files. |
| Multi-Version | Selected content consolidated in a multi-version Open Clip. **Selection order defines version order.** |
| Multi-Channel | Selected content consolidated in a multi-channel Open Clip. |
| Stereo 3D | Selected content consolidated in a Stereo 3D Open Clip. **Selection order defines the polarity (Left/Right).** |
| Pattern | Create Open Clips based on tokens (see Pattern tab). |

### Files tab

Displays the selected media files used to create the Open Clip(s). **Sort input files** modes:

| Mode | Behaviour |
|---|---|
| Sort by name | List sorted by name (default order is selection order). |
| Expand file sequence | File sequences only: displays all frames instead of grouped sequences. |
| Find file sequence | Groups files with the same base name into a continuous sequence, even with gaps in numbering. Resulting clips display a **checkerboard** for frames with missing media. |
| Find gap-defined file sequences | Groups files with the same base name into a continuous sequence, but uses numbering gaps to define the start and end of clips. |

### Metadata tab

Values are written automatically from the selected clips; defaults can be overridden:

| Field | Meaning |
|---|---|
| Name | Clip name as seen in MediaHub. By default, Tape Name is inherited from the selected media files, according to the configured Format Specific Option and Metadata Option (Format Specific Options differ by media format). |
| Source Name | Tape/Source/Reel name, inherited from media; this field defines a custom Source name (useful when the format has no Source name or it is incorrect). |
| Comment | A comment that can be seen in Batch as a Note. |

> **Agent note:** these correspond to the XML elements `<name>`, `<sourceName>` and `<comment>` (the source says `<comment>` is "unparsed text converted into a clip note"). The source does not state which XML level (clip/track) the tool writes them to.

### Pattern tab — tokens

| Token | Meaning |
|---|---|
| `{name}` | The name of the Open Clip file is used to fill this token. |
| `{version}` | Version ID from the media file name. If adjacent to another token it must be **numerical only**: in `{name}_{version}.{ext}` version can be alphanumeric; in `{name}{version}.{ext}` it must be numerical. |
| `{frame}` | File sequence content; always numerical only. Padding: add `#` after the token, e.g. `{frame####}` restricts padding to four digits. |
| `{track}` | Track identification; usually maps to a layer or a channel group. |
| `{polarity}` | Identifies Left and Right tracks; creates a stereo Open Clip. |
| `{ext}` / `{extension}` | File extension of the media file; **must be entered at the end of the pattern**. |

### Output settings

- **Output File Name** — resulting Open Clip name in single-clip creation mode. In multi Open Clip creation mode, the names of the selected clips are used. **Do not enter the `.clip` extension**; it is added automatically.
- **Output Folder** — where Open Clips are created. To avoid confusion or multiple matches in Conform, **do not create Open Clips at the location of the media files**.

## Using Open Clip Creator outside of Flame

Launch the standalone application:

| OS | Command |
|---|---|
| macOS | `/Applications/Autodesk/Open\ Clip\ Creator.app` |
| Linux | `/usr/local/bin/openclip_creator` |

Command-line help (use without GUI):

```bash
# macOS
"/Applications/Autodesk/Open Clip Creator.app/Contents/MacOS/openclip_creator" --help
# Linux
/usr/local/bin/openclip_creator --help
```

(The source writes the macOS help path unquoted: `/Applications/Autodesk/Open Clip Creator.app/Contents/MacOS/openclip_creator --help`; quoting added because of the spaces.)

Examples (verbatim):

```bash
# Create a stereo open clip file (newStereo.clip) from multiple clips (1 frame each), without displaying the UI
./openclip_creator -m Stereo -o /tmp/newStereo.clip -n "Stereo Clip Name" -noui channel1.LEFT.exr channel2.RIGHT.exr

# Create a multi-version open clip (newMultiVersion.clip) from the files matching the pattern in the folder, using the GUI
./openclip_creator -m Multi-Version -o /tmp/newMultiVersion.clip /storage/versions/A020_C003_0729FX*
```

Notes (source):
- The `-m` option defines the structure of the Open Clip (values seen: `Stereo`, `Multi-Version`).
- Only one structure setting can be specified; the tool **cannot create a multi-channel multi-version** Open Clip.
- For a stereo Open Clip, the **first listed file is the left eye**, the second the right eye.

Options seen in examples (meaning inferred from the example captions; run `--help` for the authoritative list): `-m <structure>`, `-o <output .clip path>`, `-n "<clip name>"`, `-noui` (no UI), then input files. The full option list is **not** documented in the source.

## Pattern based Open Clips

An Open Clip can be created based on patterns and tokens, so that **Open Clip versions in Flame are updated when content matching the pattern is added** to the destination location. Supported tokens:

| Token | Meaning | Examples |
|---|---|---|
| `{name}` | Name of the Open Clip and base name of the media files | `A002_0222_0202.mov` → `A002_0222_0202`; `A002_0222_0202.86400.dpx`…`A002_0222_0202.89000.dpx` → `A002_0222_0202` |
| `{frame}` | File sequence index | `A002_0222_0202.86400.dpx` → `86400` |
| `{version}` | Version ID | `A002_0222_0202_001.mov` → `001`; `A002_0222_0202_v001.86400.dpx` → `v001` |

- Note (source): **Do not use `<name>`, `<frame>`, or `<version>` as tokens. Use `{name}`, `{frame}`, and `{version}`.**
- Absolute or relative media location can be defined in the Open Clip.
- Broken file sequences with the same base name are supported; the first and last available frames define the duration, and missing frames appear as black.
- If the clip duration is updated (e.g. changing the starting frame or extending the last frame), update the clip with **Source Version > Update Source Option** (context menu).

### Pattern based Multi-Channel Open Clips

Patterned Open Clips can also use Multi-Channel OpenEXR media, enabling a versioning workflow with a variable number of channels coming from CG rendering and Desktop Compositing products. (From sample Example 2 below:) If the OpenEXR sequence is multi-layer or multi-part, tracks are created automatically (part/layer identifiers assumed consistent between versions).

## Sample Open Clips with pattern tokens

The pattern lives in the clip `<handler>` (`<name>MIO Clip</name>`) as option `ScanPattern` (see [elements.md#handler](elements.md#handler) for the `ScanPattern` token table, which also lists `{track}`, `{polarity}`, `{extension}`).

### Example 1: No-version file sequence

DPX sequence `TEST.86400.dpx` to `89000.dpx` in the `MEDIA` folder.

```xml
<clip>
    <handler>
        <name>MIO Clip</name>
        <options>
            <ScanPattern type="string">MEDIA/{name}.{frame}.dpx</ScanPattern>
        </options>
    </handler>
</clip>
```

### Example 2: Multi-version file sequence

OpenEXR sequences `TEST_001.86400.exr`–`89000.exr`, `TEST_002.86500.exr`–`88000.exr`, `TEST_003.87000.exr`–`87500.exr` in `/usr/tmp`. Start/end frames are defined from the media available in all versions; a **No Media** slate is shown where a version has no media. Multi-layer/multi-part EXR → tracks created automatically.

```xml
<clip>
    <handler>
        <name>MIO Clip</name>
        <options>
            <ScanPattern type="string">/usr/tmp/{name}.{version}.{frame}.exr</ScanPattern>
        </options>
    </handler>
</clip>
```

> **Source ambiguity:** the described files use `_` between name and version (`TEST_001...`) but the pattern uses `.` (`{name}.{version}`). Verified identical in the HTML. Write the separator that actually matches your files.

### Example 3: Multi-version movie file

```xml
<clip>
    <handler>
        <name>MIO Clip</name>
        <options>
            <ScanPattern type="string">/usr/tmp/{name}.v{version}.mov</ScanPattern>
        </options>
    </handler>
</clip>
```

> **Agent note:** these samples omit `type`/`version` on `<clip>` (which the Clip attribute table marks as occurrence 1). The Handler page's own `ScanPattern` example omits `type="string"` (string is the default value type).
