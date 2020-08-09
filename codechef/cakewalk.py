t = int(input())
while t > 0:
    a = list()
    for i in range(10):
        a.append(map(int, input().split()))
    a = list(filter(lambda x: x <= 30, a))
    if len(a) >= 60:
        print("Cakewalk")
    else:
        print("Not")
        t=t-1
