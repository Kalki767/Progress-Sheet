# Problem: Balanced Binary Tree - https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        '''Approach: DFS. The problem asks to check if the  given binary tree is balanced
        or not. To check if the root of the tree is balanced or not first we need
        to check the whether the left and right subtrees are balanced or not. For that
        reason all we have to do is perform depth first search and check if a node is
        balanced by checking if it's left and right subtree are also balanced and
        it's height fullfill the criteria'''
        def dfs(node):
            if not node: #if it's the end of a node then that node is balanced
                return 0, True
            left_height, is_left_balanced = dfs(node.left)
            right_height, is_right_balanced = dfs(node.right)

            #check if the current node is balanced
            is_balanced = is_left_balanced and is_right_balanced and abs(right_height - left_height) <= 1

            #update the current height
            current_height = 1 + max(left_height,right_height)
            return current_height, is_balanced

        height, is_balanced = dfs(root)
        return is_balanced
        #Time Complexity: O(n)
        #Space Complexity: O(n) for stack used by the recursion