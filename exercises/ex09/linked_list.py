"""Utility functions for working with Linked Lists."""

from __future__ import annotations
from typing import Optional

__author__ = "730465834"


class Node:
    """An item in a singly-linked list."""
    data: int
    next: Optional[Node]

    def __init__(self, data: int, next: Optional[Node]):
        """Construct a singly linked list. Use None for 2nd argument if tail."""
        self.data = data
        self.next = next

    def __str__(self) -> str:
        """Produce a string visualization of the linked list."""
        if self.next is None:
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"


def is_equal(lhs: Optional[Node], rhs: Optional[Node]) -> bool:
    """Test if two linked lists are deeply (values and order) equal to one another."""
    if lhs is None and rhs is None:
        return True
    elif lhs is None or rhs is None or lhs.data != rhs.data:
        return False
    else:
        return is_equal(lhs.next, rhs.next)


def last(head: Optional[Node]) -> int:
    """Return the last value of a linked list, or raise a ValueError if the list is empty."""
    if head is None:
        raise ValueError("last cannot be called with None")
    else:
        if head.next is None:  # base case, when end of linked list is reached 
            return head.data
        else: 
            return last(head.next)


def value_at(head: Optional[Node], index: int) -> int:
    """Return the data of the Node stored at the given index, or raise an IndexError if the index does not exist."""
    if head is None:
        raise IndexError("Index is out of bounds on the list.")
    else:
        if index == 0:
            return head.data
        else:
            index -= 1 
            return value_at(head.next, index)


def max(head: Optional[Node]) -> int:
    """Given a head Node, return the maximum data value in the linked list. If the linked list is empty, raise a ValueError."""
    # maximum: int = 0
    if head is None:
        raise ValueError("Cannot call max with None")
    # else:
    #     if head.data > max(head.next):
    #         return head.data
    #     else: 
    #         return max(head.next)
    else:
        if head.next is None:
            return head.data
        else: 
            maximum = max(head.next)
            if maximum > head.data:
                head.data = maximum 
            return head.data



def linkify(items: list[int]) -> Optional[Node]:
    """Given a list[int], return a linked list of Nodes with the same values, in the same order, as the input list."""
    if items == []:
        return None
    else:
        return Node(items[0], linkify(items[1:]))


def scale(head: Optional[Node], factor: int) -> Optional[Node]:
    """Given a head Node of a linked list and an int scaling factor, return a new linked list of Nodes where each value in the input list is multiplied by the scaling factor."""
    if head is None:
        return None
    else:
        return Node(head.data * factor, scale(head.next, factor))  # create a new node that contains the scaled data values