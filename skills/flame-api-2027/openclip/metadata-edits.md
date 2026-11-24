# Open Clip metadata edits (`<metadataEdits>`) — Flame 2027

> Source: "Metadata Edits", "Edits", "Edit", "Additions", "Add", "Feed", "Value", "Open Clip Reference" (Autodesk Flame Family 2027 Help).

Metadata edits let an Open Clip modify, rename, discard or add per-frame metadata read from the media file, **without changing the media**. Introduced in Open Clip format **version 8 (Flame 2027)** (version history, Open Clip Reference).

## Placement

```text
<feed>
└── <metadataEdits type="metadataEdits">   0-1
    ├── <edits>        *
    │   └── <edit>     *   @key! @type @discarded @renamedKey
    └── <additions>    *
        └── <add>      *   @key! @type @discarded
```

`<metadataEdits>` is documented only as a child of `<feed>` (Feed children table: `<metadataEdits>` | metadataEdits | 0-1 | Metadata edits). All edit units (frames) within a given feed share the same metadata edits/additions.

## Semantics (exact rules from source)

1. Metadata is evaluated on an **edit unit** basis (usually a video frame).
2. **`<edit>`** — modify a value, discard a key, rename a key, or a combination. Applied **only if the key is present** in the modified metadata dictionary read from the media file. If the key is absent, nothing happens.
3. **`<add>`** — applied **only if the key is not already present** in the modified metadata dictionary read from the media file.
4. **Order:** when both are present, `<edits>` are applied first and `<additions>` second.
5. **Discarded** `<edit>`/`<add>` elements (`discarded="yes"` etc.) are not included in the resulting metadata.
   - Discarded `<edit>`: removes the key from the metadata ("Remove a key and its Value"); "The type and value are not relevant for discarded elements."
   - Discarded `<add>`: the addition is not applied — "can be used to temporarily disable metadata additions while keeping track of the original values."
6. `renamedKey` (on `<edit>` only): the resulting metadata has the renamed key instead of the original. Without content, the value is unchanged; with content, the value is replaced.
7. Content of `<edit>`/`<add>` is a `value` variant; `type` defaults to `string`; allowed `type` values are the Value Data Types (`int`, `uint`, `int8`…`uint64`, `float`, `double`, `bool`, `string`, `binary`, `bytes`, `rate`, `rational`, `time`, `uid`, `keycode`, `dict` — see [elements.md#value](elements.md#value)). The `label` attribute is **not supported** in `<edit>` and `<add>`.

> **Agent note (derived from rules 2–4):** Because edits run first, an `<edit>` that renames or discards key `K` makes `K` absent for the subsequent `<additions>` pass, so an `<add key="K">` will then apply. This is exactly what Example 3 below relies on.

## Attributes

### `<metadataEdits>`

| Attribute | Data Type | Allowed Values | Occurrence | Description |
|---|---|---|---|---|
| `type` | string | `metadataEdits` | 0-1 | Type of the element. |

Children: `<edits>` (edits, `*`), `<additions>` (additions, `*`). (Prose says it "lists two items".)

### `<edits>` / `<additions>`

No attributes documented. Children: `<edit>` (`*`) / `<add>` (`*`).

### `<edit>`

| Attribute | Data Type | Allowed Values | Occurrence | Description |
|---|---|---|---|---|
| `key` | string | any | 1 | Key used to identify the metadata element. |
| `type` | string | Value Data Type | 0-1 | Type of the element. String is assumed if not specified. |
| `discarded` | boolean | `True`, `False`, `Yes`, `No`, `1`, `0` | 0-1 | Discarded elements are not applied to resulting metadata. |
| `renamedKey` | string | any | 0-1 | If defined, the resulting metadata will have the renamed metadata key instead of the original key. |

### `<add>`

| Attribute | Data Type | Allowed Values | Occurrence | Description |
|---|---|---|---|---|
| `key` | string | any | 1 | Metadata key used to identify the metadata element. |
| `type` | string | Value Data Type | 0-1 | Type of the element. String is assumed if not specified. |
| `discarded` | boolean | `True`, `False`, `Yes`, `No`, `1`, `0` | 0-1 | Discarded elements are not applied to resulting metadata. |

## `<edit>` examples

Modify a value (only if `ModifiedKey` is present in the media metadata):

```xml
<edit key="ModifiedKey" type="string">NewValue</edit>
```

Remove a key and its value:

```xml
<edit key="DiscardedKey" discarded="yes"/>
```

Rename a key (`ExistingKey` → `RenamedKey`, value unchanged; no-op if absent):

```xml
<edit key="ExistingKey" renamedKey="RenamedKey"/>
```

Rename a key and modify its value (value replaced with `NewValue`):

```xml
<edit key="ExistingKey" renamedKey="RenamedKey">NewValue</edit>
```

## `<add>` examples

Add a value under `Key` if the original media metadata has no `Key` entry:

```xml
<add key="Key" type="string">value</add>
```

Discarded (disabled) addition:

```xml
<add key="Key" discarded="yes" type="string">value</add>
```

## `<metadataEdits>` examples

### Example 1: Complex edit (most possible values and attributes)

```xml
<metadataEdits type="metadataEdits">
    <edits>
        <edit key="ModifiedKey" type="string">NewValue</edit>
        <edit key="DiscardedKey" discarded="yes"></edit>
        <edit key="ExistingKey" renamedKey="RenamedKey"/>
        <edit key="OtherExistingKey" renamedKey="RenamedAndModifiedKey">NewValue</edit>
    </edits>
    <additions>
        <add key="AddedKey" type="string">AddedValue</add>
        <add key="DiscardedKey" discarded="yes" type="string">DiscardedValue</add>
    </additions>
</metadataEdits>
```

### Example 2: Forcing a value

An `<edit>` applies only if the key is present and an `<add>` only if it is absent, so **both are needed to force a value**:

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

### Example 3: Replacing a value while keeping the original

Replace an existing key while keeping track of its original value, if any (useful to track modified values):

```xml
<metadataEdits type="metadataEdits">
    <edits>
        <edit key="Target" renamedKey="original/Target"></edit>
    </edits>
    <additions>
        <add key="Target" type="string">ForcedValue</add>
    </additions>
</metadataEdits>
```

### Standalone `<edits>` / `<additions>` (from the Edits / Additions pages)

```xml
<edits>
    <edit key="ModifiedKey" type="string">NewValue</edit>
    <edit key="DiscardedKey" discarded="yes"></edit>
    <edit key="ExistingKey" renamedKey="RenamedKey">NewValue</edit>
</edits>
```

```xml
<additions>
    <add key="AddedKey" type="string">AddedValue</add>
    <add key="DiscardedKey" discarded="yes" type="string">DiscardedValue</add>
</additions>
```

## Ambiguities / not documented

- No full-clip example shows `<metadataEdits>` inside a `<feed>`; placement is from the Feed children table only. Required clip `version` for this feature: format 8 per the history table.
- Which metadata keys exist for a given media format, and the key path syntax (Example 3 uses `original/Target`, suggesting `/`-separated hierarchical keys), are not specified.
- `<edits>`/`<additions>` occurrence is `*` in the table; whether multiple `<edits>` blocks are allowed/meaningful is not explained.
- The phrase "modified metadata dictionary read from the media file" is used throughout without further definition.
