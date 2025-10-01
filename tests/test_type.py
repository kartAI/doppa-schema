import jsonschema
import pytest

from src.utils import validate, make_instance


def test_theme_must_be_buildings():
    instance = make_instance({"properties": {"theme": "roads", "type": "building"}})
    with pytest.raises(jsonschema.exceptions.ValidationError):
        validate(instance)


def test_type_must_be_building():
    instance = make_instance({"properties": {"theme": "buildings", "type": "bridge"}})
    with pytest.raises(jsonschema.exceptions.ValidationError):
        validate(instance)
