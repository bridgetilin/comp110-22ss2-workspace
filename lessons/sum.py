"""Example of writing a test subject"""


# skeleton function 
# def sum(xs: list[float]) -> float:
#     """Compute the sum of a list"""
#     return -1.0

# def sum(xs: list[float]) -> float:
#     """Compute the sum of a list"""
#     total: float  = 0.0
#     i: int = 0 
#     while i < len(xs):
#         total += xs[i]
#         i += 1
#     return total

def sum(xs: list[float]) -> float:
    """Compute the sum of a list."""
    total: float = 0.0
    for x in xs:
        total += x
    return total 

for x in [1, 2, 3]:
   print(x)

ys: list[int] = [110, 120]
for y in ys:
  print(y)


i: int = 0
ys: list[int] = [110, 120]
while i < len(ys):
  y: int = ys[i]
  print(y)
  i += 1