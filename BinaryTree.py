"""
Binary Tree implementation
A tree whose element have at most two elements.
Each element can have only two children, named left and right.
"""

class BinaryTree:
    def __init__(self, node):
        self.root = node

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def __print__(self):
        print(self.value)

# TODO: insertion a node at first position available in level order
"""
def insert(tree,value):
        if tree.root:
            tree.root = Node(value)
        insert(tree.root, value)

def insertNode(node, value):
    if node.left:
        node.left = Node(value)
    if node.right: 
        node.right = Node(value)
    insert(node.left, value)
"""

def printNode(node):
    if node is not None:
        print('(', end='')
        print(node.value, end=' ')
        printNode(node.left)
        printNode(node.right)
        print(')', end='')


b = Node(10)
b.left= Node(11)
b.left.left = Node(7)
b.right = Node(9)
b.right.left = Node(15)
b.right.right = Node(8)

printNode(b)
