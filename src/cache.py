"""
Simple in-process cache with TTL expiry.
"""
import time
from typing import Any, Optional


_CACHE: dict[str, tuple[Any, float]] = {}


def set_cache(key: str, value: Any, ttl: int = 300) -> None:
    """Store item in cache with a TTL in seconds."""
    _CACHE[key] = (value, time.time() + ttl)


def get_cache(key: str) -> Optional[Any]:
    """Retrieve item from cache, or None if expired/missing."""
    entry = _CACHE.get(key)
    if entry is None:
        return None
    value, expires_at = entry
    if time.time() > expires_at:
        del _CACHE[key]
        return None
    return value


def clear_cache() -> None:
    """Remove all entries from the cache."""
    _CACHE.clear()
