# class `flame.PyCoCompass`(PyCoNode)

Class derived from PyCoNode. This class represents the compass node in the Action schematic.

**Method resolution order:** PyCoCompass → PyCoNode → PyFlameObject

> Cannot be instantiated from Python (obtained from other API objects).

## Methods

## Read-only properties defined here

### `nodes`

Return a list of PyCoNode objects enclosed by the Compass node.

## Inherited members

- **Static methods inherited from PyCoNode:** `add_reference`, `assign_media`, `cache_range`, `children`, `parents`
- **Read-only properties inherited from PyCoNode:** `type`
- **Read-only properties inherited from PyFlameObject:** `attributes`, `parent`

## Attributes (documented values)

Source: "PyCoCompass Attributes" help page. Access via `obj.<attr>`; most return a `PyAttribute` — use `.get_value()` / `.set_value()` (see PyAttribute.md).

#### `name (type 'str')`

The name of the Action node in the Action schematic.

Value range: None

#### `position (type 'tuple')`

The XYZ position of the Action node in the Action 3D space.

Value range:

- (-3.4028234663852886e+38, -3.4028234663852886e+38, -3.4028234663852886e+38)
- (3.4028234663852886e+38, 3.4028234663852886e+38, 3.4028234663852886e+38)

#### `selected (type 'bool')`

The Action node is selected.

Value range:

- True
- False

#### `collapsed_in_manager (type 'bool')`

The Action node is collapsed in the Action Manager

Value range:

- True
- False

#### `colour (type 'tuple')`

The Colour attribute of the Compass node.

Value range:

- (0.0, 0.0, 0.0)
- (1.0, 1.0, 1.0)

#### `width (type 'int')`

The Width attribute of the Compass node.

Value range:

- Min: 1.0
- Max: 10000.0

#### `height (type 'int')`

The Height attribute of the Compass node.

Value range:

- Min: 1.0
- Max: 10000.0
