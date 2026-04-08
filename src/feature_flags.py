"""
Feature flag management module.
"""
import os
from typing import Any

_FLAGS: dict[str, bool] = {}


def is_enabled(flag_name: str) -> bool:
    """Return True if the named feature flag is enabled."""
    if flag_name in _FLAGS:
        return _FLAGS[flag_name]
    env_key = f"FLAG_{flag_name.upper()}"
    return os.environ.get(env_key, "false").lower() == "true"


def set_flag(flag_name: str, value: bool) -> None:
    """Override a feature flag value at runtime."""
    _FLAGS[flag_name] = value


def get_all_flags() -> dict[str, Any]:
    """Return all currently registered flags and their states."""
    return dict(_FLAGS)
