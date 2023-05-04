class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
class BinarySearchTree():
    def __init__(self):
        self.root = None
<<<<<<< HEAD
        
    """
    # first iteration, had the recursion in the body
    # when it can be abstracted into its own function
=======
    
>>>>>>> 9edd71f7534c3f0c523741f11e17e3cb528932df
    
    def insert(self, val):
        def _insert(val, curr_node):
            if val < curr_node.val:
                if not curr_node.left:
                    curr_node.left = Node(val)
                else:
                    _insert(val, curr_node.left)
            elif val > curr_node.val:
                if not curr_node.right:
                    curr_node.right = Node(val)
                else:
                    _insert(val, curr_node.right)
            else:
                print("Value is already in tree")
        if not self.root:
            self.root = Node(val)
        else:
<<<<<<< HEAD
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
=======
            _insert(val, self.root)
    
    def print_tree(self):
        if self.root:
            self._print_tree(self.root)
            
    def _print_tree(self, curr_node):
        if curr_node:
            self._print_tree(curr_node.left)
            print("Value: ", curr_node.val)
            self._print_tree(curr_node.right)
    
    def minimum(self):
        def recurse(curr):
            if curr.left:
                recurse(curr.left)
            else:
                print(curr.val)
        if not self.root.left:
            return self.root.val
        else:
            recurse(self.root.left)


tree = BinarySearchTree()
tree.insert(10)
tree.insert(100)
tree.insert(20)
tree.insert(2000)
tree.insert(0)
tree.print_tree()
tree.minimum()
>>>>>>> 9edd71f7534c3f0c523741f11e17e3cb528932df
