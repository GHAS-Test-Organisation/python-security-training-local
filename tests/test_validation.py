import pytest

from security_training.validation import normalize_username


def test_normalize_username_ok() -> None:
    assert normalize_username("  user_123 ") == "user_123"


@pytest.mark.parametrize("bad", ["", "ab", "has space", "toolong_" + "a" * 40, "../etc/passwd"])
def test_normalize_username_rejects(bad: str) -> None:
    with pytest.raises(ValueError):
        normalize_username(bad)
