# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        '''Approach: Recursion. The problem asks to merge to trees given their
        roots. We used recursive calls both to the left and to the right to 
        maintain their left and right subtrees. Our base case is when either one
        of the trees get exhausted we get back and we don't want to sum values
        since one of them is already exhausted then we can create a new node at
        each recursive call and update it's value and it's left and right childs'''
        if not root1:
            return root2
        elif not root2:
            return root1
        else:
            merged_node = TreeNode(root1.val+root2.val)
            merged_node.left = self.mergeTrees(root1.left,root2.left)
            merged_node.right = self.mergeTrees(root1.right,root2.right)
            return merged_node
        #Time Complexity: O(n) n is number of nodes
        #Space Complexity: O(2*n) for call stack and for creating nodes