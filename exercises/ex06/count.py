"""Produce a dictionary, given a list, in which  each key corresponds to a value on the list and each value is the number of times it value appeared in the input list. """


def count(l_arg: list):
    d = {}
    for l in l_arg:
        if not l in d:
            d[l] = 0
        d[l] += 1

    return d
