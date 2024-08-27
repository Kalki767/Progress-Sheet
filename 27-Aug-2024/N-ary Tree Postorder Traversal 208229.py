# Problem: N-ary Tree Postorder Traversal - https://leetcode.com/problems/n-ary-tree-postorder-traversal/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        '''Approach: dfs. The problem asks to traverse through the tree in a post order
        manner. So to do that we can simply perform depth first search traversal on
        the root and when we reach to the end we simply append that value to our
        answer. It's the same as post order traversal of binary tree the only difference
        here is that we have n childrens instead of two.'''
        answer = []
        def dfs(node):
            if not node :
                return
            for child in node.children:
                dfs(child)
            answer.append(node.val)
            return
        dfs(root)
        return answer
        #Time Complexity: O(n) n is the total number of nodes
        #Space Complexity: O(k) where k is the maximum depth of the tree since we are using stack 
        