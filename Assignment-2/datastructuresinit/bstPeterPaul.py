class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
class BinarySearchTree():
    def __init__(self):
        self.root = None
    
    
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