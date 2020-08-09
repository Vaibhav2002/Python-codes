import math as m
n=input("Enter number")
l,n,g,s=len(n),int(n),int(n),int(0)
while n>0:
    s+=int(m.pow(n%10,l))
    n=n//10
if(s==g):
    print("Armstrong ")
else:
    print("Not armstrong")
1