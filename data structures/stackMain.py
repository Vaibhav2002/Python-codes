import stack as st

n = int(input("Enter size of stack"))
ob = st.stackClass(n)
c = int(input("Enter 1 to push\n2 to pop\n3 to display\n4 to peek\n0 to exit"))
while c != 0:
    if c == 1:
        item = int(input("Enter value"))
        ob.push(item)
