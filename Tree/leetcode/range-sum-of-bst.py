# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        '''Approach: Recursion. Traverse through the node and add node values
        which are in the given range and return the result. We used recursion
        for the traversal.'''
        total = 0
        def traversal(node):
            nonlocal total
            if not node:
                return
            if low <= node.val <= high:
                total += node.val
            traversal(node.left)
            traversal(node.right)
        traversal(root)
        return total
        #Time Complexity: O(n)
        #Space Complexity: O(d) where d is maximum depth for call stack