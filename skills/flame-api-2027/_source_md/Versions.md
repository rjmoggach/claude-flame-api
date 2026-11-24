<!-- source: Autodesk Flame Family 2027 Help _ Versions _ Autodesk.html -->
# Versions

The `<versions>` element lists two items: the available versions of a clip and the version currently in use.

Different versions of a track are described by different `<feed>` elements, each identified with a unique `vuid` attribute. In an Open Clip XML, a specific version of a clip is defined as all the `<feed>` elements sharing the same `vuid` attribute across different `<track>` elements.

The `<version>` element describes and lists the available versions, while the `currentVersion` attribute defines which `<version>` element is the current one. The client application that reads the .clip file is not required to set `currentVersion`; it only serves as a flag placed by the creator.

---

## Attributes

| Attribute | Data Type | Allowed Values | Occurrence | Description |
|---|---|---|---|---|
| type | string | `versions` | 0-1 | Type of the element. |
| version | unsigned integer | `7` | 0-1 | Version of the XML element. |
| currentVersion | string | any | 0-1 | Defines which `<version>` to use as the current, based on matching `uid` on each `<version>` child.<br><br>If not defined, the last one is considered the current. |

 Note: Optional attributes (0 occurrence attributes) will be inferred from the parent node.

Remarks: Take care with the `currentVersion` attribute. It is found in both `<feeds>` and `<versions>`. It should be kept in sync to have a properly formatted Open Clip. Its function is to flag a preferred version. In Flame, it indicates the version to display in the MediaHub. If the value is not one of the `vuid`, Flame generates a `No Media` feed for the current feed.

---

## Children

| Element | Data Type | Occurrence | Description |
|---|---|---|---|
| `<version>` | version | * | Each version contained in the list of versions. |

---

## Example

### Example 1

Consider the following simplified example.

`python
<versions currentVersion="v2">
    <version uid="v1"/>
    <version uid="v2"/>
    <version uid="v3"/>
</versions>
`

This list of versions would be paired with the following tracks.

`python
<tracks>
    <track uid="track1">
        <feeds>
            <feed vuid="v1" uid="t1f1"/>
            <feed vuid="v3" uid="t1f2"/>         </feeds>
    </track>
    <track uid="track2">
        <feeds>
            <feed vuid="v1" uid="t2f1"/>
            <feed vuid="v2" uid="t2f2"/>
            <feed vuid="v3" uid="t2f3"/>
        </feeds>
    </track>
</tracks>
`

This clip can display the following:

- Version 1: track1 using feed t1f1 and track2 using t2f1;
- Version 2: track2 using t2f2 only (there is no `vuid` in track1 matching "v2");
- Version 3: track1 using feed t1f2 and track2 using t2f3;

In this example, the client application should display version 2 of the clip because `currentVersion` = `"v2"`.

## Related pages

- Open Clip Reference
