# Problem: Cousins in Binary Tree II - https://leetcode.com/problems/cousins-in-binary-tree-ii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''Approach: BFS Traversal. The problem asks to replace the value of the 
        current node with the sum of it's cousins node. A cousin is a node that have
        the same grand parent or the parent of the cousins are siblings. To solve
        this problem first we need to know the toal sum of one level. After that
        we can find the sum of siblings and the difference between the level sum
        and the siblings sum will be the final answer for the siblings. For this case
        we need to perform the bfs traversal twice. The first one for finding the
        level sum and the second oen for finding the value on each node.'''

        #Step1: Perform bfs traversal to find the level sum for each of the levels
        queue = deque([root])
        level_sum = []
        while queue:
            cur_sum = 0
            length = len(queue)
            for _ in range(length):
                node = queue.popleft()
                cur_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level_sum.append(cur_sum)
        
        #Step2: Perform a second bfs traversal to update the node values
        root.val = 0
        queue = deque()
        queue.append([root,0])
        while queue:
            node, level = queue.popleft()
            #find the sum of the siblings
            child_sum = 0
            if node.left:
                child_sum += node.left.val
            if node.right:
                child_sum += node.right.val
            #update the value of the siblings with the difference
            if node.left:
                node.left.val = level_sum[level+1] - child_sum
                queue.append([node.left,level+1])
            if node.right:
                node.right.val = level_sum[level+1] - child_sum
                queue.append([node.right,level+1])

        return root
        #Time Complexity: O(n) where n is the total number of nodes
        #Space Complexity: O(w) where w is the maximum width of the binary tree
