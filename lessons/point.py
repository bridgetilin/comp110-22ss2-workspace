"""Example of a Point class"""
from __future__ import annotations


class Point:
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Initialize a Point with its x, y components"""
        self.x = x
        self.y = y
    
    def scale_by(self, factor: float) -> None:
        """Mutates: multiplies components by factor."""
        self.x *= factor
        self.y *= factor
    
    # def scale(self, factor: float) -> Point:
    #     """Immutable: multiplies components by factor without mutation."""
    #     x: float = self.x * factor
    #     y: float = self.y * factor
    #     scaled_point: Point = Point(x,y)
    #     return scaled_point
    
    # simpler version
    def scale(self, factor: float) -> Point:
        """Scale a Point's attributes by factor"""
        return Point(self.x * factor, self.y * factor)
    
    #using operator overloading!!
    def __mul__(self, factor: float) -> Point:
        """Overload the multiplication operator for Point * float"""
        print("__mul__ was called!")
        return Point(self.x * factor, self.y * factor)

    #addition too!
    def __add__(self, rhs: Point) -> Point:
        """Overload the addition operator"""
        print("__add__ was called!")
        return Point(self.x + rhs.x, self.y + rhs.y)

    def __str__(self) -> str:
        """Produce a str representation of a Point for humans."""
        print("__str__ was called!")
        return f"({self.x}, {self.y})"
    
    def __repr__(self) -> str:
        """Produce a str representation of a Point for Python!"""
        return f"Point({self.x}, {self.y})"
    
    def __getitem__(self, index: int) -> float:
        """Overload the subscription notation."""
        if index == 0: 
            return self.x
        elif index == 1:
            return self.y
        else: raise IndexError
    
p0: Point = Point(1.0, 2.0)
p1: Point = p0.scale(2.0)
print(p0)  # VERY WEIRD OUTPUT!!!!!
# print(p0.__str__()) # unnessary, happening automatically
print(p1)
p1_as_a_str: str = str(p1)
print(p1_as_a_str)
print(f"({p0.x}, {p0.y})")
print(f"({p1.x}, {p1.y})")

p1_repr: str = repr(p1)
print(p1_repr)

p3 = p1 * 2.0  # we must use operator overloading for this to work
print(f"p3: {p3}")

c = p0 + p3
print(c)

print(p0[0])

