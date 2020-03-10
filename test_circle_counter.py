import pytest
from circle_counter import count_circles


def test_rotate():
    tests = [
        ("tests/test1.png", (3, 1)),
        ("tests/test2.png", (0, 0)),
        ("tests/test3.png", (0, 0)),
        ("tests/test4.png", (2, 3)),
    ]
    for filename, expected in tests:
        assert count_circles(filename) == expected
