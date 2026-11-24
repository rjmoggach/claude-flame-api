<!-- source: Autodesk Flame Family 2027 Help _ Time _ Autodesk.html -->
# Time

A `<time>` element is a number of samples (such as images or audio samples) combined with a `<rate>` element.

---

## Attributes

| Attribute | Data Type | Allowed Values | Occurrence | Description |
|---|---|---|---|---|
| type | string | `time` | 0-1 | Type of the element. |
| version | unsigned integer | `8` | 0-1 | Version of the XML element. |

 Note: Optional attributes (0 occurrence attributes) will be inferred from the parent node.

---

## Children

| Element | Data Type | Occurrence | Description |
|---|---|---|---|
| `<rate>` | rate | 0-1 | Rate element.<br><br>If no rate is specified, the time is frame/sample based or inferred from the parent node. |
| `<nbTicks>` | 64-bit unsigned integer | 1 | The `nbTicks` element is the number of samples that make up the media.<br><br>For frame-based media, this is a number of frames (or images).<br><br>This number divided by the value of the `<rate>` element expresses a number of seconds. |
| `<dropMode>` | string | 0-1 | The drop frame mode of the media.<br><br>Only required for those timings with a possible drop-frame mode.<br><br>Allowed values for `<dropMode>`:<br><br> • DF: drop-frame media • NDF: non drop-frame media |

---

## Examples

### Example 1

Here is an example of a complete time construct of 30 frames at 23.976 frames per second.

`python
<time type="time">
    <rate type="rate">
        <numerator>24000</numerator>
        <denominator>1001</denominator>
    </rate>
    <nbTicks>30</nbTicks>
    <dropMode>DF</dropMode>
</time>
`

### Example 2

Here is an example of a time duration of a frame-based media without a specified frame rate. This would be, for example, a frame sequence of 30 JPEGs without context.

`python
<time type="time">
    <nbTicks>30</nbTicks>
</time>
`

### Example 3

Here is a simplified example of a duration of 1 second at 30 frames per second.

`python
<time type="time">
    <rate>30</rate>
    <nbTicks>30</nbTicks>
</time>
`

## Related pages

- Open Clip Reference
