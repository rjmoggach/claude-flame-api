<!-- source: Autodesk Flame Family 2027 Help _ Tracks _ Autodesk.html -->
# Tracks

The container for all the `<track>` elements making up an Open Clip.

---

## Attributes

| Attribute | Data Type | Allowed Values | Occurrence | Description |
|---|---|---|---|---|
| type | string | `tracks` | 0-1 | Type of the element. |
| version | unsigned integer | `8` | 0-1 | Version of the XML element. |

 Note: Optional attributes (0 occurrence attributes) will be inferred from the parent node.

---

## Children

| Element | Data Type | Occurrence | Description |
|---|---|---|---|
| `<track>` | track | * | Each track contained in the list of tracks. |

---

## Examples

### Example 1

This is the simplest form the `tracks` object can take. A single track pointing to a media file.

`python
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
`

### Example 2

This example illustrates a single multi-channel OpenEXR file, a structure that expresses the different channels of the OpenEXR.

`python
<tracks type="tracks">
    <track uid="BEAUTY:MasterBeauty">
        <trackType>video</trackType>
        <feeds>
            <feed vuid="v0" uid="v0">
                <spans>
                    <span>
                        <path encoding="pattern">Media/RGB_2Mattes.exr</path>
                    </span>
                </spans>
            </feed>
        </feeds>
    </track>
    <track uid="Matte1">
        <trackType>video</trackType>
        <feeds>
            <feed vuid="v0" uid="v0">
                <spans>
                    <span>
                        <path encoding="pattern">Media/RGB_2Mattes.exr</path>
                    </span>
                </spans>
            </feed>
        </feeds>
    </track>
    <track uid="Matte2">
        <trackType>video</trackType>
        <feeds>
            <feed vuid="v0" uid="v0">
                <spans>
                    <span>
                        <path encoding="pattern">Media/RGB_2Mattes.exr</path>
                    </span>
                </spans>
            </feed>
        </feeds>
    </track>
</tracks>
`

## Related pages

- Open Clip Reference
