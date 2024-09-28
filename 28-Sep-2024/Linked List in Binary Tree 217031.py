# Problem: Linked List in Binary Tree - https://leetcode.com/problems/linked-list-in-binary-tree/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        '''Approach: DFS. The problem asks to check if the given linked list appear
        as some sequence in the given binary tree. To check this we need to traverse
        the given binary tree and linked list. The starting point might differ from
        the head that means for every node we need to traverse through the binary
        tree considering it as a starting point. While traversing if the current
        tree value is different than the linkedlist value we immediately return False
        as this is not the sequence. Otherwise we continue traversing and if the
        linkedlist gets exhausted we have found a sequence but if the tree gets
        exhausted this can't be a valid sequence so we return False'''
        def dfs(tree_node, list_node):
            if not list_node:  # Linked list fully matched
                return True
            if not tree_node:  # Tree ended before matching the linked list
                return False
            if tree_node.val == list_node.val:
                # Continue matching down the tree
                return dfs(tree_node.left, list_node.next) or dfs(tree_node.right, list_node.next)
            return False

        def traverse(tree_node):
            if not tree_node:
                return False
            # Start DFS if values match at current tree node or continue traversing
            return dfs(tree_node, head) or traverse(tree_node.left) or traverse(tree_node.right)

        return traverse(root)
        