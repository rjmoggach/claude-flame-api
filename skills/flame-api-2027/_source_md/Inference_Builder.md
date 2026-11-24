<!-- source: Autodesk Flame Family 2027 Help _ Inference Builder _ Autodesk.html -->
# Inference Builder

A great benefit of working with trained ONNX models in Autodesk Flame and Flare is being able to create your own effects, depending on your particular needs.

An .onnx file can be loaded in the Inference node. If a corresponding .json file with the same name is present in the same directory, the node will use the attributes set in that .json file rather than the default attributes. However, to simplify the sharing of trained ONNX models, it is possible to create a package containing the ONNX model and its associated JSON and thumbnail files. This package can be created using the inference_builder command line available in `/opt/Autodesk/<application version>/bin`. This creates an encrypted .inf file only a Flame Family product can read, like a Matchbox .mx file.

Here's the high-level workflow to follow when creating a .inf file:

1. Generate the default JSON file for your model.
2. Edit the JSON file to set the proper inputs, outputs, and attributes for your model.
3. Test the model in the Inference node.
4. Fix any errors in the ONNX and/or JSON files.
5. Create a thumbnail for the file. This is optional.
6. Package and encrypt the ONNX and JSON files together.

---

## Generating the JSON Sidecar File

Use a JSON file to define inputs, outputs, and attributes for a model. This is the equivalent of the XML file for a Matchbox shader. The file must have the same file name as the ONNX model and be in the same directory.

To generate a default JSON file for a model, run the `./inference_builder -j <file name of the model>` command line in `/opt/Autodesk/<application version>/bin`. The command creates a .json file with the same name of your .onnx file to the same directory. It contains the following tokens by default:

`python
{
    "ModelDescription": {
        "MinimumVersion": "2027",
        "Name": "MyModel",
        "Description": "",
        "SupportsSceneLinear": false,
        "KeepAspectRatio": true,
        "Padding": 1,
        "Inputs": [
            {
                "Name": "inputImage",
                "Description": "",
                "Type": "Front",
                "Gain": 1.0
            }
        ],
        "Outputs": [
            {
                "Name": "outputImage",
                "Description": "",
                "Type": "Result",
                "InverseGain": 1.0,
                "ScalingFactor": 1.0,
                "ColourSpace": "Z-Depth"
            }
        ]
    }
}
`

---

## Editing the JSON Sidecar File

The content of the JSON sidecar file must be edited so Flame and Flare know what the model is expecting to produce the desired output media. Additionally, you can also set the Inference Node related attributes.

Only the input and output names are extracted from the model when the JSON file is generated with the inference_builder command line. You need to specify the values for all other tokens. For example, the **ScalingFactor** token has to be properly set if the model performs an upscaling. This will prevent the software from crashing or for memory corruption to occur while running the inference.
 Note: Contrary to the Inputs, it is not necessary to have the same amount of outputs as the model. Therefore, you can remove the extra Outputs in the generated JSON file.

### Model Description Tokens

| Model Description Tokens | Type | Default Value | Description |
|---|---|---|---|
| Description | string | None | A short description of the model. This description appears in the note attached to the Inference node. |
| KeepAspectRatio | boolean | true | Specifies whether the input clip's aspect ratio must be preserved or not when performing an automatic resize. Preserving the aspect ratio causes a slight loss of precision, so it should be used only if the model requires it. |
| Minimum Version | string | N/A | The minimum software version in which this model can be loaded. |
| Name | string | The file name (without the .onnx extension) | The user-facing model name. |
| Padding | integer | 1 (no padding) | Padding must be used if the model only supports inputs of sizes that are multiple of N pixels. All inputs and outputs will automatically be padded before performing the inference. The padding is transparent to the user and does not affect the Inference node outputs. |
| SupportsSceneLinear | boolean | false | If the model does not support scene linear media, any scene linear media input will automatically be converted to log before performing the inference. The opposite conversion is performed after. |

### Inputs Tokens

| Inputs Tokens | Type | Default Value | Description |
|---|---|---|---|
| Name | string | Model input name | The corresponding input name specified in the model. |
| Type | string | Front | The input socket type. Must be one of: Front, Back, Matte, or Aux. |
| Description | string | Defined by socket type | The input socket description. This string appears in the node's input socket tooltip. |
| SocketColor | RGB 8-bit values array | Defined by socket type | The input socket colour. Uses the colour based on the input socket type by default, but can be modified. |
| Gain | float | 1.0 | All pixels are multiplied by this gain factor before performing the inference. |
| Channels | string | BGR | The input channels to be used when performing the inference. |

### Outputs Tokens

| Outputs Tokens | Type | Default Value | Description |
|---|---|---|---|
| Name | string | Model output name | The corresponding output name in the model. |
| Type | string | Result | The output socket type. Must be Result or OutMatte. |
| Description | string | Defined by socket type | The output socket description. This string appears in the node's output socket tooltip. |
| SocketColor | RGB 8-bit values array | Defined by socket type | The output socket colour. Uses the colour based on the output socket type by default, but can be modified. |
| InverseGain | float | 1.0 | All pixels are divided by this gain factor after performing the inference. |
| ScalingFactor | float | 1.0 | This token applies to upscaling or downscaling models. Determines the size of the Inference node output in relation to the input. |
| Channels | string | BGR | The channels to be output by the inference. |
| ColourSpace | string | Defined by socket type | The colour space tag of the outputted media. |

---

## Defining Channels

Channels required and output by a model can be defined on an input and output basis inside the JSON sidecar file.

### Input Channels Rule

Use the Channels token to specify the channels to be used when performing the inference. The string can be any combination of R, G, and B for inputs expecting colours or A for inputs expecting a single channel for the matte. The order of the channels affects the result. For example, BGR won't yield the same result as RGB.

If a model requires an RGBA input, you must:

1.
Declare two inputs in the JSON sidecar file.

2.
Assign the same model input to both inputs using the **Name** token.

3.
Define the channels as RGB for one input and A for the other.

In Batch, the clips connected to the two inputs will be combined and used as a single input for the model loaded in the Inference node.
 Note: The same mechanism also applies to models that, for example, require 6 channels in a single input. In this case, the JSON file must contain two RGB inputs assigned to the same model input.

### Output Channels Rule

Use the Channels token to specify which channel(s) are output by the model. This can be used to output a Matte or an image using only two channels, such as an STMap.

| Channels | Amount Value |
|---|---|
| 1 channel | Set the Channels token to "A". |
| 2 channels | Set the Channels token to either "RG" or "GR". The latter can be used to invert the result. |
| 3 channels | Set the Channels token to any 3-letter combination ("RGB", "BGR", "GBR", etc). The order of the channels affects the result. |

### Example

The following illustrates how you can define two inputs (one RGB, the other A) in an Inference node to feed the model with the required RGBA input:

`python
{
    "ModelDescription": {
        "MinimumVersion": "2027",
        "Name": "MyModel",
        "Description": "",
        "SupportsSceneLinear": false,
        "KeepAspectRatio": true,
        "Padding": 1,
        "Inputs": [
            {
                "Name": "inputImage",
                "Channels": "RGB",
                "Description": "",
                "Type": "Front",
                "Gain": 1.0
            },
            {
                "Name": "inputImage",
                "Channels": "A",
                "Description": "",
                "Type": "Matte",
                "Gain": 1.0
            }
        ],
        "Outputs": [
            {
                "Name": "outputImage",
                "Channels": "A",
                "Description": "",
                "Type": "Result",
                "InverseGain": 1.0,
                "ScalingFactor": 1.0,
                "ColourSpace": "Z-Depth"
            }
        ]
    }
}
`

---

## Adding a Thumbnail

To simplify the selection of a model inside the Load Model file browser, a thumbnail representing the effects can be included in a .inf file.

The root of the thumbnail file name must be the same as the ONNX model (`<name>.onnx.png`). The expected file resolution is 128 x 94.

---

## The `inference_builder` Command Line

To create an encrypted .inf package, run the following command line in a Konsole/Terminal: `./inference_builder -p <file name of the model>`.

The command looks for JSON and thumbnail files of the same name and package them with the ONNX model file into a single .inf file. A package is created even if one or both files can't be found.

The following options can be added to the command line:

| Option | Description |
|---|---|
| -p or --package | Creates an encrypted '.inf' package file. |
| -u or --unpack | Extracts the JSON and thumbnail (.png) files from an '.inf' package file |
| -j or --write-json | Writes the ONNX model description in a JSON file.<br><br>When running inference_builder with the -j option, a default .json file is generated in the same directory as the given ONNX model. |
| -o or --output | Outputs all files in the specified folder. The destination folder must be specified using the following syntax: • -o <path> • --output=<path> |
| -h or --help | Displays the full documentation. |

If no options are used, the content of the given ONNX model's JSON file is printed in the Konsole/Terminal.

## Related pages

- Inference
