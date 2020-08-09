import scala

a=list()
min=0
for i in range(int(input())):
    name = input()
    score = float(input())
    if i==0:
        min=score
    elif score<min:
        min=score
    a.append((name,score))
b=list()
for i in a:
    if a[1]!=min:
        b.append(i)

b=sorted(b)
min=b[0][1]
c=list()
for i in b:
    if i[1]==min:
        c.append(i[0])
    else:
        break
c=sorted(c)
for i in c:
    print(i)


