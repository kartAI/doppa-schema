import jsonschema
import pytest

from src.utils import make_instance, validate


def test_geometry_polygon_valid():
    instance = make_instance({
        "geometry": {
            "type": "Polygon",
            "coordinates": [[[0, 0], [1, 0], [1, 1], [0, 1], [0, 0]]]
        }
    })
    validate(instance)


def test_geometry_multipolygon_valid():
    instance = make_instance({
        "geometry": {
            "type": "MultiPolygon",
            "coordinates": [[[[0, 0], [1, 0], [1, 1], [0, 1], [0, 0]]]]
        }
    })
    validate(instance)


def test_geometry_invalid_type():
    instance = make_instance({
        "geometry": {"type": "LineString", "coordinates": [[0, 0], [1, 1]]}
    })
    with pytest.raises(jsonschema.exceptions.ValidationError):
        validate(instance)
