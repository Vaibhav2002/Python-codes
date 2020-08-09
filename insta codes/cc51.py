s, s1, a = input(), "", dict()
if not s.islower():
    print("Uppercase not allowed")
    exit()
for i in range(len(s) - 1, -1, -1):
    if a.get(s[i]) is None:
        s1 = s[i] + s1
        a[s[i]] = True
print(s1)
