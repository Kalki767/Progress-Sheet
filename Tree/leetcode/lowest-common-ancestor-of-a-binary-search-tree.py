# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''Approach: Recursion. The problem asks to find the lowest common
        ancestor of two nodes. The tree is BST we can use that as an advantage.
        If the current node val is greater than both nodes we move to the left
        If it is less than both nodes we move to the right. Otherwise we return
        that node to the caller. Our Base case is when we reach a leaf node. The
        recurrence relation is what is explained and the state is the root.'''
        if not root:
            return None
        if root.val > p.val and  root.val > q.val:
            return self.lowestCommonAncestor(root.left,p,q)
        elif root.val < q.val and root.val < p.val:
            return self.lowestCommonAncestor(root.right,p,q)
        return root
        #Time Complexity: O(n) n is number of nodes
        #Space Complexity : O(d) d is maximum depth for call stack