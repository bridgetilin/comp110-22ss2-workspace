from __future__ import annotations

from typing import Union, Optional


class Node:
    data: int
    next: Optional[Node]
    
    def __init__(self, data: int, next: Optional[Node]): 
        self.data = data
        self.next = next
    
    def __str__(self) -> str:
        """Produces a string representation of a Node."""
        if self.next == None:
            return f"{self.data} -> None"
        else: 
            return f"{self.data} -> {self.next}"

# head: Node = Node(1, None)
# tail: Node = Node(2, None)
# head.next = tail

# procedural recursion 
# def sum(node: Node) -> int:
#     if node.next is None:  # can use == or is when equating to None
#         return node.data
#     else:
#         return node.data + sum(node.next)

def sum(node: Optional[Node]) -> int:
    if node is None:  # can use == or is when equating to None, no longer node.next becuase we have optional node, could be node or none
        return 0 
    else:
        return node.data + sum(node.next)  # at the end we will read a node.next = none, so plus 0


# def count(node: Node, current_count: int = 0) -> int:
#     """Return the number of nodes in a linked list."""
#     if node.next is None:  # base case
#         return current_count + 1 
#     else:
#         return count(node.next, current_count + 1)
    
def count(node: Optional[Node], current_count: int = 0) -> int:
    if node is None:
        return current_count
    else:
        return count(node.next, current_count + 1)

# recursive structure
head: Node = Node(3, None)
head: Node = Node(2, head)
head = Node(1, head)
print(sum(head))
print(count(head))
print(head)
head_2: Node = Node(1, None)
print(count(head_2))
    
