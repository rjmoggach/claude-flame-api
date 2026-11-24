# Open Clip XML elements — reference (Flame 2027)

> Source: "Clip", "Tracks", "Track", "Feeds", "Feed", "Versions", "Version", "Spans", "Span", "Paths", "Path", "Handler", "Dict", "Value", "Rate", "Rational", "Time", "Metadata Edits", "Edits", "Edit", "Additions", "Add" (Open Clip Reference section, Autodesk Flame Family 2027 Help).

Conventions used throughout this file:
- **Occurrence**: `1` required, `0-1` optional, `*` zero or more (verbatim from source tables).
- Every element documented with a `type`/`version` attribute pair: `type` (string, fixed value = element type name, usually 0-1) and `version` (unsigned integer). Source note on all such pages: *"Optional attributes (0 occurrence attributes) will be inferred from the parent node."*
- Source note on `<clip>`, `<track>`, `<feed>`, `<version>`: *"Children elements with the attribute `computed=1` are ignored when parsed."*
- The `version` attribute "Allowed Values" in the source tables is `8` for most elements and `7` for `<track>`, `<feeds>`, `<versions>`; full-clip examples use `version="9"` on `<clip>`. See [README.md#format-version](README.md#format-version).
- All XML below was verified against the original HTML.

Element order: tree order — `clip`, `tracks`, `track`, `feeds`, `feed`, `storageFormat`, `spans`, `span`, `paths`, `path`, `versions`, `version`, `handler`, `time`, `rate`, `rational`, `dict`, `value`, `metadataEdits`, `edits`, `edit`, `additions`, `add`, then [simple leaf children](#simple-leaf-child-elements).

---

## clip

`<clip>` — **root** of an Open Clip.

- **Parent:** none (document root). Examples start with `<?xml version="1.0"?>` (one uses `<?xml version="1.0" encoding="UTF-8"?>`).

**Attributes**

| Attribute | Data Type | Allowed Values | Occurrence | Description |
|---|---|---|---|---|
| `type` | string | `clip` | 1 | Type of the element. |
| `version` | unsigned integer | `8` | 1 | Version of the XML element. (Examples use `9`.) |

**Children**

| Element | Data Type | Occurrence | Description |
|---|---|---|---|
| `<name>` | string | 0-1 | Name of the clip. Inferred from the file name if absent. |
| `<tracks>` | tracks | 0-1 | List of tracks in the clip. |
| `<versions>` | versions | 0-1 | List of versions in the clip. |
| `<sourceName>` | string | 0-1 | Source Name (aka Tape Name in some workflows). |
| `<startTimecode>` | time | 0-1 | Start timecode of the clip. If not defined, the start timecode of the intersection of all the tracks' time ranges is used. |
| `<duration>` | time | 0-1 | Duration of the clip. If not defined, the union of all the feeds' duration is computed. |
| `<editRate>` | rate | 0-1 | Rate common to all tracks. If not defined, a common rate of all tracks' edit rate is computed. |
| `<comment>` | string | 0-1 | Unparsed text converted into a clip note. |
| `<handler>` | handler | 0-1 | Clip Handler. May differ from the track handler. |
| `<userData>` | dict | 0-1 | Dictionary of metadata that is passed through without interpretation. |

**Example (simplest Open Clip)**

```xml
<?xml version="1.0"?>
<clip type="clip" version="9">
    <tracks>
        <track uid="t0">
            <trackType>video</trackType>
            <feeds>
                <feed vuid="v0" uid="f0">
                    <spans>
                        <span>
                            <path encoding="file">Media/Video1.mov</path>
                        </span>
                    </spans>
                </feed>
            </feeds>
        </track>
    </tracks>
</clip>
```

Clip-level start timecode (48 ticks at 24 = 00:00:02:00) — excerpt of [examples.md Example 8](examples.md#example-8-timing-a-clip), `...` elided:

```xml
<clip type="clip" version="9">
    <startTimecode type="time">
        <rate type="rate">24</rate>
        <nbTicks>48</nbTicks>
    </startTimecode>
    <tracks>
        ...
    </tracks>
</clip>
```

Remarks (from source): only a subset of the schema is needed; information not explicitly set (timecode, duration) is inferred from the media (e.g. `.mov` header, `.dpx` sequence file name or headers). Eight complete clip examples are in [examples.md](examples.md).

---

## tracks

`<tracks>` — container for all the `<track>` elements making up an Open Clip.

- **Parent:** `<clip>`

**Attributes**

| Attribute | Data Type | Allowed Values | Occurrence | Description |
|---|---|---|---|---|
| `type` | string | `tracks` | 0-1 | Type of the element. |
| `version` | unsigned integer | `8` | 0-1 | Version of the XML element. |

**Children**

| Element | Data Type | Occurrence | Description |
|---|---|---|---|
| `<track>` | track | * | Each track contained in the list of tracks. |

**Example**

```xml
<tracks type="tracks">
    <track uid="t0">
        <trackType>video</trackType>
        <feeds>
            <feed vuid="v0" uid="f0">
                <spans>
                    <span>
                        <path encoding="file">Media/Video1.mov</path>
                    </span>
                </spans>
            </feed>
        </feeds>
    </track>
</tracks>
```

(Multi-channel OpenEXR `<tracks>` example: [examples.md](examples.md#example-6-multi-track-from-one-openexr).)

---

## track

`<track>` — the information that constitutes one track. Each track represents a distinct element of the clip, e.g.:
- A layer in a Photoshop file
- A video, or one of multiple audio tracks, in a QuickTime file
- One of multiple render passes contained in a multi-channel OpenEXR file

- **Parent:** `<tracks>`

**Attributes**

| Attribute | Data Type | Allowed Values | Occurrence | Description |
|---|---|---|---|---|
| `type` | string | `track` | 0-1 | Type of the element. |
| `version` | unsigned integer | `7` | 0-1 | Version of the XML element. |
| `uid` | string | any | **1** | Each `uid` must be unique across track elements when contained in a `<tracks>` element. |
| `currentVersion` | string | any | 0-1 | Version UID of the current version. Synchronised with the one in `<versions>` XML element if missing. |

**Children**

| Element | Data Type | Occurrence | Description |
|---|---|---|---|
| `<trackType>` | string | **1** | Track's type. Typically `video`, `audio`, or `generic`. |
| `<extendedType>` | string | 0-1 | Extended track type; refines the type (e.g. for video, the layer pass: shadow, occlusion, normal, etc.). Inferred from the parent node if missing. |
| `<feeds>` | feeds | 0-1 | Each feed contained in the list of feeds. Each feed is associated with a version in the clip `<versions>` element. |
| `<handler>` | handler | 0-1 | Track's handler information. |
| `<name>` | string | 0-1 | Name of the track. |
| `<sourceName>` | string | 0-1 | Source name of the track (sometimes referred to as tape name in older workflows). |
| `<comment>` | string | 0-1 | Unparsed text converted into a clip note. |
| `<editRate>` | rate | 0-1 | Edit rate of the track. Can be defined when all feeds' sample rates do not match, to explicitly define the working rate for the ensemble. If not defined, a common rate based on the feeds' sample rates is computed. |
| `<dropMode>` | string | 0-1 | Drop frame mode of the media. Only required for timings with a possible drop-frame mode. Allowed: `DF` (drop-frame media), `NDF` (non drop-frame media). |
| `<duration>` | time | 0-1 | Time duration of the track. If not defined, the union of all the feeds' duration is computed. |
| `<startTimecode>` | time | 0-1 | Start timecode of the track. If not defined, the earliest start timecode of all the feeds is used. |
| `<userData>` | dict | 0-1 | Dictionary of metadata that is passed through without interpretation. |

**Examples**

Additional elements override the media metadata or add metadata without changing the media header:

```xml
<track uid="t0">
    <trackType>video</trackType>
    <name>My name</name>
    <sourceName>My tape name</sourceName>
    <comment>My comment</comment>
    <feeds>
        <feed vuid="v0" uid="f0">
            <spans>
                <span>
                    <path encoding="file">Media/Video1.mov</path>
                </span>
            </spans>
        </feed>
    </feeds>
    <userData>
        <assetId type="string">11231-2312323</assetId>
    </userData>
</track>
```

Forcing track timing (duration longer than the media; gaps padded with `No Media`):

```xml
<track uid="t0">
    <trackType>video</trackType>
    <startTimecode type="time">
        <nbTicks>86400</nbTicks>
        <rate type="rate">24</rate>
    </startTimecode>
    <duration type="time">
        <nbTicks>8640</nbTicks>
        <rate type="rate">24</rate>
    </duration>
    <feeds>
        <feed vuid="v0" uid="f0">
            <spans>
                <span>
                    <path encoding="file">Media/Video1.[1000-2000].dpx</path>
                </span>
            </spans>
        </feed>
        <feed vuid="v1" uid="f1">
            <spans>
                <span>
                    <path encoding="file">Media/Video2.[1000-1500].dpx</path>
                </span>
            </spans>
        </feed>
    </feeds>
</track>
```

> **Source ambiguity:** this example (and several on Feed/Feeds) uses `encoding="file"` with a bracketed frame range, while `<path>` documents that `file` "reads the path as is" and `pattern` "interprets the brackets". For a frame range, `encoding="pattern"` is what the `<path>` page and the full-clip examples use.

> **Agent notes:** Multi-channel OpenEXR: set `track@uid` to the actual EXR layer name (e.g. `BEAUTY:MasterBeauty`, `Matte1`); if it doesn't match a layer, the track defaults to the first layer. Audio: "There is no method to set left and right for the audio stereo tracks. Use naming conventions for the media files." (Clip page.)

---

## feeds

`<feeds>` — container for all the `<feed>` elements of a `<track>`. Each `<feed>` is a version of the media; `currentVersion` selects the `<feed>` to use.

- **Parent:** `<track>`

**Attributes**

| Attribute | Data Type | Allowed Values | Occurrence | Description |
|---|---|---|---|---|
| `type` | string | `feeds` | 0-1 | Type of the element. |
| `version` | unsigned integer | `7` | 0-1 | Version of the XML element. |
| `currentVersion` | string | any | 0-1 | Defines which `<feed>` to use as the current, based on matching `vuid` on each `<feed>` child. If not defined, the current version of the `<versions>` of the `<clip>` is used. |

Remark (source): `currentVersion` is found in both `<feeds>` and `<versions>`; keep them in sync. Its function is to flag a preferred version; in Flame it indicates the version to display in MediaHub. If the value is not one of the `vuid`, Flame generates a `No Media` feed for the current feed.

**Children**

| Element | Data Type | Occurrence | Description |
|---|---|---|---|
| `<feed>` | feed | * | Each feed contained in the list of feeds. |

**Example (multi-version)**

```xml
<feeds currentVersion="v0">
    <feed vuid="v0" uid="f0">
        <spans>
            <span>
                <path encoding="file">Media/Video1.[1000-2000].dpx</path>
            </span>
        </spans>
    </feed>
    <feed vuid="v1" uid="f1">
        <spans>
            <span>
                <path encoding="file">Media/Video2.[1000-1500].dpx</path>
            </span>
        </spans>
    </feed>
</feeds>
```

> **Source ambiguity:** the prose of this example says "If the `currentVersion` attribute is not defined, the last `<feed>` in the list is assumed to be the active version", whereas the attribute table says the clip `<versions>` current version is used (and `<versions>` itself defaults to the last `<version>`).

---

## feed

`<feed>` — an actual media stream (a file container can contain one or more feeds). Within a `<track>`, a feed corresponds to a specific `<version>` (a creative iteration, or a different quality/resolution of the track).

- **Parent:** `<feeds>`
- Within a `<track>`, each `<feed>` has a different `vuid`. Across tracks, feeds with matching `vuid` constitute a version.
- `<span>` elements within a `<feed>` must all contain the same type of media, as defined by the media handler used by the Gateway.

**Attributes**

| Attribute | Data Type | Allowed Values | Occurrence | Description |
|---|---|---|---|---|
| `type` | string | `feed` | 0-1 | Type of the element. |
| `version` | unsigned integer | `8` | 0-1 | Version of the XML element. |
| `uid` | string | any | **1** | Uniquely identifies the feed. Usually universally unique but needs to be at least unique within the clip. |
| `vuid` | string | any | **1** | Identifies the version of the feed. In a `<track>`, no two `<feed>` elements can have the same `vuid`. `<feed>` elements in different `<track>` elements can share the same `vuid`. |

**Children**

| Element | Data Type | Occurrence | Description |
|---|---|---|---|
| `<storageFormat>` | dict | 0-1 | Describes the format of the media referenced. Populated by the Gateway; generally not required when creating an Open Clip (but mandatory for stereo — see [storageFormat](#storageformat)). |
| `<spans>` | spans | 0-1 | List of `<span>` representing media files to read on disk. |
| `<handler>` | handler | 0-1 | Feed's handler information. |
| `<sampleRate>` | rate | 0-1 | Sample (frame) rate of the feed. If not defined, the feed timing is frame-based. |
| `<startTimecode>` | time | 0-1 | Start timecode of the feed. If not defined, the start timecode of the first `<span>` in `<spans>` is used. Overrides the timecode inferred from the media. |
| `<startOffset>` | 64-bit integer | 0-1 | Difference between the index used when accessing the parent `<track>` and the actual sample index used to query the spans. |
| `<duration>` | time | 0-1 | Duration of the feed. The sum of the duration of all the `<span>` in `<spans>` if not specified. |
| `<comment>` | string | 0-1 | Unparsed text converted into a clip note. |
| `<userData>` | dict | 0-1 | Dictionary of metadata that is passed through without interpretation. |
| `<metadataEdits>` | metadataEdits | 0-1 | Metadata edits (format v8+). See [metadataEdits](#metadataedits). |

**Examples**

```xml
<feed vuid="v0" uid="f0">
    <comment>My comment</comment>
    <spans>
        <span>
            <path encoding="file">Media/Video1.mov</path>
        </span>
    </spans>
</feed>
```

Forced timing (feed longer than the media; gaps padded with `No Media`):

```xml
<feed vuid="v0" uid="f0">
    <startTimecode type="time">
        <nbTicks>86400</nbTicks>
        <rate type="rate">24</rate>
    </startTimecode>
    <duration type="time">
        <nbTicks>8640</nbTicks>
        <rate type="rate">24</rate>
    </duration>
    <sampleRate>24</sampleRate>
    <spans>
        <span>
            <path encoding="file">Media/Video1.[1000-2000].dpx</path>
        </span>
    </spans>
</feed>
```

`startOffset` = -2 ("a feed having two spans of four frames"):

```text
Feed indexes   [00--01--02--03--04--05--06--07--08--09--10]
Spans indexes  ########[00--01--02--03][00--01--02--03]####
```

```xml
<feed vuid="v0" uid="f0">
    <startOffset>-2</startOffset>
    <spans>
        <span>
            <path encoding="file">Media/Video1.[00-03].dpx</path>
            <path encoding="file">Media/Video2.[00-03].dpx</path>
        </span>
    </spans>
</feed>
```

`startOffset` = 2:

```text
Feed indexes   ########[00--01--02--03--04--05--06--07--08--09--10]
Spans indexes  [00--01--02--03][00--01--02--03]####################
```

```xml
<feed vuid="v0" uid="f0">
    <startOffset>2</startOffset>
    <spans>
        <span>
            <path encoding="file">Media/Video1.[00-03].dpx</path>
            <path encoding="file">Media/Video2.[00-03].dpx</path>
        </span>
    </spans>
</feed>
```

> **Source ambiguity (verified identical in HTML):** the two `startOffset` examples are described as "two spans of four frames" but the XML puts **two `<path>` elements inside one `<span>`**, which contradicts `<span>` (`<path>` occurrence 0-1). Two spans would be written as two `<span>` elements each with one `<path>`. They also use `encoding="file"` with bracket ranges (see the note under [track](#track)). Also note the diagrams: with `startOffset` = -2 the span samples begin 2 indexes *after* feed index 0; with +2 they begin 2 indexes *before*.

---

## storageFormat

`<storageFormat>` — describes the format of the media referenced by a `<feed>`. Documented data type: `dict`; the only example uses `type="format"`. No reference table exists for its children; the only source is the stereo example on the "Clip" page.

- **Parent:** `<feed>`
- "This element is populated by the Gateway and is generally not required when creating an Open Clip." **But** for stereo: "In a Stereo Open Clip, the `storageFormat` element is a mandatory child of each `feed` that is stereo (with a `subFeedID` for each eye). It must be written as it appears here:"

```xml
<storageFormat type="format">
    <type>video</type>
    <isStereo type="bool">true</isStereo>
    <lSubFeedId type="uid">Left</lSubFeedId>
    <rSubFeedId type="uid">Right</rSubFeedId>
</storageFormat>
```

| Child (from example only) | Content in example |
|---|---|
| `<type>` | `video` |
| `<isStereo type="bool">` | `true` |
| `<lSubFeedId type="uid">` | `Left` — sub-feed id of the left eye |
| `<rSubFeedId type="uid">` | `Right` — sub-feed id of the right eye |

> **Agent note:** In the stereo example the `<path subFeedId="...">` values (`Left`/`Right`) match `lSubFeedId`/`rSubFeedId`. The "Span" page's stereo fragment uses lowercase `right`/`left` without a `<storageFormat>`; when writing a full stereo clip, follow the Clip-page example exactly (source says "must be written as it appears here"). The source prose writes `subFeedID`; the attribute in all XML is `subFeedId`.

---

## spans

`<spans>` — contains all the `<span>` elements that make up the `<feed>`. Spans are concatenated in order, top to bottom, into one stream (e.g. camera files split by a file-size limit).

- **Parent:** `<feed>`

**Attributes**

| Attribute | Data Type | Allowed Values | Occurrence | Description |
|---|---|---|---|---|
| `type` | string | `spans` | 0-1 | Type of the element. |
| `version` | unsigned integer | `8` | 0-1 | Version of the XML element. |

**Children**

| Element | Data Type | Occurrence | Description |
|---|---|---|---|
| `<span>` | span | * | Each span contained in the list of spans. |

**Example**

```xml
<spans>
    <span>
        <path encoding="file">Media/Video1.mov</path>
    </span>
    <span>
        <path encoding="file">Media/Video2.mov</path>
    </span>
    <span>
        <path encoding="file">Media/Video3.mov</path>
    </span>
</spans>
```

---

## span

`<span>` — media that make up all or part of the `<feed>`; describes its duration and the path to the physical media. Multiple spans = multiple media files/sequences make up one feed; listing order = reading order.

- **Parent:** `<spans>`
- All media referenced in a `<span>` must have homogeneous properties (same codec, compression, format, length, rate...). To mix media types in a `<clip>`, use different `<track>` elements. Formats cannot be mixed across spans of a feed (e.g. DPX in one span, TIFF in another).
- **A `<span>` with a `<duration>` but no `<path>` is a gap.**
- No offset can be applied to a span; a span has no timing information other than what can be inferred from its media (Clip page, Example 4 remarks). Feed duration = sum of spans.

**Attributes**

| Attribute | Data Type | Allowed Values | Occurrence | Description |
|---|---|---|---|---|
| `type` | string | `span` | 0-1 | Type of the element. |
| `version` | unsigned integer | `8` | 0-1 | Version of the XML element. |

**Children**

| Element | Data Type | Occurrence | Description |
|---|---|---|---|
| `<duration>` | time | 0-1 | Time duration of the span. If not defined, duration from the media will be used. |
| `<trackIndex>` | unsigned integer | 0-1 | Track index in the media file track. Used to read a specific track/channel of multi-track/multi-channel media in different span objects. |
| `<path>` | path | 0-1 | Path pointing to the actual media files. Cannot be used with `<paths>`. |
| `<paths>` | paths | 0-1 | Path map pointing to the actual media files. Used to represent stereo video media. Cannot be used with `<path>`. |
| `<userData>` | dict | 0-1 | Dictionary of metadata that is passed through without interpretation. |

**Examples**

Duration override (file's actual duration overridden):

```xml
<span>
    <duration type="time">
        <nbTicks>48</nbTicks>
        <rate type="rate">24</rate>
    </duration>
    <path encoding="file">Media/Video1.mov</path>
</span>
```

Gap of two seconds:

```xml
<span>
    <duration type="time">
        <nbTicks>48</nbTicks>
        <rate type="rate">24</rate>
    </duration>
</span>
```

Second track (layer) of a multi-channel OpenEXR (`trackIndex` is 0-based per this example):

```xml
<span>
    <trackIndex>1</trackIndex>
    <path encoding="pattern">ABGR.[00001001-00001004].exr</path>
</span>
```

Stereo video media:

```xml
<span>
    <paths>
      <path subFeedId="right" encoding="pattern">right.[00001001-00001004].exr</path>
      <path subFeedId="left" encoding="pattern">left.[00001001-00001004].exr</path>
    </paths>
</span>
```

---

## paths

`<paths>` — a map of `<path>` elements, each a different view on the same material, in multiple files. Most common use: stereo video (right and left polarities). Each `<path>` child represents media uniform in all aspects (timing, duration, rate, format, codec). Differs from `<tracks>`, which shows different representations of the same event (layers or passes) that can vary in any aspect.

- **Parent:** `<span>` (mutually exclusive with `<path>` there)

**Attributes**

| Attribute | Data Type | Allowed Values | Occurrence | Description |
|---|---|---|---|---|
| `type` | string | `paths` | 0-1 | Type of the element. |
| `version` | unsigned integer | `8` | 0-1 | Version of the XML element. |

**Children**

| Element | Data Type | Occurrence | Description |
|---|---|---|---|
| `<path>` | path | * | Each path in the list. Each `<path>` needs a **unique `subFeedId` attribute** identifying the sub-feed (e.g. "Left" for the left eye, "Right" for the right eye). |

**Example**

```xml
<paths>
    <path subFeedId="Left" encoding="pattern">MEDIA/left-eye.[0001-0005].tif</path>
    <path subFeedId="Right" encoding="pattern">MEDIA/right-eye.[0001-0005].tif</path>
</paths>
```

---

## path

`<path>` — the path to the media. Absolute, or **relative to the Open Clip file**. Either a regular file or a pattern; a pattern can be a base name with a ranged frame suffix, a path with tokens, or a combination of both.

- **Parents:** `<span>`, `<paths>`

**Attributes**

| Attribute | Data Type | Allowed Values | Occurrence | Description |
|---|---|---|---|---|
| `type` | string | `path` | 0-1 | Type of the element. |
| `version` | unsigned integer | `8` | 0-1 | Version of the XML element. |
| `encoding` | string | `file` or `pattern` | 0-1 | Encoding of the path. `file` reads the path as is. `pattern` interprets the brackets. |
| `subFeedId` | string (not in table) | e.g. `Left`, `Right` | required inside `<paths>` | Not in the Path attribute table; documented on `<paths>` ("needs a unique `subFeedId`") and used in stereo examples. |

**Text content**

| Element | Data Type | Occurrence | Description |
|---|---|---|---|
| #cdata | string | 1 | File or pattern |

**Pattern syntax (from examples)**

| Form | Example | Meaning |
|---|---|---|
| Absolute file | `<path encoding="file">/dir/file.mov</path>` | QuickTime movie file |
| Relative file | `<path encoding="file">subDir/file.mov</path>` | relative to the `.clip` location; with clip at `/dir/MyClip.clip` → source says `/dir/subdir/file.mov` (casing differs in source) |
| Frame range | `<path encoding="pattern">/dir/file_[1-5].dpx</path>` | file sequence |
| Zero-padded range | `<path encoding="pattern">/dir/file_[0001-0005].dpx</path>` | padded sequence |
| Padding smaller than largest frame | `<path encoding="pattern">/dir/file_[099-10005].dpx</path>` | padding can be smaller than the largest file |
| `{frame}` token | `<path encoding="pattern">/dir/file_{frame}.dpx</path>` | unbounded sequence; length = smallest to largest file; gaps ignored |
| Literal braces | `<path encoding="file">/dir/file_{frame}.dpx</path>` | reads a file literally named `/dir/file_{frame}.dpx` |
| Literal brackets | `<path encoding="file">/dir/file_[12].dpx</path>` | reads a file literally named `/dir/file_[12].dpx` |

`{frame}` equivalence table (verbatim):

| Files | Equivalent range |
|---|---|
| `/dir/files_3.dpx`, `/dir/files_4.dpx`, `/dir/files_5.dpx` | `/dir/files_[3-4].dpx` |
| `/dir/files_3.dpx`, `/dir/files_99.dpx`, `/dir/files_105.dpx` | `/dir/files_[3-105].dpx` |

> **Source ambiguity:** the first row's equivalent range `[3-4]` (verified identical in HTML) looks like a typo for `[3-5]` given "length matching the range of the smallest to the largest file". Also the table uses `files_` while the example uses `file_`.

> **Agent note:** "Using the `encoding="file"` on a pattern allows reading files that would otherwise conflict" — i.e. use `file` for literal paths containing `{}`/`[]`, and `pattern` for ranges/tokens.

---

## versions

`<versions>` — lists the available versions of a clip and the version currently in use. A specific version of a clip = all `<feed>` elements sharing the same `vuid` across different `<track>` elements. The client application reading the `.clip` is not required to set `currentVersion`; it only serves as a flag placed by the creator.

- **Parent:** `<clip>`

**Attributes**

| Attribute | Data Type | Allowed Values | Occurrence | Description |
|---|---|---|---|---|
| `type` | string | `versions` | 0-1 | Type of the element. |
| `version` | unsigned integer | `7` | 0-1 | Version of the XML element. |
| `currentVersion` | string | any | 0-1 | Defines which `<version>` to use as the current, based on matching `uid` on each `<version>` child. If not defined, the last one is considered the current. |

Additional attribute seen in examples (not in table): `nbVersions` (e.g. `nbVersions="2"`), the number of versions.

**Children**

| Element | Data Type | Occurrence | Description |
|---|---|---|---|
| `<version>` | version | * | Each version contained in the list of versions. |

**Example**

```xml
<versions currentVersion="v2">
    <version uid="v1"/>
    <version uid="v2"/>
    <version uid="v3"/>
</versions>
```

paired with:

```xml
<tracks>
    <track uid="track1">
        <feeds>
            <feed vuid="v1" uid="t1f1"/>
            <feed vuid="v3" uid="t1f2"/>
        </feeds>
    </track>
    <track uid="track2">
        <feeds>
            <feed vuid="v1" uid="t2f1"/>
            <feed vuid="v2" uid="t2f2"/>
            <feed vuid="v3" uid="t2f3"/>
        </feeds>
    </track>
</tracks>
```

- Version 1: track1 using feed `t1f1` and track2 using `t2f1`;
- Version 2: track2 using `t2f2` only (no `vuid` in track1 matching "v2");
- Version 3: track1 using `t1f2` and track2 using `t2f3`.
- The client application should display version 2 because `currentVersion="v2"`.

(This example is "simplified": tracks omit the required `<trackType>` and feeds omit `<spans>`.)

---

## version

`<version>` — metadata about one clip version; which version is defined by `uid`. Usually contained in `<versions>`.

- **Parent:** `<versions>`

**Attributes**

| Attribute | Data Type | Allowed Values | Occurrence | Description |
|---|---|---|---|---|
| `type` | string | `version` | 0-1 | Type of the element. |
| `version` | unsigned integer | `8` | 0-1 | Version of the XML element. |
| `uid` | string | any | **1** | Defines which `<feed>` of each `<track>` to use, based on matching `vuid`. Each `uid` must be unique across version elements. |

**Children**

| Element | Data Type | Occurrence | Description |
|---|---|---|---|
| `<name>` | string | 0-1 | Name of the version. |
| `<comment>` | string | 0-1 | Unparsed text converted into a clip note. |
| `<creationDate>` | string | 0-1 | Unparsed text used to store the creation date of the version. |
| `<userData>` | dict | 0-1 | Dictionary of metadata that is passed through without interpretation. |

**Examples**

```xml
<version uid="v0"/>
```

```xml
<version uid="v0">
    <name>First version</name>
    <comment>Roto done by John</comment>
    <creationDate>January 12, 2025</creationDate>
    <userData>
        <assetId type="string">11231-2312323</assetId>
    </userData>
</version>
```

---

## handler

`<handler>` — the object responsible for reading the media and metadata files; its options control how media is structured, read and interpreted. Two main forms:
- **Clip handler** (child of `<clip>`): responsible for clip metadata and track organization.
- **Feed handler** (child of `<feed>`): responsible for I/O operations.
- Simple/homogeneous clips: all handlers identical. Complex/heterogeneous clips: clip handler and individual feed handlers can differ.

- **Parents:** `<clip>`, `<track>`, `<feed>`

**Attributes**

| Attribute | Data Type | Allowed Values | Occurrence | Description |
|---|---|---|---|---|
| `type` | string | `handler` | 0-1 | Type of the element. |
| `version` | unsigned integer | `8` | 0-1 | Version of the XML element. |

**Children**

| Element | Data Type | Occurrence | Description |
|---|---|---|---|
| `<name>` | string | 0-1 | Name of the handler. (Examples: `MIO Clip`.) |
| `<version>` | unsigned integer | 0-1 | Version of the handler. (Not the `version` attribute.) |
| `<longName>` | string | 0-1 | Display name of the handler, to be used in UI. (Example: `Open Clip`.) |
| `<options>` | dict | 0-1 | Options for metadata and I/O operations. Handler specific. |
| `<conversionOptions>` | dict | 0-1 | Options for the image conversion pipeline. |

**Open Clip handler option `ScanPattern`**

The Open Clip handler can dynamically populate the Open Clip from file-system content. `ScanPattern` specifies a browsing pattern used to construct the clip.

| Token | Description |
|---|---|
| `{name}` | Name of the resulting clip. If the Open Clip defines the name in the XML, it must match. If not, it is inferred from files on disk. If no match is found or the name cannot be inferred, the clip may not be constructed correctly. |
| `{frame}` | Numerical frame sequence. Treated as infinite: no gap detection. Padding inferred from files on disk. |
| `{extension}` | File extension. Used to build a clip with heterogeneous media types. |
| `{version}` | Version. Builds a multi-version clip. Numerical only if adjacent to another token. |
| `{track}` | Track. Builds a multi-track clip. |
| `{polarity}` | Polarity. Builds a multi-feed track; used to define Left/Right feed for stereo video media. |

(Open Clip Creator additionally documents `{ext}` as an alias form `{ext}/{extension}` and `{frame####}` padding — see [open-clip-creator.md](open-clip-creator.md).)

**Other options seen in the Gateway-filled example** (no further documentation in source): `AlignToZero` (bool), `RateMode` (string, e.g. `Header`), `RateValue` (rate), `SourceNameDirLevelUp` (uint32), `SourceNameMode` (string, e.g. `Auto`), `SourceNameValue` (string).

**Examples**

Complete handler as filled by the Wiretap Gateway:

```xml
<handler type="handler">
    <name>MIO Clip</name>
    <version>2</version>
    <longName>Open Clip</longName>
    <options type="dict">
        <AlignToZero type="bool">false</AlignToZero>
        <RateMode type="string">Header</RateMode>
        <RateValue type="rate">
            <numerator>24000</numerator>
            <denominator>1001</denominator>
        </RateValue>
        <SourceNameDirLevelUp type="uint32">1</SourceNameDirLevelUp>
        <SourceNameMode type="string">Auto</SourceNameMode>
        <SourceNameValue type="string">IMPORT</SourceNameValue>
    </options>
</handler>
```

Scan pattern (multi-version):

```xml
<handler>
    <name>MIO Clip</name>
    <options>
        <ScanPattern>Media/Video_v{version}.{frame}.dpx</ScanPattern>
    </options>
</handler>
```

Scan pattern (multi-channel / multi-version, heterogeneous media types):

```xml
<handler>
    <name>MIO Clip</name>
    <options>
        <ScanPattern>Media/Video_t{track}_v{version}.{frame}.{extension}</ScanPattern>
    </options>
</handler>
```

Expansion results of the multi-version scan pattern: [examples.md](examples.md#handler-scanpattern-expansion).

---

## time

Time value type — a number of samples (images or audio samples) combined with a `<rate>`. Used by `<startTimecode>`, `<duration>` (on `<clip>`, `<track>`, `<feed>`, `<span>`), and as a value type (`type="time"`) in dicts.

**Attributes**

| Attribute | Data Type | Allowed Values | Occurrence | Description |
|---|---|---|---|---|
| `type` | string | `time` | 0-1 | Type of the element. |
| `version` | unsigned integer | `8` | 0-1 | Version of the XML element. |

**Children**

| Element | Data Type | Occurrence | Description |
|---|---|---|---|
| `<rate>` | rate | 0-1 | Rate element. If no rate is specified, the time is frame/sample based or inferred from the parent node. |
| `<nbTicks>` | 64-bit unsigned integer | **1** | Number of samples that make up the media. For frame-based media, a number of frames (images). `nbTicks / rate` = seconds. |
| `<dropMode>` | string | 0-1 | Drop frame mode. Only required for timings with a possible drop-frame mode. Allowed: `DF` (drop-frame), `NDF` (non drop-frame). |

Child order varies in the sources (`<rate>` before or after `<nbTicks>`).

**Examples**

30 frames at 23.976 fps:

```xml
<time type="time">
    <rate type="rate">
        <numerator>24000</numerator>
        <denominator>1001</denominator>
    </rate>
    <nbTicks>30</nbTicks>
    <dropMode>DF</dropMode>
</time>
```

30 frames, no rate (e.g. 30 JPEGs without context):

```xml
<time type="time">
    <nbTicks>30</nbTicks>
</time>
```

1 second at 30 fps:

```xml
<time type="time">
    <rate>30</rate>
    <nbTicks>30</nbTicks>
</time>
```

> **Agent note:** A `<startTimecode>` "does not have to be at the rate of the media: it is just a unit of measure that defines where the media starts on the Timeline. The selected rate defines how many ticks are in a second." E.g. `rate 24, nbTicks 48` = 00:00:02:00; `rate 24, nbTicks 86400` = 01:00:00:00.

---

## rate

Rate value type — prefer numerator/denominator over decimals for arithmetic accuracy. Similar to rational, but for rates: **a decimal close to a known fractional rate is converted to that fraction** (e.g. `23.98` → `24000/1001`). Used by `<editRate>`, `<sampleRate>`, `<rate>` inside time, and `type="rate"` dict values.

**Attributes**

| Attribute | Data Type | Allowed Values | Occurrence | Description |
|---|---|---|---|---|
| `type` | string | `rate` | 0-1 | Type of the element. |
| `version` | unsigned integer | `8` | 0-1 | Version of the XML element. |

**Children** — two mutually exclusive formats:

Rational format:

| Element | Data Type | Occurrence | Description |
|---|---|---|---|
| `<numerator>` | 64-bit integer | 1 | Upper portion of a rational number representing a rate. |
| `<denominator>` | unsigned integer | 1 | Lower portion of a rational number representing a rate. |

Decimal format:

| Element | Data Type | Occurrence | Description |
|---|---|---|---|
| #cdata | float | 1 | Decimal number representing a rate. |

**Examples**

```xml
<rate type="rate">
    <numerator>24000</numerator>
    <denominator>1001</denominator>
</rate>
```

```xml
<rate type="rate">23.976</rate>
```

---

## rational

Rational value type — a fraction for general (non-rate) use.

**Attributes**

| Attribute | Data Type | Allowed Values | Occurrence | Description |
|---|---|---|---|---|
| `type` | string | `rational` | 0-1 | Type of the element. |
| `version` | unsigned integer | `8` | 0-1 | Version of the XML element. |

**Children** — two mutually exclusive formats:

| Format | Element | Data Type | Occurrence | Description |
|---|---|---|---|---|
| Rational | `<numerator>` | 64-bit integer | 1 | Upper portion of the fraction. |
| Rational | `<denominator>` | unsigned integer | 1 | Lower portion of the fraction. |
| Decimal | #cdata | 64-bit integer | 1 | Numerator of a fraction; 1 is assumed for the denominator. |

**Examples**

```xml
<rational type="rational">
    <numerator>16</numerator>
    <denominator>9</denominator>
</rational>
```

```xml
<rational type="rational">5</rational>
```

---

## dict

Dictionary — key-value container of arbitrary key-value pairs with heterogeneous types. The **element name is the key**; children are [value](#value) variants. Nested dictionaries supported (format v5+). Used by `<userData>`, `<options>`, `<conversionOptions>`, `<storageFormat>`.

**Attributes**

| Attribute | Data Type | Allowed Values | Occurrence | Description |
|---|---|---|---|---|
| `type` | string | `dict` | 0-1 | Type of the element. |
| `version` | unsigned integer | `8` | 0-1 | Version of the XML element. |

**Children:** variants of the type `value`.

**Examples**

```xml
<userData type="dict">
    <appName type="string">Flame</appName>
    <appVersion type="int16">2017</appVersion>
    <mode type="int16" label="Full Res / No Proxy">0x12341</mode>
</userData>
```

Nested complex types:

```xml
<userData type="dict">
    <options type="dict">
        <disable type="bool">True</disable>
        <sampleRate type="rate">
            <numerator>24</numerator>
            <denominator>1001</denominator>
        </sampleRate>
        <speed type="int8">23</speed>
    </options>
</userData>
```

> **Source oddity:** `0x12341` stored as `int16` exceeds the 16-bit range; it is the source's illustrative value, not a validated one.

---

## value

`value` — user-defined variant element representing many data types. The element name is arbitrary (it is the key); used as children of `<dict>`, and as the content of `<edit>` and `<add>`.

**Attributes**

| Attribute | Data Type | Allowed Values | Occurrence | Description |
|---|---|---|---|---|
| `type` | string | Value Data Type (table below) | 0-1 | Type of the element. **String is assumed if not specified.** |
| `label` | string | any | 0-1 | Display label for complex types. Value is converted to string if possible when not specified. **Not supported in `<edit>` and `<add>` elements.** |

**Allowed `type` values (Value Data Types)**

| `type` | Description |
|---|---|
| `int` | integer |
| `uint` | unsigned integer |
| `int8` | 8-bit integer |
| `uint8` | 8-bit unsigned integer |
| `int16` | 16-bit integer |
| `uint16` | 16-bit unsigned integer |
| `int32` | 32-bit integer |
| `uint32` | 32-bit unsigned integer |
| `int64` | 64-bit integer |
| `uint64` | 64-bit unsigned integer |
| `float` | single precision floating point number |
| `double` | double precision floating point number |
| `bool` | boolean (`True`, `False`, `Yes`, `No`, `1`, `0`) |
| `string` | string |
| `binary` | escaped string to allow XML encoding (displayable/non null) |
| `bytes` | escaped string to allow XML encoding (not displayable/may contain null) — format v9 (2027.1) |
| `rate` | rate |
| `rational` | rational |
| `time` | time |
| `uid` | string |
| `keycode` | space-separated keycode |
| `dict` | dict |

The escaping scheme for `binary`/`bytes` is not specified in the source.

**Examples**

```xml
<value>Str</value>
```

Same serialization, different types:

```xml
<value1 type="string">12341</value1>
<value2 type="int">12341</value2>
<value3 type="float">12341</value3>
```

```xml
<mode type="int16" label="Full Res / No Proxy">0x12341</mode>
```

```xml
<sampleRate type="rate">
    <numerator>24</numerator>
    <denominator>1001</denominator>
</sampleRate>
```

---

## metadataEdits

`<metadataEdits>` — per-feed metadata modifications (format v8, Flame 2027). Contains `<edits>` and `<additions>`; **`<edits>` are applied first, `<additions>` second.** Evaluated per edit unit (usually a video frame). Full semantics: [metadata-edits.md](metadata-edits.md).

- **Parent:** `<feed>`

**Attributes**

| Attribute | Data Type | Allowed Values | Occurrence | Description |
|---|---|---|---|---|
| `type` | string | `metadataEdits` | 0-1 | Type of the element. |

**Children**

| Element | Data Type | Occurrence | Description |
|---|---|---|---|
| `<edits>` | edits | * | List of `<edit>` elements. To be applied, the metadata key must be present in the modified metadata dictionary read from the media file. |
| `<additions>` | additions | * | List of `<add>` elements. To be applied, the metadata key must not be present in the modified metadata dictionary read from the media file. |

**Example**

```xml
<metadataEdits type="metadataEdits">
    <edits>
        <edit key="ModifiedKey" type="string">NewValue</edit>
        <edit key="DiscardedKey" discarded="yes"></edit>
        <edit key="ExistingKey" renamedKey="RenamedKey"/>
        <edit key="OtherExistingKey" renamedKey="RenamedAndModifiedKey">NewValue</edit>
    </edits>
    <additions>
        <add key="AddedKey" type="string">AddedValue</add>
        <add key="DiscardedKey" discarded="yes" type="string">DiscardedValue</add>
    </additions>
</metadataEdits>
```

---

## edits

`<edits>` — list of `<edit>` elements applied to the metadata of each edit unit (each frame) read from the media file. All edit units within a feed share the same edits.

- **Parent:** `<metadataEdits>`
- **Attributes:** none documented.

| Element | Data Type | Occurrence | Description |
|---|---|---|---|
| `<edit>` | `<edit>` | * | Metadata edit to be applied to a modified metadata dictionary read from the media file. |

```xml
<edits>
    <edit key="ModifiedKey" type="string">NewValue</edit>
    <edit key="DiscardedKey" discarded="yes"></edit>
    <edit key="ExistingKey" renamedKey="RenamedKey">NewValue</edit>
</edits>
```

---

## edit

`<edit>` — modifies a value, discards a metadata key, renames a metadata key, or a combination. **Applied only if the key is present** in the modified metadata dictionary read from the media file. Discarded edits are not included in the resulting metadata.

- **Parent:** `<edits>`

**Attributes**

| Attribute | Data Type | Allowed Values | Occurrence | Description |
|---|---|---|---|---|
| `key` | string | any | **1** | Key used to identify the metadata element. |
| `type` | string | Value Data Type | 0-1 | Type of the element. String is assumed if not specified. |
| `discarded` | boolean | `True`, `False`, `Yes`, `No`, `1`, `0` | 0-1 | Discarded elements are not applied to resulting metadata. |
| `renamedKey` | string | any | 0-1 | If defined, the resulting metadata will have the renamed key instead of the original key. |

**Content:** variants of the type `value` (text for scalar types). `label` is not supported.

```xml
<edit key="ModifiedKey" type="string">NewValue</edit>
<edit key="DiscardedKey" discarded="yes"/>
<edit key="ExistingKey" renamedKey="RenamedKey"/>
<edit key="ExistingKey" renamedKey="RenamedKey">NewValue</edit>
```

(Each line is a separate source example; see [metadata-edits.md](metadata-edits.md).)

---

## additions

`<additions>` — list of `<add>` elements applied to the metadata read from the media file. All edit units within a feed share the same additions.

- **Parent:** `<metadataEdits>`
- **Attributes:** none documented.

| Element | Data Type | Occurrence | Description |
|---|---|---|---|
| `<add>` | `<add>` | * | Metadata addition to be applied to a modified metadata dictionary read from the media file. |

```xml
<additions>
    <add key="AddedKey" type="string">AddedValue</add>
    <add key="DiscardedKey" discarded="yes" type="string">DiscardedValue</add>
</additions>
```

---

## add

`<add>` — inserts a new metadata value; **applied only if the key does not already exist** in the current metadata dictionary. Discarded adds are not included in the resulting metadata. Evaluated per edit unit (frame).

- **Parent:** `<additions>`

**Attributes**

| Attribute | Data Type | Allowed Values | Occurrence | Description |
|---|---|---|---|---|
| `key` | string | any | **1** | Metadata key used to identify the metadata element. |
| `type` | string | Value Data Type | 0-1 | Type of the element. String is assumed if not specified. |
| `discarded` | boolean | `True`, `False`, `Yes`, `No`, `1`, `0` | 0-1 | Discarded elements are not applied to resulting metadata. |

(No `renamedKey` on `<add>`.)

**Content:** variants of the type `value`. `label` is not supported.

```xml
<add key="Key" type="string">value</add>
<add key="Key" discarded="yes" type="string">value</add>
```

---

## Simple leaf child elements

These have no page of their own; definitions come from the parent tables.

| Element | Data type | Parents | Meaning (source) |
|---|---|---|---|
| `<name>` | string | `clip`, `track`, `version`, `handler` | Clip name (inferred from file name if absent) / track name / version name / handler name |
| `<sourceName>` | string | `clip`, `track` | Source Name, aka Tape Name |
| `<comment>` | string | `clip`, `track`, `feed`, `version` | Unparsed text converted into a clip note (Open Clip Creator: "seen in Batch as a Note") |
| `<trackType>` | string | `track` (required) | Typically `video`, `audio`, or `generic` |
| `<extendedType>` | string | `track` | Refines track type (e.g. shadow, occlusion, normal pass) |
| `<dropMode>` | string | `track`, time | `DF` or `NDF` |
| `<editRate>` | rate | `clip`, `track` | Common / working rate |
| `<sampleRate>` | rate | `feed` | Sample (frame) rate; if absent timing is frame-based |
| `<startTimecode>` | time | `clip`, `track`, `feed` | Start timecode (defaults described per parent) |
| `<duration>` | time | `clip`, `track`, `feed`, `span` | Duration (defaults described per parent) |
| `<startOffset>` | 64-bit integer | `feed` | Track index minus span sample index offset |
| `<trackIndex>` | unsigned integer | `span` | Track/channel index inside multi-track media |
| `<userData>` | dict | `clip`, `track`, `feed`, `span`, `version` | Pass-through metadata, not interpreted |
| `<creationDate>` | string | `version` | Unparsed creation date text |
| `<longName>` | string | `handler` | UI display name |
| `<version>` (child) | unsigned integer | `handler` | Handler version |
| `<options>` | dict | `handler` | Handler-specific options (e.g. `ScanPattern`) |
| `<conversionOptions>` | dict | `handler` | Image conversion pipeline options |
| `<nbTicks>` | 64-bit unsigned integer | time | Sample count |
| `<rate>` | rate | time | Rate of the time |
| `<numerator>` / `<denominator>` | 64-bit integer / unsigned integer | rate, rational | Fraction parts |
