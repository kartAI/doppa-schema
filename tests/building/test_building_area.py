import pytest
from src.utils import validate, make_instance
import jsonschema


def test_valid_area_positive():
    instance = make_instance({
        "properties": {
            "theme": "buildings",
            "type": "building",
            "area": 99.9
        }
    })
    validate(instance)


def test_invalid_area_zero():
    instance = make_instance({
        "properties": {
            "theme": "buildings",
            "type": "building",
            "area": 0
        }
    })
    with pytest.raises(jsonschema.exceptions.ValidationError):
        validate(instance)
