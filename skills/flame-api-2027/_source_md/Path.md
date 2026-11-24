<!-- source: Autodesk Flame Family 2027 Help _ Path _ Autodesk.html -->
# Path

The `<path>` element is the path to the media.

The path can be absolute or relative to the Open Clip file.

A path can be represented as a regular file or as a pattern.

A pattern can be a base name with a ranged frame suffix, a path with tokens, or a combination of both.

---

## Attributes

| Attribute | Data Type | Allowed Values | Occurrence | Description |
|---|---|---|---|---|
| type | string | `path` | 0-1 | Type of the element. |
| version | unsigned integer | `8` | 0-1 | Version of the XML element. |
| encoding | string | `file` or `pattern` | 0-1 | Encoding of the path.<br><br>`file` reads the path as is.<br><br>`pattern` interprets the brackets. |

 Note: Optional attributes (0 occurrence attributes) will be inferred from the parent node.

---

## Children

| Element | Data Type | Occurrence | Description |
|---|---|---|---|
| #cdata | string | 1 | File or pattern |

---

## Examples

### Example 1

The simplest form of a path element is an absolute path. For example, this could be the path to a QuickTime movie file.

`python
<path encoding="file">/dir/file.mov</path>
`

### Example 2

The path can also be a relative path. With the following path, assuming the Open Clip is located in `/dir/MyClip.clip`, the QuickTime file reference would be `/dir/subdir/file.movpython
<path encoding="file">subDir/file.mov</path>
`

### Example 3

The path can reference a file sequence.

`python
<path encoding="pattern">/dir/file_[1-5].dpx</path>
`

### Example 4

The path can reference a file sequence padded with zeros.

`python
<path encoding="pattern">/dir/file_[0001-0005].dpx</path>
`

### Example 5

The padding can be smaller than the largest file in the sequence.

`python
<path encoding="pattern">/dir/file_[099-10005].dpx</path>
`

### Example 6

The `{frame}` token can be used instead of a frame range to support an unbounded file sequence.

`python
<path encoding="pattern">/dir/file_{frame}.dpx</path>
`

The resulting sequence will be of length matching the range of the smallest to the largest file. Gaps in the sequence are ignored when using the `{frame}` token.

| Files | Equivalent range |
|---|---|
| `/dir/files_3.dpx`<br><br>`/dir/files_4.dpx`<br><br>`/dir/files_5.dpx` | `/dir/files_[3-4].dpx` |
| `/dir/files_3.dpx`<br><br>`/dir/files_99.dpx`<br><br>`/dir/files_105.dpx` | `/dir/files_[3-105].dpx` |

### Example 7

Using the `encoding="file"` on a pattern allows reading files that would otherwise conflict.

To read the file `/dir/file_{frame}.dpxpython
<path encoding="file">/dir/file_{frame}.dpx</path>
`

To read the file `/dir/file_[12].dpxpython
<path encoding="file">/dir/file_[12].dpx</path>
`

## Related pages

- Open Clip Reference
