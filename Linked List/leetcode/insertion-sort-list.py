# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''Approach:making the list a doubly linked list to iterate through
        both forward and backward'''
        #Step1: make the list a doubly linked list by using a dummy node
        prev = None

        '''Step2: define a function that will return the previous node given
        that the current node and it's next are passed as argument'''
        def prevs(node,prev):
            node.prev = prev

        #Step3: iterate through the list to find all previous elements
        temp = head
        head.prev = None
        while temp.next:
            prevs(temp.next,temp)
            temp = temp.next
        
        #Step4: iterate through the list and perform insertion sort
        left  = head
        while left.next:
            right = left.next
            while right and right.prev and right.val<right.prev.val:
                right.val, right.prev.val = right.prev.val, right.val
                right = right.prev
            left = left.next
        return head
    