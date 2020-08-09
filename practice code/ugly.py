n = int(input("Enter the number"))
c = int(2)
flag = True
while n > 1:
    while n % c == 0:
        n = n // c
        if c != 2 and c != 3 and c != 5:
            flag = False
            break
    c = c + 1

if flag:
    print("Ugly no.")
else:
    print("Not ugly no.")
