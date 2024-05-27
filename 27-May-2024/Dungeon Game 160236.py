# Problem: Dungeon Game - https://leetcode.com/problems/dungeon-game/

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        '''Approach: Bottom up Dp. The problem asks to find the minimum
        health the knight need to have so that he could save the princess.
        For that matter we need to choose a path that has the least cost.
        So we started from the bottom right and move our way up to the princess.
        We take the minimum at each stage and update the health needed. If
        at any point we need another health and the previous was zero then
        we increment what we will have by one.'''
        rows = len(dungeon)
        cols = len(dungeon[0])
        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        if dungeon[-1][-1] <= 0:
            dp[-1][-1] = abs(dungeon[-1][-1]) + 1

        for row in range(rows-2,-1,-1):
            if dungeon[row][cols-1] > dp[row+1][cols-1]:
                continue
            else:
                dp[row][cols-1] = dp[row+1][cols-1] - dungeon[row][cols-1]
                if dp[row+1][cols-1] == 0:
                    dp[row][cols-1] += 1

        for col in range(cols-2,-1,-1):
            if dungeon[rows-1][col] > dp[rows-1][col+1]:
                continue
            else:
                dp[rows-1][col] = dp[rows-1][col+1] - dungeon[rows-1][col]
                if dp[rows-1][col+1] == 0:
                    dp[rows-1][col] += 1

        for row in range(rows-2,-1,-1):
            for col in range(cols-2,-1,-1):
                current = min(dp[row+1][col],dp[row][col+1])
                if dungeon[row][col] > current:
                    continue
                else:
                    dp[row][col] = current - dungeon[row][col]
                    if current == 0:
                        dp[row][col] += 1

        return dp[0][0] if dp[0][0] != 0 else 1
        #Time Complexity: O(n**2)
        #Space Complexity: O(n**2)