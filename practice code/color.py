t = int(input())
while t > 0:
    s = list(input().split())
    x, y, l, r = int(s[0]), int(s[1]), int(s[2]), int(s[3])
    b = list(z for z in range(l, r + 1))
    a = list((x & z) * (y & z) for z in range(l, r + 1))
    c = dict(zip(b, a))
    print(list(c.keys())[list(c.values()).index(max(a))])
    t = t - 1
