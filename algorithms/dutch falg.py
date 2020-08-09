def sort(a):
    l, m, h = 0, 0, len(a) - 1
    while m <= h:
        if a[m] == 0:
            a[m], a[l] = a[l], a[m]
            m += 1
            l += 1
        elif a[m] == 1:
            m += 1
        else:
            a[h], a[m] = a[m], a[h]
            h -= 1


a = list(map(int, input("Enter elements").split()))
print("original array ", a)
sort(a)
print("sorted array ", a)
