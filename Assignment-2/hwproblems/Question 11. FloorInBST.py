"""
Peter Mora-Stevens
10:07 pm

Question 11 FloorInBST
Time: __mins
Solution: __mins
Testcases: __mins

Given a target numeric value and a binary search tree, return the floor (greatest element less than or equal to the target) in the BST.

Algorithm: Binary search
Time Complexity O(log(n)) - binary search
Space Complexity O(log(n)) - call stack needed

Information we know
    - input is a binary search tree, we need to find the greatest element less than or equal to the target in the BST

Edge Cases
    - input is null, return null
    
Assumptions
    - 
    
Difficulties
    - 
    
Approach
    - Binary search in a BST
    a) keep track of the highest value less than or equal to the target
    b)      do a search if the curr node val is less than target search right
    c)      if curr node val is greater than target search left
    d)          for both update floor if the value found is less than or equal to the target value
    e) once we hit null for either ends, return the floor value
"""

class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
def FloorinBST(root, target):
    if not root:
        return -1 # used to indicate that we've reached a leaf node
    
    if root.val == target:
        return root.val
    
    if root.val > target:
        return FloorinBST(root.left, target)
    else:
        floor = FloorinBST(root.right, target)
        if floor <= target and floor != -1:
            return floor
        else:
            root.val
    

if __name__ == "__main__":
    
    # provided
    root = Node(10)
    root.left = Node(8)
    root.left.right = Node(9)
    root.right = Node(16)
    root.right.left = Node(13)
    root.right.right = Node(17)
    root.right.right.right = Node(20)
    print("Actual: ", FloorinBST(root, 13), "Expected: 13")
    
    root = Node(10)
    root.left = Node(8)
    root.left.right = Node(9)
    root.right = Node(16)
    root.right.left = Node(13)
    root.right.right = Node(17)
    root.right.right.right = Node(20)
    print("Actual: ", FloorinBST(root, 15), "Expected: 13")