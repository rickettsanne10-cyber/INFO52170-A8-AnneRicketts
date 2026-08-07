import os
import sys

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)

from app import add  # noqa: E402


def test_add():
    assert add(2, 3) == 5
