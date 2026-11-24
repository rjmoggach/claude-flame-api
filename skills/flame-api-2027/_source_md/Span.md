<!-- source: Autodesk Flame Family 2027 Help _ Span _ Autodesk.html -->
# Span

The `<span>` element contains media that make up all or parts of the `<feed>`. A `<span>` element describes its duration and the path to the physical media files. A `<feed>` made up of multiple `<span>` elements means that multiple media files/sequences make up that one `<feed>`. The order in which each `<span>` element is listed is the order in which they are read to rebuild the sequence.

All media referenced in a `<span>` must have homogeneous properties (same codec, compression, format, length, rate...). To mix types of media in a `<clip>`, use different `<track>` elements.

A `<span>` with a `<duration>` but no `<path>` is a gap.

---

## Attributes

| Attribute | Data Type | Allowed Values | Occurrence | Description |
|---|---|---|---|---|
| type | string | `span` | 0-1 | Type of the element. |
| version | unsigned integer | `8` | 0-1 | Version of the XML element. |

 Note: Optional attributes (0 occurrence attributes) will be inferred from the parent node.

---

## Children

| Element | Data Type | Occurrence | Description |
|---|---|---|---|
| `<duration>` | time | 0-1 | Time duration of the span.<br><br>If not defined, duration from the media will be used. |
| `<trackIndex>` | unsigned integer | 0-1 | Track index in the media file track.<br><br>Used to read specific track/channel of multi-track/multi-channel media in different span objects. |
| `<path>` | path | 0-1 | Path pointing the actual media files.<br><br>Cannot be used with `<paths>`. |
| `<paths>` | paths | 0-1 | Path map pointing the actual media files.<br><br>Used to represent the stereo video media.<br><br>Cannot be used with `<path>`. |
| `<userData>` | dict | 0-1 | Dictionary of metadata that is passed through without interpretation. |

---

## Examples

### Example 1

The simplest span object can only point to the media it references.

`python
<span>
    <path encoding="file">Media/Video1.mov</path>
</span>
`

### Example 2

In this example, the file's actual duration would be overridden by the span information.

`python
<span>
    <duration type="time">
        <nbTicks>48</nbTicks>
        <rate type="rate">24</rate>
    </duration>
    <path encoding="file">Media/Video1.mov</path>
</span>
`

### Example 3

This is an example of a span representing a gap of two seconds.

`python
<span>
    <duration type="time">
        <nbTicks>48</nbTicks>
        <rate type="rate">24</rate>
    </duration>
</span>
`

### Example 4

This is an example of a span using the second track, also known as a layer, of a multi-channel OpenEXR.

`python
<span>
    <trackIndex>1</trackIndex>
    <path encoding="pattern">ABGR.[00001001-00001004].exr</path>
</span>
`

### Example 5

This is an example of a span representing stereo video media.

`python
<span>
    <paths>
      <path subFeedId="right" encoding="pattern">right.[00001001-00001004].exr</path>
      <path subFeedId="left" encoding="pattern">left.[00001001-00001004].exr</path>
    </paths>
</span>
`

## Related pages

- Open Clip Reference
