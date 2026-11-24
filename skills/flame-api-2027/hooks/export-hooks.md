# Export Hooks (`exportHook.py`) (Flame 2027)

> Source: "Python Hooks Tips" (section `exportHook.py` and its workflow diagram), cross-referenced with the `flame.PyExporter.export` docstring ("Autodesk Flame Python: flame module" pydoc).

**Coverage warning:** the 2027 help pages do **not** document the export hooks in detail. There is no table of `info` keys, no signatures for the module-level hooks and no example code. What follows is everything the sources say. For real work, read the installed no-op file (`exportHook.py`, in `/opt/Autodesk/<PRODUCT>_<VERSION>/python/`) where "the hooks themselves are documented".

## File

"`exportHook.py` contains all the hooks related to exporting clips. These hooks are used during export operations from the application."

Name discrepancy: the Tips page says `exportHook.py`; the `PyExporter.export` docstring says "regular export python hooks implemented in `exportHooks.py`". Check which file exists in your install.

## Call order (Tips page)

1. `pre_custom_export` — Optional. Called if required by `get_custom_export_profiles`. Called when the context menu item defined by `getCustomExportProfiles` is selected.
2. `pre_export` — Always called. In a regular export, `pre_export` is called as the Export dialog window is displayed. In a custom export, called after `pre_custom_export`.
3. `pre_export_sequence` — Always called. Called before writing the sequence.
4. `pre_export_asset` — Always called. When it is called depends on the export option. With **Foreground Export**, all `pre_export_asset` are called for each asset immediately in one go. With **Background Export**, each `pre_export_asset` is called as each asset job is submitted to Backburner.
5. `post_export_asset` — Always called. Called after an asset is written. Can be done in Backburner as determined by `useBackburnerPostExportAsset`.
6. `post_export_sequence` — Always called. Called after `post_export_asset`.
7. `post_export` — Always called. Called after `post_export_sequence`.
8. `post_custom_export` — Optional: called if required by `get_custom_export_profiles`. Called after `post_export`.

### Workflow diagram (transcribed from the Tips page image `flame_hooks_wkflw_fg_oct1.png`)

```
Populate Contextual Menu (getCustomExportProfiles)
  -> List of Custom Export Options
  -> Select Custom Export Option
  -> Custom Export
  -> Pre Process for Custom Export   (preCustomExport)      -> info, userData
  -> Pre Process for Export          (preExport)            -> info, userData
  -> Pre Process for Sequence Export (preSequenceExport)    -> info, userData
  -> [loop per asset]
       Pre Process for Asset         (preExportAsset)       -> info, userData
       Post Process for Asset        (postExportAsset)      -> info, userData
       All Assets Processed?  No -> back to preExportAsset
                              Yes -> continue
  -> Post Process for Sequence Export (postSequenceExport)  -> info, userData
  -> Post Process for Export          (postExport)          -> info, userData
  -> Post Process for Custom Export   (postCustomExport)    -> info, userData
```

The diagram shows every pre/post step receiving **`info, userData`**. The diagram's step boxes do not say which steps are optional; the text above does.

## Hook inventory

| Hook (Tips text) | Name in diagram | Name in `PyExporter` override | Called | Args per sources |
|---|---|---|---|---|
| `get_custom_export_profiles` (also written `getCustomExportProfiles` in the same paragraph) | `getCustomExportProfiles` | — | To populate the contextual menu with custom export options | Not documented |
| `pre_custom_export` | `preCustomExport` | — | Optional; when a custom export menu item is selected | `info, userData` (diagram) |
| `pre_export` | `preExport` | `preExport` | Always; as the Export dialog is displayed (regular) / after `pre_custom_export` (custom) | `info, userData` |
| `pre_export_sequence` | `preSequenceExport` | `preExportSequence` | Always; before writing the sequence | `info, userData` |
| `pre_export_asset` | `preExportAsset` | `preExportAsset` | Always; per asset (timing depends on Foreground/Background export) | `info, userData` |
| `post_export_asset` | `postExportAsset` | `postExportAsset` | Always; after an asset is written (possibly in Backburner) | `info, userData` |
| `post_export_sequence` | `postSequenceExport` | `postExportSequence` | Always; after `post_export_asset` | `info, userData` |
| `post_export` | `postExport` | `postExport` | Always; after `post_export_sequence` | `info, userData` |
| `post_custom_export` | `postCustomExport` | — | Optional; after `post_export` | `info, userData` (diagram) |
| `useBackburnerPostExportAsset` | — | — | Determines whether `post_export_asset` runs in Backburner. The source does not say whether it is a hook function, a key or a setting. | Not documented |
| — | — | `exportOverwriteFile(self, path, *args, **kwargs)` | Override-only; returns `"ask"` or `"overwrite"` | `path` |

### Naming ambiguity (important)

The sources use **three spellings** for the same hooks:
- Tips text: snake_case (`pre_export_sequence`, `get_custom_export_profiles`) — but the same paragraph also writes `getCustomExportProfiles`.
- Tips diagram: camelCase with different word order (`preSequenceExport`, `postSequenceExport`).
- `PyExporter.export` hook-override object: camelCase (`preExportSequence`, `postExportSequence`).

The function names Flame actually looks up in `exportHook.py` are therefore **not reliably established by the help pages**. Take the names from the installed no-op export hook file.

## Programmatic export hook override (`PyExporter.export(..., hooks=..., hooks_user_data=...)`)

From the `PyExporter.export` docstring (see [../api/classes/PyExporter.md](../api/classes/PyExporter.md)):

```python
export( (PyExporter)arg1, (object)sources, (str)preset_path, (str)output_directory [, (BackgroundJobSettings)background_job_settings=None [, (object)hooks=None [, (object)hooks_user_data=None]]]) -> None
```

- `hooks` — "Export python hooks override. If passed, regular export python hooks implemented in exportHooks.py will be bypassed for this export and methods in the passed object with matching name will be called."
- `hooks_user_data` — "User data object passed to the export python hooks. This object can be modified by the PythonHookOverride methods but cannot be re-assigned."

Required shape of the `hooks` object (docstring, reformatted from its flattened text; the docstring omits the colon after the first `def`):

```python
class PythonHookOverride(object):
    def preExport(self, info, userData, *args, **kwargs):
        pass

    def postExport(self, info, userData, *args, **kwargs):
        pass

    def preExportSequence(self, info, userData, *args, **kwargs):
        pass

    def postExportSequence(self, info, userData, *args, **kwargs):
        pass

    def preExportAsset(self, info, userData, *args, **kwargs):
        pass

    def postExportAsset(self, info, userData, *args, **kwargs):
        pass

    def exportOverwriteFile(self, path, *args, **kwargs):
        return "ask" # or "overwrite"
```

## Related notes

- **Locked Shared Libraries** (Tips): export hooks in the context menu for Shared Libraries are always accessible regardless of lock status; if the library is locked when the export hook is called and the selected preset re-imports the exported material with the source clip in the library, the **re-import fails silently**.
- Installed examples (`/opt/Autodesk/<PRODUCT>_<VERSION>/python_utilities/examples/`): `post_export_asset_after_snapshot.py` — "how to scope the post_export_asset hook to be called only after a snapshot operation"; `post_export_dependency.py` — "custom actions that use the Python export API (PyExporter)".
- Batch **Write File node** exports use different hooks: `batch_export_begin` / `batch_export_end` ([batch-hooks.md](batch-hooks.md#batch-export-hooks-write-file-node)).
