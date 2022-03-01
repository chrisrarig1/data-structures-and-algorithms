
class BinaryTree:
    def __init__(self, root = None):
        self.root = root
        self.max_val = 0

    def pre_order(self):
        values = []

        def walk(root):
            if root is None:
                return
            values.append(root.value)
            walk(root.left)
            walk(root.right)
        walk(self.root)
        return values

    def in_order(self):
        #left > root > right
        values = []

        def walk(root):
            if root is None:
                return
            walk(root.left)
            values.append(root.value)
            walk(root.right)
        walk(self.root)
        return values

    def post_order(self):
        #left > right > root
        values = []

        def walk(root):
            if root is None:
                return
            walk(root.left)
            walk(root.right)
            values.append(root.value)
        walk(self.root)
        return values

    def max(self):
        def walk(root):
            if root is None:
                return  
            if root.value > self.max_val:
                self.max_val = root.value
            walk(root.left)
            walk(root.right)
            return self.max_val
        return walk(self.root)




