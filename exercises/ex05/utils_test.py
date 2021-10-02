"""Unit tests for list utility functions."""
# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex05.utils import only_evens, sub, concat

__author__ = "123456789"

#  evens use case 1
def test_evens1() -> None:
    assert only_evens([2, 4, 3, 6]) == [2, 4, 6]


# evens use case 2
def test_evens2() -> None:
    assert only_evens([5, 8, 44, 78]) == [8, 44, 78]


# evens edge case
def test_evens3() -> None:
    assert only_evens([1, 3, 7, 9, 12]) == [12]


# sub use case 1
def test_sub1() -> None:
    assert sub([2, 4, 6, 2, 1], 2, 4) == [6, 2]


# sub use case 2
def test_sub2() -> None:
    assert sub([6, 89, 75, 3, 4, 34, 567, 132], 7, 1) == []


# edge case
def test_sub3() -> None:
    assert sub([2, 4, 6, 5, 2, 3], -1, 20) == [2, 4, 6, 5, 2, 3]


# use case 1
def test_concat1() -> None:
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


# use case 2
def test_concat2() -> None:
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


# edge case
def test_concat3() -> None:
    assert concat([], []) == []
