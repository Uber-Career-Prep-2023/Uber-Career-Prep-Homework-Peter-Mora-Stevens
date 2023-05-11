"""
Peter Mora-Stevens
9:44 am

Question 4. CopyTree
Time: __mins
Solution: __mins
Testcases: __mins

Given a binary tree, create a deep copy. Return the root of the new tree.

Algorithm: bfs level order traversal
Time Complexity O(n) - looking at every node of the input tree
Space Complexity O(n) - Making the new tree will take O(n) space, that is the space of the input tree

Information we know
    - we need to make a deep copy, so create a new node with the value associated with the corresponding tree

Edge Cases
    - Null tree, return null tree
    
Assumptions
    - 
    
Difficulties
    - 
    
Approach
    - bfs level order
    a) for every element in the queue, create 

"""
class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
    def print_inOrder(self, root):
        res = []
        def dfs(root):
            if not root:
                return root
            
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)
        dfs(root)
        return res
        
def deepCopy(root):
    def dfs(root, new_root):
        if not root:
            return None
        
        new_root = Node(root.val)
        new_root.left = dfs(root.left, new_root.left)
        new_root.right = dfs(root.right, new_root.right)
        return new_root
    return dfs(root, None)
        

if __name__ == "__main__":
    
    # provided
    root = Node(10)
    root.left = Node(8)
    root.left.right = Node(9)
    root.right = Node(16)
    root.right.left = Node(13)
    root.right.right = Node(17)
    root.right.right.right = Node(20)
    new_root = deepCopy(root)
    print(root == new_root)
    print("Actual: ", new_root.print_inOrder(new_root), "Expected: [8, 9, 10, 13, 16, 17, 20]")
    
    root = Node(10)
    root.left = Node(8)
    root.left.right = Node(9)
    root.right = Node(16)
    root.right.left = Node(13)
    root.right.right = Node(17)
    root.right.right.right = Node(15)
    new_root = deepCopy(root)
    print(root == new_root)
    print("Actual: ", new_root.print_inOrder(new_root), "Expected: [8, 9, 10, 13, 16, 17, 15]")