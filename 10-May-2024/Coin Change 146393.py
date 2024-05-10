# Problem: Coin Change - https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        value = {0:0}
        for target in range(1,amount+1):
            value[target] = float('inf')
            for coin in coins:
                if target-coin >= 0:
                    value[target] = min(value[target],value[target-coin]+1)
        return value[amount] if value[amount] != float('inf') else -1