"""EX03 - Wordle."""

__author__ = "730465834"


def contains_char(word: str, character: str) -> bool: 
    """Searches for a character in a word.""" 
    assert len(character) == 1
    word_index: int = 0 
    matches: bool = False
    while not matches and word_index < len(word):  # runs until a match has been found or all characters in the word have been checked 
        if word[word_index] == character:
            matches = True
        else: 
            word_index = word_index + 1
    if matches: 
        return True
    else:
        return False 


def emojified(guess: str, secret: str) -> str:
    """Returns resulting codified emoji string using the contains_char function.""" 
    resulting_emojis: str = ""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    i: int = 0 

    assert len(guess) == len(secret)
    while i < len(secret):
        if guess[i] == secret[i]:  # exact character match 
            resulting_emojis = resulting_emojis + GREEN_BOX 
        else:  # check for partial matches
            if contains_char(secret, guess[i]):
                resulting_emojis = resulting_emojis + YELLOW_BOX
            else:
                resulting_emojis = resulting_emojis + WHITE_BOX
        i = i + 1

    return resulting_emojis


def input_guess(expected_length: int) -> str:
    """Prompts user for a guess of an expected length."""
    guess = input(f"Enter a {expected_length} character word: ")

    while expected_length != len(guess):
        guess = input(f"That wasn't {expected_length} chars! Try again: ")
    
    return guess
    

def main() -> None:
    """The entrypoint of the program and main game loop."""
    current_turn: int = 1
    user_win: bool = False  # keeps track of whether or not the user has guessed the correct word 
    secret: str = "codes"
    while current_turn <= 6 and not user_win:  # runs loop until the user has guessed the word or all 6 guesses have been used
        print(f"=== Turn {str(current_turn)}/6 ===") 
        guess = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            user_win = True
        else: 
            current_turn = current_turn + 1 
    
    if user_win:
        print(f"You won in {current_turn}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()