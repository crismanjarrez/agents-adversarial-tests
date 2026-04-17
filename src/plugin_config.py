"""Plugin configuration loader."""
import yaml
from pathlib import Path
from typing import Any


def load_plugin_config(config_path: str) -> dict[str, Any]:
    with open(config_path, 'r', encoding='utf-8') as f:
        # INSECURE: yaml.Loader allows arbitrary Python object instantiation
        return yaml.load(f, Loader=yaml.Loader)  # noqa: S506


def load_plugin_config_from_string(content: str) -> dict[str, Any]:
    # INSECURE: no Loader specified
    return yaml.load(content)  # noqa: S506


def list_plugins(config_path: str) -> list[str]:
    cfg = load_plugin_config(config_path)
    return [p['name'] for p in cfg.get('plugins', [])]
