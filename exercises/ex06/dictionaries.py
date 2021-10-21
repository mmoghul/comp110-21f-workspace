"""Practice with dictionaries."""

__author__ = "123456789"


def invert(d: dict[str, str]) -> dict[str, str]:
    res = {}
    keys = list(d.keys())
    for k in keys:
        if keys.count(k) > 1:
            raise KeyError("More than one of the same key!")
        res[d[k]] = k
    return res


def favorite_color(d: dict[str, str]) -> [str]:
    colors = {}
    for v in list(d.values()):
        if v not in colors:
            colors[v] = 0
        colors[v] += 1

    vals = list(colors.values())
    keys = list(colors.keys())

    return keys[vals.index(max(vals))]


def count(l_arg: list[str]) -> dict[str, int]:
    res = {}
    for current in l_arg:
        if current not in res:
            res[current] = 0
        res[current] += 1

    return res
