x, y, a, d = map(int, input().split())
if a == 180:
    x += d
elif a == 0:
    x -= d
elif a == 90:
    y += d
else:
    y -= d

print("({},{})".format(x, y))
