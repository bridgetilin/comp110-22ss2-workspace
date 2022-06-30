"""Examples of using lists in a simple 'game'."""


# first need the ability to roll a random number
from random import randint

rolls: list[int] = list()

while len(rolls) == 0 or rolls[len(rolls) -1] != 1: 
    rolls.append(randint(1,6))

# rolls.append(randint(1,6))
# rolls.append(randint(1,6))
# rolls.append(randint(1,6))

print(rolls)

# Remove an item from a list by it's index 
rolls.pop(len(rolls)-1)
print(rolls)

# proces each litem; sum the values of our rolls 
i: int = 0
sum: int = 0 
while i < len(rolls):  # based on the number of items left in the list 
    sum = sum + rolls[i]
    i = i + 1 

print(f"Total score: {sum}")


# # Access an individual item 
# print(rolls[0])

# # create a while loop to roll the dice multiple times 

# #Access the length of a list (Number of items)
# print(len(rolls))

# # Access the last item of a list
# last_index: int = len(rolls) - 1 
# print(rolls[len(rolls) - 1])

# 