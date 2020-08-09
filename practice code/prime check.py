import math as m
n=int(input())
flag = True
for j in range(2, int(m.sqrt(n)) + 1):
    if n % j == 0:
        flag = False
        break
if flag:
    print("Prime")
else:
    print("Not prime")
