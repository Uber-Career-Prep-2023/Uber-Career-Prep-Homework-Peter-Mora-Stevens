class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    # Time Complexity: O(1) as we're given the head, and we simply add a node before
    def insertAtFront(self, head, val):
        newNode = Node(val)
        newNode.next = head
        return newNode

    # Time Complexity: O(n) as we're visiting every node until we reach the end of the LL
    def insertAtBack(self, head, val):
        itr = head
        while itr.next != None:
            itr = itr.next
        newNode = Node(val)
        itr.next = newNode
        
    # Time Complexity: O(1) as we're given the node in which we will be inserting after
    def insertAfter(self, val, loc):
        newNode = Node(val)
        newNode.next = loc.next
        loc.next = newNode

    # Time Complexity: O(1) as we're simply removing the first node, and that only requires changing the next ref and reassigning head
    def deleteFront(self, head):
        head = head.next
        return head

    # Time Complexity: O(n) as we're traversing the LL to get to the end and delete the last node
    def deleteBack(self, head):
        itr = head
        while itr.next.next != None:
            itr = itr.next
        itr.next = None
    
    # Time Complexity: O(n) as we're at worst case, traversing the entire list until we find the given nodes location
    def deleteNode(self, head, loc):
        itr = head
        while itr.next != loc:
            itr = itr.next
        itr.next = loc.next
        return head
    
    # Time Complexity: O(n) as we're having to look through every element in the LL
    def length(self, head):
        count, itr = 0, head
        while itr != None:
            itr = itr.next
            count += 1
        return count
    
    # Time Complexity: O(n) as we must visit every node to reverse the connections
    def reverseIterative(self, head):
        curr, tail = head, None
        while curr != None:
            temp = curr.next
            curr.next = tail
            tail = curr
            curr = temp
        return tail
    
    def reverseRecursive(self, head):
        pass
    
# Time Complexity: O(n) visits every node to print them
    def printNodes(self, head):
        output = ""
        itr = head
        while itr != None:
            output += str(itr.data) + "-->"
            itr = itr.next
        print(output)

if __name__ == "__main__":
    head = Node(10)
    secondNode = Node(20)
    head.next = secondNode
    head = head.insertAtFront(head, 100)
    head.insertAtBack(head, 70)
    head.insertAfter(100000, secondNode)
    head = head.deleteFront(head)
    #head = head.deleteNode(head, head.next.next)
    #head.deleteBack(head)
    head = head.reverseIterative(head)
    head.printNodes(head)
    print(head.length(head))