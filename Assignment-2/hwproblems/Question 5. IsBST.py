"""
Peter Mora-Stevens
11:30 am

Question 5. IsBST
Time: 20mins
Solution: 10mins
Testcases: 10mins

Given the root of a Binary Tree, return true if it is a binary tree, otherwise false

Algorithm: DFS 
Time Complexity O(n)
Space Complexity O(n)

Information we know
    - The binary tree could be a BST, could be null

Edge Cases
    - if null, return null
    
Assumptions
    - there can be cases where every node and its children follow bst rules, but a node above the subtree doesn't
    
Approach
    - dfs w/ upper and lower bounds
    a) start with upper and lower bounds set to appropriate inf
    b) for left case, check with same lowerbound, new upperbound
    c) for right case, check with new lowerbound, same upperbound
    d) return false if case is wrong
    e) return true if hit base case
    f) check if both sides are true after recursive call stack returns

"""
class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
def isBST(root):
    def dfs(root, left, right):
        if not root:
            return True
        if not(left < root.val < right):
            return False
        
        return(dfs(root.left, left, root.val) and
               dfs(root.right, root.val, right))
    return dfs(root, float('-inf'), float('inf'))


if __name__ == "__main__":
    root = Node(10)
    root.left = Node(8)
    root.left.right = Node(9)
    root.right = Node(16)
    root.right.left = Node(13)
    root.right.right = Node(17)
    root.right.right.right = Node(20)
    print("Actual: ", isBST(root), "Expected: True")
    
    root = Node(10)
    root.left = Node(8)
    root.left.right = Node(9)
    root.right = Node(16)
    root.right.left = Node(13)
    root.right.right = Node(17)
    root.right.right.right = Node(15)
    print("Actual: ", isBST(root), "Expected: False")
    
    root = None
    print("Actual: ", isBST(root), "Expected: True")
    
    root = Node(2)
    root.left = Node(2)
    root.right = Node(2)
    print("Actual: ", isBST(root), "Expected: False")
    
    root = Node(2)
    root.right = Node(3)
    root.right.right = Node(4)
    root.right.right.right = Node(5)
    root.right.right.right.right = Node(6)
    print("Actual: ", isBST(root), "Expected: True")