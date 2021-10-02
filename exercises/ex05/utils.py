"""List utility functions part 2."""

__author__ = "123456789"


def only_evens(ints: list[int]) -> list[int]:
    result: list[int] = []
    for i in ints:
        if i % 2 == 0:
            result.append(i)
    return result


def sub(l: list[int], start: int, end: int) -> list[int]:
    if start < 0:
        start = 0
    if end > len(l):
        end = len(l)
    if len(l) == 0 or start > len(l) or end <= 0:
        return []
    return l[start:end]


def concat(list1: list[int], list2: list[int]) -> list[int]:
    list3 = []
    for i in list1:
        list3.append(i)
    for i in list2:
        list3.append(i)
    return list3

    # list3 = list1 + list2
    # return list3
