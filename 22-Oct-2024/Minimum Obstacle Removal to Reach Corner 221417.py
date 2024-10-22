# Problem: Minimum Obstacle Removal to Reach Corner - https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        '''Approach: Shortest Path Dijkstra Algorithm. The problem asks to find the
        minimum number of obstacles that need to be removed to reach the right
        bottom corner. To solve this we need to move with a path that removes the
        minimum among all after that we need to move to the next minimum until we
        explore every path. While traversing we will simply update the number of
        obstacles needed to remove to reach that cell. Finally we will return the
        minimum number of obstacles on the last cell. This is the same as finding
        shortest path using Dijkstra algorithm by treating the obstacles as distances
        and the grid as connected graph.'''

        #a function to check if we are still inbound
        def inbound(row,col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        
        #declare neccessary variables at the start
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        rows = len(grid)
        cols = len(grid[0])
        min_heap = [(grid[0][0],0,0)]
        distances = [[float('inf') for _ in range(cols)] for _ in range(rows)]
        processed = set()

        #perform Dijkstra algorithm on the grid
        while min_heap:
            dist, row, col = heappop(min_heap)
            if (row,col) in processed: #if the node has been processed no need to process it again
                continue
            processed.add((row,col))

            #explore all the four negihbours of it
            for x,y in directions:
                next_row, next_col = row + x, col + y
                #check if the current distance is less than the previous one
                if inbound(next_row,next_col) and dist + grid[next_row][next_col] < distances[next_row][next_col]:
                    heappush(min_heap,(dist + grid[next_row][next_col],next_row,next_col))
                    distances[next_row][next_col] = dist + grid[next_row][next_col]

        return distances[rows-1][cols-1]
        #Time Complexity: O(4*rows*cols)
        #Space Complexity: O(rows*cols)
