# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''Approach: Recursion. The problem asks to traverse a tree in zigzag
        level. To do that all we have to do is perform any kind of traversal
        we want and store the values with the same row together using a 
        dictionary Then we can reverse our values for those which are not divisible
        by 2. Our states are the current node and the current row everytime we
        go down we increment our row by one and Our basecase is when we reach a
        leaf node we return back. The recurrence relation is just the traversal.'''
        answer = defaultdict(list)
        def traversal(node,row):
            if not node:
                return 
            answer[row].append(node.val)
            traversal(node.left,row+1)
            traversal(node.right,row+1)
        traversal(root,0)
        values = []
        for key,value in answer.items():
            if key%2!=0:
                value.reverse()
            values.append(value)
        return values
        #Time Complexity: O(n) n is number of nodes
        #Space Complexity: O(d) where d is maximum depth of call stack