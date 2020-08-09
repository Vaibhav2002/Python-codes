s = input("Enter the sentence").upper().replace(" ", "")
a = list(0 for i in range(26))
for i in s:
    a[ord(i) - 65] += 1
for j in range(len(a)):
    if a[j] != 0:
        print("Frequency of {}  =  {}".format(chr(j + 65), a[j]))
