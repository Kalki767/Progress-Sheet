# Problem: Reverse Linked List - https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''Approach: traverse through the linked list while changing each
        link backwards and return the head'''
        previous_node = None
        while head:
            temp = head.next
            head.next = previous_node
            previous_node = head
            head = temp
        return previous_node
        #Time Complexity:O(n)
        #Space Complexity:O(1)