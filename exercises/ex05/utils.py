"""EX05 - 'list' utility functions."""

__author__ = "730465834"

 
def only_evens(numbers: list[int]) -> list[int]:
    """Given a list of integers, return a list of the even elements of the input list."""
    i: int = 0
    even_values: list[int] = list()
    while i < len(numbers):
        if numbers[i] % 2 == 0:  # a number modulo 2 will return 0 if said number is even 
            even_values.append(numbers[i])
        i = i + 1 

    return even_values


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Given 2 lists of integers, return True if the two lists are deeply equal to one another and False otherwise."""
    i: int = 0 
    matches: int = 0  # variable to keep track of the number of elements that are equal at the same index in both input lists
    if len(list_1) != len(list_2): 
        return False
    while i < len(list_1):
        if list_1[i] == list_2[i]:
            matches += 1  # each time there is a match at the same index, add one to the number of matches
        i += 1 
    if matches == len(list_1):  # if the number of matches is the same as the length of the list, the 2 lists are deeply equal 
        return True  
    else:
        return False 


def sub(numbers: list[int], start: int, end: int) -> list[int]:
    """Given a list of integers, a start index, and an end index, return a subset list of the input list that is between the specified start index and one less than the end index."""
    sub_list: list[int] = list()
    if start < 0:  # If the start index is negative, start from the beginning of the list.
        start = 0
    i: int = start
    if end > len(numbers):  # If the end index is greater than the length of the list, end with the end of the list.
        end = len(numbers)
    if len(numbers) == 0 or start > len(numbers) or end <= 0:  # If the length of the list is 0, start > len of the list or end <= 0, return the empty list.
        return sub_list
    while i < end: 
        sub_list.append(numbers[i])
        i += 1 

    return sub_list 