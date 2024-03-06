# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        '''Approach: Recursion. The problem asks to find the kth smallest
        element in a BST. Here we have two approaches. The first one is
        since Inorder traversal of BST results in sorted order we can just
        return the k-1 element since k is 1 indexed. But here we are using
        extra space to store our elements. But since it's a BST we can use
        that to our cause the smallest element will be left most side. That
        means once we reach the left most we can start counting as we
        recursively call the right subtree and go back then when our
        counting reaches k then we can return back and update our answer.
        This way we won't be using any extra space. But their time complexity
        is the same. '''
        answer = counter = 0
        def traversal(node,k):
            nonlocal counter,answer
            if not node:
                return
            traversal(node.left,k)
            counter +=1
            if counter == k:
                answer = node.val
                return 
            traversal(node.right,k)
        traversal(root,k)
        return answer
        #Time Complexity: O(n) n is number of nodes
        #Space Complexity: O(d) where d is maximum depth of the call stack