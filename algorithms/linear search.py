a = list(map(int, input("Enter numbers :").split()))
x = int(input("Enter element to be searched : "))
for i in a:
    if i == x:
        print("Element found")
        break
else:
    print("Element not found")
