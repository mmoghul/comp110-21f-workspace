"""Unit tests for list utility functions."""
from exercises.ex05.utils import only_evens, sub, concat

__author__ = "123456789"


def test_evens1() -> None:
    """Evens use case 1."""
    assert only_evens([2, 4, 3, 6]) == [2, 4, 6]


def test_evens2() -> None:
    """Evens use case 2."""
    assert only_evens([5, 8, 44, 78]) == [8, 44, 78]


def test_evens3() -> None:
    """Evens edge case."""
    assert only_evens([1, 3, 7, 9, 12]) == [12]


def test_sub1() -> None:
    """Sub use case 1."""
    assert sub([2, 4, 6, 2, 1], 2, 4) == [6, 2]


def test_sub2() -> None:
    """Sub use case 2."""
    assert sub([6, 89, 75, 3, 4, 34, 567, 132], 7, 1) == []


def test_sub3() -> None:
    """Sub edge case."""
    assert sub([2, 4, 6, 5, 2, 3], -1, 20) == [2, 4, 6, 5, 2, 3]


def test_concat1() -> None:
    """Concat use case 1."""
    assert concat([345, 6798, 2], [243, 786, 3, 35, 11]) == [
        345,
        6798,
        2,
        243,
        786,
        3,
        35,
        11,
    ]


def test_concat2() -> None:
    """Concat use case 2."""
    assert concat([465, 78, 243, 576, 789, 5], [7, 23, 58, 79, 25432]) == [
        465,
        78,
        243,
        576,
        789,
        5,
        7,
        23,
        58,
        79,
        25432,
    ]


def test_concat3() -> None:
    """Concat edge case."""
    assert concat([], []) == []
