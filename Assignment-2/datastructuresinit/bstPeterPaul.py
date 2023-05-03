class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
class BinarySearchTree():
    def __init__(self):
        self.root = None
        
    """
    # first iteration, had the recursion in the body
    # when it can be abstracted into its own function
    
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
        """
                
                
    def insert(self, val):
        def recurseInsert(root, val):
            if root == None:
                root = Node(val)
                return root
            
            if root.data > val:
                root.left = recurseInsert(root.left, val)
            else:
                root.right = recurseInsert(root.right, val)
            return root
                
        recurseInsert(self.root, val)

    def search(self, target):
        def recurse(root, target):
            if not root:
                return False

            if target > root.val:
                return recurse(root.right, target)
            elif target < root.val:
                return recurse(root.left, target)
            else:
                return True
        return recurse(self.root, target)


            
if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(20)
    bst.insert(4)
    
    print(bst.search(4))