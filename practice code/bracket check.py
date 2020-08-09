a = list()
s = input("Enter expression")
c, c1 = '[{(', ']})'
for i in s:
    if i in c + c1:
        try:
            if i in c:
                a.append(i)
            elif i in c1 and c.index(a.pop()) != c1.index(i):
                print("illegal expression")
                exit(0)
        except Exception:
            print("illegal expression")
            exit(0)
if not a:
    print("Legal expression")
else:
    print("illegal expression")
