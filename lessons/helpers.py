"""Demonstrate defining a modeule imported elsewhere """

from sys import float_repr_style

THE_ANSWER: int = 42 

def main() -> None:
    print(powerful(2,10))
    print("helpers run as a module")


def powerful(x: float, n: float) -> float:
    """Raise x to the power of n"""
    return x ** n 

# print("helpers.py was evaluated")

# idiom for making a module able to run as a program
# or have its global definitions imported elsewhere

if __name__ == "__main__":
    main()
else:
    # usually dont have an else branch
    print (f"helpers.py was imported: {__name__}")
