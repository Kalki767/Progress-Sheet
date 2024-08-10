# Problem: Checking Existence of Edge Length Limited Paths - https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/

class UnionFind:
    def __init__(self,n):
        self.parents = {i:i for i in range(n)}
        self.size = {i:1 for i in range(n)}

    def findParent(self,u):
        if u == self.parents[u]:
            return self.parents[u]
        self.parents[u] = self.findParent(self.parents[u])
        return self.parents[u]

    def union(self,u,v):
        parent_u = self.findParent(u)
        parent_v = self.findParent(v)

        if parent_u == parent_v:
            return 
        if self.size[parent_u] > self.size[parent_v]:
            self.parents[parent_v] = parent_u
            self.size[parent_u] += 1
        else:
            self.parents[parent_u] = parent_v
            self.size[parent_v] += 1
        return
    
    def connected(self,u,v):
        parent_u = self.findParent(u)
        parent_v = self.findParent(v)
        return parent_u == parent_v

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        '''Approach: Union Find. The problem asks to check if two nodes can be connected
        with the given limited distance. So the first thing that we need to do is connect
        nodes that can be connected with the current limit. Then check if the two nodes
        are already connected. if they are that means we were able to connect them if
        not the answer to that query would be no. Therefore we sorted both the query and
        the edgelist based on the distance so that we could connect elements with
        smaller distance first. Then we used union find to check whether the two nodes
        belong to the same componenet or not.'''
        #Step1: create a union find class to check if two elements belong to the same component
        union_find = UnionFind(n)
        
        #Step2: append the index on the end of each query so that we know where it was in the final answer
        for index, query in enumerate(queries):
            query.append(index)

        #Step3: sort both the query and the edgelist based on the distance
        queries.sort(key = lambda x : x[2])
        edgeList.sort(key = lambda x : x[2])
        answer = [False for _ in range(len(queries))]
        index = 0

        #Step4: iterate through each query and connect nodes that can be connected with the current limit
        for query in queries:
            u, v, limit = query[:3]
            while index < len(edgeList) and edgeList[index][2] < limit:
                first, second = edgeList[index][:2]
                union_find.union(first,second)
                index += 1

            #check if the two nodes in the query are already connected with the given limit  
            if union_find.connected(u,v):
                answer[query[3]] = True
        
        
        return answer
        #Time Complexity:O(n+m + nlogn) assuming the union find takes amortized O(1) and m is the length of the query
        #Space Complexity: O(2n) for the union find 