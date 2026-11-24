<!-- source: Autodesk Flame Family 2027 Help _ Version _ Autodesk.html -->
# Version

The `<version>` element contains metadata about a clip version. Which version the metadata applies to is defined by the `uid` attribute. This element will usually be contained in a `<versions>` element.

---

## Attributes

| Attribute | Data Type | Allowed Values | Occurrence | Description |
|---|---|---|---|---|
| type | string | `version` | 0-1 | Type of the element. |
| version | unsigned integer | `8` | 0-1 | Version of the XML element. |
| uid | string | any | 1 | Defines which `<feed>` of each `<track>` to use, based on matching `vuid`.<br><br>Each `uid` must be unique across version elements. |

 Note: Optional attributes (0 occurrence attributes) will be inferred from the parent node.

---

## Children

| Element | Data Type | Occurrence | Description |
|---|---|---|---|
| `<name>` | string | 0-1 | Name of the version. |
| `<comment>` | string | 0-1 | Unparsed text converted into a clip note. |
| `<creationDate>` | string | 0-1 | Unparsed text used to store the creation date of the version. |
| `<userData>` | dict | 0-1 | Dictionary of metadata that is passed through without interpretation. |

 Note: Children elements with the attribute `computed=1` will be ignored when parsed.

---

## Examples

### Example 1

This is the simplest version possible. It does not carry any information other than a version UID, which is used to index feeds in a track list.

`python
<version uid="v0"/>
`

### Example 2

Metadata elements can be added. The following shows a complete form of the element.

`python
<version uid="v0">
    <name>First version</name>
    <comment>Roto done by John</comment>
    <creationDate>January 12, 2025</creationDate>
    <userData>
        <assetId type="string">11231-2312323</assetId>
    </userData>
</version>
`

## Related pages

- Open Clip Reference
