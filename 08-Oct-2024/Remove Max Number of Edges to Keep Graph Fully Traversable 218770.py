# Problem: Remove Max Number of Edges to Keep Graph Fully Traversable - https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/

class UnionFind:
    def __init__(self,size):
        self.parents = {i:i for i in range(1,size+1)}
        self.size = {i:0 for i in range(1,size+1)}
    
    def findParent(self,u):
        if self.parents[u] == u:
            return u
        self.parents[u] = self.findParent(self.parents[u])
        return self.parents[u]
    
    def union(self,u,v):
        parent_u = self.findParent(u)
        parent_v = self.findParent(v)
        if parent_u == parent_v:
            return False
        if self.size[parent_u] > self.size[parent_v]:
            self.parents[parent_v] = parent_u
            self.size[parent_u] += self.size[parent_v]
        else:
            self.parents[parent_u] = parent_v
            self.size[parent_v] += self.size[parent_u]
        return True
    def connected(self,u,v):
       parent_u = self.findParent(u)
       parent_v = self.findParent(v)
       return parent_u == parent_v 

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        '''Approach: Union Find. The problem asks to remove maximum number of edges
        to make the graph traversable or if the graph wasn't traversable in the first
        place then simply return -1. There are three types of edges one is traversable
        by both and the other two are only traversable by one of them. To solve this
        problem let's first build the graph to see who can traverse it or not. Here
        while building one thing to notice is that if the two nodes are connected 
        directly or indirectly then the current edge is unnecessary between them so
        we can remove it. So whenever we are connecting we are checking if the two
        nodes are already connected or not. To check their connectivity we can use
        any traversal method like bfs or dfs but we are doing this multiple times
        so it will make our approach inefficient. So which algorithm checks the
        connectivity of two nodes in a constant time? Union Find! One thing that
        might complicate the problem a little bit is the type of edges. We can observe
        that we need to process edges that can be traversed by both first to remove maximum
        edges because if we have that edge between them then it's better to keep that
        edge instead of two edges. So we will have to graphs for alice and bob. For
        type 3 edges we will simply connect in both of them for the other types we
        will connect the nodes with in their respective person. Then finally after
        building the graph for both of them we check if there is only one connected
        component or not by matching the parent for every node from 1 to n. If at
        least one of them cannot fully traversable we simply return -1 otherwise
        we return how many edges we were able to remove while still keeping the graph
        traversable.'''

        #Step1: sort the edges in reverse order to process type 3 edges first
        edges.sort(key = lambda x : x[0],reverse = True)
        
        answer = 0
        alice = UnionFind(n)
        bob = UnionFind(n)

        #Step2: iterate through the edges and build the network based on the type of edges
        for types, u, v in edges:
            if types == 3:
                if alice.connected(u,v):
                    answer += 1
                    continue
                elif bob.connected(u,v):
                    answer += 1
                    continue
                else:
                    alice.union(u,v)
                    bob.union(u,v)
            elif types == 1:
                if alice.connected(u,v):
                    answer += 1
                else:
                    alice.union(u,v)
            else:
                if bob.connected(u,v):
                    answer += 1
                else:
                    bob.union(u,v)
        
        #Step3: check if there is only one component in both bob and alice
        parent = alice.findParent(1)
        for i in range(1,n+1):
            if alice.findParent(i) != parent:
                return -1
        parent = bob.findParent(1)
        for i in range(1,n+1):
            if bob.findParent(i) != parent:
                return -1

        return answer
        #Time Complexity: O(n + m)
        #Space Complexity: O(2n) where n is the number of nodes and m is the length of edges considering the union operation takes amortized O(1)
        
