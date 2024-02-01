# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #Approach: Floyd's cycle determination algorithm
        '''Step1: assign two pointers that would traverse through the linked
        list simulataneously one faster and the other slower'''
        fast = slow = head
        while fast and fast.next:
            '''Step2:if the fast pointer become equal to the slow pointer
            then the linked list has a cycle'''
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        
        return False
        #Time Complexity:O(n)
        #Space Complexity:O(1)