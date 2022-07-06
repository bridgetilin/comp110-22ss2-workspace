"""EX06 - Unit Tests for Dictionary Functions."""

__author__ = "730465834"

 
from dictionary import invert, favorite_color, count


# Unit tests for invert function
# Edge case
def test_invert_empty() -> None:
    """Test to confirm that given the empty dictionary, the invert function returns the empty dictionary."""
    dict_1: dict[str, str] = {}
    assert invert(dict_1) == {}


# Use cases
def test_invert_grocery_stores() -> None:
    """Test for proper inversion of a dict[str, str] containing 2-word grocery store names using the invert function."""
    dict_1: dict[str, str] = {"Trader": "Joes", "Whole": "Foods", "Harris": "Teeter", "Food": "Lion"}
    assert invert(dict_1) == {"Joes": "Trader", "Foods": "Whole", "Teeter": "Harris", "Lion": "Food"}


def test_invert_names() -> None:
    """Test for proper inversion of a dict[str, str] containing first and last name pairings using the invert function."""
    dict_1: dict[str, str] = {"Shawn": "Spencer", "Burton": "Guster", "Carlton": "Lassiter", "Juliet": "O'Hara"}
    assert invert(dict_1) == {"Spencer": "Shawn", "Guster": "Burton", "Lassiter": "Carlton", "O'Hara": "Juliet"}


# Unit tests for favorite_color function
# Edge cases 
def test_favorite_color_empty() -> None:
    """Test to confirm that given the empty dictionary, the favorite_color function returns the empty string."""
    favs: dict[str, str] = {}
    assert favorite_color(favs) == ""


def test_favorite_color_one_name() -> None:
    """Test for favorite_color function on a single item dictionary."""
    favs: dict[str, str] = {"Bridget": "Blue"}
    assert favorite_color(favs) == "Blue"


# Use cases
def test_favorite_color_one_favorite() -> None:
    """Test for proper return of a decisive overall favorite color in a multi-item dictionary using the favorite_color function."""
    favs: dict[str, str] = {"Bridget": "Blue", "Bob": "Pink", "Brad": "Blue", "Bella": "Pink", "Becky": "Yellow", "Betty": "Pink"}
    assert favorite_color(favs) == "Pink"


def test_favorite_color_tie() -> None:
    """Test for proper return of an overall favorite color when there is a tie using the favorite_color function."""
    favs: dict[str, str] = {"Bridget": "Blue", "Bob": "Pink", "Brad": "Blue", "Bella": "Pink", "Becky": "Yellow", "Betty": "Pink", "Brenda": "Blue"}
    assert favorite_color(favs) == "Blue"


# Unit tests for count function
# Edge case
def test_count_empty() -> None: 
    """Test to confirm that given the empty list, the count function returns the empty dictionary."""
    items: list[str] = []
    assert count(items) == {}


# Use cases
def test_count_names() -> None:
    """Test for proper return of a dict[str, int] from count function that counts the number of times each name appeared in an input list."""
    items: list[str] = ["Bridget", "Bob", "Betty", "Bob", "Brad"]
    assert count(items) == {"Bridget": 1, "Bob": 2, "Betty": 1, "Brad": 1}


def test_count_tv_shows() -> None:
    """Test for proper return of a dict[str, int] from count function that counts the number of times each tv show appeared in an input list."""
    items: list[str] = ["Friends", "Psych", "New Girl", "New Girl", "Psych", "HIMYM", "New Girl"]
    assert count(items) == {"Friends": 1, "Psych": 2, "New Girl": 3, "HIMYM": 1}   