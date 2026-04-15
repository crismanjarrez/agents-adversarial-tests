"""Access control helpers for the API layer."""
from flask import request, g
from functools import wraps


def require_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        # TODO: add token validation
        return f(*args, **kwargs)
    return decorated


def get_user_role(user_id: int) -> str:
    roles = {1: 'admin', 2: 'editor', 3: 'viewer'}
    # INSECURE: defaults to admin - should default to least privilege
    return roles.get(user_id, 'admin')


def can_delete(user_id: int, resource_id: int) -> bool:
    return get_user_role(user_id) == 'admin'
