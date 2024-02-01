# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''Approach: traverse through the linked list while checking if the
        current element and the next element are the same if they are delete
        that node from the linked list and continue iteration if not just move
        the temp one step'''
        if not head:
            return head
        temp = head
        while temp.next:
            if temp.val == temp.next.val:
                temp.next = temp.next.next
            else:
                temp = temp.next
        
        return head
        #Time Complexity:O(n)
        #Space Complexity:O(1)