n=input()
k,n=int(n[2]),int(n[0])
a=list()
for i in range(k):
    g=input()
    a.append(g.replace(' ',''))
for i in a:
    s=list(i)
    for j in range(len(s)-1,0,-1):
        if s[j]>s[j-1]:
            s[j],s[j-1]=s[j-1],s[j]
            "".join(s)
            break
    for k in s:
        print(k,end="")
    print()




