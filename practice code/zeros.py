l = list(input("Enter the list").split())
for i in l:
    if i == "0":
        l.remove(i)
        l.append(i)
print(l)
