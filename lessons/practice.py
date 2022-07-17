# print(type(9/len(str(110))))

# word_bank: str = "the brown, lazy dog!"

# tar = word_bank[0] + word_bank[12] + word_bank[5]

# print(tar)



# def main() -> None:
#     print(invert({'a': 'z', 'b': 'y', 'c': 'x'}))
#     print(len(invert({'apple': 'cat'})))
    
    # print(invert({'kris': 'jordan', 'michael': 'jordan'}))

# def invert(a: dict[str, str]) -> dict[str, str]:
#     # raise key error needed 
    
#     inverted_a: dict[str, str] = {}
#     for key in a:
#         inverted_a[a[key]] = key

#     a_counter: int = 0  # counts the number of key-value pairings in the input dictionary
#     for key in a:
#         a_counter += 1

#     inverted_a_counter: int = 0  # counts the number of key-value pairings in the inverted dictionary
#     for key in inverted_a:
#         inverted_a_counter += 1
    
#     if a_counter != inverted_a_counter:  # if the number of key-value pairings is not the same before and after the inversion, this indicates the existence of a duplicate key
#         raise KeyError("The same key was encountered more than once in the inverted dictionary.")

#     return inverted_a 

def main() -> None:
    items: list[str] = ["Bridget", "Bob", "Betty", "Bob", "Brad"]
    print(count(items))

def count(items: list[str]) -> dict[str, int]:
    item_count: dict[str, int] = {}

    for item in items:
        if item in item_count:
            item_count[item] += 1
        else: 
            item_count[item] = 1 
    
    return item_count
        
if __name__ == "__main__":
    main()

# if __name__ == "__main__":
#     raise KeyError("KeyError")

    # a_counter: int = 0  # counts the number of key-value pairings in the input dictionary
    # for key in a:
    #     a_counter += 1

    # inverted_a_counter: int = 0  # counts the number of key-value pairings in the inverted dictionary
    # for key in inverted_a:
    #     inverted_a_counter += 1
    
    # if a_counter != inverted_a_counter:  # if the number of key-value pairings is not the same before and after the inversion, this indicates the existence of a duplicate key
    #     raise KeyError("The same key was encountered more than once in the inverted dictionary.")

class Foo:
   bar: int = 0

f: Foo = Foo()
f.bar = 10

print(f)
print(f.bar)