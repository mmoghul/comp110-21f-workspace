"""List utility functions."""

__author__ = "123456789"

# ________ALL__________


def all(l: int, num: int) -> bool:
    size = len(l) - 1
    while size >= 0:
        if l[size] != num:
            return False
        size -= 1
    return True
    """return true if all numbers are equal, otherwise return false"""


# _______IS EQUAL_______


def is_equal(n1: list[int], n2: list[int]) -> bool:
    if len(n1) != len(n2):
        return False
    size = len(n1) - 1
    while size >= 0:
        if n1[size] != n2[size]:
            return False
        size -= 1
    return True


# _______MAX_______


def max(input: list[int]) -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    maximum = input[0]
    i = 1
    while i < len(input):
        if input[i] > maximum:
            maximum = input[i]
    return input[i]


def main():
    max([56, 863, 33])
    is_equal([543, 907, 123], [534543, 98, 1])


if __name__ == "__main__":
    main()
