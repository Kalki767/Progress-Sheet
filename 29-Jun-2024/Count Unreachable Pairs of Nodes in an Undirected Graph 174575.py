# Problem: Count Unreachable Pairs of Nodes in an Undirected Graph - https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/

class UnionFind:
    def __init__(self,n):
        self.size = {i:1 for i in range(n)}
        self.parents = {i:i for i in range(n)}

    def findParent(self,u):
        if u == self.parents[u]:
            return u
        self.parents[u] = self.findParent(self.parents[u])
        return self.parents[u]
    
    def union_by_size(self,u,v):
        parent_u = self.findParent(u)
        parent_v = self.findParent(v)

        if parent_u == parent_v:
            return
        if self.size[parent_u] > self.size[parent_v]:
            self.parents[parent_v] = parent_u
            self.size[parent_u] += self.size[parent_v]
        else:
            self.parents[parent_u] = parent_v
            self.size[parent_v] += self.size[parent_u]

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        '''Approach: Union Find. The problem asks to find the number of
        unreachable nodes from each other. In other words we need to find
        connected component and from each node we are going to count how
        many nodes are not connected with it. For this reason we need to
        know which component is connected together. And which datastructure
        is suitable for this? Union Find!. Therefore all we have to do is
        perform union find but we have two version of union find one is by
        rank the other is by size we have to use by size here because we
        want to avoid another work to count the number of nodes in one
        connected components. Therefore if we know how many elements are
        there in one connected component then the number of pair would be
        the remaining nodes that are not in that component. If we have
        m nodes then we would have m times the remaining components would
        be created from that component only. Finally since we double counted
        we need to divide it by two.'''

        # create an object to access the methods and variables of the class
        union_find = UnionFind(n)
        for u, v in edges:
            union_find.union_by_size(u,v) #connect the components

        # intialize to handle the parents of the connected component   
        parents = set()
        for i in range(n):
            parent = union_find.findParent(i)
            parents.add(parent)
        
        #iterate through each component and calculate the number of pairs
        answer = 0
        for parent in parents:
            current = union_find.size[parent] * ((n - union_find.size[parent]))
            answer += current
       
        return answer//2
        #Time Complexity: O(n)
        #Space Complexity: O(n)