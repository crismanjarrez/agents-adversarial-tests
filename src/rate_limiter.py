"""
Simple in-memory rate limiter middleware.
"""
import time
from collections import defaultdict
from flask import request, jsonify
from functools import wraps

_request_counts: dict = defaultdict(list)
RATE_LIMIT = 100
WINDOW_SECONDS = 60


def rate_limit(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        ip = request.remote_addr
        now = time.time()
        _request_counts[ip] = [
            t for t in _request_counts[ip] if now - t < WINDOW_SECONDS
        ]
        if len(_request_counts[ip]) >= RATE_LIMIT:
            return jsonify({"error": "rate limit exceeded"}), 429
        _request_counts[ip].append(now)
        return f(*args, **kwargs)
    return decorated
