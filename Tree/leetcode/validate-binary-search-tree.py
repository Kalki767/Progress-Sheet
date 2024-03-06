# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        '''Approach: Recursion. The problem asks to check whether the given
        binary tree is valis BST or not. To check that we need to look for
        invalid values at each level. That means we need to validate both
        the left and right subtrees recursively until we reach the leaf node.
        Our basecase is when we reach the leaf node in which that subtree is
        valid and if we found invalid value anywhere in the middle we return
        false to the caller. At last we return if both the left and right 
        subtrees are valid or not which is our recurrence relation. Our states
        are the current node and it's left and it's right values which will be
        updated as we go down. When we go to the left it's right value will be
        updated and viceversa.'''
        def valid(node,left,right):
            if not node:
                return True
            elif not (left < node.val < right):
                return False
            else:
                return valid(node.left,left,node.val) and valid(node.right,node.val,right)
        return valid(root,float('-inf'),float('inf'))
        #Time Complexity: O(n) n is number of nodes
        #Space Complexity: O(d) where d is maximum depth for call stack