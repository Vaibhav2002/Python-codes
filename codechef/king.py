n = int(input())
a = list()
for i in range(n):
    x = int(input())
    a.append(x)
    a.sort(reverse=True)
    print(a.index(x)+1)
