<!-- source: Autodesk Flame Family 2027 Help _ Rate _ Autodesk.html -->
# Rate

Use numerator/denominator elements to express a rate rather than using decimals; this increases the accuracy of arithmetic operations.

This type is similar to rational but is meant to be used in the context of a rate. When passed a decimal number close to a known fractional rate, the fractional rate will be used instead. This means that passing 23.98 will automatically convert to the more precise and standard 24000/1001.

---

## Attributes

| Attribute | Data Type | Allowed Values | Occurrence | Description |
|---|---|---|---|---|
| type | string | `rate` | 0-1 | Type of the element. |
| version | unsigned integer | `8` | 0-1 | Version of the XML element. |

 Note: Optional attributes (0 occurrence attributes) will be inferred from the parent node.

---

## Children

The rate can be in either of these two mutually exclusive formats:

### Rational Format

| Element | Data Type | Occurrence | Description |
|---|---|---|---|
| `<numerator>` | 64-bit integer | 1 | Upper portion of a rational number representing a rate. |
| `<denominator>` | unsigned integer | 1 | Lower portion of a rational number representing a rate. |

### Decimal Format

| Element | Data Type | Occurrence | Description |
|---|---|---|---|
| #cdata | float | 1 | Decimal number representing a rate. |

---

## Examples

### Example 1

The following expresses a frame rate of 23.976 fps.

`python
<rate type="rate">
    <numerator>24000</numerator>
    <denominator>1001</denominator>
</rate>
`

### Example 2

Alternatively, a floating-point number can still be used for simplicity.

`python
<rate type="rate">23.976</rate>
`

## Related pages

- Open Clip Reference
