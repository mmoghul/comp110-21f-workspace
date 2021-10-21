"""Practice with dictionaries."""

__author__ = "123456789"


def invert(d: dict[str, str]) -> dict[str, str]:
    res = {}
    keys = list(d.keys())
    for k in keys:
        if keys.count(k) > 1:
            raise KeyError
        res[d[k]] = k
    return res


def favorite_color(d: dict[str, str]) -> dict[str, str]:
    colors = {}
    for v in list(d.values()):
        if v not in colors:
            colors[v] = 0
        colors[v] += 1

    vals = list(colors.values())
    keys = list(colors.keys())

    return keys[vals.index(max(vals))]


def count(l_arg: list):
    d = {}
    for l in l_arg:
        if l not in d:
            d[l] = 0
        d[l] += 1

    return d
