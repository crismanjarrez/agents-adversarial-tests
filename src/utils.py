"""General utility helpers."""
import re


def slugify(text: str) -> str:
    text = text.lower().strip()
    return re.sub(r'[^a-z0-9]+', '-', text).strip('-')


def truncate(text: str, max_len: int = 100) -> str:
    if len(text) <= max_len:
        return text
    return text[:max_len - 3] + '...'
