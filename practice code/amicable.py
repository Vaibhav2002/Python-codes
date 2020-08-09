
n = int(input("Enter rhe first no."))
num = int(input("Enter the second no."))
s1 = s2 = 0
for i in range(1, n // 2 + 1):
    if n % i == 0:
        s1 += i
for i in range(1, num // 2 + 1):
    if num % i == 0:
        s2 += i
if s1 == num and s2 == n:
    print("Amicable no.s")
else:
    print("Not amicable no.s")
