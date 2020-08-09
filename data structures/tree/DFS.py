def inorderRecur(root):
    inorderRecur(root.left)
    print(root.data, end=" ")
    inorderRecur(root.right)


def preorderRecur(root):
    print(root.data, end=" ")
    preorderRecur(root.left)
    preorderRecur(root.right)


def postorderRecur(root):
    postorderRecur(root.left)
    postorderRecur(root.right)
    print(root.data, end=" ")
