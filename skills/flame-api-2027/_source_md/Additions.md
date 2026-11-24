<!-- source: Autodesk Flame Family 2027 Help _ Additions _ Autodesk.html -->
# Additions

The `<additions>` element is a list of `<add>` elements to be applied to the metadata read from the media file.

The `<additions>` element is contained in a `<metadataEdits>` element.

An `<add>` will be applied only if the modified metadata dictionary read from the media file does not already contain a matching key.

Discarded `<add>` elements will not be included in the resulting metadata.

All edit units (frames) within a given feed share the same metadata additions and are evaluated on an edit unit (each frame) basis.

---

## Children

| Element | Data Type | Occurrence | Description |
|---|---|---|---|
| `<add>` | `<add>` | * | Metadata addition to be applied to a modified metadata dictionary read from the media file. |

---

## Examples

`python
<additions>
    <add key="AddedKey" type="string">AddedValue</add>
    <add key="DiscardedKey" discarded="yes" type="string">DiscardedValue</add>
</additions>
`

See `<add>` for more detailed examples.

## Related pages

- Open Clip Reference
