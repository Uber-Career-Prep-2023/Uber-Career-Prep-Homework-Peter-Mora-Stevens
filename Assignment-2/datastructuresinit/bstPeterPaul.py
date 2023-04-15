class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
class BinarySearchTree():
    def __init__(self):
        self.root = None
        
    def insert(self, val):
        if self.root == None:
            self.root = Node(val)
            return
            
        if self.root.data == val:
            return
        
        if self.root.data > val:
            if self.root.left:
                self.root.left.insert(val)
            else:
                self.root.left = Node(val)
        else:
            if self.root.right:
                self.root.right.insert(val)
            else:
                self.root.right = Node(val)
                
    def insert(self, val):
        def recurse(root, val):
            if root == None:
                root = Node(val)
                return root
            
            if root.data > val:
                root.left = recurse(root.left, val)
            else:
                root.right = recurse(root.right, val)
            return root
                
        recurse(self.root, val)