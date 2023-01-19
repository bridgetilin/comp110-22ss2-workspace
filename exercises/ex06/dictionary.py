"""EX06 - Dictionary Functions."""

__author__ = "730465834"


def invert(dict_1: dict[str, str]) -> dict[str, str]:
    """Given a dict[str, str], return a dict[str, str] that inverts the keys and values."""
    inverted_dict_1: dict[str, str] = {}
    for key in dict_1:
        # if dict_1[key] in inverted_dict_1:
            # raise KeyError("")
            
        inverted_dict_1[dict_1[key]] = key

    if len(dict_1) != len(inverted_dict_1):  # if the number of key-value pairings is not the same before and after the inversion, this indicates the existence of one or more duplicate keys
        raise KeyError("The same key was encountered more than once in the inverted dictionary.")

    return inverted_dict_1 


def favorite_color(favs: dict[str, str]) -> str:
    """Given a dictionary of names and favorite colors, return the color that appeared most frequently."""
    color_count: dict[str, int] = {}
    for name in favs:
        if favs[name] in color_count:  # if the color already exists in the color_count dictionary, add one to the value associated with the color key
            color_count[favs[name]] += 1
        else:
            color_count[favs[name]] = 1

    greatest_count: int = 0  # counting variable to keep track of the value associated with the color that appears most frequently 
    favorite: str = ""
    for color in color_count:  
        if color_count[color] > greatest_count:
            greatest_count = color_count[color]  # reassign greatest_count variable if a greater value is encountered in the color_count dictionary 
            favorite = color 
    return favorite
    

def count(items: list[str]) -> dict[str, int]:
    """Given a list[str], return a dict[str, int] that contains the items of the input the list and the associated number of times each item appeared."""
    item_count: dict[str, int] = {}
    for item in items:
        if item in item_count:
            item_count[item] += 1
        else: 
            item_count[item] = 1 
    
    return item_count