import jsonschema
import pytest

from src.utils import validate, make_instance


def test_valid_uuid_v4():
    instance = make_instance({"id": "550e8400-e29b-41d4-a716-446655440000"})  # valid UUID v4
    validate(instance)  # should not raise


def test_invalid_uuid_v1():
    instance = make_instance({"id": "123e4567-e89b-12d3-a456-426614174000"})  # UUID v1
    with pytest.raises(jsonschema.exceptions.ValidationError):
        validate(instance)


def test_invalid_uuid_too_short():
    instance = make_instance({"id": "550e8400-e29b-41d4-a716-44665544"})  # missing chars
    with pytest.raises(jsonschema.exceptions.ValidationError):
        validate(instance)


def test_invalid_uuid_uppercase():
    instance = make_instance({"id": "550E8400-E29B-41D4-A716-446655440000"})  # uppercase not allowed
    with pytest.raises(jsonschema.exceptions.ValidationError):
        validate(instance)


def test_invalid_uuid_wrong_variant():
    instance = make_instance({"id": "550e8400-e29b-41d4-c716-446655440000"})  # 'c' not allowed in variant
    with pytest.raises(jsonschema.exceptions.ValidationError):
        validate(instance)


def test_valid_building():
    instance = {
        "type": "Feature",
        "id": "550e8400-e29b-41d4-a716-446655440000",
        "geometry": {
            "type": "Polygon",
            "coordinates": [[[0, 0], [1, 0], [1, 1], [0, 1], [0, 0]]]
        },
        "properties": {
            "theme": "buildings",
            "type": "building",
            "level": 1,
            "buildingType": 101
        }
    }

    validate(instance)  # should not raise


def test_wrong_theme_triggers_else():
    instance = {
        "type": "Feature",
        "id": "123e4567-e89b-12d3-a456-426614174000",
        "geometry": {
            "type": "Polygon",
            "coordinates": [[[0, 0], [1, 0], [1, 1], [0, 1], [0, 0]]]
        },
        "properties": {
            "theme": "roads",
            "type": "road"
        }
    }
    with pytest.raises(jsonschema.ValidationError):
        validate(instance)
