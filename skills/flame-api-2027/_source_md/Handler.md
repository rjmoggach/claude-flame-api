<!-- source: Autodesk Flame Family 2027 Help _ Handler _ Autodesk.html -->
# Handler

The handler is an object responsible for reading the media and metadata files. The handler has options that control the way the media is structured, read and interpreted.

Handlers come in two main forms: clip and feed handlers.

- For simple or homogeneous clips, all handlers in the whole clip structure are identical.
- For complex or heterogeneous clips, the clip handler and all individual feed handlers can differ.

The clip handler is responsible for the clip metadata and the track organization. The feed handler is responsible for I/O operations.

---

## Attributes

| Attribute | Data Type | Allowed Values | Occurrence | Description |
|---|---|---|---|---|
| type | string | `handler` | 0-1 | Type of the element. |
| version | unsigned integer | `8` | 0-1 | Version of the XML element. |

 Note: Optional attributes (0 occurrence attributes) will be inferred from the parent node.

---

## Children

| Element | Data Type | Occurrence | Description |
|---|---|---|---|
| `<name>` | string | 0-1 | Name of the handler. |
| `<version>` | unsigned integer | 0-1 | Version of the handler. |
| `<longName>` | string | 0-1 | Display name of the handler.<br><br>To be used in UI. |
| `<options>` | dict | 0-1 | Dictionary containing options for metadata and I/O operations.<br><br>These options are handler specific. |
| `<conversionOptions>` | dict | 0-1 | Dictionary containing options for image conversion pipeline. |

---

## Open Clip Handler Options

### ScanPattern

The Open Clip handler can be used to dynamically populate the Open Clip based on the file system content.

The option `ScanPattern` can specify a browsing pattern to apply to construct the clip.

| Token | Description |
|---|---|
| `{name}` | Name of the resulting clip<br><br>If the Open Clip defines the name in the XML, it must match.<br><br>If the Open clip does not define the name, it will be inferred from files on disk.<br><br>If no match is found or the name cannot be inferred, the clip may not be constructed correctly. |
| `{frame}` | Represents a numerical frame sequence.<br><br>The sequence is treated as infinite, meaning no gap detection will be performed.<br><br>Padding will be inferred from files on disk. |
| `{extension}` | File extension<br><br>Used to build clip with heterogeneous media types. |
| `{version}` | Version<br><br>Will build a multi-version clip when used.<br><br>Numerical only if adjacent to another token. |
| `{track}` | Track<br><br>Will build a multi-track clip when used. |
| `{polarity}` | Polarity<br><br>Will build a multi-feed track when used.<br><br>Used to define Left/Right feed for stereo video media. |

---

## Example

### Example 1

This is a complete handler structure as filled by the Wiretap Gateway.

`python
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
`

### Example 2

This is an example of building an Open Clip using a scan pattern.

`python
<handler>
    <name>MIO Clip</name>
    <options>
        <ScanPattern>Media/Video_v{version}.{frame}.dpx</ScanPattern>
    </options>
</handler>
`

Assuming the following files exist:

`python
Media/Video_v0.001.dpx
Media/Video_v0.002.dpx
Media/Video_v0.003.dpx
Media/Video_v0.004.dpx
Media/Video_v1.001.dpx
Media/Video_v1.002.dpx
Media/Video_v1.003.dpx
Media/Video_v1.004.dpx
`

This would be equivalent to building the following Open Clip, assuming the media exists:

`python
<clip type="clip" version="9">
    <tracks>
        <track uid="t0">
            <trackType>video</trackType>
            <feeds>
                <feed vuid="v0" uid="f0">
                    <spans>
                        <span>
                            <path encoding="file">Media/Video_v0.[001-0004].dpx</path>
                        </span>
                    </spans>
                </feed>
                <feed vuid="v1" uid="f1">
                    <spans>
                        <span>
                            <path encoding="file">Media/Video_v1.[001-0004].dpx</path>
                        </span>
                    </spans>
                </feed>
            </feeds>
        </track>
    </tracks>
</clip>
`

When adding the following files:

`python
Media/Video_v2.001.dpx
Media/Video_v2.002.dpx
`

This would be the result, after a refresh to the following Open Clip:

`python
<clip type="clip" version="9">
    <tracks>
        <track uid="t0">
            <trackType>video</trackType>
            <feeds>
                <feed vuid="v0" uid="f0">
                    <spans>
                        <span>
                            <path encoding="file">Media/Video_v0.[001-0004].dpx</path>
                        </span>
                    </spans>
                </feed>
                <feed vuid="v1" uid="f1">
                    <spans>
                        <span>
                            <path encoding="file">Media/Video_v1.[001-0004].dpx</path>
                        </span>
                    </spans>
                </feed>
                <feed vuid="v2" uid="f2">
                    <spans>
                        <span>
                            <path encoding="file">Media/Video_v2.[001-0002].dpx</path>
                        </span>
                    </spans>
                </feed>
            </feeds>
        </track>
    </tracks>
</clip>
`

### Example 3

This is a more complex example of building an Open Clip using a scan pattern that builds a multi-channel/multi-version that could support heterogeneous media type.

`python
<handler>
    <name>MIO Clip</name>
    <options>
        <ScanPattern>Media/Video_t{track}_v{version}.{frame}.{extension}</ScanPattern>
    </options>
</handler>
`

## Related pages

- Open Clip Reference
