<!-- source: Autodesk Flame Family 2027 Help _ Rational _ Autodesk.html -->
# Rational

Use numerator/denominator elements to express a fraction rather than using decimals; this increases the accuracy of arithmetic operations.

This type is similar to rate, but it is meant to be used in a general context.

---

## Attributes

| Attribute | Data Type | Allowed Values | Occurrence | Description |
|---|---|---|---|---|
| type | string | `rational` | 0-1 | Type of the element. |
| version | unsigned integer | `8` | 0-1 | Version of the XML element. |

 Note: Optional attributes (0 occurrence attributes) will be inferred from the parent node.

---

## Children

The rational can be in either of these two mutually exclusive formats:

### Rational Format

| Element | Data Type | Occurrence | Description |
|---|---|---|---|
| `<numerator>` | 64-bit integer | 1 | Upper portion of a rational number representing a fraction. |
| `<denominator>` | unsigned integer | 1 | Lower portion of a rational number representing a fraction. |

### Decimal Format

| Element | Data Type | Occurrence | Description |
|---|---|---|---|
| #cdata | 64-bit integer | 1 | Number representing the numerator of a fraction.<br><br>1 is assumed for the denominator. |

---

## Examples

### Example 1

The following expresses a ratio of 16:9:

`python
<rational type="rational">
    <numerator>16</numerator>
    <denominator>9</denominator>
</rational>
`

### Example 2

Alternatively, an integer number can still be used for simplicity:

`python
<rational type="rational">5</rational>
`

## Related pages

- Open Clip Reference
