import math as m

n = int(input("Enter the number"))
num, s = n, 0
while n > 0:
    s += m.factorial(n % 10)
    n //= 10
if s == num:
    print("Peterson no.")
else:
    print("Not peterson no.")
