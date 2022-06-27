"""Challenge Question 3"""
def silly(n: int) -> str:
    """A silly function"""
    result: str = ""
    i: int = 0
    h: int
    while i < n:
        if i > 0:
            result = result + "h"
        h = i + 1 
        while h > 0: 
            result = result + "e"
            h = h - 1
        i = i + 1
    return result

print(silly(3))
