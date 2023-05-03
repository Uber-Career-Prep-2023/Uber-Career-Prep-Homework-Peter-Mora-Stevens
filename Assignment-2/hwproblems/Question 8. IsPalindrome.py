"""
Peter Mora-Stevens
00:00 am/pm

Question 8: IsPalindrome
Time: 27mins
Solution: 15 (10 mins Pseduo, 5 minutes solution)mins
Testcases: 12 (takes time to write tests and methods)mins

Given a doubly linked list, determine if it is a palindrome.

Algorithm: Doubly Linked List forward backward two-pointer
Time Complexity O(n)
Space Complexity O(1)

Information we know
    - Input will be a doubly linked list (if it is not null or empty)
    - Return a boolean value

Edge Cases
    - A single node or empty input, null input
        - make sure to return False
    
Assumptions
    - 
    
Difficulties
    - 
    
Approach
    - Two pointer forward backward doubly linked list approach
    a) Assuming we're not given the tail of the LL, we'll need to do a two pass approach to see the values
    b) We'll have two pointers, both assigned to head to start, labeled L and R. R will traverse the DLL until R.next == None, we'll also keep track of the length we've moved
    c) at that point, we'll do 2 operations while length of l is less than or equal to length of r.
        1) check that the two nodes values are not equal to eachother, if so, return false
        2) otherwise, default to moving the left node forward and iterating the length tracker, and do the same for the right node reducing the length tracker
    d) if the while loop finishes, we have a palindrome and can return True

"""

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
    def printHere(self, head):
        output = ""
        itr = head
        while itr:
            output += str(itr.data) + " <--> "
            itr = itr.next
        return output
    
    def populate(self, arr):
        head = Node(arr[0])
        itrFirst = head
        itrSecond = head
        for i in range(1, len(arr)):
            itrSecond.next = Node(arr[i])
            itrSecond = itrSecond.next
            itrSecond.prev = itrFirst
            itrFirst = itrFirst.next
        return head

def IsPalendrome(head):
    L, R = head, head
    
    if not head:
        return False
    
    lLength, rLength = 0, 0
    while R.next:
        R = R.next
        rLength += 1
    
    while lLength <= rLength:
        if L.data != R.data:
            return False
        L, R = L.next, R.prev
        lLength += 1
        rLength -= 1
    return True
    
    
if __name__ == "__main__":
    vals = [9, 2, 4, 2, 9]
    head = Node(0)
    head = head.populate(vals)
    print("Actual:", IsPalendrome(head), " Expected: True")
    print(head.printHere(head))
    
    vals = [9, 12, 4, 2, 9]
    head = Node(0)
    head = head.populate(vals)
    print("Actual:", IsPalendrome(head), " Expected: False")
    print(head.printHere(head))
    
    head = None
    print("Actual:", IsPalendrome(head), " Expected: False")