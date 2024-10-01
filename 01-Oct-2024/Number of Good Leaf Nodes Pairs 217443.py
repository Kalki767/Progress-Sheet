# Problem: Number of Good Leaf Nodes Pairs - https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self,root: TreeNode, distance: int) -> int:
        '''Approach: DFS. The problem asks to find the number of pairs of leaf nodes
        that have a distance of less than or equal to the given distance. To solve
        this problem starting from each node we need to know the distance to the
        leaf node both in the left and right subtrees and for that we will use
        Dfs for traversing through the tree. So whenever we reach the leaf node the
        distance is obviously one upon backtracking we find that the distance would
        be one plus the distance that we have found. At this point once we have the
        distances we can calculate the total distance and if it's less than the given
        distance we add the number of good pairs by one.'''
        good_pairs = 0

        # Helper DFS function
        def dfs(node):
            nonlocal good_pairs
            
            if not node:
                return []
            
            # If it's a leaf node, return a list with a single element 1 (distance 0)
            if not node.left and not node.right:
                return [1]
            
            # Get the distances of leaf nodes from the left and right subtrees
            left_distances = dfs(node.left)
            right_distances = dfs(node.right)
            
            # Check all pairs of leaves, one from left subtree and one from right subtree
            for left in left_distances:
                for right in right_distances:
                    if left + right <= distance:
                        good_pairs += 1
            
            # Return the distances of all leaf nodes to the current node, incremented by 1
            return [d + 1 for d in left_distances + right_distances if d + 1 <= distance]

        # Call the DFS from the root node
        dfs(root)
        
        # Return the total number of good pairs
        return good_pairs
        #Time Complexity: O(n**2) where n is the number of leaf nodes
        #Space Complexity: O(m) for recursion stack where m is the maximum depth
