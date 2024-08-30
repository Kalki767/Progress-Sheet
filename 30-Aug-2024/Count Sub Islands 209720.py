# Problem: Count Sub Islands - https://leetcode.com/problems/count-sub-islands/

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        '''Approach: BFS. The problem asks how many islands of grid2 are subislands of
        grid1. That means the island in grid2 also exists in grid1 too. An island is
        a connected land. So easily we can try to check the existence of an island
        in grid1. Which means we can perform breadth first search to find the islands
        in grid2 and if there is no land on those positions that means we know that
        this island isnot a subisland of grid1. For that case we used a helper function
        for checking if it's an island or not. Instead of holding visited set we
        updated the input specifically the lands to waters. Evenif the island is
        not a subisland of grid1 we still need to finish traversing through it.'''

        #Step1: define a function to check if an island is a subisland of grid1
        def check(x,y):

            #if the starting points differ no need to traverse through the rest
            if grid1[x][y] != 1:
                return False

            answer = True
            queue = deque()
            queue.append([x,y])
            grid2[x][y] = 0

            #perform normal bfs
            while queue:
                cur_x, cur_y = queue.popleft()
                for x, y in directions:
                    next_x, next_y = cur_x + x, cur_y + y
                    if inbound(next_x,next_y) and grid2[next_x][next_y] == 1:
                        #if it's not a subisland update the answer
                        if grid1[next_x][next_y] != 1:
                            answer = False
                        
                        #update the grid instead of using a visited set
                        grid2[next_x][next_y] = 0
                        queue.append([next_x,next_y])
            return answer

        #define a function to check if we are still inbound
        def inbound(x,y):
            return 0 <= x < len(grid1) and 0 <= y < len(grid1[0])
        
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        result = 0
        rows = len(grid1)
        cols = len(grid1[0])

        #iterate through the grid and count the islands that are also subislands 
        for row in range(rows):
            for col in range(cols):
                if grid2[row][col] == 1:
                    res = check(row,col)
                    if res:
                        result += 1

        return result
        #Time Complexity: O(n*m)
        #Space Complexity: O(1)