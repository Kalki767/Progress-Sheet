# Problem: Minimum Score of a Path Between Two Cities - https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/description/

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        '''Approach: Union Find. The problem asks to find the minimum edge
        between 1 and n when we mean by that even if the current cities
        are not leading to n as long as they are connected with 1 they need
        to be consider in the minimum calculation. We can use different approaches
        like dfs or bfs but we will be using union find for this problem.
        Therefore we just need to make cities that are indirectly connected
        to one make them connected. After that if the parent of any city is
        one then we will calculate the minimum score.'''

        #Step1: initialize the parents for union find
        parents = {i:i for i in range(1,n+1)}
        

        #Step2: define a function to find a parent of node using path compression
        def findParents(node):
            if node == parents[node]:
                return node
            parents[node] = findParents(parents[node])
            return parents[node]
        
        #Step3: define a function for merging two nodes
        def union_find(u,v):
            parent_u = findParents(u)
            parent_v = findParents(v)
            if parent_u == parent_v:
                return
            
            #connect the two cities to the smaller one so that one would be the parent
            if parent_u < parent_v:
                parents[parent_v] = parent_u
            else:
                parents[parent_u] = parent_v
        
        #Step4: iterate through each city and merge them
        for u, v, w in roads:
            union_find(u,v)
        
        #for each city if their parent is one then find the minimum score
        answer = float('inf')
        for u, v, w in roads:
            parent = findParents(u)
            if parent == 1:
                answer = min(answer,w)
            
        return answer
        #Time Complexity: O(n)
        #Space Complexity: O(n)