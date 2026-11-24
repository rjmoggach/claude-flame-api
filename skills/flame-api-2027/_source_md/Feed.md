<!-- source: Autodesk Flame Family 2027 Help _ Feed _ Autodesk.html -->
# Feed

A feed is an actual media stream. A file container can contain a single or multiple feeds.

While contained in a `<track>`, a feed corresponds to a specific `<version>`. A version can be either a creative iteration or different qualities and resolutions for the parent `<track>`.

The `vuid` attribute indicates the version of the `<feed>`.

- Within a `<track>`, each `<feed>` has a different `vuid`.
- Across multiple `<track>` elements, any `<feed>` with matching `vuid` constitutes a version.

`<span>` elements within a `<feed>` must all contain the same type of media, as defined by the media handler used by the Gateway.

---

## Attributes

| Attribute | Data Type | Allowed Values | Occurrence | Description |
|---|---|---|---|---|
| type | string | `feed` | 0-1 | Type of the element. |
| version | unsigned integer | `8` | 0-1 | Version of the XML element. |
| uid | string | any | 1 | Uniquely identifies the feed.<br><br>This ID is usually universally unique but needs to be at least unique within the clip. |
| vuid | string | any | 1 | Identifies the version of the feed.<br><br>In a `<track>` element, no two `<feed>` elements can have the same `vuid`.<br><br>`<feed>` elements in different `<track>` elements can share the same `vuid`. |

 Note: Optional attributes (0 occurrence attributes) will be inferred from the parent node.

---

## Children

| Element | Data Type | Occurrence | Description |
|---|---|---|---|
| `<storageFormat>` | dict | 0-1 | Describes the format of the media referenced.<br><br>This element is populated by the Gateway and is generally not required when creating an Open Clip. |
| `<spans>` | spans | 0-1 | List of `<span>` representing media files to read on disk. |
| `<handler>` | handler | 0-1 | Feed's handler information. |
| `<sampleRate>` | rate | 0-1 | Sample (frame) rate of the feed.<br><br>If not defined, the feed timing is frame-based. |
| `<startTimecode>` | time | 0-1 | Start timecode of the feed.<br><br>If not defined, the start timecode of the first `<span>` in `<spans>` is used. |
| `<startOffset>` | 64-bit integer | 0-1 | The offset represents the difference between the used index when accessing the parent `<track>` and the actual sample index used to query the spans. |
| `<duration>` | time | 0-1 | The duration of the feed.<br><br>The sum of the duration of all the `<span>` in `<spans>` if not specified. |
| `<comment>` | string | 0-1 | Unparsed text converted into a clip note. |
| `<userData>` | dict | 0-1 | Dictionary of metadata that is passed through without interpretation. |
| `<metadataEdits>` | metadataEdits | 0-1 | Metadata edits |

 Note: Children elements with the attribute `computed=1` are ignored when parsed.

---

## Examples

### Example 1

The simplest feed object can only point to the media it references.

`python
<feed vuid="v0" uid="f0">
    <spans>
        <span>
            <path encoding="file">Media/Video1.mov</path>
        </span>
    </spans>
</feed>
`

### Example 2

Any additional elements added override the media metadata or add metadata to the media without changing its header.

`python
<feed vuid="v0" uid="f0">
    <comment>My comment</comment>
    <spans>
        <span>
            <path encoding="file">Media/Video1.mov</path>
        </span>
    </spans>
</feed>
`

### Example 3

The feed start timecode and duration can be modified to enforce specific timing, ignoring the media's actual duration. This example creates a feed longer than the existing media. Gaps where no media exists are padded with `No Media` content.

`python
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
`

### Example 4

Here is an example with a feed having two spans of four frames and a start offset of -2.

`python
Feed indexes   [00--01--02--03--04--05--06--07--08--09--10]
Spans indexes  ########[00--01--02--03][00--01--02--03]####
python
<feed vuid="v0" uid="f0">
    <startOffset>-2</startOffset>
    <spans>
        <span>
            <path encoding="file">Media/Video1.[00-03].dpx</path>
            <path encoding="file">Media/Video2.[00-03].dpx</path>
        </span>
    </spans>
</feed>
`

### Example 5

Here is an example with a feed having two spans of four frames and a start offset of 2.

`python
Feed indexes   ########[00--01--02--03--04--05--06--07--08--09--10]
Spans indexes  [00--01--02--03][00--01--02--03]####################
python
<feed vuid="v0" uid="f0">
    <startOffset>2</startOffset>
    <spans>
        <span>
            <path encoding="file">Media/Video1.[00-03].dpx</path>
            <path encoding="file">Media/Video2.[00-03].dpx</path>
        </span>
    </spans>
</feed>
`

## Related pages

- Open Clip Reference
