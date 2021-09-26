"""List utility functions."""

__author__ = "123456789"


# ________ALL__________
def all(nums: list[int], num: int) -> bool:
    """Return true if all numbers are equal, otherwise return false."""
    if len(nums) == 0:
        return False
    size = len(nums) - 1
    while size >= 0:
        if nums[size] != num:
            return False
        size -= 1
    return True


# _______IS EQUAL_______
def is_equal(n1: list[int], n2: list[int]) -> bool:
    """Return True if every element at every index is equal in both lists, else return false."""
    if len(n1) != len(n2):
        return False
    size = len(n1) - 1
    while size >= 0:
        if n1[size] != n2[size]:
            return False
        size -= 1
    return True


# _______MAX_______
def max(inp: list[int]) -> int:
    """Return max vlaue, or if list is empty, return error message."""
    if len(inp) == 0:
        raise ValueError("max() arg is an empty List")
    maximum = inp[0]
    i = 1
    while i < len(inp):
        if inp[i] > maximum:
            maximum = inp[i]
        i += 1
    return maximum