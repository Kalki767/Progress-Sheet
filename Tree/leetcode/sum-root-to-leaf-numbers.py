# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        '''Approach: Recursion. The problem asks to sum all paths starting 
        from the root to the leaf. To do that we need to calculate the path
        at each traversal the way we do that is just by passing the path
        as a parameter meaning as a state and update it to the current path
        multiplied by 10 plus the current value. We know that a path comes
        to an end when it doesn't have any child. Therefore we have two base
        case one when the node doesn't have any child where we will end up
        updating our sum and the other is just a dead end and we have to 
        return back. The recurrence relation is just the one that is
        mentioned which is updating the path one thing we don't want to forget
        is we need to update the path when we found a node with no child too.'''
        answer = 0
        def SumNumbers(node,path):
            nonlocal answer
            if not node:
                return
            elif node.left is None and node.right is None:
                path = path *10 + node.val
                answer += path
                return
            path = path*10 + node.val
            SumNumbers(node.left,path)
            SumNumbers(node.right,path)
        SumNumbers(root,0)
        return answer
        #Time Complexity: O(n) where n is number of nodes
        #Space Complexity: O(d) where d is maximum depth of call stack
