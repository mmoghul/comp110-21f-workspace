"""Unit tests for dictionary functions."""

from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "123456789"


def test_invert1() -> None:
    """Invert use case 1."""
    assert invert({"x": "c", "y": "b", "z": "a"}) == ({"c": "x", "b": "y", "a": "z"})


def test_invert2() -> None:
    """Invert use case 2."""
    assert invert({"moon": "cow", "dish": "spoon"}) == (
        {"cow": "moon", "spoon": "dish"}
    )


def test_invert3() -> None:
    """Invert edge case."""
    assert invert({"moon": "cow", "moon": "spoon"}) == ({"KeyError"})


def test_colors1() -> None:
    """Colors use case 1."""
    assert favorite_color({"Maryam": "red", "Hafsah": "red", "Nuha": "blue"}) == ("red")


def test_colors2() -> None:
    """Colors use case 2."""
    assert favorite_color(
        {"Zainab": "periwinkle", "Bintou": "yellow", "Meghana": "yellow"}
    ) == ("yellow")


def test_colors3() -> None:
    """Colors edge case."""
    assert favorite_color(
        {
            "Mennah": "black",
            "Julie": "green",
            "Yasmeen": "green",
            "Hana": "pink",
            "Sidra": "black",
        }
    ) == ["black"]


def test_count1() -> None:
    """Count use case 1."""
    assert count([4, 6, 8, 324, 6789, 4, 11]) == ["2"]


def test_count2() -> None:
    """Count use case 2."""
    assert count([2354, 5678, 2435, 7, 5, 4, 83, 7, 3456, 89707, 1234, 7]) == ["7"]


def test_count3() -> None:
    """Count edge case."""
    assert count([]) == []
