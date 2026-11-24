<!-- source: Autodesk Flame Family 2027 Help _ Open Clip Reference _ Autodesk.html -->
# Open Clip Reference

The Open Clip is an XML-structured file containing the following information:

- Physical location of files
- Metadata information, such as timecode
- Structural information, such as tracks
- Clip versions

The Open Clip is **not** a compositional timeline with edits or effects.

The Open Clip is similar to a P2 clip: it is a wrapper for media files (or essence) and the layout of these media files on disk.

---

## Version

This documentation only covers Open Clip version 7. Some of the documented tags and attributes will not apply to older versions. Although some support exists for versions prior to 4, it is encouraged to use the latest format when writing new Open Clips.

### Version History

| Version | Description | Application Support |
|---|---|---|
| 4 | First documented version | 2011 |
| 5 | Nested dictionary support | 2017.1 |
| 6 | Added support for conditions | 2019 |
| 6 | Added support for start frame | 2024 |
| 7 | Format now has distinct metadata and resolved colour spaces | 2026 |
| 8 | Metadata edits | 2027 |
| 9 | Bytes value type | 2027.1 |

---

## Examples

Simplified examples are provided for each node type in this documentation. Complete examples, including sample media files, are available with the Flame installation at `/opt/Autodesk/openclip_examples`.

---

## Open Clip Creator

A standalone tool, Open Clip Creator, is also available for creating Open Clips. This tool can be used to infer structure and assist in the creation process.

## Related pages

- Clip
- Tracks
- Track
- Feeds
- Feed
- Versions
- Version
- Dict
- Value
- Handler
- Path
- Paths
- Rate
- Rational
- Span
- Spans
- Time
- Metadata Edits
- Edits
- Edit
- Additions
- Add
