# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''Approach: Recursion. The problem asks to find the vertical order
        traversal of a tree. Our approach is to track the row and column
        of each node in a dictionary while traversing and sort them based on
        their column. After that we need to sort values for which they have
        the same row and column we can differentiate them in the dictionary
        by their length. Then we should put together values with the same column
        together. Our base case is when we reach the leaf node. Our staes are 
        rows columns and node. At last we will append our dictionary values to
        our answer list'''
        order = defaultdict(list)
        def traversal(row,col,node):
            if not node:
                return
            traversal(row+1,col-1,node.left)
            order[(col,row)].append(node.val)
            traversal(row+1,col+1,node.right)
        traversal(0,0,root)
        sorted_order = dict(sorted(order.items()))
        for key,values in sorted_order.items():
            if len(values) > 1:
                values.sort()
        
        result = defaultdict(list)
        for key,values in sorted_order.items():
            result[key[0]].extend(values)
        answer = [values for values in result.values()]
        return answer
        #Time Complexity: O(n+nlogn) n is number of nodes
        #Space Complexity: O(n+d) n for dictionary and d for call stack