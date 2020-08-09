s = input("Enter the infix expression").upper()
a = list()
s1 = ""


def rev(s):
    s4 = ""
    for i in s:
        if i == ')':
            s4 = '(' + s4
        elif i == '(':
            s4 = ')' + s4
        else:
            s4 = i + s4
    return s4


s = rev(s)


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

print("Prefix : ", rev(s1))
