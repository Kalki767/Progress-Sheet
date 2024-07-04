# Problem: Find All People With Secret - https://leetcode.com/problems/find-all-people-with-secret/

class UnionFind:
    def __init__(self,n):
        self.parents = {i:i for i in range(n)}
        self.rank = {i:0 for i in range(n)}
    
    def findParent(self,u):
        if u == self.parents[u]:
            return u
        self.parents[u] = self.findParent(self.parents[u])
        return self.parents[u]
    
    def union(self,u,v):
        parent_u = self.findParent(u)
        parent_v = self.findParent(v)

        if parent_u == parent_v:
            return
        if self.rank[parent_u] > self.rank[parent_v]:
            self.parents[parent_v] = parent_u
        elif self.rank[parent_v] > self.rank[parent_u]:
            self.parents[parent_u] = parent_v
        else:
            self.parents[parent_v] = parent_u
            self.rank[parent_u] += 1
    
    def reset(self,u):
        self.parents[u] = u
        self.rank[u] = 0
    
    def connected(self,u,v):
        return self.findParent(u) == self.findParent(v)

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetings.sort(key = lambda x : x[2])
        same_time_meetings = defaultdict(list)

        for first, second, time in meetings:
            same_time_meetings[time].append((first,second))

        union_find = UnionFind(n)
        union_find.union(0,firstPerson)

        answer = set([0,firstPerson])
        for key in same_time_meetings:
            for first, second in same_time_meetings[key]:
                union_find.union(first,second)
            
            for first,second in same_time_meetings[key]:
                if not union_find.connected(first,0) :
                    union_find.reset(first)
                    union_find.reset(second)
                
        return [i for i in range(n) if union_find.connected(i, 0)]
        