import jsonschema
import pytest

from src.utils import make_instance, validate


def test_type_feature_valid():
    instance = make_instance({"type": "Feature"})
    validate(instance)  # should not raise


def test_type_invalid_value():
    instance = make_instance({"type": "Foo"})
    with pytest.raises(jsonschema.exceptions.ValidationError):
        validate(instance)


def test_properties_can_be_object():
    instance = make_instance({"properties": {"theme": "buildings", "type": "building"}})
    validate(instance)


def test_properties_can_be_null():
    instance = make_instance({"properties": None})
    with pytest.raises(jsonschema.exceptions.ValidationError):
        validate(instance)


def test_properties_invalid_string():
    instance = make_instance({"properties": "not-an-object"})
    with pytest.raises(jsonschema.exceptions.ValidationError):
        validate(instance)


def test_geometry_can_not_be_null():
    instance = make_instance({"geometry": None})
    with pytest.raises(jsonschema.exceptions.ValidationError):
        validate(instance)


def test_geometry_invalid_type():
    instance = make_instance({
        "geometry": {"type": "Circle", "coordinates": [0, 0]}
    })
    with pytest.raises(jsonschema.exceptions.ValidationError):
        validate(instance)


def test_bbox_valid():
    instance = make_instance({"bbox": [0, 0, 1, 1]})
    validate(instance)


def test_bbox_too_short():
    instance = make_instance({"bbox": [0, 1]})
    with pytest.raises(jsonschema.exceptions.ValidationError):
        validate(instance)
