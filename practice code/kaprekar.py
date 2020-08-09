n = int(input("Enter the number"))
num = str(n * n)
s, l, left = 0, len(num), 0
if len == 1:
    left = 0
else:
    left = int(num[:l // 2])
right = int(num[l // 2:])
if left + right == n:
    print("Kaprekar")
else:
    print("Not kaprekar")
