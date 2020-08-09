import math as m

n = int(input("Enter the number"))
g = int(m.sqrt(n))
if g * (g + 1) == n:
    print("pronic")
else:
    print("Not pronic")

