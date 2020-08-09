def selectionsort(a):
    for i in range(len(a) - 1):
        min = i
        for j in range(i + 1, len(a)):
            if a[j] < a[min]:
                min = j
        a[i], a[min] = a[min], a[i]


a = list(map(int, input("Enter numbers :").split()))
print("original array :", a)
selectionsort(a)
print("after sort: ", a)
