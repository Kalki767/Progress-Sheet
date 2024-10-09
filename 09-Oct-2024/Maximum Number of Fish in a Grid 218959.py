# Problem: Maximum Number of Fish in a Grid - https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/

class UnionFind:
    def __init__(self,rows,cols,grid):
        self.parents = {i:i for i in range(rows*cols)}
        self.size = {i:0 for i in range(rows*cols)}
        self.fishes = {i:grid[i//cols][i%cols] for i in range(rows*cols)}
    
    def findParent(self,u):
        if self.parents[u] == u:
            return u
        self.parents[u] = self.findParent(self.parents[u])
        return self.parents[u]
    
    def union(self,u,v):
        parent_u = self.findParent(u)
        parent_v = self.findParent(v)
        if parent_u == parent_v:
            return
        if self.size[parent_u] > self.size[parent_v]:
            self.parents[parent_v] = parent_u
            self.size[parent_u] += self.size[parent_v]
            self.fishes[parent_u] += self.fishes[parent_v]
        else:
            self.parents[parent_u] = parent_v
            self.size[parent_v] += self.size[parent_u]
            self.fishes[parent_v] += self.fishes[parent_u]
class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        '''Approach: Union Find. The problem asks to find the maximum number of fishes
        that the fisher could catch. The fisher could catch fishes if they are neighbours
        To solve this problem we can use multiple approaches. The only thing that
        we need to do is traverse through the graph as long as the neighbours contain
        fishes. For this we can use either bfs or dfs traversal. But here we are using
        Union Find to calculate the total number of fishes in one connected component
        To create a connected component we have one condition that it must have fish.
        One issue here might be how we will store the parents since the given graph
        is in matrix. For that case we will label each cell starting from 0 and we
        will drive some formula to go back to row and col and the label. After that
        we check if either the right next or bottom next element has fishes and we
        connect it with the current. We are not checking the four direction because it
        would be duplicate.'''
        def inbound(row,col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        answer = 0
        rows = len(grid)
        cols = len(grid[0])
        union_find = UnionFind(rows,cols,grid)
        for row in range(rows):
            for col in range(cols): #if the current cell has fishes
                if grid[row][col] > 0:
                    index = row*cols + col
                    #check for the right next and bottom next
                    if inbound(row+1,col) and grid[row+1][col] > 0:
                        union_find.union(index,index+cols)
                    if inbound(row,col+1) and grid[row][col+1] > 0:
                        union_find.union(index,index+1)

        return max(union_find.fishes.values())
        #Time Complexity: O(rows*cols)
        #Space Complexity: O(rows*cols)