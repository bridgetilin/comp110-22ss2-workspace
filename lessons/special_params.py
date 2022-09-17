"""Examples of Special Parameters (optional paramters and Union types)."""

from typing import Union 

def hello(name: Union[str, int, float] = "World") -> str:
    """A delightful greeting!"""
    greeting: str = "Hello, "
    if isinstance(name, str):
        greeting += name
    elif isinstance(name, int):
        greeting += "COMP" + str(name)
    else:
        greeting += "Alien Life from Sector " + str(name)
    return greeting

print(hello("Sally"))

# want it to work with no pramters too!
print(hello())


# int argument works to
print(hello(110))

def add(lhs: float = 0.0, rhs: Union[str, float] = 0.0) -> float:
    result: float = lhs
    if isinstance(rhs, str):
        result += float(rhs)
    else:
        result += rhs
    return result


print(add())
print(add(1.0))
print(add(1.0, 2.0))
print(add(2.0, "1.0"))
# print(add("2.0", 1.0))
print(add(110.0))
print(add(110.0, "100.0"))
