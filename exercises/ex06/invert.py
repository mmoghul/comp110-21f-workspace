"""Invert every key and value for a given dictionary. """

# invert_dict = {'key_name':str, 'value_name': str} -> [str, str]:
#     """Switches the keys and values of a dictionary. """
#     if key_name :
#         return a
#     else:
#         return b


def invert_dict(d: dict):
    res = {}
    keys = list(d.keys())
    for k in keys:
        if keys.count(k) > 1:
            raise KeyError
        res[d[k]] = k
    return res
