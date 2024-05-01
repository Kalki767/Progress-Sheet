# Problem: Most Stones Removed with Same Row or Column - https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        '''Approach: Union Find. The problem asks to find how many stones
        we can remove from the given stones. A stone can be removed if there
        is atleast one other stone that has either the same row or column
        with the current stone. So basically we need to find if there is
        any stone from the remaining ones that have a connection with the
        current one. This problem in another words is about grouping components
        together. In that case if the stones are connected then we can remove
        at most n - 1 elements from that component so that one element will be
        left out. Therfore all we need to do is group stones that have either
        matching columns or rows. But when finding a stone that matches starting
        from the begnning till the current index we need to make a connection
        between the current one and all the matching ones because there might
        be indirect connections. In that case we won't miss the original parent.'''

        #Step1: initialize the parents and rank for performing union find
        parents = {i:i for i in range(len(stones))}
        rank = {i:0 for i in range(len(stones))}
        mapping = {}

        #Step2: define a function to find the parent of the given node
        def findParents(node):
            if node == parents[node]:
                return node
            parents[node] = findParents(parents[node])
            return parents[node]
        
        #Step3: define a function to merge to nodes together
        def union_find(u,v):
            parent_u = findParents(u)
            parent_v = findParents(v)
            if parent_u == parent_v:
                return
            
            #use union by rank for efficient merging
            if rank[parent_u] < rank[parent_v]:
                parents[parent_u] = parent_v
            elif rank[parent_u] > rank[parent_v]:
                parents[parent_v] = parent_u
            else:
                parents[parent_u] = parent_v
                rank[parent_v] += 1
        
        #Step4: iterate starting from the begnning to the current index to find matching stones
        def find_similar(index):
            row, col = stones[index]
            ans = []

            #Since there might be multiple matches add all of them to our answer
            for i in range(index):
                r, c = stones[i]
                if r == row or c == col:
                    ans.append(i)
            return ans
        
        #Step5: iterate through each stone and create a connection with each of it's matches
        for index in range(len(stones)):
            res = find_similar(index)
            for val in res:
                union_find(val,index)
            mapping[tuple(stones[index])] = index
        
        #Step6: iterate through each coordinate of the stones and update their parent
        result = defaultdict(int)
        for key, value in mapping.items():
            parent = findParents(value)
            result[parent] += 1
        
        #Step7: for each parent take their childrens minus one
        answer = 0
        for key, value in result.items():
            answer += (value - 1)
        
        return answer
        #Time Complexity: O(n**2)
        #Space Complexity: O(n)
