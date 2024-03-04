# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        '''Approach: Recusrsion. The problem asks if the right side of the
        tree is a mirror of the left side. We can divide the problem into
        subproblems by checking if the left subtree is symmetric and if the
        right subtree is symmetric then we can join their results. Therefore
        we use a recursion to do that if a both left and right doesn't have 
        any child then it means it's symmetric. if one of them is null it's 
        not symmetric other wise we check their value and their subtree'''
        def symmetric(left,right):
            if not left and not right:
                return True
            elif not left or not right:
                return False
            else:
                return left.val == right.val and symmetric(left.left,right.right) and symmetric(left.right,right.left)
        return symmetric(root.left,root.right)
        #Time Complexity: O(n) n is number of nodes
        #Space Complexity: O(d) for call stack maximum depth