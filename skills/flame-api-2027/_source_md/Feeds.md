<!-- source: Autodesk Flame Family 2027 Help _ Feeds _ Autodesk.html -->
# Feeds

The container for all the `<feed>` elements making up a `<track>`.

With the `currentVersion` attribute, `<feeds>` defines the `<feed>` to use. In an Open Clip, each `<feed>` is a version of the media.

---

## Attributes

| Attribute | Data Type | Allowed Values | Occurrence | Description |
|---|---|---|---|---|
| type | string | `feeds` | 0-1 | Type of the element. |
| version | unsigned integer | `7` | 0-1 | Version of the XML element. |
| currentVersion | string | any | 0-1 | Defines which `<feed>` to use as the current, based on matching `vuid` on each `<feed>` child.<br><br>If not defined, the current version of the `<versions>` of the `<clip>` is used. |

 Note: Optional attributes (0 occurrence attributes) will be inferred from the parent node.

Remarks: Take care with the `currentVersion` attribute. It is found in both `<feeds>` and `<versions>`. It should be kept in sync to have a properly formatted Open Clip. Its function is to flag a preferred version. In Flame, it indicates the version to display in the MediaHub. If the value is not one of the `vuid`, Flame generates a `No Media` feed for the current feed.

---

## Children

| Element | Data Type | Occurrence | Description |
|---|---|---|---|
| `<feed>` | feed | * | Each feed contained in the list of feeds. |

---

## Examples

### Example 1

This example demonstrates the simplest `<feeds>` object, which references a single media file.

`python
<feeds>
    <feed vuid="v0" uid="f0">
        <spans>
            <span>
                <path encoding="file">Media/Video1.mov</path>
            </span>
        </spans>
    </feed>
</feeds>
`

### Example 2

Here is an example with multiple versions, where each `<feed>` represents a different version of the media. The `currentVersion` attribute specifies which version is active and should be used by the client application. If the `currentVersion` attribute is not defined, the last `<feed>` in the list is assumed to be the active version.

`python
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
`

## Related pages

- Open Clip Reference
