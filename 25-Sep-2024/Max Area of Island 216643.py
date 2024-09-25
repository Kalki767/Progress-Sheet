# Problem: Max Area of Island - https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        answer = 0
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        def inbound(row,col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        def dfs(row,col):
            counter = 1
            grid[row][col] = 0
            for x, y in directions:
                next_x, next_y = row + x, col + y
                if inbound(next_x,next_y) and grid[next_x][next_y] == 1:
                    counter += dfs(next_x,next_y)
            return counter
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    answer = max(answer,dfs(row,col))
        return answer