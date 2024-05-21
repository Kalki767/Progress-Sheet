# Problem: Triangle - https://leetcode.com/problems/triangle/

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        rows = len(triangle)
        dp = [float('inf')]
        dp[0] = triangle[0][0]
        for row in range(1,rows):
            current = [float('inf') for i in range(len(triangle[row]))]
            for col in range(len(triangle[row])):
                if col == 0 :
                    current[col] = min(current[col],triangle[row][col] + dp[col])
                elif col == len(triangle[row]) - 1:
                    current[col] = min(current[col],triangle[row][col] + dp[col-1])
                else:
                    current[col] = min(dp[col-1]+triangle[row][col],dp[col]+triangle[row][col],current[col])
            dp = current
        return min(dp)