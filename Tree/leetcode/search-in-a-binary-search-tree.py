# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        '''Approach: Recursion. The problem asks to find a value in a BST. Here
        we can use that as an advantage so if our current node is none that
        means we haven't found our value if not we check the current value
        with the target. if we haven't found it we search either to the left
        or to the right based on our condition.'''
        def search(node):
            if not node:
                return None
            elif node.val == val:
                return node
            elif val < node.val:
                return search(node.left)
            else:
                return search(node.right)
        return search(root)
        #Time Complexity: O(d) d is depth of the tree
        #Space Complexity: O(d) d if depth of the tree for call stack
