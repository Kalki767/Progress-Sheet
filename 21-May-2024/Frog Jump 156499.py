# Problem: Frog Jump - https://leetcode.com/problems/frog-jump/

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if len(stones) == 1:
            return True
        if stones[1] - stones[0] > 1:
            return False
        dp = {}
        for stone in stones:
            dp[stone] = set()
        dp[1].add(1)
        stone_set = set(stones)
        for i in range(1,len(stones)):
            stone = stones[i]
            for j in range(-1,2):
                for val in dp[stone]:
                    if val == 1 and j == -1:
                        continue
                    next_stone = val + j + stone
                    if next_stone not in stone_set:
                        continue
                    dp[next_stone].add(val+j)       
        return dp[stones[-1]]
        
