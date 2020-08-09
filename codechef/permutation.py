from itertools import permutations


def convert(s):
    strings = [str(integer) for integer in s]
    a_string = "".join(strings)
    return int(a_string)


s = list(input().split())
n, k = int(s[0]), int(s[1])
perm = list(i for i in range(1, n + 1))
while k > 0:
    s1 = int(input().replace(" ", ""))
    p = permutations(perm)
    for i in list(p):
        z = list(i)
        s = convert(z)
        if s > s1:
            print(s)
            break
    k = k - 1
