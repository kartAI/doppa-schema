import pytest
from src.utils import validate, make_instance
import jsonschema


def test_valid_ext_property():
    instance = make_instance({
        "properties": {
            "theme": "buildings",
            "type": "building",
            "ext_material": "concrete"
        }
    })
    validate(instance)


def test_invalid_non_ext_property():
    instance = make_instance({
        "properties": {
            "theme": "buildings",
            "type": "building",
            "material": "concrete"
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
