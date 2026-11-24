<!-- source: Autodesk Flame Family 2027 Help _ Paths _ Autodesk.html -->
# Paths

The `<paths>` element is a map of `<path>` elements, each representing a different view on the same material, in multiple files.

The most common use case is stereo video, which includes media for both right and left polarities.

Each `<path>` child represents media that is uniform in all aspects, such as timing, duration, rate, format, and codec.

This is different from the `<tracks>` element, which shows different representations of the same event (layers or passes) that can vary in any aspect.

---

## Attributes

| Attribute | Data Type | Allowed Values | Occurrence | Description |
|---|---|---|---|---|
| type | string | `paths` | 0-1 | Type of the element. |
| version | unsigned integer | `8` | 0-1 | Version of the XML element. |

 Note: Optional attributes (0 occurrence attributes) will be inferred from the parent node.

---

## Children

| Element | Data Type | Occurrence | Description |
|---|---|---|---|
| `<path>` | path | * | Each path contained in the list of paths.<br><br>Each `<path>` element needs a unique `subFeedId` attribute, which identifies the specific sub-feed (for example, "Left" for the left eye or "Right" for the right eye in stereo video). |

---

## Examples

### Example 1

This example demonstrates the use of the `subFeedId` attribute to represent two eyes of a stereo video media feed.

`python
<paths>
    <path subFeedId="Left" encoding="pattern">MEDIA/left-eye.[0001-0005].tif</path>
    <path subFeedId="Right" encoding="pattern">MEDIA/right-eye.[0001-0005].tif</path>
</paths>
`

## Related pages

- Open Clip Reference
