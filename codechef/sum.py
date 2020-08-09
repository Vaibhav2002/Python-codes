t = int(input())
while t > 0:
    s = list(input().split())
    n = int(s[0])
    k = int(s[1])
    a = list(map(int, input().split()))
    a = list(filter(lambda x: x <= k, a))
    flag = True
    for i in range(0, len(a) - 1):
        for j in range(i + 1, len(a)):
            if a[i] + a[j] == k:
                print("Yes")
                flag = False
                break
        if not flag:
            break
    if flag:
        print("No")
    t = t - 1
