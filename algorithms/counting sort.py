def sort(a):
    m = max(a)
    count = list(0 for i in range(m + 1))
    for i in a:
        count[i] += 1
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    output = list(0 for i in range(len(a)))
    for i in range(len(a)):
        output[count[a[i]] - 1] = a[i]
        count[a[i]] -= 1
    for i in range(len(output)):
        a[i] = output[i]


a = list(map(int, input("Enter elements").split()))
print("original array ", a)
sort(a)
print("sorted array ", a)
