a = list(map(int, input("Enter numbers :").split()))
a.sort()
x = int(input("Enter element to be searched : "))
l, u = 0, len(a) - 1
while l < u:
    mid = (l + u) // 2
    if a[mid] == x:
        print("Element found")
        break
    elif a[mid] < x:
        l = mid + 1
    else:
        u = mid - 1
else:
    print("Element not found")
