# """EX05 - Unit tests for utils functions."""

# __author__ = "730465834"


# from utils import only_evens, is_equal, sub

# # edge case
# def test_only_evens_empty() -> None:
#     numbers: list[int] = []
#     assert only_evens(numbers) == []  # using ==??? okay??

# def test_only_evens_multiple_items() -> None:
#     numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     assert only_evens(numbers) == [2, 4, 6, 8, 10]

# def test_ony_evens_multiple_items() -> None:
#     numbers: list[int] = [12, 8, 7, 22, 25, 30, 27]
#     assert only_evens(numbers) == [12, 8, 22, 30]


# # edge case 
# def test_is_equal_empty() -> None:
#     list_1: list[int] = []
#     list_2: list[int] = []
#     assert is_equal(list_1, list_2) == True

# # three use cases
# def test_is_equal_different_sizes() -> None:
#     list_1: list[int] = [1]
#     list_2: list[int] = [1, 2, 3, 4, 5]
#     assert is_equal(list_1, list_2) == False

# def test_is_equal_same_size() -> None:
#     list_1: list[int] = [1, 2, 3, 4, 5]
#     list_2: list[int] = [1, 2, 3, 3, 4]
#     assert is_equal(list_1, list_2) == False

# def test_is_equal_same_size_2() -> None:
#     list_1: list[int] = [4, 6, 8, 12]
#     list_2: list[int] = [4, 6, 8, 12]
#     assert is_equal(list_1, list_2) == True

# # edge cases, return empty set 
# def test_sub_bad_input() -> None:
#     numbers: list[int] = []
#     start: int = 0 
#     end: int = 3
#     assert sub(numbers, start, end) == []
    
# def test_sub_empty() -> None:
#     numbers: list[int] = [1, 2, 3, 4, 5]
#     start: int = 0
#     end: int = 0
#     assert sub(numbers, start, end) == []


# # use cases 
# def test_sub_many_items() -> None:
#     numbers: list[int] = [2, 4, 5, 6, 8]
#     start: int = 2
#     end: int = 4
#     assert sub(numbers, start, end) == [5, 6]

# def test_sub_many_items_2() -> None:
#     numbers: list[int] = [2, 7, 5, 8, 10]
#     start: int = 0
#     end: int = 5
#     assert sub(numbers, start, end) == [2, 7, 5, 8, 10]



