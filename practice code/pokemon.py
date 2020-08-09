s1, a1, h1 = input(), int(input()), int(input())
s2, a2, h2 = input(), int(input()), int(input())
if (s1 == 'Water' and s2 == 'Fire') or (s1 == 'Grass' and s2 == 'Water') or (s1 == 'Fire' and s2 == 'Grass'):
    a1 *= 2
    a2 //= 2
else:
    a1 //= 2
    a2 *= 2
m = h2 / a1 if h2 % a1 == 0 else h2 / a1 + 1
n = h1 / a2 if h1 % a2 == 0 else h1 / a2 + 1
if m <= n:
    print("Trainer 1 wins")
else:
    print("Trainer 2 wins")
