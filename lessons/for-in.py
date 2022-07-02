"""An example of for in syntax."""

names: list[str] = ["Bridget", "Sammi", "Jada"]

# Example of iterating through names using while

#prints names 
i: int = 0 
while i < len(names):
    name: str = names[i]
    print(name)
    i += 1

# the following for.. in loop is the same as above 

for name in names:
    print(name)