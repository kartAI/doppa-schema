import pytest
from src.utils import validate, make_instance
import jsonschema


def test_valid_feature_capture_time():
    instance = make_instance({
        "properties": {
            "theme": "buildings",
            "type": "building",
            "featureCaptureTime": "2025-09-30T14:05:00Z"
        }
    })
    validate(instance)


def test_invalid_feature_capture_time_format():
    instance = make_instance({
        "properties": {
            "theme": "buildings",
            "type": "building",
            "featureCaptureTime": "30-09-2025 14:05"
        }
    })
    with pytest.raises(jsonschema.exceptions.ValidationError):
        validate(instance)
