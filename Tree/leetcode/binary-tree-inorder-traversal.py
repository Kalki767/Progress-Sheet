# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        '''Approach: Recursion. To traverse in postorder first we go to the
        left as much as possible then when we meet a dead end we append that
        value to our list and go the right node as possible.'''
        answer = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            answer.append(node.val)
            inorder(node.right)
        inorder(root)
        return answer
        #Time Complexity: O(n) n is number of nodes
        #Space Compelxity: O(d) d is depth of the tree