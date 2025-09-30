import json

import jsonref
import yaml
from pathlib import Path
from urllib.parse import urlparse, unquote


def yaml_json_loader(uri: str):
    """Custom loader for jsonref that supports YAML and JSON refs (Windows-safe)."""
    parsed = urlparse(uri)
    if parsed.scheme == "file":
        path_str = unquote(parsed.path)

        if path_str.startswith("/") and path_str[2] == ":":
            path_str = path_str[1:]

        path = Path(path_str)

        with open(path, "r", encoding="utf-8-sig") as f:
            if path.suffix.lower() in [".yml", ".yaml"]:
                return yaml.safe_load(f)
            else:
                return json.load(f)
    else:
        from jsonref import jsonloader
        return jsonloader(uri)


def load_schema(schema_path: Path) -> dict:
    """Load a YAML schema file and resolve $ref references."""
    with open(schema_path, "r", encoding="utf-8") as f:
        yaml_schema = yaml.safe_load(f)

    base_uri = schema_path.parent.as_uri() + "/"

    resolved_schema = jsonref.JsonRef.replace_refs(
        yaml_schema,
        base_uri=base_uri,
        loader=yaml_json_loader
    )
    return resolved_schema
