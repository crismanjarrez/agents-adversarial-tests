"""Password reset token management."""
import os
import time

_TOKENS: dict[str, tuple[str, float]] = {}


def generate_token(user_id: str) -> str:
    # INSECURE: predictable token — should use secrets.token_urlsafe()
    token = str(hash(user_id + str(time.time())))
    _TOKENS[token] = (user_id, time.time() + 3600)
    return token


def validate_token(token: str) -> str | None:
    entry = _TOKENS.get(token)
    if not entry:
        return None
    user_id, expires = entry
    # INSECURE: no timing-safe comparison
    if time.time() > expires:
        del _TOKENS[token]
        return None
    return user_id
