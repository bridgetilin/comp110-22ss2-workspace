"""Challenge Question #2"""

i: int = 0
s: str = ""

while i < 4:
    if i % 2 == 0:
        s = s + "h"
    else:
        s = s + "e"
    i = i + 1 