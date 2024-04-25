# Problem: Redundant Connection - https://leetcode.com/problems/redundant-connection/

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        '''Approach: Union Find. The problem asks given n node to remove an
        edge that is not useful which means that edge is creating a cycle
        in the given graph. To find out that since the graph is connected
        all nodes should represent to the same node at last. Therefore if
        at some point we find two nodes whose parents are already the same
        that means we don't need a new edge betweem them. Therefore we used
        union find to check if the new edge is needed or not by making the
        nodes to point to their representatives. We used rank and path
        compression to increase the efficiency of our algorithm. The rank
        will hold the height of the current node and will be used when we
        are merging two nodes together.'''

        #create the rank and the parent
        n = len(edges)
        rank = {i:1 for i in range(n+1)}
        parent = {i:i for i in range(n+1)}

        # a function for merging two nodes
        def union(x, y):
            #first find the parent of the two nodes
            parent_x = find(x)
            parent_y = find(y)

            #if the height of one of them is greater then the height won't increase but if not the height will increase by one
            if rank[parent_x] > rank[parent_y]:
                parent[parent_y] = parent_x
            elif rank[parent_x] < rank[parent_y]:
                parent[parent_x] = parent_y
            else:
                parent[parent_x] = parent_y
                rank[parent_y] += 1
        
        # a function for finding the parent of a node
        def find(x):
            #if the parent of a node is the node itself then simply return
            if x == parent[x]:
                return parent[x]
            parent[x] = find(parent[x]) #update the parent of the current node to be the ancestor of all
            return parent[x]
        
        #iterate through the edges and perform union operation
        for first, second in edges:

            #if the nodes are already connected then return that edge
            if find(first) == find(second):
                return [first,second]
            
            union(first,second) #otherwise perform the union operation
        #Time Complexity: O(n**2)
        #Space Complexity: O(n)