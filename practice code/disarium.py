import math as m

n = input("Enter the number")
l = int(len(n))
n = int(n)
s, num = 0, n
while n > 0:
    s += int(m.pow(n % 10, l))
    n //= 10
    l = l - 1
if s == num:
    print("Disarium no.")
else:
    print("Not disarium no.")
