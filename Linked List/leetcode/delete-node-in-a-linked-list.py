# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        '''Approach: Since we don't know the address of the node that appears
        before the given node what we can do is move one step and change the
        value of the current node to be the value of the next node after that
        we can delete the next node from our linked list'''
        node.val = node.next.val
        node.next = node.next.next