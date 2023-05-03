"""
Peter Mora-Stevens
2:06 pm

Question 9. Disconnect Cycle
Time: __mins
Solution: __mins
Testcases: __mins

problem description

Algorithm: Fast and Slow pointers
Time Complexity O(n)
Space Complexity O(1)

Information we know
    - The input LL could or could not have a cycle
    - we must output a LL w/ out a cycle

Edge Cases
    - There is not a LL
    
Assumptions
    - If there is no LL, return null
    
Difficulties
    - 
    
Approach
    - Fast and Slow pointer
    a) set a fast pointer which moves forward at 2 nodes per move and a slow node with 1 node per move
    b) if the two nodes meet, make slow.next set to none
    c) otherwise return the head

"""

class Node():
    def __init__(self, val):
        self.val = val
        self.next = None

    def printLL(self, head):
        output = ""
        itr = head
        while itr:
            output += itr.val + " --> "
            itr = itr.next
        print(output)
        
    def populate(self, head, arr):
        itr = head
        for i in range(1, len(arr)):
            itr.next = Node(arr[i])
            itr = itr.next
        return head
    
    def DisconnectCycle(head):
        fast, slow = head, head
        while fast and fast.next:
            if fast == slow:
                pass

if __name__ == "__main__":
    
    # provided
    
    print("Actual: ", function(), "Expected: ")