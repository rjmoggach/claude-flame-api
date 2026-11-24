<!-- source: Autodesk Flame Family 2027 Help _ Python Console and how to Execute Scripts _ Autodesk.html -->
# Python Console and how to Execute Scripts

Accessible from the Flame menu, the Flame Python Console is your main tool when using the Python API. It allows you to write, edit, and run code, while being able to view the console output. The major parts are discussed in this section.

Console windows:

-
Terminal Window: This is where any output from your code will be shown. The terminal is useful when debugging an error, you will get a detailed report of the error within the console (in a red font). This is also the place where any "print()" command or any calls to the help() function will be output.

-
Editor Window: The Editor window is a simple text editor used to write or edit your Python scripts. The editor has the feature of being able to have multiple tabs of Python Script files; you can access the multiple tabs underneath the editor's window. To create a new tab, simply click the 'plus' (+) sign in the bottom right corner of the Python Console.

| Icon | Name | Description |
|---|---|---|
| [image: Eraser] | Eraser | Clears all output in the terminal window |
| [image: Sound Wave] | Sound Wave | Choose whether the Python code that is executed will be displayed within the terminal (Will output when icon is Blue) |
| [image: Play Button] | Play Button | Executes all code within the current tab of the editor window or selected code segments |
| [image: Save] | Save | Prompts user to save the script in the current tab of the editor |
| [image: Load] | Load | Prompts user to load a Script which will become a new tab in the editor |
| [image: Eraser] | Eraser | Clears all code within the current tab of the editor |
| [image: Line Number Indicator] | Line Number Indicator | Toggling this button will show or hide line numbers within the editor (Line numbers will be visible when icon is blue) |

---

## Executing Scripts

There are two ways to execute Python API scripts in Flame.

The Python API allows a user to run a script when the project is loaded by defining what script should be run when starting flame from the command line.

Running a script at Startup

1.
Launch Flame from the command line with `/opt/Autodesk/<version>/bin/startApplication`

2.
To define a script to be ran at startup, append the -s argument to the `startApplication` command and then include a valid path to a valid Python script.

Example: `/opt/Autodesk/<version>/bin/startApplication -s /home/user/scripts/onStart.py`

 Note: A Valid Python script must start with "import flame" otherwise the script will not work.

There are two ways to execute code from within the Python Console.

Running a script from the console:

-
By Script: Clicking the 'Play' button within the Python Console will run the entire script (start to finish) that is open in the current tab of the Editor.

-
By Selection: With a section of the script highlighted, using the 'Play' button within the Python Console will only execute the selected parts of the code.

 Important: When working in the Python Console, the "import flame" command must only be declared once per tab. Once declared, a single line can be highlighted and executed without the need of another "import flame" command.

## Related pages

- Python API
