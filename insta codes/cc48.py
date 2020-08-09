d = int(input("Enter difference"))
a = list(map(int, input("Enter elements").split()))
l, r, count = 0, 1, 0
a.sort()
while l < len(a) and r < len(a):
    if a[r] - a[l] == d:
        count += 1
        l += 1
        r += 1
    elif a[r] - a[l] > d:
        l += 1
    else:
        r += 1
print(count)
