"""
Peter Mora-Stevens
2:06 pm

Question 9. Disconnect Cycle
Time: __mins
Solution: __mins
Testcases: __mins

problem description

Algorithm: Adding nodes to a set
Time Complexity O(n)
Space Complexity O(n)

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
            output += str(itr.val) + " --> "
            itr = itr.next
        print(output)
    
    def DisconnectCycle(self, head):
        node_set = set()
        curr, prev = head, head
        while curr:
            if curr in node_set:
                prev.next = None
                return head
            else:
                node_set.add(curr)
            if curr != head:
                prev = prev.next
            curr = curr.next
        return head

if __name__ == "__main__":
    
    # provided
    head = Node(10)
    head.next = Node(18)
    head.next.next = Node(12)
    head.next.next.next = Node(9)
    head.next.next.next.next = Node(11)
    head.next.next.next.next.next = Node(4)
    head.next.next.next.next.next.next = head.next.next
    head.DisconnectCycle(head)
    print("Actual: ", head.printLL(head), "Expected: 10 -> 18 -> 12 -> 9 -> 11 -> 4")
    
    head = Node(10)
    head.next = Node(18)
    head.next.next = Node(12)
    head.next.next.next = Node(9)
    head.next.next.next.next = Node(11)
    head.next.next.next.next.next = Node(4)
    head.next.next.next.next.next.next = head.next.next.next.next.next
    head.DisconnectCycle(head)
    print("Actual: ", head.printLL(head), "Expected: 10 -> 18 -> 12 -> 9 -> 11 -> 4")