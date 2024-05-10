# Problem: Climbing Stairs - https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {1:1,2:2}
        def climb(n):
            if n <= 2:
                return n
            if n not in memo:
                memo[n] = climb(n-1) + climb(n-2)
            return memo[n]
        climb(n)
        return memo[n]