# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        '''Approach: Recursion. The problem asks to find the modes of a BST 
        to do that we need to count the occurence of each element and we take
        the maximum frequen element and if there are many elements with maximum
        frequency we will return them all. To count the occurence we can use
        any traversal method and we use a helper function to traverse the tree
        and call it recursively until our node is empty'''
        counter = defaultdict(int)
        def traversal(node):
            if not node:
                return
            traversal(node.left)
            counter[node.val] += 1
            traversal(node.right)
        traversal(root)
        maximum = max(counter.values())
        answer = []
        for key,value in counter.items():
            if value == maximum:
                answer.append(key)
        return answer
        #Time Complexity: O(n) where n is the number of nodes
        #Space Complexity: O(d) where d is the depth of the tree