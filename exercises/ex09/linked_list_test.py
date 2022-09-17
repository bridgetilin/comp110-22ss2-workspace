"""Tests for linked list utils."""

import pytest
from exercises.ex09.linked_list import Node, last, value_at, max, linkify, scale

__author__ = "Your PID"


def test_last_empty() -> None:
    """Last of an empty Linked List should raise a ValueError."""
    with pytest.raises(ValueError):
        last(None)


def test_last_non_empty() -> None:
    """Last of a non-empty list should return its last data value."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert last(linked_list) == 3


def test_value_at_empty() -> None:
    """Test for value_at function on an empty linked list."""
    with pytest.raises(IndexError):
        value_at(None, 0)


def test_value_at_index_out_of_bounds() -> None:
    """Test for value_at function with an out of range index."""
    with pytest.raises(IndexError):
        value_at(Node(1, Node(2, Node(3, None))), 4)


def test_value_at_non_empty() -> None:
    """Test for value_at function called on non-empty linked list."""
    linked_list = Node(1, Node(10, Node(100, Node(1000, None))))
    index: int = 2
    assert value_at(linked_list, index) == 100


def test_max_empty() -> None:
    """Test for max function called on an empty linked."""
    with pytest.raises(ValueError):
        max(None)


def test_max_non_empty() -> None:
    """Test for max function called on a non-empty linked list."""
    head = Node(10, Node(100, Node(37, None)))
    assert max(head) == 100


def test_linkify_empty() -> None:
    """Test for linkify function called on an empty list."""
    items: list[int] = []
    assert linkify(items) is None


def test_linkify_1_item() -> None:
    """Test for linkify function on a single-item list."""
    items: list[int] = [1]
    assert str(linkify(items)) == "1 -> None"  # convert to str to match output of linkify


def test_linkify_multiple_items() -> None:
    """Test for linkify function on a multi-item list."""
    items: list[int] = [1, 2, 3, 4, 5]
    assert str(linkify(items)) == "1 -> 2 -> 3 -> 4 -> 5 -> None"


def test_scale_empty() -> None:
    """Test for scale function called on an empty linked list."""
    head = None
    factor: int = 1
    assert scale(head, factor) is None


def test_scale_non_empty() -> None:
    """Test for scale function on a non-empty linked list and with a valid scaling factor."""
    head = linkify([10, 100, 1000])
    factor: int = 2
    assert str(scale(head, factor)) == "20 -> 200 -> 2000 -> None"