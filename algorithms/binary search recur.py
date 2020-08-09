def binsearch(a, x, l, u):
    mid = (l + u) // 2
    if l > u:
        return False
    if a[mid] == x:
        return True
    if x < a[mid]:
        return binsearch(a, x, l, mid - 1)
    else:
        return binsearch(a, x, mid + 1, u)


a = list(map(int, input("Enter numbers :").split()))
a.sort()
x = int(input("Enter element to be searched : "))
if binsearch(a, x, 0, len(a) - 1):
    print("Element found")
else:
    print("Element not found")
