# Problem: Maximum Depth of Binary Tree - https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        '''Approach: BFS. The problem asks to find the maximum depth of a
        binary tree. So we can traverse in two ways either with dfs or bfs.
        if we traverse in dfs we need to take the maximum depth whenever
        we reach a leaf node. but if we traverse bfs level wise we can
        increment the distance by one at each level and when we are done
        iterating through all of the elements we will have the maximum depth
        available.'''
        distance = 0
        # If the given root is empty then the distance is empty we can't traverse an empty tree
        if not root:
            return distance
        
        #otherwise perform bfs traversal
        queue = deque()
        queue.append(root)
        while queue:
            Boundary = len(queue)

            for _ in range(Boundary): #for level order traversal
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            distance += 1 #increment the distance by one at the end of each level

        return distance
        #Time Complexity: O(V+E)
        #Space Complexity: O(d) where d is maximum number of elements in the queue at a time