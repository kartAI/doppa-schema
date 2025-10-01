import pytest
from src.utils import validate, make_instance
import jsonschema


def test_valid_feature_update_time():
    instance = make_instance({
        "properties": {
            "theme": "buildings",
            "type": "building",
            "featureUpdateTime": "2025-10-01T12:00:00Z"
        }
    })
    validate(instance)


def test_invalid_feature_update_time_format():
    instance = make_instance({
        "properties": {
            "theme": "buildings",
            "type": "building",
            "featureUpdateTime": "01/10/2025 12:00"
        }
    })
    with pytest.raises(jsonschema.exceptions.ValidationError):
        validate(instance)
