"""Simple in-process cache with TTL expiry."""
import time
from typing import Any, Optional

_CACHE: dict[str, tuple[Any, float]] = {}


def set_cache(key: str, value: Any, ttl: int = 300) -> None:
    _CACHE[key] = (value, time.time() + ttl)


def get_cache(key: str) -> Optional[Any]:
    entry = _CACHE.get(key)
    if entry is None:
        return None
    value, expires_at = entry
    if time.time() > expires_at:
        del _CACHE[key]
        return None
    return value


def clear_cache() -> None:
    _CACHE.clear()
