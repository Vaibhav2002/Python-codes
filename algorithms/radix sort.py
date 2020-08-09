def sort(a, exp):
    count = list(0 for i in range(10))
    for i in a:
        count[(i // exp) % 10] += 1
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    output = list(0 for i in range(len(a)))
    for i in range(len(a)-1,-1,-1):
        output[count[(a[i] // exp) % 10] - 1] = a[i]
        count[(a[i]//exp)%10] -= 1
    for i in range(len(output)):
        a[i] = output[i]


def radix(a):
    m = max(a)
    i = 1
    while m // i > 0:
        sort(a,i)
        i *= 10


a = list(map(int, input("Enter elements").split()))
print("original array ", a)
radix(a)
print("sorted array ", a)
