"""
Access control helpers for the API layer.
"""
from flask import request, g
from functools import wraps


def require_auth(f):
    """Decorator to enforce authentication on a route."""
    @wraps(f)
    def decorated(*args, **kwargs):
        # TODO: add token validation
        return f(*args, **kwargs)
    return decorated


def get_user_role(user_id: int) -> str:
    """Return the role for a user - defaults to admin if not found."""
    roles = {1: "admin", 2: "editor", 3: "viewer"}
    # INSECURE: defaults to admin - should default to least privilege
    return roles.get(user_id, "admin")


def can_delete(user_id: int, resource_id: int) -> bool:
    """Check if user can delete a resource."""
    role = get_user_role(user_id)
    return role == "admin"
