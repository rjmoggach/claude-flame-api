<!-- source: Autodesk Flame Family 2027 Help _ Clip _ Autodesk.html -->
# Clip

The `<clip>` element is the root of an Open Clip.

---

## Attributes

| Attribute | Data Type | Allowed Values | Occurrence | Description |
|---|---|---|---|---|
| type | string | `clip` | 1 | Type of the element. |
| version | unsigned integer | `8` | 1 | Version of the XML element. |

 Note: Optional attributes (0 occurrence attributes) will be inferred from the parent node.

---

## Children

| Element | Data Type | Occurrence | Description |
|---|---|---|---|
| `<name>` | string | 0-1 | Name of the clip.<br><br>Inferred from the file name if absent. |
| `<tracks>` | tracks | 0-1 | List of tracks in the clip. |
| `<versions>` | versions | 0-1 | List of versions in the clip. |
| `<sourceName>` | string | 0-1 | Source Name<br><br>(aka Tape Name in some workflows). |
| `<startTimecode>` | time | 0-1 | Start timecode of the clip.<br><br>If not defined, the start timecode of the intersection of all the tracks' time ranges is used. |
| `<duration>` | time | 0-1 | Duration of the clip.<br><br>If not defined, the union of all the feeds' duration is computed. |
| `<editRate>` | rate | 0-1 | Rate common to all tracks.<br><br>If not defined, a common rate of all tracks' edit rate is computed. |
| `<comment>` | string | 0-1 | Unparsed text converted into a clip note. |
| `<handler>` | handler | 0-1 | Clip Handler.<br><br>May differ from the track handler. |
| `<userData>` | dict | 0-1 | Dictionary of metadata that is passed through without interpretation. |

 Note: Children elements with the attribute `computed=1` are ignored when parsed.

---

## Examples

### Example 1: One Track

`python
                  0     1     2     3     4     5     6     7
Clip                    [=====+=====+=====+=====+=====[
  Track 0               [=====+=====+=====+=====+=====[
    Feed  v0            [=====+=====+=====+=====+=====[
`

This first example of an Open Clip contains a single video track. This one track has one `<feed>` for which there is only a single referenced media file. This example is the simplest Open Clip you can create.

`python
<?xml version="1.0"?>
<clip type="clip" version="9">
    <tracks>
        <track uid="t0">
            <trackType>video</trackType>
            <feeds>
                <feed vuid="v0" uid="f0">
                    <spans>
                        <span>
                            <path encoding="file">Media/Video1.mov</path>
                        </span>
                    </spans>
                </feed>
            </feeds>
        </track>
    </tracks>
</clip>
`

Remarks:

- Only a subset of the XML schema is used. Nothing more is needed to create an Open Clip.
- Since the referenced file in the `<span>` is a streaming media, the path encoding is set to `"file"`.
- The `<clip>` starts at frame 1: It uses the timing defined by the media in the `<span>`. There is no need to specify any timecode or duration: information not explicitly set in an Open Clip is inferred from the media. In this case, the timecode is inferred from the .mov file header. As for the duration of the `<clip>`, it is inferred from the media duration.

### Example 2: Audio/Video Clip

`python
                  0     1     2     3     4     5
Clip              [=====+=====+=====+=====+=====[
  Track 0         [=====+=====+=====+=====+=====[
    Feed  v0      [=====+=====+=====+=====+=====[
  Track 1         [=====+=====+=====+=====+=====[
    Feed  a0      [=====+=====+=====+=====+=====[
  Track 2         [=====+=====+=====+=====+=====[
    Feed  a1      [=====+=====+=====+=====+=====[
`

This second example illustrates an Open Clip with audio and video components from heterogeneous sources. One video track from a DPX sequence and two audio tracks from two individual WAVE files.

`python
<?xml version="1.0"?>
<clip type="clip" version="9">
    <tracks>
        <track uid="t0">
            <trackType>video</trackType>
            <feeds>
                <feed vuid="v0" uid="f0">
                    <spans>
                        <span>
                            <path encoding="pattern">Media/Video1.[0000-0004].dpx</path>
                        </span>
                    </spans>
                </feed>
            </feeds>
        </track>
        <track uid="t1">
            <trackType>audio</trackType>
            <feeds>
                <feed vuid="v0" uid="f0">
                    <spans>
                        <span>
                            <path encoding="file">Media/Audio1_1L.wav</path>
                        </span>
                    </spans>
                </feed>
            </feeds>
        </track>
        <track uid="t2">
            <trackType>audio</trackType>
            <feeds>
                <feed vuid="v0" uid="f0">
                    <spans>
                        <span>
                            <path encoding="file">Media/Audio1_1R.wav</path>
                        </span>
                    </spans>
                </feed>
            </feeds>
        </track>
    </tracks>
</clip>
`

Remarks:

- Each `<track>` has its own `<feeds>`.
- Each `<track>` has a unique `uid`, used to identify the track.
- The element `<trackType>` contains the `audio` keyword to identify the two audio tracks.
- Since the referenced file in the `<span>` is a sequence of files, the path encoding is set to `"pattern"`.
- The `<clip>` starts at frame 0: It uses the timing defined by the media in the `<span>`. There is no need to specify any timecode or duration: information not explicitly set in an Open Clip is inferred from the media. In this case, the timecode is inferred from the .dpx sequence file name, but could also be derived from the contents of the file headers. As for the duration of the `<clip>`, it is inferred from the media duration.
- There is no method to set left and right for the audio stereo tracks. Use naming conventions for the media files.

### Example 3: One Track, two Versions

`python
                  0     1     2     3     4     5     6     7
Clip                    [=====+=====+=====+=====+=====[
  Track 0               [=====+=====+=====+=====+=====[
    Feed  v0            [=====+=====+=====+=====[
    Feed  v1                  [=====+=====+=====+=====[
`

This example displays an Open Clip containing one track with two versions. Use this structure for multi-version workflows.

`python
<?xml version="1.0"?>
<clip type="clip" version="9">
    <tracks>
        <track uid="t0">
            <trackType>video</trackType>
            <feeds currentVersion="version0">
                <feed vuid="version0" uid="v0">
                    <spans>
                        <span>
                            <path encoding="pattern">Media/Video1.[0001-0004].dpx</path>
                        </span>
                    </spans>
                </feed>
                <feed vuid="version1" uid="v1">
                    <spans>
                        <span>
                            <path encoding="pattern">Media/Video3.[0002-0005].dpx</path>
                        </span>
                    </spans>
                </feed>
            </feeds>
        </track>
    </tracks>
    <versions nbVersions="2" currentVersion="version0">
        <version uid="version0"/>
        <version uid="version1"/>
    </versions>
</clip>
`

Remarks:

- `<feed>` is the element that marks a version. In a `<track>` element, each `<feed>` is a different version.
- The `vuid` attribute of a `<feed>` identifies the version to which that `<feed>` belongs. It must match one of the `uid` of a version.
- In one `<track>`, each `<feed>` must have a different `vuid`.
- Be careful with the `currentVersion` attribute. It is found in both `<feeds>` and `<versions>`. It should be kept in sync to have a properly formatted Open Clip. Its function is to flag a preferred version. In Flame, it indicates the version to display in the MediaHub. If the value is not one of the `vuid`, Flame will generate `No Media` feed for the current feed.
- The duration of the `<track>` is the union of the 2 `<feed>`. In Flame, gaps due to differences between versions are indicated with the presence of No Media slates.
- The two versions do not share the same start timecode because of the .dpx-defined timecode. See this example on how to manage start timecodes between versions.

### Example 4: One Track Multiple Spans

`python
            0     1     2     3     4     5     6     7     8     9    10    11    12    13    14    15    16
Clip              [=====+=====+=====+=====+=====+=====+=====+=====+=====+=====+=====+=====+=====+=====+=====[
  Track 0         [=====+=====+=====+=====+=====+=====+=====+=====+=====+=====+=====+=====+=====+=====+=====[
    Feed v0       [=====+=====+=====+=====+=====|ooooo+ooooo+ooooo+ooooo|=====+=====+=====+=====+=====+=====[

`

In this Open Clip, one track is an aggregate of multiple media sources. When time comes to present the track in the application, each `<span>` is concatenated to the previous one, top to bottom.

`python
<?xml version="1.0"?>
<clip type="clip" version="9">
    <tracks>
        <track uid="t0">
            <trackType>video</trackType>
            <feeds>
                <feed vuid="v0" uid="v0">
                    <spans>
                        <span>
                            <path encoding="pattern">Media/Video1.[0001-0005].dpx</path>
                        </span>
                        <span>
                            <path encoding="pattern">Media/Video2.[0001-0004].dpx</path>
                        </span>
                        <span>
                            <path encoding="pattern">Media/Video3.[0001-0006].dpx</path>
                        </span>
                    </spans>
                </feed>
            </feeds>
        </track>
    </tracks>
</clip>
`

Remarks:

- This example represents a single track (or layer). For multiple tracks, multiple `<track>` elements are required.
- An offset cannot be applied to a `<span>`: There are no provisions to create black between `<span>` elements since a span is not an editorial decision, but rather a storage location: `<span>` does not have any timing information other than what can be inferred from the media it refers to.
- The duration of the `<feed>` is equal to the sum of the `<span>` elements.
- Media has to be homogeneous across `<span>` elements. Formats cannot be mixed, such as having DPX for one `<span>`, and then TIFF for another `<span>`.

### Example 5: Stereo Video Clip

`python
                  0     1     2     3     4     5     6     7
Clip                    [=====+=====+=====+=====+=====[
  Track 0               [=====+=====+=====+=====+=====[
    Feed  v0s0          [=====+=====+=====+=====+=====[
    Feed  v0s1          [=====+=====+=====+=====+=====[
`

This Open Clip illustrates a stereoscopic case with media for the right eye and the left eye.

`python
<?xml version="1.0" encoding="UTF-8"?>
<clip type="clip" version="9">
    <tracks>
        <track uid="t0">
            <trackType>video</trackType>
            <feeds>
                <feed vuid="v0" uid="f0">
                    <storageFormat type="format">
                        <type>video</type>
                        <isStereo type="bool">true</isStereo>
                        <lSubFeedId type="uid">Left</lSubFeedId>
                        <rSubFeedId type="uid">Right</rSubFeedId>
                    </storageFormat>
                    <spans>
                        <span>
                            <paths>
                                <path subFeedId="Left" encoding="pattern">MEDIA/left-eye.[0001-0005].tif</path>
                                <path subFeedId="Right" encoding="pattern">MEDIA/right-eye.[0001-0005].tif</path>
                            </paths>
                        </span>
                    </spans>
                </feed>
            </feeds>
        </track>
    </tracks>
</clip>
`

Remarks:

-
There is only one track and one feed to account for both eyes.

-
In `<path>` elements, the `subFeedId` attribute is what differentiates the left eye from the right one.

-
In a Stereo Open Clip, the `storageFormat` element is a mandatory child of each `feed` that is stereo (with a `subFeedID` for each eye). It must be written as it appears here:

`python
<storageFormat type="format">
    <type>video</type>
    <isStereo type="bool">true</isStereo>
    <lSubFeedId type="uid">Left</lSubFeedId>
    <rSubFeedId type="uid">Right</rSubFeedId>
</storageFormat>
`

### Example 6: Multi-Track From one OpenEXR

`python
Clip
  Track 0 - BEAUTY:MasterBeauty
    Feed  v0
  Track 1 – Matte1
    Feed  v0
  Track 2 – Matte2
    Feed  v0
`

This example illustrates how an Open Clip can create a structure that expresses the different channels of a single multi-channel OpenEXR file.

`python
<?xml version="1.0"?>
<clip type="clip" version="9">
    <tracks>
        <track uid="BEAUTY:MasterBeauty">
            <trackType>video</trackType>
            <feeds>
                <feed vuid="v0" uid="v0">
                    <spans>
                        <span>
                            <path encoding="pattern">Media/RGB_2Mattes.exr</path>
                        </span>
                    </spans>
                </feed>
            </feeds>
        </track>
        <track uid="Matte1">
            <trackType>video</trackType>
            <feeds>
                <feed vuid="v0" uid="v0">
                    <spans>
                        <span>
                            <path encoding="pattern">Media/RGB_2Mattes.exr</path>
                        </span>
                    </spans>
                </feed>
            </feeds>
        </track>
        <track uid="Matte2">
            <trackType>video</trackType>
            <feeds>
                <feed vuid="v0" uid="v0">
                    <spans>
                        <span>
                            <path encoding="pattern">Media/RGB_2Mattes.exr</path>
                        </span>
                    </spans>
                </feed>
            </feeds>
        </track>
    </tracks>
</clip>
`

Remarks:

- In this case, the `uid` of the different tracks are not random at all: they are the actual layer names of the multi-layer OpenEXR file. This is the important bit: if the `uid` does not match an OpenEXR layer, that track defaults to the first layer of the file, in this case the BEAUTY pass. For example, if the `uid` is set to `Matte3` but the OpenEXR file only contains layers named `BEAUTY:MasterBeauty`, `Matte1`, and `Matte2`, the track will default to the `BEAUTY:MasterBeauty` layer.
- This structure opens up the possibility to version an OpenEXR.

### Example 7: Timing Versions

`python
                  0     1     2     3     4     5     6     7     8     9    10    11    12    13    14
Clip              [=====+=====+=====+=====+=====+=====+**\*\*\*\**+=====+=====+=====+=====[
  Track 0         [=====+=====+=====+=====+=====+=====+**\*\*\*\**+=====+=====+=====+=====[
    Feed  v0      [=====+=====+=====+=====+=====+=====[
    Feed  v1                                                                      [=====+=====+=====+=====[
`

This example illustrates one track with two versions, each with a different start timecode: version 1 starts at 0 frames, and the other starts at 10 frames.

`python
<?xml version="1.0"?>
<clip type="clip" version="9">
    <tracks>
        <track uid="t0">
            <trackType>video</trackType>
            <feeds currentVersion="version0">
                <feed vuid="version0" uid="v0">
                    <spans>
                        <span>
                            <path encoding="pattern">Media/Video1.[0000-0005].dpx</path>
                        </span>
                    </spans>
                </feed>
                <feed vuid="version1" uid="v1">
                    <startTimecode type="time">
                        <rate type="rate">24</rate>
                        <nbTicks>10</nbTicks>
                    </startTimecode>
                    <spans>
                        <span>
                            <path encoding="pattern">Media/Video3.[0001-0004].dpx</path>
                        </span>
                    </spans>
                </feed>
            </feeds>
        </track>
    </tracks>
    <versions type="versions" nbVersions="2" currentVersion="version0">
        <version type="version" uid="version0"/>
        <version type="version" uid="version1"/>
    </versions>
</clip>
`

Remarks:

- The duration of the `<clip>` covers the whole of the durations of the 2 versions.
- Frames where there is no media are presented in Flame as No Media slates.
- Feed `v0` starts at 0 because it uses the start timecode of the media defined in its span.
- The `<startTimecode>` does not have to be at the rate of the media: It is just a unit of measure that defines where the media starts on the Timeline. It is still good practice to keep similar timings across the Open Clip to avoid conversion mix-ups.

### Example 8: Timing a Clip

`python
         00:00:02+00   +01   +02   +03   +04   +05   +06   +07   +08   +09   +10   +11   +12   +13   +14
Clip              [=====+=====+=====+=====+=====+=====+**\*\*\*\**+=====+=====+=====+=====[
  Track 0         [=====+=====+=====+=====+=====+=====+**\*\*\*\**+=====+=====+=====+=====[
    Feed  v0      [=====+=====+=====+=====+=====+=====[
    Feed  v1                                                                      [=====+=====+=====+=====[
`

This example illustrates how to define the start timecode for an Open Clip.

`python
<?xml version="1.0"?>
<clip type="clip" version="9">
    <startTimecode type="time">
        <rate type="rate">24</rate>
        <nbTicks>48</nbTicks>
    </startTimecode>
    <tracks>
        <track uid="t0">
            <trackType>video</trackType>
            <feeds currentVersion="version0">
                <feed vuid="version0" uid="v0">
                    <spans>
                        <span>
                            <path encoding="pattern">Media/Video1.[0000-0005].dpx</path>
                        </span>
                    </spans>
                </feed>
                <feed vuid="version1" uid="v1">
                    <startTimecode type="time">
                        <rate type="rate">24</rate>
                        <nbTicks>10</nbTicks>
                    </startTimecode>
                    <spans>
                        <span>
                            <path encoding="pattern">Media/Video3.[0001-0004].dpx</path>
                        </span>
                    </spans>
                </feed>
            </feeds>
        </track>
    </tracks>
    <versions type="versions" nbVersions="2" currentVersion="version0">
        <version type="version" uid="version0"/>
        <version type="version" uid="version1"/>
    </versions>
</clip>
`

Remarks:

- The duration of the `<clip>` covers the whole span covered by the 2 versions.
- Times where there is no media are presented in Flame as No Media slates.
- Feed `v0` starts at 0 because it uses the start timecode of the media defined in its span.
- `<startTimecode>` does not have to be at the rate of the media: It is just a unit of measure that defines where the media starts on the Timeline. The selected rate defines how many ticks are in a second.
- `<startTimecode>` defined in the second `<feed>` overrides the timecode inferred from the media within.

## Related pages

- Open Clip Reference
