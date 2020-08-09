from DFS import *


class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None


head = Node(5)
head.left = Node(7)
head.right = Node(10)
head.left.left = Node(18)
head.left.right = Node(15)
head.right.left = Node(20)
head.right.right = Node(0)

inorder(head)
print()
preorder(head)
print()
postorder(head)
