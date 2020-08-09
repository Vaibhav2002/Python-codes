s = list(set(i for i in input("Enter sentence : ") if i!=" "))
a=list(i for i in s if s.count(i)%2!=0)
print(a)