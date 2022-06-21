"""An example of conditional if-else statements"""

SECRET: int = 3

print("I'm thinking of a number between 1 and 5. What is it?")

guess: int = int(input("What is your guess?"))

if guess == SECRET:
    print("You guessed correctly!!!")
    print("Have a great day!")
    
else:
    print("Sorry, you guessed incorrectly.")
    if guess > SECRET:
        print("You guessed too high.")
    else:
        print("You guessed too low.")
    print("Try again.")

print("Game over")

