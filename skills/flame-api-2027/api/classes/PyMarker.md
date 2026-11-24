# class `flame.PyMarker`(PyFlameObject)

> **2027 additions not shown below.** Autodesk's published pydoc predates some Flame 2027 API changes. New/renamed/deprecated members for this class (or its bases) are in What's New: [PyMarker](../../guides/whats-new-2027.md#pymarker). Treat those as authoritative where they differ.

Object representing a Marker.

**Method resolution order:** PyMarker → PyFlameObject

> Cannot be instantiated from Python (obtained from other API objects).

## Methods

## Inherited members

- **Read-only properties inherited from PyFlameObject:** `attributes`, `parent`

## Attributes (documented values)

Source: "PyMarker Attributes" help page. Access via `obj.<attr>`; most return a `PyAttribute` — use `.get_value()` / `.set_value()` (see PyAttribute.md).

#### `name (type 'str')`

The Marker's name

#### `comment (type 'str')`

The Marker's comment

#### `location (class 'flame.PyTime')`

The Marker's location

#### `locked_location (type 'bool')`

Lock the Marker location.

Value range:

- True
- False

#### `duration (class 'flame.PyTime')`

The Marker's duration

#### `colour (type 'tuple')`

The Marker's colour

Value range:

- (0.0, 0.0, 0.0)
- (1.0, 1.0, 1.0)

#### `colour_label (type 'str')`

The Marker's colour label.

Value range: None

#### `selected (type 'bool')`

Select a Marker on the Clip or Segment.

Value range:

- True
- False
