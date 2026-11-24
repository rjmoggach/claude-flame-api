<!-- source: Autodesk Flame Family 2027 Help _ Track _ Autodesk.html -->
# Track

The `<track>` element contains the information that constitutes a track in an Open Clip. Each track represents a distinct element from the clip.

Examples of tracks in an Open Clip context include:

- A layer in a Photoshop file
- A video, or one of multiple audio tracks, in a QuickTime file
- One of multiple render passes contained in a multi-channel OpenEXR file

---

## Attributes

| Attribute | Data Type | Allowed Values | Occurrence | Description |
|---|---|---|---|---|
| type | string | `track` | 0-1 | Type of the element. |
| version | unsigned integer | `7` | 0-1 | Version of the XML element. |
| uid | string | any | 1 | Each `uid` must be unique across track elements when contained in a `<tracks>` element. |
| currentVersion | string | any | 0-1 | Version UID of the current version.<br><br>Synchronised with the one in `<versions>` XML element if missing. |

 Note: Optional attributes (0 occurrence attributes) will be inferred from the parent node.

---

## Children

| Element | Data Type | Occurrence | Description |
|---|---|---|---|
| `<trackType>` | string | 1 | Track's type.<br><br>Typically `video`, `audio`, or `generic`. |
| `<extendedType>` | string | 0-1 | Extended track's type.<br><br>The extended track type refines the type of a given track. For example, for video, it could describe the layer pass (shadow, occlusion, normal, etc.). Inferred from the parent node if missing. |
| `<feeds>` | feeds | 0-1 | Each feed contained in the list of feeds.<br><br>Each feed is associated with a version in the clip `<versions>` element. |
| `<handler>` | handler | 0-1 | Track's handler information. |
| `<name>` | string | 0-1 | Name of the track. |
| `<sourceName>` | string | 0-1 | Source name of the track.<br><br>Sometimes referred to as tape name in older workflows. |
| `<comment>` | string | 0-1 | Unparsed text converted into a clip note. |
| `<editRate>` | rate | 0-1 | Edit rate of the track.<br><br>An edit rate can be defined when all feeds' sample rates do not match in order to explicitly define the working rate for the ensemble.<br><br>If not defined, a common rate based on the feeds' sample rates is computed. |
| `<dropMode>` | string | 0-1 | The drop frame mode of the media.<br><br>Only required for those timings with a possible drop-frame mode.<br><br>Allowed values for `<dropMode>`:<br><br> • DF: drop-frame media • NDF: non drop-frame media |
| `<duration>` | time | 0-1 | Time duration of the track.<br><br>If not defined, the union of all the feeds' duration is computed. |
| `<startTimecode>` | time | 0-1 | Start timecode of the track.<br><br>If not defined, the earliest start timecode of all the feeds is used. |
| `<userData>` | dict | 0-1 | Dictionary of metadata that is passed through without interpretation. |

 Note: Children elements with the attribute `computed=1` are ignored when parsed.

---

## Examples

### Example 1

The simplest track object can only point to media it references.

`python
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
`

### Example 2

Any additional elements added override the media metadata or add metadata to media without changing the media header.

`python
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
`

### Example 3

Track start timecode and duration can be modified to force a specific timing, ignoring the media's actual duration. This example demonstrates how to create a track with a duration longer than the existing media. Gaps where no media exist are padded with `No Media` content.

`python
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
`

## Related pages

- Open Clip Reference
