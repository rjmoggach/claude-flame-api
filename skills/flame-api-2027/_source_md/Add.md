<!-- source: Autodesk Flame Family 2027 Help _ Add _ Autodesk.html -->
# Add

An `<add>` element is used to insert a new metadata value into the metadata extracted from a media file. The addition is applied only if the specified metadata key does not already exist in the current metadata dictionary.

Discarded `<add>` elements will not be included in the resulting metadata.

Metadata to be added is evaluated on an edit unit (that is, frame) basis.

---

## Attributes

| Attribute | Data Type | Allowed Values | Occurrence | Description |
|---|---|---|---|---|
| key | string | any | 1 | Metadata key used to identify the metadata element. |
| type | string | Value Data Type | 0-1 | Type of the element.<br><br>String is assumed if not specified. |
| discarded | boolean | True, False, Yes, No, 1, 0 | 0-1 | Discarded elements are not applied to resulting metadata. |

---

## Children

Children of an `add` element are variants of the type `value`.

---

## Examples

### Example 1: Add a Metadata Value

In this example, the metadata value will be associated with the metadata key 'Key', provided the original media metadata does not already contain a 'Key' metadata entry in its header.

`python
<add key="Key" type="string">value</add>
`

### Example 2: Discard a Metadata Addition

In this example, the metadata key will not be applied to the resulting metadata. This can be used to temporarily disable metadata additions while keeping track of the original values.

`python
<add key="Key" discarded="yes" type="string">value</add>
`

## Related pages

- Open Clip Reference
