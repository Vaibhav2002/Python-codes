import math as m

n = int(input("Enter the number"))
s = 0
while n > 9:
    while n > 0:
        s += int(m.pow(n % 10, 2))
        n = n // 10
    n = s
    s = 0
if n == 1:
    print("Happy no.")
else:
    print("Not happy no.")
