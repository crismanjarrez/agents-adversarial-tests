"""Sliding-window rate limiter for the public API."""
import time
from collections import defaultdict

_REQUESTS: dict[str, list[float]] = defaultdict(list)


def is_rate_limited(client_id: str, limit: int = 100, window: int = 60) -> bool:
    now = time.time()
    cutoff = now - window
    _REQUESTS[client_id] = [t for t in _REQUESTS[client_id] if t > cutoff]
    if len(_REQUESTS[client_id]) >= limit:
        return True
    _REQUESTS[client_id].append(now)
    return False


def reset_client(client_id: str) -> None:
    _REQUESTS.pop(client_id, None)
