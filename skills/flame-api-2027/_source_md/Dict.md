<!-- source: Autodesk Flame Family 2027 Help _ Dict _ Autodesk.html -->
# Dict

A dictionary is a key-value container of arbitrary key-value pairs with heterogeneous types.

---

## Attributes

| Attribute | Data Type | Allowed Values | Occurrence | Description |
|---|---|---|---|---|
| type | string | `dict` | 0-1 | Type of the element. |
| version | unsigned integer | `8` | 0-1 | Version of the XML element. |

 Note: Optional attributes (0 occurrence attributes) will be inferred from the parent node.

---

## Children

Children of a `dict` element are variants of the type `value`.

---

## Examples

### Example 1: Simple Example

`python
<userData type="dict">
    <appName type="string">Flame</appName>
    <appVersion type="int16">2017</appVersion>
    <mode type="int16" label="Full Res / No Proxy">0x12341</mode>
</userData>
`

### Example 2: Example with Nested Complex Types

`python
<userData type="dict">
    <options type="dict">
        <disable type="bool">True</disable>
        <sampleRate type="rate">
            <numerator>24</numerator>
            <denominator>1001</denominator>
        </sampleRate>
        <speed type="int8">23</speed>
    </options>
</userData>
`

## Related pages

- Open Clip Reference
