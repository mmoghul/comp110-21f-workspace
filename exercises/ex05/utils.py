"""List utility functions part 2."""

__author__ = "123456789"


def only_evens(ints: list[int]) -> list[int]:
    """Function only returns even vlaues of list."""
    result: list[int] = []
    for i in ints:
        if i % 2 == 0:
            result.append(i)
    return result


def sub(list_arg: list[int], start: int, end: int) -> list[int]:
    """Function generate list which is a subset of the given list, between the  start index and end index."""
    if start < 0:
        start = 0
    if end > len(list_arg):
        end = len(list_arg)
    if len(list_arg) == 0 or start > len(list_arg) or end <= 0:
        return []
    return list_arg[start:end]


def concat(list1: list[int], list2: list[int]) -> list[int]:
    """Generates new List which contains all of the elements of the first list followed by all of the elements of the second list."""
    list3 = []
    for i in list1:
        list3.append(i)
    for i in list2:
        list3.append(i)
    return list3

    # list3 = list1 + list2
    # return list3
