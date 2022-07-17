"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730465834"


class Simpy:
    """A utility class inspired by NumPy for working with a column of numerical values."""
    
    values: list[float]

    def __init__(self, values: list[float]): 
        """Iniitalize a new Simpy object."""
        self.values = values

    def __str__(self) -> str:
        """Produce a string representation of a Simpy."""
        return f"Simpy({self.values})"

    def fill(self, value: float, times: int) -> None: 
        """Fill a Simpy's values with a specific number of repeating values."""
        self.values = []
        i: int = 0
        while i < times:  # loop until the desired number of repeats is reached 
            self.values.append(value)
            i += 1
    
    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fill in the values attribute with values within a given range."""
        self.values = []
        assert step != 0.0
        if step > 0.0: 
            current: float = start  # variable to keep track of the next value to be added to the list
            while current < stop:  
                self.values.append(current)
                current += step
        else:
            current: float = start
            while current > stop:
                self.values.append(current)
                current += step 

    def sum(self) -> float:
        """Compute and return the sum of all items in the values attribute."""
        return sum(self.values)
    
    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Overload the addition operator in conjuction with Simpy objects and floats."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            for value in self.values:
                result.values.append(value + rhs)  # add the input float to each value in left-hand Simpy object
        else:
            assert len(self.values) == len(rhs.values)
            i: int = 0 
            while i < len(self.values):
                result.values.append(self.values[i] + rhs.values[i])  # add each corresponding item in the two Simpys
                i += 1
        return result
    
    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Overload the power operator in conjunction with Simpy objects and floats."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            for value in self.values:
                result.values.append(value ** rhs)
        else:
            assert(len(self.values)) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                result.values.append(self.values[i] ** rhs.values[i])  # raise each value in the left-hand Simpy to the power of the corresponding value in the right-hand Simpy
                i += 1
        return result

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]: 
        """Overload the == operator in conjuction with Simpy objects and floats and produces a mask."""
        mask: list[bool] = []  # resulting mask based on the equality of each item in the values attribute with another Simpy or float value
        if isinstance(rhs, float):
            for value in self.values:
                mask.append(value == rhs)
        else:
            assert len(self.values) == len(rhs.values)
            i: int = 0 
            while i < len(self.values):
                mask.append(self.values[i] == rhs.values[i])
                i += 1
        return mask

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Overload the > operator in conjuction with Simpy objects and floats and produces a mask."""
        mask: list[bool] = []  # resulting mask based on the greater than relationship between each item in the values attribute with another Simpy or a float value
        if isinstance(rhs, float):
            for value in self.values:
                mask.append(value > rhs)
        else:
            assert len(self.values) == len(rhs.values)
            i: int = 0 
            while i < len(self.values):
                mask.append(self.values[i] > rhs.values[i])
                i += 1
        return mask 

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Overload the subscription notation operator."""
        if isinstance(rhs, int):  # if rhs is an int, access a specific item from the Simpy array
            return self.values[rhs]
        else:  # if rhs is a mask of type list[bool], create a new Simpy containing only the masked values
            result: Simpy = Simpy([])
            i: int = 0
            for i in range(len(rhs)):
                if rhs[i]:
                    result.values.append(self.values[i])
            return result