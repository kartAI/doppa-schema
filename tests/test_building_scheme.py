import jsonschema
import pytest

from src.utils import validate, make_instance


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


def test_theme_must_be_buildings():
    instance = make_instance({"properties": {"theme": "roads", "type": "building"}})
    with pytest.raises(jsonschema.exceptions.ValidationError):
        validate(instance)


def test_type_must_be_building():
    instance = make_instance({"properties": {"theme": "buildings", "type": "bridge"}})
    with pytest.raises(jsonschema.exceptions.ValidationError):
        validate(instance)


def test_level_integer_valid():
    instance = make_instance({"properties": {"theme": "buildings", "type": "building", "level": 3}})
    validate(instance)


def test_level_invalid_string():
    instance = make_instance({"properties": {"theme": "buildings", "type": "building", "level": "three"}})
    with pytest.raises(jsonschema.exceptions.ValidationError):
        validate(instance)


def test_building_type_valid():
    instance = make_instance({"properties": {"theme": "buildings", "type": "building", "buildingType": 200}})
    validate(instance)


def test_building_type_zero_invalid():
    instance = make_instance({"properties": {"theme": "buildings", "type": "building", "buildingType": 0}})
    with pytest.raises(jsonschema.exceptions.ValidationError):
        validate(instance)


def test_building_type_negative_invalid():
    instance = make_instance({"properties": {"theme": "buildings", "type": "building", "buildingType": -5}})
    with pytest.raises(jsonschema.exceptions.ValidationError):
        validate(instance)


def test_area_and_length_valid():
    instance = make_instance({
        "properties": {
            "theme": "buildings",
            "type": "building",
            "level": 1,
            "buildingType": 101,
            "area": 123.4,
            "length": 56.7
        }
    })
    validate(instance)


def test_area_zero_invalid():
    instance = make_instance({
        "properties": {
            "theme": "buildings",
            "type": "building",
            "buildingType": 101,
            "area": 0
        }
    })
    with pytest.raises(jsonschema.exceptions.ValidationError):
        validate(instance)


def test_length_negative_invalid():
    instance = make_instance({
        "properties": {
            "theme": "buildings",
            "type": "building",
            "buildingType": 101,
            "length": -10
        }
    })
    with pytest.raises(jsonschema.exceptions.ValidationError):
        validate(instance)


def test_ext_prefixed_property_valid():
    instance = make_instance({
        "properties": {
            "theme": "buildings",
            "type": "building",
            "buildingType": 101,
            "ext_custom": "ok"
        }
    })
    validate(instance)


def test_non_ext_property_invalid():
    instance = make_instance({
        "properties": {
            "theme": "buildings",
            "type": "building",
            "buildingType": 101,
            "custom": "bad"
        }
    })
    with pytest.raises(jsonschema.exceptions.ValidationError):
        validate(instance)
