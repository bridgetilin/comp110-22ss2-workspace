"""Example of a class and object instantiaion."""

class Pizza: 
    """Models the idea of a Pizza."""


 #Attribute definitions 
    size: str 
    toppings: int 

    extra_cheese: bool = False

    # constructor function:
    def __init__(self, size: str, toppings: int): 
        """Constrctor defintion for intitalizaiton """
        self.size = size
        self.toppings = toppings
        

    # or you can set default, unneeded if we have constructor!
    # size: str = "small"
    # toppings: int = 0
    # extra_cheese: bool = False


# defining a function!!
# def price(pizza: Pizza) -> float:
#     """Calculate the price of a pizza"""
#     total: float = 0.0
#     if pizza.size == "large":
#         total += 10
#     else:
#         total += 8
    
#     total += pizza.toppings * 0.75

#     if pizza.extra_cheese:
#         total += 1.0

#     return total

# using a method call

    def price(self, tax) -> float:
        """Calculate the price of a pizza"""
        total: float = 0.0
        if self.size == "large":
            total += 10
        else:
            total += 8
        
        total += self.toppings * 0.75

        if self.extra_cheese:
            total += 1.0
        
        total *= tax 

        return total


# set up the first pizza! set up a pizza object!
a_pizza: Pizza = Pizza("large", 3)
# assign attributes to this new object, unnecessary if we defined a constructor, which we did!
# a_pizza.size = "large"
# a_pizza.toppings = 3
# a_pizza.extra_cheese = False 
print(Pizza)
print(a_pizza)
print(a_pizza.size)

another_pizza: Pizza = Pizza("small", 0)
another_pizza.extra_cheese = True
print(another_pizza.size)
print(f"Price: ${another_pizza.price(1.05)}")



# print(f"Price: ${price(a_pizza)}")

# method call
print(f"Price: ${a_pizza.price(1.05)}")