def bubblesort(a):
    for i in range(len(a) - 1):
        for j in range(len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]


a = list(map(int, input("Enter numbers :").split()))
print("original array :", a)
bubblesort(a)
print("sorted array :", a)
