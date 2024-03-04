# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        '''Approach: Recursion. The problem asks to check whether or not the
        two trees are the same or not. We can check that by if both nodes are
        empty we return true if one of them is not empty we return false to
        the caller. otherwise we check if their values are equal or not.'''
        if not p and not q:
            return True
        elif not p or not q:
            return False
        else:
            return p.val == q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        #Time Complexity: O(n) n is number of nodes
        #Space Complexity: O(d) d is maximum depth for call stack