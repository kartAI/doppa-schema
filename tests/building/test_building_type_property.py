import pytest
from src.utils import validate, make_instance
import jsonschema


def test_valid_building_type():
    instance = make_instance({
        "properties": {
            "theme": "buildings",
            "type": "building",
            "buildingType": 150
        }
    })
    validate(instance)


def test_invalid_building_type_negative():
    instance = make_instance({
        "properties": {
            "theme": "buildings",
            "type": "building",
            "buildingType": -1
        }
    })
    with pytest.raises(jsonschema.exceptions.ValidationError):
        validate(instance)


def test_building_type_zero_invalid():
    instance = make_instance({"properties": {"theme": "buildings", "type": "building", "buildingType": 0}})
    with pytest.raises(jsonschema.exceptions.ValidationError):
        validate(instance)
