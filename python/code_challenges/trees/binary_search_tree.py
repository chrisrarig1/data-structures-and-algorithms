from code_challenges.trees.binary_tree import BinaryTree
from code_challenges.trees.node import Node

class BinarySearchTree(BinaryTree):
    def __init__(self, root=None):
        super().__init__(root)

    def add(self, value):
        def walk(root):
            if self.root == None:
                self.root = Node(value)
                return
            if root.value < value:
                if root.left == None:
                    root.left = Node(value)
                else:
                    walk(root.left)
            else:
                if root.right == None:
                    root.right = Node(value)
                else:
                    walk(root.right)
        walk(self.root)
    
    def contains(self, value):
        if self.root.value == value:
            return True
        def walk(root,value):
            if root == None:
                return False
            elif root.value == value:
                return True
            elif root.value > value:
                return walk(root.left, value)
            elif root.value < value:
                return walk(root.right, value)
            else:
                return False
        return walk(self.root, value)
                

