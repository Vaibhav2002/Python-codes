import math as m
l=int(input("Enter lower range"))
u=int(input("Enter upper range"))
for i in range(l,u+1):
    n=i
    flag=True
    for j in range(2,int(m.sqrt(n))+1):
        if n%j==0:
            flag=False
            break
    if flag and n>1:
        print(i)