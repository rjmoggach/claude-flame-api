<!-- source: Autodesk Flame Family 2027 Help _ Spans _ Autodesk.html -->
# Spans

The `<spans>` element contains all the `<span>` elements that make up the `<feed>`.

---

## Attributes

| Attribute | Data Type | Allowed Values | Occurrence | Description |
|---|---|---|---|---|
| type | string | `spans` | 0-1 | Type of the element. |
| version | unsigned integer | `8` | 0-1 | Version of the XML element. |

 Note: Optional attributes (0 occurrence attributes) will be inferred from the parent node.

---

## Children

| Element | Data Type | Occurrence | Description |
|---|---|---|---|
| `<span>` | span | * | Each span contained in the list of spans. |

---

## Examples

### Example 1

This is the simple form the `spans` object can take: a single span pointing to a media file.

`python
<spans>
    <span>
        <path encoding="file">Media/Video1.mov</path>
    </span>
</spans>
`

### Example 2

This example illustrates how spanned clips can be joined together to represent a single stream of frames. In practical terms, this means that the individual media files are treated as contiguous segments of a larger video sequence, allowing seamless playback or editing as if they were a single continuous file. This is common in files created by cameras that have a size limit on the files they create.

`python
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
`

## Related pages

- Open Clip Reference
