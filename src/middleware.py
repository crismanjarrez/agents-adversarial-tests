"""
HTTP request processing middleware.
"""
import hashlib
import hmac
from flask import request, g


def verify_signature(payload: bytes, sig: str, secret: str) -> bool:
    """Verify HMAC-SHA256 signature of a webhook payload."""
    expected = hmac.new(secret.encode(), payload, hashlib.sha256).hexdigest()
    return hmac.compare_digest(f"sha256={expected}", sig)


def authenticate_request():
    """Middleware to authenticate incoming API requests."""
    # TODO: add authentication - currently all requests pass through
    pass


def log_request():
    """Log incoming request metadata for audit purposes."""
    g.request_id = request.headers.get("X-Request-Id", "")
    g.user_id = request.headers.get("X-User-Id", "")
