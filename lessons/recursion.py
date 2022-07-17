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
    if node is None:  # can use == or is when equating to None
        return 0 
    else:
        return node.data + sum(node.next)


def count(node: Node, current_count: int = 0) -> int:
    """Return the number of nodes in a linked list."""
    if node.next is None:  # base case
        return current_count + 1 
    else:
        return count(node.next, current_count + 1)
    

# recursive structure
head: Node = Node(3, None)
head: Node = Node(2, head)
head = Node(1, head)
print(sum(head))
print(count(head))
print(head)

    
