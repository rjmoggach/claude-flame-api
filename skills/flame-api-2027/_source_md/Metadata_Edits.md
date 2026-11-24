<!-- source: Autodesk Flame Family 2027 Help _ Metadata Edits _ Autodesk.html -->
# Metadata Edits

The `<metadataEdits>` element lists two items: `<edits>` and `<additions>`.

The `<edits>` element is a list of `<edit>` elements to be applied to the metadata of each edit unit (usually a video frame) read from the media file.

An `<edit>` can modify a value, discard a metadata key, rename a metadata key, or apply a combination of these operations. To be applied, the metadata key must be present in the modified metadata dictionary read from the media file.

An `<add>` will be applied only if the modified metadata dictionary read from the media file does not already contain a matching key.

Discarded `<add>` or `<edit>` elements will not be included in the resulting metadata.

Metadata to be edited or added is evaluated on an edit unit (usually a video frame) basis.

When both `<edits>` and `<additions>` are present, `<edits>` are applied first and `<additions>` are applied second.

---

## Attributes

| Attribute | Data Type | Allowed Values | Occurrence | Description |
|---|---|---|---|---|
| type | string | `metadataEdits` | 0-1 | Type of the element. |

---

## Children

| Element | Data Type | Occurrence | Description |
|---|---|---|---|
| `<edits>` | edits | * | List of `<edit>` elements to be applied.<br><br>To be applied, the metadata key must be present in the modified metadata dictionary read from the media file. |
| `<additions>` | additions | * | List of `<add>` elements to be applied.<br><br>To be applied, the metadata key must not be present in the modified metadata dictionary read from the media file. |

---

## Examples

### Example 1: Complex Edit

This example shows most of the possible values and attributes.

See `<edit>` and `<add>` for more detailed examples.

`python
<metadataEdits type="metadataEdits">
    <edits>
        <edit key="ModifiedKey" type="string">NewValue</edit>
        <edit key="DiscardedKey" discarded="yes"></edit>
        <edit key="ExistingKey" renamedKey="RenamedKey"/>
        <edit key="OtherExistingKey" renamedKey="RenamedAndModifiedKey">NewValue</edit>
    </edits>
    <additions>
        <add key="AddedKey" type="string">AddedValue</add>
        <add key="DiscardedKey" discarded="yes" type="string">DiscardedValue</add>
    </additions>
</metadataEdits>
`

### Example 2: Forcing a Value

Since an `<edit>` will only be applied if the metadata element is present in the media file metadata and an `<add>` will only be applied when the metadata element is not present, both need to be used to force a specific value.

`python
<metadataEdits type="metadataEdits">
    <edits>
        <edit key="Target" type="string">ForcedValue</edit>
    </edits>
    <additions>
        <add key="Target" type="string">ForcedValue</add>
    </additions>
</metadataEdits>
`

### Example 3: Replacing a Value While Keeping the Original

The following example shows how to replace an existing metadata key while keeping track of its original value, if any. This can be used to track modified values.

`python
<metadataEdits type="metadataEdits">
    <edits>
        <edit key="Target" renamedKey="original/Target"></edit>
    </edits>
    <additions>
        <add key="Target" type="string">ForcedValue</add>
    </additions>
</metadataEdits>
`

## Related pages

- Open Clip Reference
