# """EX04 - CYOA."""

# __author__ = "730465834"


# from random import randint
# points: int = 0 
# player: str = ""
# running: bool = True
# # emoji bank
# MONEY_EYES: str = "\U0001F911"
# SAD_FACE: str = "\U0001F62D"
# HAPPY_FACE: str = "\U0001F606"
# CELEBRATION: str = "\U0001F973"
# WAVING_HAND: str = "\U0001F44B"
# LOCK: str = "\U0001F512"
# UNLOCKED: str = "\U0001F513"

# def main() -> None:
#     """Entrypoint of game."""
#     greet()
#     global points
#     global running
#     print(f"Current points: {points}")
#     while running: 
#         begin = str(input("Would you like to play 'Guess the Number'? (Yes/No): "))
#         while begin != "Yes" and begin != "yes" and begin != "No" and begin != "no":  # ensures valid selection is made 
#             begin = input("Invalid selection. Try again: ")

#         if len(begin) == 3:  # a length of 3 would mean the player selected yes
#             level = int(input(f"Yay! {HAPPY_FACE} Let's get started! There are 3 different levels: Level 1: Easy, Level 2: Medium, Level 3: Custom (choose your own range of numbers). Enter the number of level you would like to play: "))
#             while level != 1 and level != 2 and level != 3:
#                 level = int(input("Invalid selection. Try again: "))
#             if level == 1: 
#                 level_1()
#             if level == 2: 
#                 level_2()
#             if level == 3:
#                 print("Good choice! You get to create your own range of numbers to guess from.")
#                 min = int(input("Enter the minimum value of your choosing: "))
#                 max = int(input("Enter the maximum value of your choosing: "))
#                 level_3(min, max, points)

#         else:
#             print(f"Aw {SAD_FACE}, you have accumulated {points} points. Hope to see you another time. Goodbye!")
#             running = False


# def greet() -> None:
#     player = input("What is your name? ")
#     print(f"Welcome to 'Guess the Number,' {player}! In this game, we will pick a random number, and your goal is to correctly guess the secret number to unlock the valut {LOCK}! Each time you guess, you add points to your very cool (and very real) bank!")

# def retry(guess: int, secret: int) -> int:
#     if guess < secret:
#         hint = int(input("That was too low. Try again: "))
#     else:
#         hint = int(input("That was too high. Try again: "))
#     return hint

# def level_1() -> None:
#     """Number from 1 to 10"""
#     global points
#     secret: int = randint(1,10)
#     guess = int(input("Pick a number from 1 to 10. You have 3 tries to guess the correct number. Enter your first guess: "))
#     if guess < 1 or guess > 10:
#         guess = int(input("Invalid selection. Try again: "))
#     turn: int = 1 
#     print(guess)
#     while guess != secret and turn < 3: 
#         guess = retry(guess, secret)
#         if abs(secret - guess) <=2:
#             points = points + 20
#         else:
#             points = points + 10
#         turn = turn + 1 
#     if guess == secret:
#         print(win(turn, points))
#     else:
#         goodbye(points)

# def level_2() -> None:
#     """Number from 1 to 25"""
#     global points 
#     secret: int = randint(1,25)
#     guess = int(input("Pick a number from 1 to 25. You have 5 tries to guess the correct number. Enter your first guess: "))
#     if guess < 1 or guess > 25:
#         guess = int(input("Invalid selection. Try again: "))
#     turn: int = 1 
#     print(guess)
#     while guess != secret and turn < 5: 
#         guess = int(input("Not quite! Try again: "))
#         if abs(secret - guess) <=2:
#             points = points + 20
#         else:
#             points = points + 10
#         turn = turn + 1 
#     if guess == secret:
#         print(win(turn, points))
#     else:
#         goodbye(points)

# def level_3(min: int, max: int, points: int) -> int:
#     """Number from 1 to a number of the players choice"""
#     secret: int = randint(min,max)
#     guess = int(input(f"Pick a number from {min} to {max}. You have 10 tries to guess the correct number. Enter your first guess: "))
#     assert guess <= max and guess >= min
#     turn: int = 1
#     print(guess)
#     while guess != secret and turn < 10: 
#         guess = input("Not quite! Try again: ")
#         if abs(guess-secret) < (max-min) * 0.1:
#             points = points + 20
#         else:
#            points = points + 10  
#         turn = turn + 1
#         print(retry(guess, secret))
#     if guess == secret:
#         points = points + 100
#         print(win(turn, points))

#     return points 

# def win(turns: int, points: int) -> str:
#     global running
#     if turns == 1:
#         message: str = f"Wow! You got it in 1 turn! You've unlocked the vault, and you now have {points} points! {UNLOCKED} {CELEBRATION} {MONEY_EYES} "
#     else: 
#         message: str = f"Wow! You got it in {turns} turns! You've unlocked the valut, and you now have {points} points {UNLOCKED}! {CELEBRATION} {MONEY_EYES}"
#     return message
    

# def goodbye(points: int) -> None:
#     print(f"Game Over. You have {points} points! ")
    

# if __name__ == "__main__":
#     main()

# def main() -> None:
#     print(only_evens([1,2,3,4,5,6,7,123,122,0]))

# def main() -> None:
#     list_ex = []
#     print(sub(list_ex, 1, 3))
def main() -> None:
    print(is_equal([1, 0, 1], [1, 0, 1]))

def only_evens(numbers: list[int]) -> list[int]:
    i: int = 0
    even_values: list[int] = list()
    while i < len(numbers):
        if numbers[i] % 2 == 0:
            even_values.append(numbers[i])
        i = i + 1 
    return even_values

def sub(numbers: list[int], start: int, end: int) -> list[int]:
    sub_list: list[int] = list()
    i: int = start
    if len(numbers) == 0 or start > len(numbers) or end <= 0: 
        return sub_list
    while i < end: 
        sub_list.append(numbers[i])
        i += 1 
    return sub_list 

def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    i: int = 0 
    match: int = 0 
    if len(list_1) != len(list_2): 
        return False

    while i < len(list_1):
        if list_1[i] == list_2[i]:
            match += 1  # each time there is a match at the same index, add one to the number of matches
        i += 1 
    if match == len(list_1):  # if the matches is the same as the number of elements in the 
        return True  
    else:
        return False 



if __name__ == "__main__":
    main()