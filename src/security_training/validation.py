from __future__ import annotations

import re


_USERNAME_RE = re.compile(r"^[a-zA-Z0-9_]{3,32}$")


def normalize_username(value: str) -> str:
    if value is None:
        raise TypeError("value must not be None")

    cleaned = value.strip()
    if not _USERNAME_RE.match(cleaned):
        raise ValueError("invalid username format")

    return cleaned
