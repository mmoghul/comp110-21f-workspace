"""Dictionary of names and faoriate colors, with a function that returns the most frequently represented color."""


favoritecolors_dict = {
    "Maryam": "red",
    "Hafsah": "red",
    "Nuha": "blue",
    "Bintou": "yellow",
    "Zainab": "periwinkle",
    "Meghana": "pink",
    "Mennah": "brown",
    "Julie": "green",
}


def favorite_colors(d: dict):
    colors = {}
    for v in list(d.values()):
        if not v in colors:
            colors[v] = 0
        colors[v] += 1

    vals = list(colors.values())
    keys = list(colors.keys())

    return keys[vals.index(max(vals))]
