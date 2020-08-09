from math import factorial
n = int(input("Enter the number"))
f = 1
for i in range(2, n + 1):
    f*= i
print(f)
print(factorial(int(input("Enter the number"))))
