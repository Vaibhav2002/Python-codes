s, s1 = input(), ""
a = [0 for i in range(26)]
b = [0 for i in range(26)]
for i in s:
    if i.isupper():
        a[ord(i) - 65] += 1
    else:
        b[ord(i) - 97] += 1
for i in s:
    if i.isupper() and a[ord(i) - 65] == 1:
        s1 += i * 2
    elif i.islower() and b[ord(i) - 97] == 1:
        s1 += i * 2
    else:
        s1 += i

print(s1);
