# Problem: Design Linked List - https://leetcode.com/problems/design-linked-list/

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        #handle invalid indexes
        if index < 0:
            return -1
        
        #iterate until either the index becomes zero or the list got exhausted
        temp = self.head
        while temp and index > 0:
            temp = temp.next
            index -= 1

        #if the current temp that we are at is None then simply return -1
        if not temp:
            return -1

        return temp.val #otherwise return the value at that node

    def addAtHead(self, val: int) -> None:
        #handle the case where the list is empty
        if not self.head:
            self.head = Node(val)
            return
        
        #create a new node and manipulate the links
        current = Node(val)
        current.next = self.head
        self.head = current
        

    def addAtTail(self, val: int) -> None:
        #if the list is empty simply the tail and the head are the same
        if not self.head:
            self.head = Node(val)
            return
        
        #iterate until the list gets exhausted
        temp = self.head
        while temp.next:
            temp = temp.next
        
        #create a new node and update the links
        current = Node(val)
        temp.next = current

    def addAtIndex(self, index: int, val: int) -> None:
        #if the index is less than zero it's invalid
        if index < 0:
            return
        
        #if the index is equal to 0 then it's the same as adding at the head
        if index == 0:
            self.addAtHead(val)
            return
        
        #otherwise create a node and iterate until not the given node but the previous node because we will need the link
        current = Node(val)
        temp = self.head
        while temp and index > 1:
            temp = temp.next
            index -= 1
        
        #if the index was out of bound simply we can't add this value at the given index
        if not temp:
            return
        current.next = temp.next
        temp.next = current
        

    def deleteAtIndex(self, index: int) -> None:
        #if the index is invalid or the list is empty simply return
        if index < 0 or not self.head:
            return
        
        #if the index is 0 only manipulate the head pointer
        if index == 0:
            self.head = self.head.next
            return
        
        #otherwise iterate until the index-1 element and update the links
        temp = self.head
        while temp and index > 1:
            temp = temp.next
            index -= 1
        if not temp or not temp.next:
            return
        temp.next = temp.next.next
   


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)