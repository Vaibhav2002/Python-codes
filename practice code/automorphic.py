n = input("Enter the number")
num = int(n)
n2 = str(num * num)
if n2.endswith(n):
    print("Automorphic no.")
else:
    print("Not automorphi cno.")
