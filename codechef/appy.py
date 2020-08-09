t = int(input())
while t > 0:
    n, a, b, k = map(int, input().split())
    l = list(i for i in range(1, n + 1))
    first = list(filter(lambda x: x % a == 0 and x % b != 0, l))
    second = list(filter(lambda x: x % b == 0 and x % a != 0, l))
    if len(first) + len(second) == k:
        print("Win")
    else:
        print("Lose")
    t=t-1