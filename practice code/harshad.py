n = int(input("Enter the number"))
s = 0
num = n
while n > 0:
    s += n % 10
    n //= 10
if num % s == 0:
    print('Harshad no.')
else:
    print(" Not Harshad no.")
