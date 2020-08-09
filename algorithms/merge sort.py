def split(a):
    if len(a)==1:
        return
    mid = len(a) // 2
    left, right = [], []
    for i in range(mid):
        left.append(a[i])
    for i in range(mid, len(a)):
        right.append(a[i])
    split(left)
    split(right)
    merge(left, right, a)


def merge(a, b, c):
    i, j, k = 0, 0, 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c[k] = a[i]
            i = i + 1
        else:
            c[k] = b[j]
            j = j + 1
        k = k + 1
    while i < len(a):
        c[k] = a[i]
        k, i = k + 1, i + 1
    while j < len(b):
        c[k] = b[j]
        k, j = k + 1, j + 1


def main():
    a = list(map(int, input("Enter the elements").split()))
    print("Original array : ", a)
    split(a)
    print("Sorted array : ", a)


main()
