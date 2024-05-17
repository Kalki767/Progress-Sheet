# Problem: Unique Paths II - https://leetcode.com/problems/unique-paths-ii/

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        '''Approach: Bottom Up Dynamic Programming. The problem asks to reach
        the target but we can't follow any path that has obstacle in it. So we
        need to count the unique paths that will lead us to the last cell. The
        only difference with the problem unique path is there is obstacle in
        our path. Therefore we can resuse the same code with a little modification
        We need to check if the current cell has obstacle or not. If it have
        then it cannot be path if it doesn't have then it can be a path. So
        we accumulate our previously calculated values in our dp matrix. We
        are iterating from the target to zero so the final answer would be
        stored at index 0.'''
        #if there is an obstacle either in the last cell or the starting cell simply return 0
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[rows-1][cols-1] or obstacleGrid[0][0]:
            return 0
        
        #initialize our dp matrix and the base case
        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        dp[rows-1][cols-1] = 1
        for row in range(rows-1,-1,-1):
            for col in range(cols-1,-1,-1):
                if obstacleGrid[row][col] != 1: #if the current cell has obstacle cannot be path
                    down = right = 0
                    if row < rows - 1: #ways to jump to the current state from the below
                        down = dp[row+1][col]
                    if col < cols - 1: #ways to jump to the current state from the right
                        right = dp[row][col+1]

                    dp[row][col] += down + right #update the current state

        return dp[0][0]
        #Time Complexity: O(n**2)
        #Space Complexity: O(n**2)

        '''Top Down Approach:
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[rows-1][cols-1] or obstacleGrid[0][0]:
            return 0
        memory = {}
        def dp(row,col):
            if row == len(obstacleGrid) - 1 and col == len(obstacleGrid[0]) - 1:
                return 1
            state = (row,col)
            if state not in memory:
                down = right = 0
                if row < len(obstacleGrid) - 1 and obstacleGrid[row+1][col] != 1:
                    down = dp(row+1,col)
                if col < len(obstacleGrid[0]) - 1 and obstacleGrid[row][col+1] != 1:
                    right = dp(row,col+1)
                memory[state] = down + right
            return memory[state]
        return dp(0,0)
        '''