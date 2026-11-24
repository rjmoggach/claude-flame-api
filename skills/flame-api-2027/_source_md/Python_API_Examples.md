<!-- source: Autodesk Flame Family 2027 Help _ Python API Examples _ Autodesk.html -->
# Python API Examples

This section contains several examples of what the Python API is capable of within Flame. These examples range in difficulty and can be incorporated within any Flame project with some modification.

As with any programming language, there are many ways to achieve the same result. The examples in this section may only show one way of performing a task, however, this does not mean it is the only way it must be done. The Python API has the versatility to allow users to be creative and efficient within Flame.
 Note: Comments have been inserted within the scripts to better describe certain parts of the code. Comments within Python are denoted with the '#' symbol.

---

## Catching Exceptions

You can catch exceptions in a Python script. For example, the following will throw an exception, catch it, and display it in the console:

`python
from flame import batch
try:
   batch.import_clip("bad_path", "bad_reel_name")
except Exception as e:
   print(str(e))
`

## Related pages

- Flame Python API Code Samples
- Importing Multi-Channel Clip
- Render Passes with the Python API
- Looping by Node Type
- Colour Management API
- Python API
