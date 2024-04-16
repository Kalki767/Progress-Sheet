# Problem: Delete Nodes And Return Forest - https://leetcode.com/problems/delete-nodes-and-return-forest/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        '''Approach: DFS. The problem asks to return set of nodes after deleting
        list of nodes from the tree. Since after deletion the tree will be turned
        into forest we need to hold the start node of every forest. The problem
        can be solved using both dfs and bfs. Here we will solve it using dfs.
        The intution of dfs is going depth therefore we went depth first and when
        we reach a leaf node we check if it's going to be deleted or not. If
        it's going to be deleted then we don't need that node therefore we need
        to break the link between it's parent and the node by returning none.
        But the deleted node might have childs since we are going from bottom
        to up for checking the elements to be deleted we can simply add the
        childs of the deleted node to our result because they won't be deleted
        after their parent has been deleted. If the current node isnot the one
        that gets deleted we simply return the node to the caller.'''
        answer = []
        to_delete_set = set(to_delete) #convert it to set for efficeint access

        #perform normal dfs traversal
        def dfs(node):
            if node is None: #base case
                return None
            #find the left and right child of the current_node
            node.left = dfs(node.left) 
            node.right = dfs(node.right)

            #if the current node needs to be deleted then we need to add the childs of it to our answer since we are going bottom up
            if node.val in to_delete_set:
                if node.left:
                    answer.append(node.left)
                if node.right:
                    answer.append(node.right)
                return None
            #otherwise return the current node to the caller
            return node
        last = dfs(root)
        #if the root is not going to be deleted append it to the list
        if last:
            answer.append(root)

        return answer
        #Time Complexity: O(V+E)
        #Space Complexity: O(d) where d is maximum depth of the tree for recursion stack
