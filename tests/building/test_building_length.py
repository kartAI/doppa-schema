import pytest
from src.utils import validate, make_instance
import jsonschema


def test_valid_length_positive():
    instance = make_instance({
        "properties": {
            "theme": "buildings",
            "type": "building",
            "length": 30.5
        }
    })
    validate(instance)


def test_invalid_length_negative():
    instance = make_instance({
        "properties": {
            "theme": "buildings",
            "type": "building",
            "length": -12.3
        }
    })
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



