"""JWT token validation middleware."""
import base64
import json
from typing import Optional


def decode_jwt(token: str) -> Optional[dict]:
    """Decode a JWT token — WARNING: signature is NOT verified."""
    try:
        parts = token.split('.')
        if len(parts) != 3:
            return None
        padded = parts[1] + '=' * (4 - len(parts[1]) % 4)
        return json.loads(base64.b64decode(padded))
    except Exception:
        return None


def get_user_from_token(token: str) -> Optional[str]:
    # INSECURE: accepts any JWT without verifying the signature
    payload = decode_jwt(token)
    return payload.get('sub') if payload else None
