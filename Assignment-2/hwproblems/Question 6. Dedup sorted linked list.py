"""
Question 6: DedupSortedList
Given a sorted singly linked list, remove any duplicates so that no value appears more than once.

Peter Mora-Stevens
10:56 am

Question 6: DedupSortedList
Time: 45 mins
Solution: 15 (10 for psuedocode, 5 for implementation, 5-10 to understand last bug, last value wasn't being removed)mins
Testcases: 20mins (LL Methods and making testcases were difficult)

Given a sorted singly linked list, remove any duplicates so that no value appears more than once.

Algorithm: Simultaneous iteration two-pointer
Time Complexity O(n)
Space Complexity O(n)

Information we know
    - The input LL is sorted

Edge Cases
    - What if input is null
        - test if tail.next = None case, output based on that too (using a dummy node to initialize a LL)
    - What if input ll is all 1 value
        - we just return a ll with that value
    - what if input ll is entirely unique?
        - we just make a copy of originial list
    
Assumptions
    - All the values in the LL will be Ints, based on the language used ("values") and the testcases shown. Would ask if int's are the only datatypes in an interview though
    - We must return the head of a new ll which is also sorted and has no dup values (at least that's my implementation, we could make an algorithm which does this in in-space O(1) memory but I can't think of a solution for that right now)
    
Difficulties
    - Just figuring out the correct algorithm for keeping track of values, but with a sorted input head, this is much easier.
    
Approach
    - using a new LL, we can add values to it, while simultaniously traversing the original LL.
    a) Testcase for bad inputs, i.e. null or empty lists, return an empty statement
    b) initialize a new ll node for the dedupedLL, setting first node to dummy, assign tail pointer to dummy
    c) use a while loop for the input LL, check the value currently being pointed at, against the value in the dummy LL, if they're not ==, make tail.next = LL
    d) we know the other case is that the values are equal, so don't do anything and at the end, the LL will update to LL.nextc
    e) once we're through the original list, check if output dummy.next != None, and if so return the head (dummy.next) otherwise, return -1, or any other value to specify that the LL is empty

Optimizations
    - we could remove the O(n) memory by making the solution a two pointer on the input LL
"""

class LLNode():
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def printLL(self, head):
        output = ""
        itr = head
        while itr:
            output += str(itr.data) + " --> "
            itr = itr.next
        return output
    
    def populate(self, head, arr):
        itr = head
        for i in range(1, len(arr)):
            itr.next = LLNode(arr[i])
            itr = itr.next
        return head
            

def dedupSortedLL(head):
    if not head or head.data == None:
        return LLNode(-1)
    
    dummy = LLNode(0)
    tail = dummy
    
    while head:
        if head.data != tail.data:
            tail.next = head
            tail = tail.next
        head = head.next
        
    tail.next = None
    
    if dummy.next:
        return dummy.next
    return LLNode(-1)

if __name__ == "__main__":
    vals = [1, 2, 2, 4, 5, 5, 5, 10, 10]
    head = LLNode(vals[0])
    head = head.populate(head, vals)
    newhead = LLNode(0)
    newhead.next = dedupSortedLL(head)
    print("Actual: ", newhead.next.printLL(newhead.next), "Expected: 1, 2, 4, 5, 10",)
    
    vals = [8, 8, 8, 8]
    head = LLNode(vals[0])
    head = head.populate(head, vals)
    newhead = LLNode(0)
    newhead.next = dedupSortedLL(head)
    print("Actual: ", newhead.next.printLL(newhead.next), "Expected: 8",)
    
    vals = []
    head = LLNode(None)
    head = head.populate(head, vals)
    newhead = LLNode(0)
    newhead.next = dedupSortedLL(head)
    print("Actual: ", newhead.next.printLL(newhead.next), "Expected: -1",)
    
    vals = []
    head = None
    newhead = LLNode(0)
    newhead.next = dedupSortedLL(head)
    print("Actual: ", newhead.next.printLL(newhead.next), "Expected: -1",)
    
    vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    head = LLNode(vals[0])
    head = head.populate(head, vals)
    newhead = LLNode(0)
    newhead.next = dedupSortedLL(head)
    print("Actual: ", newhead.next.printLL(newhead.next), "Expected: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10",)
    
    vals = [1]
    head = LLNode(vals[0])
    head = head.populate(head, vals)
    newhead = LLNode(0)
    newhead.next = dedupSortedLL(head)
    print("Actual: ", newhead.next.printLL(newhead.next), "Expected: 1",)