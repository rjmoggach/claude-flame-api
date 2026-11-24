# Open Clip XML examples (verified) — Flame 2027

> Source: "Clip", "Handler", "Versions", "Track", "Feed", "Span", "Metadata Edits", "Open Clip Creator" (Autodesk Flame Family 2027 Help).

All XML below was compared (whitespace-normalized) against the original HTML `<pre>` blocks and matches. In the source, these blocks are mislabelled as `python`; they are XML. Timeline diagrams: `[=====` = frames with media, `[` start/end; `ooooo` = frames from a different span. More complete examples with sample media ship with Flame at `/opt/Autodesk/openclip_examples`.

Element reference: [elements.md](elements.md). Metadata edit examples: [metadata-edits.md](metadata-edits.md). Pattern (`ScanPattern`) clip samples: [open-clip-creator.md](open-clip-creator.md#sample-open-clips-with-pattern-tokens).

---

## Example 1: One track

Single video track, one `<feed>`, one referenced media file — the simplest Open Clip.

```text
                  0     1     2     3     4     5     6     7
Clip                    [=====+=====+=====+=====+=====[
  Track 0               [=====+=====+=====+=====+=====[
    Feed  v0            [=====+=====+=====+=====+=====[
```

```xml
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
```

- Only a subset of the schema is used; nothing more is needed.
- Streaming media (`.mov`) → `encoding="file"`.
- The clip starts at frame 1, using the timing of the media; timecode inferred from the `.mov` header, duration from the media duration.

## Example 2: Audio/video clip

One video track from a DPX sequence and two audio tracks from two WAVE files (heterogeneous sources).

```text
                  0     1     2     3     4     5
Clip              [=====+=====+=====+=====+=====[
  Track 0         [=====+=====+=====+=====+=====[
    Feed  v0      [=====+=====+=====+=====+=====[
  Track 1         [=====+=====+=====+=====+=====[
    Feed  a0      [=====+=====+=====+=====+=====[
  Track 2         [=====+=====+=====+=====+=====[
    Feed  a1      [=====+=====+=====+=====+=====[
```

```xml
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
```

- Each `<track>` has its own `<feeds>` and a unique `uid`; `<trackType>audio</trackType>` marks audio tracks.
- File sequence → `encoding="pattern"`.
- Clip starts at frame 0; timecode inferred from the `.dpx` sequence file name (could also come from file headers).
- No method exists to set left/right for stereo audio tracks; use media file naming conventions.
- (Diagram labels feeds `a0`/`a1`, but the XML uses `vuid="v0"` for all — all three tracks belong to the same version.)

## Example 3: One track, two versions

Multi-version workflow: one `<feed>` per version.

```text
                  0     1     2     3     4     5     6     7
Clip                    [=====+=====+=====+=====+=====[
  Track 0               [=====+=====+=====+=====+=====[
    Feed  v0            [=====+=====+=====+=====[
    Feed  v1                  [=====+=====+=====+=====[
```

```xml
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
```

- `<feed>` marks a version; its `vuid` must match one `version@uid`; within a track each feed has a different `vuid`.
- Keep `currentVersion` on `<feeds>` and `<versions>` in sync; it flags the preferred version (displayed in MediaHub). A value not matching any `vuid` → Flame generates a `No Media` feed.
- Track duration = union of both feeds; gaps between versions show No Media slates.
- The versions have different start timecodes because of the `.dpx`-defined timecode (see Example 7).

## Example 4: One track, multiple spans

A track aggregated from multiple media sources; spans are concatenated top to bottom.

```text
            0     1     2     3     4     5     6     7     8     9    10    11    12    13    14    15    16
Clip              [=====+=====+=====+=====+=====+=====+=====+=====+=====+=====+=====+=====+=====+=====+=====[
  Track 0         [=====+=====+=====+=====+=====+=====+=====+=====+=====+=====+=====+=====+=====+=====+=====[
    Feed v0       [=====+=====+=====+=====+=====|ooooo+ooooo+ooooo+ooooo|=====+=====+=====+=====+=====+=====[
```

```xml
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
```

- Represents a single track (layer); multiple tracks need multiple `<track>` elements.
- No offset can be applied to a `<span>`; no provision to create black between spans (a span is a storage location, not an editorial decision).
- Feed duration = sum of spans. Media must be homogeneous across spans (no DPX in one and TIFF in another).

## Example 5: Stereo video clip

One track and one feed for both eyes; `<paths>` with `subFeedId` distinguishes eyes.

```text
                  0     1     2     3     4     5     6     7
Clip                    [=====+=====+=====+=====+=====[
  Track 0               [=====+=====+=====+=====+=====[
    Feed  v0s0          [=====+=====+=====+=====+=====[
    Feed  v0s1          [=====+=====+=====+=====+=====[
```

```xml
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
```

- In a Stereo Open Clip, `<storageFormat>` is a **mandatory** child of each stereo `feed` and "must be written as it appears here".

## Example 6: Multi-track from one OpenEXR

Expose the channels (layers) of one multi-channel OpenEXR as tracks.

```text
Clip
  Track 0 - BEAUTY:MasterBeauty
    Feed  v0
  Track 1 – Matte1
    Feed  v0
  Track 2 – Matte2
    Feed  v0
```

```xml
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
```

- Track `uid`s are the actual OpenEXR layer names. If a `uid` doesn't match a layer (e.g. `Matte3`), that track defaults to the first layer (`BEAUTY:MasterBeauty`).
- This structure makes it possible to version an OpenEXR.
- (The same `uid="v0"` is reused for feeds in different tracks here, although Feed says `uid` "needs to be at least unique within the clip" — source inconsistency.)

## Example 7: Timing versions

One track, two versions with different start timecodes (one at 0 frames, the other at 10 frames).

```text
                  0     1     2     3     4     5     6     7     8     9    10    11    12    13    14
Clip              [=====+=====+=====+=====+=====+=====+**\*****\*****\*****\******+=====+=====+=====+=====[
  Track 0         [=====+=====+=====+=====+=====+=====+**\*****\*****\*****\******+=====+=====+=====+=====[
    Feed  v0      [=====+=====+=====+=====+=====+=====[
    Feed  v1                                                                      [=====+=====+=====+=====[
```

> **Garbled in source (HTML too):** the `**\*****\*****...` run on the Clip/Track lines is corrupted markup. It represents frames 6–9 where no feed has media (shown as No Media). Reconstructed intent (not verbatim): `Clip [=====+=====+=====+=====+=====+=====+*****+*****+*****+*****+=====+=====+=====+=====[`.

```xml
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
```

- Clip duration covers both versions; frames with no media are No Media slates.
- Feed `v0` starts at 0 (start timecode of its media); feed `v1`'s `<startTimecode>` places it at 10.
- `<startTimecode>` need not be at the media's rate — it's a unit of measure for where the media starts on the timeline; keeping similar timings avoids conversion mix-ups.

## Example 8: Timing a clip

Defining the clip start timecode (48 ticks at 24 fps = `00:00:02+00`).

```text
         00:00:02+00   +01   +02   +03   +04   +05   +06   +07   +08   +09   +10   +11   +12   +13   +14
Clip              [=====+=====+=====+=====+=====+=====+**\*****\*****\*****\******+=====+=====+=====+=====[
  Track 0         [=====+=====+=====+=====+=====+=====+**\*****\*****\*****\******+=====+=====+=====+=====[
    Feed  v0      [=====+=====+=====+=====+=====+=====[
    Feed  v1                                                                      [=====+=====+=====+=====[
```

(Same garbled gap markup as Example 7.)

```xml
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
```

- The selected rate defines how many ticks are in a second.
- `<startTimecode>` in the second `<feed>` overrides the timecode inferred from its media.

---

## Handler ScanPattern expansion

Scan-pattern clip handler (from "Handler", Example 2):

```xml
<handler>
    <name>MIO Clip</name>
    <options>
        <ScanPattern>Media/Video_v{version}.{frame}.dpx</ScanPattern>
    </options>
</handler>
```

Files on disk:

```text
Media/Video_v0.001.dpx
Media/Video_v0.002.dpx
Media/Video_v0.003.dpx
Media/Video_v0.004.dpx
Media/Video_v1.001.dpx
Media/Video_v1.002.dpx
Media/Video_v1.003.dpx
Media/Video_v1.004.dpx
```

Equivalent Open Clip (assuming the media exists):

```xml
<clip type="clip" version="9">
    <tracks>
        <track uid="t0">
            <trackType>video</trackType>
            <feeds>
                <feed vuid="v0" uid="f0">
                    <spans>
                        <span>
                            <path encoding="file">Media/Video_v0.[001-0004].dpx</path>
                        </span>
                    </spans>
                </feed>
                <feed vuid="v1" uid="f1">
                    <spans>
                        <span>
                            <path encoding="file">Media/Video_v1.[001-0004].dpx</path>
                        </span>
                    </spans>
                </feed>
            </feeds>
        </track>
    </tracks>
</clip>
```

After adding `Media/Video_v2.001.dpx` and `Media/Video_v2.002.dpx`, a refresh yields:

```xml
<clip type="clip" version="9">
    <tracks>
        <track uid="t0">
            <trackType>video</trackType>
            <feeds>
                <feed vuid="v0" uid="f0">
                    <spans>
                        <span>
                            <path encoding="file">Media/Video_v0.[001-0004].dpx</path>
                        </span>
                    </spans>
                </feed>
                <feed vuid="v1" uid="f1">
                    <spans>
                        <span>
                            <path encoding="file">Media/Video_v1.[001-0004].dpx</path>
                        </span>
                    </spans>
                </feed>
                <feed vuid="v2" uid="f2">
                    <spans>
                        <span>
                            <path encoding="file">Media/Video_v2.[001-0002].dpx</path>
                        </span>
                    </spans>
                </feed>
            </feeds>
        </track>
    </tracks>
</clip>
```

> **Source oddities (verified identical in HTML):** the "equivalent" paths use inconsistent padding (`[001-0004]`) and `encoding="file"` with bracket ranges; per the `<path>` page a range needs `encoding="pattern"` and the files are 3-digit padded (`[001-004]`). Treat these as illustrative.

## Versions pairing (simplified, from "Versions")

```xml
<versions currentVersion="v2">
    <version uid="v1"/>
    <version uid="v2"/>
    <version uid="v3"/>
</versions>
```

```xml
<tracks>
    <track uid="track1">
        <feeds>
            <feed vuid="v1" uid="t1f1"/>
            <feed vuid="v3" uid="t1f2"/>
        </feeds>
    </track>
    <track uid="track2">
        <feeds>
            <feed vuid="v1" uid="t2f1"/>
            <feed vuid="v2" uid="t2f2"/>
            <feed vuid="v3" uid="t2f3"/>
        </feeds>
    </track>
</tracks>
```

Version 1 = `t1f1` + `t2f1`; Version 2 = `t2f2` only; Version 3 = `t1f2` + `t2f3`. The client should display version 2 (`currentVersion="v2"`).

## Fragment: track with overridden metadata and userData (from "Track")

```xml
<track uid="t0">
    <trackType>video</trackType>
    <name>My name</name>
    <sourceName>My tape name</sourceName>
    <comment>My comment</comment>
    <feeds>
        <feed vuid="v0" uid="f0">
            <spans>
                <span>
                    <path encoding="file">Media/Video1.mov</path>
                </span>
            </spans>
        </feed>
    </feeds>
    <userData>
        <assetId type="string">11231-2312323</assetId>
    </userData>
</track>
```

## Fragment: span gap and EXR layer selection (from "Span")

Two-second gap (span with duration, no path):

```xml
<span>
    <duration type="time">
        <nbTicks>48</nbTicks>
        <rate type="rate">24</rate>
    </duration>
</span>
```

Second layer of a multi-channel OpenEXR:

```xml
<span>
    <trackIndex>1</trackIndex>
    <path encoding="pattern">ABGR.[00001001-00001004].exr</path>
</span>
```

## Fragment: forcing a metadata value (from "Metadata Edits")

```xml
<metadataEdits type="metadataEdits">
    <edits>
        <edit key="Target" type="string">ForcedValue</edit>
    </edits>
    <additions>
        <add key="Target" type="string">ForcedValue</add>
    </additions>
</metadataEdits>
```

Goes inside a `<feed>`. Other metadata-edit examples: [metadata-edits.md](metadata-edits.md).
