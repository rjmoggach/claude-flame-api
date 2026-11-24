# Open Clip format (`.clip` XML) — overview (Flame 2027)

> Source: "Open Clip Reference", "Open Clip Creator", "Clip" (+ element pages listed in the index below) — Autodesk Flame Family 2027 Help.

## What an Open Clip is

An Open Clip is an **XML-structured file** (extension **`.clip`**), native to Autodesk Flame, containing:

- Physical location of files
- Metadata information, such as timecode
- Structural information, such as tracks
- Clip versions

It points to single or multiple video and/or audio sources and wraps them in a single entity. It is similar to a P2 clip: a wrapper for media files (essence) and the layout of these media files on disk.

**The Open Clip is _not_ a compositional timeline with edits or effects.** A `<span>` is a storage location, not an editorial decision: there is no offset on spans and no way to insert black between spans (except a `<span>` with `<duration>` and no `<path>`, which is a gap — see [elements.md#span](elements.md#span)).

Hierarchy (from "Open Clip Creator"): the most atomic portions, **Spans** (paths to the media), are at the bottom; above them **Feeds** (track versions); then **Tracks** (the sum of information about a single channel); and finally the **Clip** as the topmost entity.

## How it is used in Flame

- Open Clips are browsed/imported via **MediaHub** (the `currentVersion` flag decides which version MediaHub displays) and can be imported in Batch (e.g. `flame.batch.import_clip("/path/robot_CGI.clip", "Reel")` in the Python example "Importing Multi-Channel Clip" — see `../guides/`; that page is a Python Batch example, not format documentation).
- Typical uses: single-version, **multi-version** (one `<feed>` per version per track), **multi-channel** (one `<track>` per OpenEXR layer / channel), **Stereo 3D** (one feed with `<paths>` keyed by `subFeedId`), and **pattern-based** clips (a `<handler>` with a `ScanPattern` option that rescans the file system so new versions appear).
- Gaps (time with no media, version mismatches, invalid `currentVersion`) are shown in Flame as **No Media** slates.
- Anything not explicitly written in the Open Clip (timecode, duration, rates, names) is **inferred from the media**. Elements you add override/add metadata *without changing the media header*.
- To update a pattern-based clip whose duration changed: context menu **Source Version > Update Source Option** (from "Open Clip Creator"; the separator glyph is an image in the source).
- Open Clips can be created by hand, by script, or with the **Open Clip Creator** tool ([open-clip-creator.md](open-clip-creator.md)) — MediaHub context menu **Create Open Clip**, standalone app, or CLI `openclip_creator`.
- Complete examples with sample media ship with Flame at `/opt/Autodesk/openclip_examples`.

## Format version

| Version | Description | Application Support |
|---|---|---|
| 4 | First documented version | 2011 |
| 5 | Nested dictionary support | 2017.1 |
| 6 | Added support for conditions | 2019 |
| 6 | Added support for start frame | 2024 |
| 7 | Format now has distinct metadata and resolved colour spaces | 2026 |
| 8 | Metadata edits | 2027 |
| 9 | Bytes value type | 2027.1 |

- The Reference page says: "This documentation only covers Open Clip **version 7**... Although some support exists for versions prior to 4, it is encouraged to use the latest format when writing new Open Clips."
- **Inconsistency in source:** per-element attribute tables list `version` allowed value `8` (most elements) or `7` (`<track>`, `<feeds>`, `<versions>`), while every full-clip example uses `<clip type="clip" version="9">`. `metadataEdits` needs ≥ 8 and value type `bytes` needs 9 (2027.1).
- "conditions" (v6) and "start frame" (v6, 2024) are listed in the history but **no element or attribute for them is documented** anywhere in these pages.

> **Agent note:** For new clips targeting Flame 2027, the source's own examples write `<clip type="clip" version="9">`; `version="8"` is the value in the `<clip>` attribute table. Both are "supported" by the history table for 2027.1 / 2027 respectively. `type` and `version` are the only **required** (occurrence 1) attributes on `<clip>`.

## Element tree

Legend: `1` = exactly one (required), `0-1` = optional, `*` = zero or more (as given in the source tables). `@attr` = attribute (`!` = required). Types in `{}` are the documented data type of the child.

```text
<clip>  @type!="clip" @version!  (root)
├── <name>              0-1  {string}   inferred from file name if absent
├── <sourceName>        0-1  {string}
├── <startTimecode>     0-1  {time}
├── <duration>          0-1  {time}
├── <editRate>          0-1  {rate}
├── <comment>           0-1  {string}
├── <handler>           0-1  {handler}  clip handler
├── <userData>          0-1  {dict}
├── <tracks>            0-1  @type @version
│   └── <track>         *    @uid! @type @version @currentVersion
│       ├── <trackType>     1    {string}  video | audio | generic (typically)
│       ├── <extendedType>  0-1  {string}
│       ├── <name>          0-1  {string}
│       ├── <sourceName>    0-1  {string}
│       ├── <comment>       0-1  {string}
│       ├── <editRate>      0-1  {rate}
│       ├── <dropMode>      0-1  {string}  DF | NDF
│       ├── <duration>      0-1  {time}
│       ├── <startTimecode> 0-1  {time}
│       ├── <handler>       0-1  {handler}
│       ├── <userData>      0-1  {dict}
│       └── <feeds>         0-1  @type @version @currentVersion
│           └── <feed>      *    @uid! @vuid! @type @version
│               ├── <storageFormat> 0-1  {dict; examples use type="format"}
│               ├── <handler>       0-1  {handler}  feed handler
│               ├── <sampleRate>    0-1  {rate}
│               ├── <startTimecode> 0-1  {time}
│               ├── <startOffset>   0-1  {64-bit integer}
│               ├── <duration>      0-1  {time}
│               ├── <comment>       0-1  {string}
│               ├── <userData>      0-1  {dict}
│               ├── <metadataEdits> 0-1  @type   (format v8+)
│               │   ├── <edits>     *
│               │   │   └── <edit>  *   @key! @type @discarded @renamedKey   (text/value content)
│               │   └── <additions> *
│               │       └── <add>   *   @key! @type @discarded               (text/value content)
│               └── <spans>         0-1  @type @version
│                   └── <span>      *    @type @version
│                       ├── <duration>   0-1  {time}   (span with duration and no path = gap)
│                       ├── <trackIndex> 0-1  {unsigned integer}
│                       ├── <userData>   0-1  {dict}
│                       ├── <path>       0-1  @encoding (file|pattern) @type @version  (#cdata path)
│                       └── <paths>      0-1  (mutually exclusive with <path>)
│                           └── <path>   *    @subFeedId @encoding
└── <versions>          0-1  @type @version @currentVersion
    └── <version>       *    @uid! @type @version
        ├── <name>          0-1  {string}
        ├── <comment>       0-1  {string}
        ├── <creationDate>  0-1  {string}
        └── <userData>      0-1  {dict}

Shared value types (used wherever the child's data type says so):
<handler>  @type @version
├── <name>              0-1  {string}   e.g. "MIO Clip"
├── <version>           0-1  {unsigned integer}
├── <longName>          0-1  {string}   e.g. "Open Clip"
├── <options>           0-1  {dict}     e.g. <ScanPattern>, <RateMode>, ...
└── <conversionOptions> 0-1  {dict}
time  (e.g. <startTimecode>, <duration>)  @type="time" @version
├── <rate>     0-1  {rate}
├── <nbTicks>  1    {64-bit unsigned integer}
└── <dropMode> 0-1  {string}  DF | NDF
rate  (e.g. <editRate>, <sampleRate>, <rate>)  @type="rate" @version
├── <numerator> 1 + <denominator> 1      (rational format)   — OR —
└── #cdata float                         (decimal format, e.g. 23.976)
rational  @type="rational" @version
├── <numerator> 1 + <denominator> 1      — OR —  #cdata 64-bit integer (denominator 1)
dict  (e.g. <userData>, <options>)  @type="dict" @version
└── <anyKeyName type="...">  *  value variants (any element name; type attr selects data type; nested dict allowed, v5+)
```

Notes on the tree:
- Children with attribute `computed=1` are ignored when parsed (stated on `<clip>`, `<track>`, `<feed>`, `<version>`).
- Optional attributes (occurrence 0-1) "will be inferred from the parent node".
- `<metadataEdits>` is documented only as a child of `<feed>`.
- `<edits>`/`<additions>` occurrence is `*` in the source table, though the prose says `<metadataEdits>` "lists two items".
- `<storageFormat>` children (`<type>`, `<isStereo>`, `<lSubFeedId>`, `<rSubFeedId>`) are known only from the stereo example; no reference table exists.

## Key identity rules (summary)

- `track@uid`: unique among tracks in `<tracks>`. For multi-channel OpenEXR, the `uid` is the **layer name**; a non-matching `uid` falls back to the file's first layer.
- `feed@vuid`: version of the feed; unique within one `<track>`; feeds with the same `vuid` across tracks form one version; must match a `version@uid`.
- `feed@uid`: unique at least within the clip.
- `currentVersion` appears on `<feeds>`, `<versions>` (and `<track>`); keep them in sync. If it doesn't match a `vuid`, Flame generates a `No Media` feed.

## Index

| File | Contents |
|---|---|
| [elements.md](elements.md) | Every element: purpose, parents, children, attributes, text, examples (tree order) |
| [metadata-edits.md](metadata-edits.md) | `<metadataEdits>`, `<edits>`, `<edit>`, `<additions>`, `<add>` — semantics and recipes |
| [open-clip-creator.md](open-clip-creator.md) | Open Clip Creator UI, CLI (`openclip_creator`), pattern tokens, `ScanPattern` samples |
| [examples.md](examples.md) | Complete verified XML examples (full clips and fragments) with captions |
| `../guides/` | "Importing Multi-Channel Clip" Python Batch example (covered elsewhere) |
