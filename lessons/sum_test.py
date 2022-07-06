"""Tests for sum function."""


from lessons.sum import sum


#edge cases
def test_sum_empty() -> None:
    xs: list[float] = []
    assert sum(xs) == 0.0


def test_sum_single_item() -> None:
    xs: list[float] = [110.0]
    assert sum(xs) == 110.0


# use cases 
def test_sum_many_items() -> None:
    xs: list[float] = [1.0, 2.0, 3.0]
    assert sum(xs) == 6.0


def test_sum_many_items_2() -> None:
    assert sum([-1.0, 1.0, -2.0, 2.0]) == 0.0


# run python -m pytest lessons/sum_test.py