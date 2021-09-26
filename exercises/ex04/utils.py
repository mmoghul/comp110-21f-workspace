"""List utility functions."""

__author__ = "123456789"

# ________ALL__________


def all(nums: list, num: int) -> bool:
 """return true if all numbers are equal, otherwise return false"""
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
"""return True if every element at every index is equal in both lists, else return false"""
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
"""return max vlaue, or if list is empty, return error message"""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    maximum = input[0]
    i = 1
    while i < len(input) - 1:
        if input[i] > maximum:
            maximum = input[i]
        i += 1
    return input[i]


def main():
    max([56, 863, 33])
    is_equal([543, 907, 123], [534543, 98, 1])


if __name__ == "__main__":
    main()
