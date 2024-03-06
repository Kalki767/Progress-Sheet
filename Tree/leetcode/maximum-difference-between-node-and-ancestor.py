# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        '''Approach: Recursion. The problems asks to find the maximum absoulte
        difference between an ancestor and a node. We use recursive call to
        call the left and right subtrees while updating the maximum and the 
        minimum along that path. Then the maximum difference is the maximum of
        either the current value minus the minimum or maximum. Therefore our
        base case is when we reached a leaf node at each stage we don't return
        anything we just update the maximum value our states are the current
        node the maximum and the minimum along that path until the current element
        starting from the root.'''
        max_difference = 0
        def maxdifference(node,maximum,minimum):
            nonlocal max_difference
            if not node:
                return
            max_difference = max(abs(node.val-maximum),abs(node.val-minimum),max_difference)
            maximum = max(maximum,node.val)
            minimum = min(minimum,node.val)
            maxdifference(node.left,maximum,minimum)
            maxdifference(node.right,maximum,minimum)
        maxdifference(root,root.val,root.val)
        return max_difference
        #Time Complexity: O(n) n is number of nodes
        #Space Complexity: O(d) d is maximum depth of call stack