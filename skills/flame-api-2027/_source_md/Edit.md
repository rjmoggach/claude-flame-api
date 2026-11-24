<!-- source: Autodesk Flame Family 2027 Help _ Edit _ Autodesk.html -->
# Edit

An `<edit>` can modify a value, discard a metadata key, rename a metadata key, or apply a combination of these operations. To be applied, the metadata key must be present in the modified metadata dictionary read from the media file.

Discarded `<edit>` elements will not be included in the resulting metadata.

All edit units (frames) within a given feed share the same metadata edit and are evaluated on an edit unit (each frame) basis.

---

## Attributes

| Attribute | Data Type | Allowed Values | Occurrence | Description |
|---|---|---|---|---|
| key | string | any | 1 | Key used to identify the metadata element. |
| type | string | Value Data Type | 0-1 | Type of the element.<br><br>String is assumed if not specified. |
| discarded | boolean | True, False, Yes, No, 1, 0 | 0-1 | Discarded elements are not applied to resulting metadata. |
| renamedKey | string | any | 0-1 | If defined, the resulting metadata will have the renamed metadata key instead of the original key. |

---

## Children

Children of an `edit` element are variants of the type `value`.

---

## Examples

### Example 1: Modify a Value

This will modify the value of the `ModifiedKey` metadata element only if the key is present in the media file metadata. If the key is not present, no changes will be applied.

`python
<edit key="ModifiedKey" type="string">NewValue</edit>
`

### Example 2: Remove a key and its Value

This example demonstrates how to remove a metadata key from the metadata read from a media file. The type and value are not relevant for discarded elements.

`python
<edit key="DiscardedKey" discarded="yes"/>
`

### Example 3: Rename a Key

This will rename the `ExistingKey` metadata element to `RenamedKey`. If the metadata key is not present, no changes will be applied. The value of `ExistingKey` remains unchanged.

`python
<edit key="ExistingKey" renamedKey="RenamedKey"/>
`

### Example 4: Rename a key and Modify its Value

This will rename the `ExistingKey` metadata element to `RenamedKey`. If the metadata key is not present, no changes will be applied. The value of `ExistingKey` is replaced with `NewValue`.

`python
<edit key="ExistingKey" renamedKey="RenamedKey">NewValue</edit>
`

## Related pages

- Open Clip Reference
