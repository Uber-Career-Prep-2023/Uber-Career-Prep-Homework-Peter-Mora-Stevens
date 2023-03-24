class Node():
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
        
    # time complexity: O(1) we resassign the newNode's next pointer to be the current head
    #                  and assign the current head's prev pointer to the newNode. 
    def insertAtFront(self, head, val):
        newNode = Node(val)
        newNode.next = head
        head.prev = newNode
        return newNode
    
    # time complexity: O(n) we must visit every node until we reach the end and add our new last node
    def insertAtBack(self, head, val):
        newNode = Node(val)
        itr = head
        while itr.next != None:
            itr = itr.next
        itr.next = newNode
        newNode.prev = itr
        
    # time complexity: O(1) as we're given a node we want to insert after
    def insertAfter(self, val, loc):
        newNode = Node(val)
        newNode.next = loc.next
        if loc.next != None:
            loc.next.prev = newNode
        loc.next = newNode
        newNode.prev = loc
        
    # time complexity: O(1) as we're simply removing the front node and reassigning head to head.next as well as removing prev pointer
    def deleteFront(self, head):
        newHead = head.next
        head.next = None
        newHead.prev = None
        return newHead
    
    # time complexity: O(n) as we must traverse the entire LL until we reach the last node
    def deleteBack(self, head):
        itr = head
        while itr.next != None:
            itr = itr.next
        itr.prev.next = None
        itr.prev = None
    
    # time complexity: O(1) since we're given the node to delete, we just set next and prev pointers to updated values
    def deleteNode(self, head, loc):
        if head == loc:
            head = head.deleteFront(head)
            return head
        
        loc.prev.next = loc.next
        if loc.next != None:
            loc.next.prev = loc.prev
        loc.prev = None
        loc.next = None
        return head
    
    # time complexity: O(n) since we must visit every element in the LL to find the length of it.
    def length(self, head):
        length = 0
        itr = head
        while itr != None:
            length += 1
            itr = itr.next
        print(length)
        
    # time complexity: O(n) as we must visit every single node to reverse the connections between .next and .prev
    def reverseIterative(self, head):
        curr, tail = head, None
        while curr != None:
            temp = curr.next
            curr.next = tail
            curr.prev = temp
            tail = curr
            curr = temp
        return tail
    
    def reverseRecursive(self, head):
        pass
    
    def printNodes(self, head):
        output = ""
        itr = head
        while itr != None:
            output += str(itr.data) + "<-->"
            itr = itr.next
        print(output)
    
        


if __name__ == "__main__":
    head = Node(10)
    head = head.insertAtFront(head, 20)
    head.insertAtBack(head, 100)
    head.insertAfter(50, head.next.next)
    head.insertAtBack(head, 765433)
    head = head.insertAtFront(head, 2000000)
    #head = head.deleteFront(head)
    #head.deleteBack(head)
    #head = head.deleteNode(head, head.next.next)
    head = head.reverseIterative(head)
    head.printNodes(head)
    head.length(head)