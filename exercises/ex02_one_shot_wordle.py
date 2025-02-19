"""EX02 - One-Shot Wordle."""

__author__ = "730465834"

secret: str = "python"
guess: str = input(f"What is your {len(secret)}-letter guess? ")

while len(guess) != len(secret): 
    guess = input(f"That was not {len(secret)} letters! Try again: ") 

guess_index: int = 0
resulting_emojis: str = ""
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

while guess_index < len(secret):
    if guess[guess_index] == secret[guess_index]:  # checks for EXACT matches first at each index
        resulting_emojis = resulting_emojis + GREEN_BOX    
    else:  # enters else block if not exact, cross checks between secret and guess for partial character matches
        secret_index: int = 0  
        partial_matches: bool = False  # boolean variable to keep track of whether the guessed character exists in secret
        while not partial_matches and secret_index < len(secret):
            if secret[secret_index] == guess[guess_index]: 
                partial_matches = True
            else:
                secret_index = secret_index + 1 
        if partial_matches:  # indicates a guessed character exist somewhere else in the secret word
            resulting_emojis = resulting_emojis + YELLOW_BOX
        else:  
            resulting_emojis = resulting_emojis + WHITE_BOX

    guess_index = guess_index + 1 

print(resulting_emojis)

if guess == secret:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")