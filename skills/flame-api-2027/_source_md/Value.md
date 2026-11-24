<!-- source: Autodesk Flame Family 2027 Help _ Value _ Autodesk.html -->
# Value

A `value` is a user-defined variant element that can be used to represent a wide array of data types. Values are used in `<dict>`, `<edit>`, and `<add>` as child elements.

---

## Attributes

| Attribute | Data Type | Allowed Values | Occurrence | Description |
|---|---|---|---|---|
| type | string | Value Data Type | 0-1 | Type of the element.<br><br>String is assumed if not specified. |
| label | string | any | 0-1 | Display label for complex types.<br><br>Value is converted to string if possible when not specified.<br><br>Not supported in `<edit>` and `<add>` elements. |

---

## Children

No child elements are defined for a `value` element since its data structure is undefined; each child element created by the client must define its data type using the `type` attribute. The allowed data types are listed below.

| Children Data Type | Type Description |
|---|---|
| int | integer |
| uint | unsigned integer |
| int8 | 8-bit integer |
| uint8 | 8-bit unsigned integer |
| int16 | 16-bit integer |
| uint16 | 16-bit unsigned integer |
| int32 | 32-bit integer |
| uint32 | 32-bit unsigned integer |
| int64 | 64-bit integer |
| uint64 | 64-bit unsigned integer |
| float | single precision floating point number |
| double | double precision floating point number |
| bool | boolean (True, False, Yes, No, 1, 0) |
| string | string |
| binary | escaped string to allow XML encoding (displayable/non null) |
| bytes | escaped string to allow XML encoding (not displayable/may contain null) |
| rate | rate |
| rational | rational |
| time | time |
| uid | string |
| keycode | space-separated keycode |
| dict | dict |

---

## Examples

### Example 1

This is the simplest form a value can take. A string type will be assumed if nothing is specified.

`python
<value>Str</value>
`

### Example 2

Type can be specified to avoid ambiguity on how to interpret the data. In this example, each value has the same serialization but represents a different data type.

`python
<value1 type="string">12341</value1>
<value2 type="int">12341</value2>
<value3 type="float">12341</value3>
`

### Example 3

When the data stored has little meaning for the end user, a string label can be added to be used in the user interface instead.

`python
<mode type="int16" label="Full Res / No Proxy">0x12341</mode>
`

### Example 4

Some types can be more complex than a single string. For example, rate can be expressed in rational format to avoid rounding errors caused by serializing/deserializing a float as a string.

`python
<sampleRate type="rate">
    <numerator>24</numerator>
    <denominator>1001</denominator>
</sampleRate>
`

## Related pages

- Open Clip Reference
