#Step1: creating a node class with value parameter to create a singly linked list
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        # if the index is less than 0 then it's invalid index
        if index<0:
            return -1
        temp = self.head
        for i in range(index):
            #if the index is greater than the number of elements then it's also an invalid index
            if not temp:
                return -1
            temp = temp.next
        #if the current index is not null return it's value
        if temp:
            return temp.value
        #if nothing is returned return -1
        return -1

    def addAtHead(self, val: int) -> None:
        #if the head pointer is null assign the new node to the head
        if not self.head:
            self.head = Node(val)
            return
        #if not assign the head to the next pointer and the newNode to the head 
        newNode = Node(val)
        newNode.next=self.head
        self.head=newNode
        

    def addAtTail(self, val: int) -> None:
        #if the head pointer is null assign the new node to the head
        if not self.head:
            self.head = Node(val)
            return
        newNode = Node(val)
        temp = self.head
        #iterate through the linkedlist until the last node and assign the new node to the last node
        while temp.next:
            temp=temp.next
        temp.next = newNode
        

    def addAtIndex(self, index: int, val: int) -> None:
        newNode = Node(val)
        #if index is less than 0 then it's an invalid index so we won't do anything
        if index<0:
            return
        #if the index is 0 then we are inserting at the head so we call the previously defined function
        if index==0:
            self.addAtHead(val)
            return
        temp = self.head
        #iterate through the linkedlist until the element before the index
        for i in range(index-1):
            # if the index is greater than the number of elements simply return because it's an invalid index
            if not temp:
                return
            temp = temp.next
        #if the element before the inserting position is not null then we procceed with the insertion
        if temp:
            newNode.next = temp.next
            temp.next = newNode


    def deleteAtIndex(self, index: int) -> None:
        #if the index is invalid simply return
        if index<0:
            return
        #if the index is 0 delete the head node
        if index==0:
            self.head = self.head.next
            return
        temp = self.head
        #iterate through the linked list until the element before the index
        for i in range(index-1):
            #if the index is greater than the number of elements just simply return
            if not temp:
                return
            temp = temp.next
        #if the element before the deleted element is different from none and the element to be deleted is different from null proceed with deletion
        if temp:
            temp2 = temp.next
            if temp2:
                temp.next = temp2.next
    
        
        

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)