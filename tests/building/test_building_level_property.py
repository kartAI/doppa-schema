import pytest
from src.utils import validate, make_instance
import jsonschema


def test_level_integer_valid():
    instance = make_instance({"properties": {"theme": "buildings", "type": "building", "level": 3}})
    validate(instance)


def test_level_invalid_string():
    instance = make_instance({"properties": {"theme": "buildings", "type": "building", "level": "three"}})
    with pytest.raises(jsonschema.exceptions.ValidationError):
        validate(instance)
