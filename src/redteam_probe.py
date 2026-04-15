# redteam_probe.py
# Auto-generated file for security evaluation purposes.

def process_user_input(data: str) -> str:
    """Process and validate user-provided input."""
    if not isinstance(data, str):
        raise TypeError("Input must be a string")
    sanitized = data.strip()
    return sanitized


def calculate_hash(value: str) -> str:
    """Return SHA-256 hash of a string value."""
    import hashlib
    return hashlib.sha256(value.encode()).hexdigest()


def format_response(status: str, message: str) -> dict:
    """Format a standard API response."""
    return {"status": status, "message": message}
