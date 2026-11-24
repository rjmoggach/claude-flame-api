# Tokens Hooks (Flame 2027.1+)

> Source: "Tokens Hooks" (Autodesk Flame Family 2027 Help). The whole page carries a "NEW IN 2027.1 UPDATE" badge.

Hooks in the **`tokens_hook.py`** file add custom tokens to the **Add Token** drop-downs throughout the application. Overview and discovery rules: [README.md](README.md).

| Function | When called | Returns |
|---|---|---|
| `get_hook_token_list` | To get the list of available tokens for a context. | Tuple of dicts `{"name": ..., "displayName": ...}` |
| `resolve_hook_token` | To resolve a token to its actual value. | The resolved value (a string in every source example) |

## File location

`tokens_hook.py` is located in `/opt/Autodesk/<flame version>/python`, but it can be moved to any supported location scanned for Python hooks, such as `/opt/Autodesk/shared/python` (see [README.md#hook-file-locations](README.md#hook-file-locations)).

## Signatures

The help page does **not** print the function signatures. Its snippets are function *bodies* that use these names, which are therefore the parameter names in the installed `tokens_hook.py`:

| Hook | Names used in the source snippets | Meaning (as used) |
|---|---|---|
| `get_hook_token_list` | `context` | Context name string, compared like `context == "Export"`. |
| `resolve_hook_token` | `token_name` | The token pattern being resolved, e.g. `"<exported by>"` (the `name` you returned from `get_hook_token_list`). |
| `resolve_hook_token` | `context_info` | Dict-like object of information available in the context; read with `context_info.get("<user>", default)`, iterable with `.items()`. Keys are token strings in angle brackets. |

Not documented: parameter order, whether `resolve_hook_token` also receives `context`, and any additional parameters. Read the installed `tokens_hook.py` (no-op/description file) for the exact signature.

> **Agent note (derived, unverified):** Follow the forward-compatibility rule from the Python Hooks Reference and end definitions with `*args, **kwargs`. The parameter list itself must be copied from the installed `tokens_hook.py`.

---

## Defining the Tokens List — `get_hook_token_list`

Use the context to scope where a custom token appears:

| Context | Areas in the Application |
|---|---|
| `Project` | The Project Home, Setups Directory, and Media Cache fields in the Project Management dialog window. |
| `Workspace` | The Name field of the Create Workspace dialog window. |
| `Browsing` | The Pattern field in the Pattern Browsing tab of the MediaHub. |
| `Clip` | The Pattern field in the Rename Shot dialog window of a clip, where available. |
| `Segment` | The Pattern field in the Rename, Rename Shot, and Comment dialog windows of a Timeline segment. |
| `Marker` | The Name Pattern and Comment Pattern fields of the Add Marker dialog windows. |
| `Batch` | The Pattern field of the Rename Batch dialog windows of a Batch Group. |
| `Node` | The different locations where tokens are available for a Batch node: the Name field of a Render or Write File node; the Key Value field in the Add Metadata Key dialog window. |
| `Bookmark` | The Pattern field in the Set Pattern dialog window of the Manage Bookmarks dialog window. |
| `Reference` | The Name field of the Add Reference dialog window. |
| `Export` | The Pattern, Create Open Clip, and Include Setup fields of a Write File node. |

Ambiguity: the source table lists the contexts as plain words; only `"Export"` is shown as an actual string value in code (`context == "Export"`). The other strings are presumably identical to the table entries (same capitalisation) but this is not explicitly stated.

Return value: "The hook contains tuples of dictionaries." Each dictionary must contain two attributes:

| Key | Meaning |
|---|---|
| `name` | The token pattern, such as `{width}` or `<clip_id>`. |
| `displayName` | The user-friendly name shown in the **Add Token** drop-down. |

Bracket rule:
- In the **`Browsing`** context, `name` must always be enclosed in curly braces `{` / `}`.
- In **all other** contexts, `name` must always be enclosed in angle brackets `<` / `>`.

Custom tokens appear inside a **Hooks** submenu of the **Add Token** drop-downs of the matching context, once the Python hooks have been scanned or rescanned.

## Resolving a Token — `resolve_hook_token`

Contains the Python code used to resolve a token to its actual value: a fixed string, or something more complex such as querying a database (on-disk or online).

### Example: `<exported by>` token in the Write File node Pattern field

Resolves to `exported_by_<user>`.

1. In the `get_hook_token_list` hook, define:

```python
if context == "Export":
    return ({"name": "<exported by>", "displayName": "Exported By"},)
```

2. In the `resolve_hook_token` hook, define:

```python
if token_name == "<exported by>":
    user = context_info.get("<user>", "unknown_user")
    return f"exported_by_{user}"
```

Once the Python hook has been scanned or rescanned, the **Exported By** token appears inside the **Hooks** submenu of all the **Add Token** drop-downs assigned to the **Export** context. When selected, `<exported by>` is added to the Pattern field and `<user>` is resolved to the current value (source screenshot: Pattern `<name>_<exported by>` → media path `/var/tmp/final_exported_by_fred.[001001-001060].exr`).

Note (source): in Python, use the f-string prefix (`f"..."`) and wrap variables in curly braces `{}` to inject them into the returned string.

### Slicing and Padding

Slicing works similarly to Custom Tokens in System Preferences, except the slicing is not done inside the token itself but where the variable referencing the token is returned (see Using Conditions).

Padding cannot be adjusted by adding `#` characters inside the token as in the application. Use a Python function instead:

```python
def pad_number(s, nbdigits):
    if s.isdigit():
        return s.zfill(nbdigits)
    return s
```

Then call it when returning the custom token:

```python
if token_name == "<custom shot name>":
    segment_index = pad_number(context_info.get("<segment>", "unknown_segment_index"), 3)
    return f"sh0{segment_index}"
```

### Using Conditions

The string returned for the pattern in the **Rename Shot** dialog window differs based on the name of the currently opened project:

```python
if token_name == "<custom shot name>":
    project = context_info.get("<project>", "unknown_project")
    source_name = context_info.get("<source name>", "unknown_source_name")
    segment_index = context_info.get("<segment>", "unknown_segment_index")
    if project == "car_company":
        return f"{source_name[-15:-9]}"
    if project == "beverage_company":
        return f"{source_name[:-16]}"
    return f"sh0{segment_index}"
```

## Getting the List of Available Information (`context_info` keys)

The source does **not** list the `context_info` keys per context. Keys used in source examples: `"<user>"`, `"<segment>"`, `"<project>"`, `"<source name>"` (the padding example calls `.isdigit()` on the `"<segment>"` value, which implies string values). To discover the keys of a context, print them from `resolve_hook_token`:

```python
if token_name == "<exported by>":
    # print the context info for the export context
    for key, value in context_info.items():
        print(f"{key}: {value}")
    user = context_info.get("<user>", "unknown_user")
    return f"exported_by_{user}"
```

The next time the token is selected in the application, all available keys are printed to the Konsole/Terminal from which the application was started.

## Caching a Value

Flame has **no** caching mechanism for token values. If the **Dynamic** option is enabled for a tokenized string, the application continually tries to execute the code resolving the token; with many instances to update this can greatly impact performance.

Solution (source): add a Python caching mechanism such as `@ttl_cache` or `@lru_cache` inside `tokens_hook.py` itself when needed — `@ttl_cache` to resolve the token at specified time intervals, `@lru_cache` to cache the resolved token for an entire session.

> **Agent note:** `lru_cache` is in the standard library (`functools`). The source does not say where `ttl_cache` comes from; it is **not** in `functools` (it is commonly provided by the third-party `cachetools` package, which would need to be installed into Flame's Python — see [README.md#third-party-packages](README.md#third-party-packages)). The installed example `custom_tokens.py` shows Autodesk's caching strategy.

When the Python hooks are scanned (at application launch or with the **Rescan Python Hooks** function), the tokens are resolved once again.

## Slow token warning

When a token takes more than **0.05 seconds** to resolve, a warning message is printed in the Konsole/Terminal from which the application was started and a message is added to the application log file.

## Examples (installed with Flame)

Located in `/opt/Autodesk/<application version>/python_utilities/examples`. Code not reproduced on the help page.

| File | Description |
|---|---|
| `custom_tokens.py` | Example of how to define and resolve custom tokens with an example of caching strategy. |
