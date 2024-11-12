# Problem: Populating Next Right Pointers in Each Node - https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        '''Approach: BFS. The problem asks to update the next pointer for each node.
        The next pointer will point to the right node on the same level if there is
        otherwise it would point to null. To solve this problem we obviously need
        level order traversal. And what traversal can perform level order traversal
        BFS. But let's observe some things here if we perform the normal bfs traversal
        we will definitely use queue that means we will use an extra space but can
        we do it without using extra space. The answer would be yes we can leverage
        the problem behaviour to our benefit. We know that using the next pointer
        we can jump to the sibling of the current node. That means we can traverse
        level wise using the next pointer once we set it. For that matter we can
        traverse and update the next pointer at the same time. While performing
        level order traversal we can update the next pointer of every child of
        the current node. And since the tree is a complete tree we can stop when
        the left node is empty.'''
        if not root:
            return root
        previous_node = root
        while previous_node.left:
            current_node = previous_node
            while current_node:
                if current_node.left:
                    current_node.left.next = current_node.right
                if current_node.next:
                    current_node.right.next = current_node.next.left
                current_node = current_node.next
            previous_node = previous_node.left
        return root
        #Time Complexity: O(n) where n is the the number of nodes
        #Space Complexity: O(1)