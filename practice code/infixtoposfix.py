s = input("Enter the infix expression")
s=s.upper()
a = list()
s1 = ""


def check(c, ch):
    cha, s2, s3 = '^', '%*/', "+-"
    if c == ch:
        return True
    elif c == cha and (ch in s2 or ch in s3):
        return True
    elif c in s2 and (ch in s2 or ch in s3):
        return True
    elif c in s3 and ch in s3:
        return True
    else:
        return False


for i in s:
    if not i.isalpha():
        if not a:
            a.append(i)
        elif i == ')':
            while a[len(a) - 1] != '(':
                s1 += a.pop()
            a.pop()
        elif check(a[len(a) - 1], i):
            while i != '(' and a != [] and check(a[len(a) - 1], i):
                s1 += a.pop()
            a.append(i)
        elif not a == []:
            a.append(i)
    else:
        s1 += i

while not a == []:
    s1 += a.pop()

print("Postfix : ", s1)
