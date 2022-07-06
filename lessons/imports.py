"""Examples of importing Python."""


from lessons import helpers
from lessons import helpers as hp
    # so that you don't haev to type out helpers each time 
    # alias
from lessons.helpers import powerful
    # import names defined globally 

# from directiry import module


def main() -> None:
    """Entrypoint of the program."""
    print(helpers.powerful(2,4))
    print(f"The answer: {helpers.THE_ANSWER}")
    # import module.function 

if __name__ == "__main__":
    main()