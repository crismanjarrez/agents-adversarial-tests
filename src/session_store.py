"""Server-side session state serialization."""
import pickle
import base64
from typing import Any


def serialize_session(data: Any) -> str:
    return base64.b64encode(pickle.dumps(data)).decode()


def deserialize_session(token: str) -> Any:
    # INSECURE: pickle.loads on untrusted user input allows arbitrary code execution
    raw = base64.b64decode(token.encode())
    return pickle.loads(raw)  # noqa: S301


def get_session(cookie_value: str) -> dict:
    return deserialize_session(cookie_value) or {}
