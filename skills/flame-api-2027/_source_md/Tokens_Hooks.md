<!-- source: Autodesk Flame Family 2027 Help _ Tokens Hooks _ Autodesk.html -->
# Tokens Hooks

Use the hooks in the **tokens_hook.py** file to add custom tokens to the multiple **Add Token** drop-downs available throughout the application.

Two hooks are available:

| Function | Description |
|---|---|
| `get_hook_token_list` | Hook called to get the list of available tokens for a context. |
| `resolve_hook_token` | Hook called to resolve a token to its actual value. |

The **tokens_hook.py** file is located in `/opt/Autodesk/<flame version>/python`, but it can be moved to any supported location scanned for python hooks like `/opt/Autodesk/shared/python`. For more information on the different locations scanned for python hooks, see Hooks Location.

---

## Defining the Tokens List

The list of tokens to be added is defined using the `get_hook_token_list` hook.

Use the following context options to scope where a custom token appears:

| Context | Areas in the Application |
|---|---|
| Project | The Project Home, Setups Directory, and Media Cache fields in the Project Management dialog window. |
| Workspace | The Name field of the Create Workspace dialog window. |
| Browsing | The Pattern field in the Pattern Browsing tab of the MediaHub. |
| Clip | The Pattern field in the Rename Shot dialog window of a clip, where available. |
| Segment | The Pattern field in the Rename, Rename Shot, and Comment dialog windows of a Timeline segment. |
| Marker | The Name Pattern and Comment Pattern fields of the Add Marker dialog windows. |
| Batch | The Pattern field of the Rename Batch dialog windows of a Batch Group. |
| Node | The different locations where tokens are available for a Batch node.<br><br> • The Name field of a Render or Write File node • The Key Value field in the Add Metadata Key dialog window. |
| Bookmark | The Pattern field in the Set Pattern dialog window of the Manage Bookmarks dialog window. |
| Reference | The Name field of the Add Reference dialog window. |
| Export | The Pattern, Create Open Clip, and Include Setup fields of a Write File node. |

The hook contains tuples of dictionaries. Each dictionary must contain two attributes:

- **name:** The token pattern, such as `{width}` or `<clip_id>`.
- **displayName:** The user-friendly name shown in the **Add Token** drop-down.

In the **Browsing** context, the name must always be enclosed in curly braces `{`/`}`. In other contexts, the name must always be enclosed in angle brackets `<`/`>`.

---

## Resolving a Token

The `resolve_hook_token` hook contains the Python code used to resolve a token to its actual value. Each entry can be used to simply add a fixed string or fetch information in more complex scenarios, like querying a database (either on-disk or online) to retrieve a value.

For example, to add a custom token that resolves to `exported_by_<user>` in the **Pattern** field of a Write File node:

1.
In the `get_hook_token_list` hook, define:

`python
if context == "Export":
    return ({"name": "<exported by>", "displayName": "Exported By"},)
`

2.
In the `resolve_hook_token` hook, define:

`python
if token_name == "<exported by>":
    user = context_info.get("<user>", "unknown_user")
    return f"exported_by_{user}"
`

In the application, once the Python hook has been scanned or rescanned, the **Exported By** token appears inside the **Hooks** submenu of all the **Add Token** drop-downs assigned to the **Export** context.

When selected, `<exported by>` is added to the Pattern field and <user> is resolved to the current value.

 Note: In Python, use the f-string prefix (f"...") and wrap variables in curly braces {} to inject them into the returned string.

### Slicing and Padding

Slicing the output of a token works similarly to the Custom Tokens in the System Preferences. The main difference is that the slicing is not done inside the token itself, but where the variable referencing the token is returned. See Using Conditions for an example.

In contrast, the padding cannot be adjusted by adding # characters inside the token like in the application. Therefore, to add padding, a Python function like the following must be used:

`python
def pad_number(s, nbdigits):
    if s.isdigit():
        return s.zfill(nbdigits)
    return s
`

Then, this function can be called when returning the custom token:

`python
if token_name == "<custom shot name>":
    segment_index = pad_number(context_info.get("<segment>", "unknown_segment_index"), 3)
    return f"sh0{segment_index}"
`

### Using Conditions

Just like with any Python code, it is possible to scope the returned string depending on the available information. In the following example, the string returned for the pattern in the **Rename Shot** dialog window differs based on the name of the project currently opened.

`python
if token_name == "<custom shot name>":
    project = context_info.get("<project>", "unknown_project")
    source_name = context_info.get("<source name>", "unknown_source_name")
    segment_index = context_info.get("<segment>", "unknown_segment_index")
    if project == "car_company":
        return f"{source_name[-15:-9]}"
    if project == "beverage_company":
        return f"{source_name[:-16]}"
    return f"sh0{segment_index}"
`

---

## Getting the List of Available Information

Use `context_info.get` to obtain information available in a context and use it to set variables. To get a list of available information for a context, add a print function to an entry in the `resolve_hook_token` hook. For example:

`python
if token_name == "<exported by>":
    # print the context info for the export context
    for key, value in context_info.items():
        print(f"{key}: {value}")
    user = context_info.get("<user>", "unknown_user")
    return f"exported_by_{user}"
`

The next time the token is selected inside the application, all the available keys will be printed to the Konsole/Terminal from which the application was started.

---

## Caching a Value

Flame does not have a caching mechanism in place to cache a value. This means that if the **Dynamic** option is enabled for a tokenized string, the application will continually try to execute the code resolving the token. Depending on the code, having multiple instances to update can greatly impact the performance of the application.

A solution to this is to add a python caching mechanism such as `@ttl_cache` or `@lru_cache` inside the `tokens_hook.py` file itself, when needed. Use the former to resolve the token at specified time intervals and the latter to cache the resolved token for an entire session.

When the python hooks are scanned, when launching the application or when using the **Rescan Python Hooks** function, the tokens are resolved once again.

---

## Warning About Longer Token Resolution

When a token takes more than 0.05 seconds to be resolved, a warning message is printed in the Konsole/Terminal from which the application was started and a message is added to the application log file.

---

## Custom Tokens Examples

Examples of how tokens can be added are available in `/opt/Autodesk/<application version>/python_utilities/examples`.

| File | Description |
|---|---|
| `custom_tokens.py` | Example of how to define and resolve custom tokens with an example of caching strategy. |

## Related pages

- Python Hooks Reference
