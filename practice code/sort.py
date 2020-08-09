a = list(map(int, input("Enter elements :").split()))
x = int(input("Enter element : "))
m1, m2 = 9999, -9999
index = a.index(x)


def check(a):
    flag = True
    for i in range(len(a) - 1):
        if a[i] > a[i + 1]:
            flag = False
            break

    if flag:
        print("Swapped", end=" ")
        for i in a:
            print(i, end=" ")
    else:
        print("Not swapped")


for i in range(index):
    if m2 < a[i] > x:
        m2 = a[i]
for i in range(index + 1, len(a)):
    if m1 > a[i] < x:
        m1 = a[i]
if m2 != -9999:
    a[a.index(m2)], a[index] = a[index], a[a.index(m2)]
    check(a)
elif m1 != 9999:
    a[a.index(m1)], a[index] = a[index], a[a.index(m1)]
    check(a)
elif index == 0 or index == len(a) - 1:
    print("Not swapped")
else:
    print("Already sorted")
