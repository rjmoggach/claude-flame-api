<!-- source: Autodesk Flame Family 2027 Help _ Edits _ Autodesk.html -->
# Edits

The `<edits>` element is a list of `<edit>` elements to be applied to the metadata of each edit unit (each frame) read from the media file.

The `<edits>` element is contained in a `<metadataEdits>` element.

An `<edit>` can modify a value, discard a key, rename a key, or apply a combination of these operations. To be applied, the key must be present in the modified metadata dictionary read from the media file.

Discarded `<edit>` elements will not be included in the resulting metadata.

All edit units (frames) within a given feed share the same metadata edits and are evaluated on an edit unit (each frame) basis.

---

## Children

| Element | Data Type | Occurrence | Description |
|---|---|---|---|
| `<edit>` | `<edit>` | * | Metadata edit to be applied to a modified metadata dictionary read from the media file. |

---

## Example

`python
<edits>
    <edit key="ModifiedKey" type="string">NewValue</edit>
    <edit key="DiscardedKey" discarded="yes"></edit>
    <edit key="ExistingKey" renamedKey="RenamedKey">NewValue</edit>
</edits>
`

See `<edit>` for more detailed examples.

## Related pages

- Open Clip Reference
