"""
Peter Mora-Stevens
1:00 pm

Question 7. MoveNthLastToFront
Time: 35mins
Solution: 15mins (10mins psuedocode, 5mins coding)
Testcases: 20mins (10mins writing methods, 10mins testing bug... found in method, type in itr name didn't print LL correctly, code worked fine)

Given a singly linked list, move the nth from the last element to the front of the list.

Algorithm: Linked list fixed-distance two-pointer
Time Complexity O(n) # iterating through all values
Space Complexity O(1) # in-space moving nodes

Information we know
    - LL is not in order

Edge Cases
    - LL is Null
    - LL has 1 element
    - LL is made of all the same values (would be hard to show that it changed that is)
    - k is the last element of the list
    - k is first element of the LL, nothing changes (keep track of len, and if len == k, return head)
    
Assumptions
    - LL is made of Int's (though should be confirmed)
    
Difficulties
    - 
    
Approach
    -  Initial approach, still O(n), but more operations, check the len in one pass, after, move tell we hit that node on second pass, and perform node swap
    -  More optimal single pass solution, keep track of num times first pointer has moved, and once it reaches k + 1, allow second pointer to move as well.
    -  then we can make the previous node's next value, = to it's next.next value, and make the k from last node.next our head
    a) assign two pointers to head's node, first and second. k + 1, since we need to track the value prior to k as well, and we don't have access without prior nodes
    b) while loop for first node to traverse to the end of the LL with second following. Loop stops once first.next == None.
    c) we know that once while loop has been terminated, we've reached the end of the list, and can perform our swap operations
    d) store second.next in a temp variable, second.next = second.next.next, cutting our k value from the array
    e) temp.next = head
    f) return temp as new head

"""
class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

    def populate(self, arr):
        head = Node(arr[0])
        itr = head
        for i in range(1, len(arr)):
            itr.next = Node(arr[i])
            itr = itr.next
        return head

    def print(self, head):
        output = ""
        itr = head
        while itr:
            output += str(itr.data) + " --> "
            itr = itr.next
        return output

def NthLastToFront(head, k):
    if not head:
        return Node(-1)
    if head.next == None:
        return head
    
    first, second, length = head, head, 1
    while first.next:
        if length >= k + 1:
            second = second.next
        first = first.next
        length += 1
    
    if length == k:
        return head
    
    temp = second.next
    second.next = second.next.next
    temp.next = head
    return temp

if __name__ == "__main__":
        # len = 3, k = 2, temp = 6
        #                          s      f
    arr, k = [15, 2, 8, 7, 20, 9, 11, 6, 19], 2
    head = Node(0)
    head = head.populate(arr)
    head = NthLastToFront(head, k)
    print("Actual: ", head.print(head), "Expected: 6, 15, 2, 8, 7, 20, 9, 11, 19")
    
    arr, k = [15, 2, 8, 7, 20, 9, 11, 6, 19], 7
    head = Node(0)
    head = head.populate(arr)
    head = NthLastToFront(head, k)
    print("Actual: ", head.print(head), "Expected: 8, 15, 2, 7, 20, 9, 11, 6, 19")
    
    arr, k = [15, 2, 8, 7, 20, 9, 11, 6, 19], 9
    head = Node(0)
    head = head.populate(arr)
    head = NthLastToFront(head, k)
    print("Actual: ", head.print(head), "Expected: 15, 2, 8, 7, 20, 9, 11, 6, 19")
    
    head = NthLastToFront(None, k)
    print("Actual: ", head.print(head), "Expected: -1")
    
    arr, k = [15], 1
    head = Node(0)
    head = head.populate(arr)
    head = NthLastToFront(head, k)
    print("Actual: ", head.print(head), "Expected: 15")