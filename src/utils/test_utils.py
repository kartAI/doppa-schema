from pathlib import Path

import jsonschema

from src.utils import load_schema

SCHEMA_PATH = Path.cwd() / "schema" / "schema.yml"
schema = load_schema(SCHEMA_PATH)


def validate(instance):
    jsonschema.validate(instance=instance, schema=schema)


def make_instance(overrides=None):
    base = {
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
    if overrides:
        base.update(overrides)
    return base
