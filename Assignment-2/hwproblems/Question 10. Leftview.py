"""
Peter Mora-Stevens
00:00 am/pm

problem_name
Time: 40mins
Solution: 15-20mins
Testcases: 20mins

Given a binary tree, create an array of the left view (leftmost elements in each level) of the tree.

Algorithm: BFS
Time Complexity O(n)
Space Complexity O(n)

Information we know
    - Binary Tree, the values aren't sorted

Edge Cases
    - No tree/root
    
Assumptions
    - 
    
Difficulties
    - 
    
Approach
    - BFS
    a) initialize queue with first level
    b) while the queue is not empty
        For i in range(len(queue)):
            when i == 1
        loop through the nodes on the level in queue
            for the first value in the queue, append to output array
            add children if available

"""
from collections import deque

class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
class bst():
    def __init__(self):
        self.root = None   

def Leftview(self):
    if not self.root:
        return None
    
    output = []
    q = deque()
    q.append(self.root)
    while q:
        for i in range(len(q)):
            if i == 0:
                output.append(q[0].val)
            curr = q.popleft()
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
    return output

if __name__ == "__main__":
    
    # provided
    tree = bst()
    tree.root = Node(7)
    tree.root.left = Node(8)
    tree.root.right = Node(3)
    tree.root.right.left = Node(9)
    tree.root.right.right = Node(13)
    tree.root.right.left.left = Node(20)
    tree.root.right.right.left = Node(14)
    tree.root.right.right.left.right = Node(15)
    print("Actual: ", Leftview(tree), "Expected: [7, 8, 9, 20, 15]")
    
    tree = bst()
    tree.root = Node(7)
    tree.root.left = Node(20)
    tree.root.left.left = Node(15)
    tree.root.left.right = Node(6)
    tree.root.right = Node(4)
    tree.root.right.left = Node(8)
    tree.root.right.right = Node(11)
    print("Actual: ", Leftview(tree), "Expected: [7, 20, 15]")
    tree = bst()
    tree.root = Node(None)
    print("Actual: ", Leftview(tree), "Expected: None")
    