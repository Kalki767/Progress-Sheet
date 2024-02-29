# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        '''Approach: Recursion. The problem asks to traverse a tree in
        preorder. First we traverse the left then the parent then the right
        Therefore here we are doing the same operation for each subtree so
        we can use recursion to handle that.'''
        answer = []
        def preorder(node):
            if not node:
                return
            answer.append(node.val)
            preorder(node.left)
            preorder(node.right)
        preorder(root)
        return answer
        #Time Complexity: O(n) where n is the number of nodes
        #Space Complexity: O(h) where h is the height of call stack

