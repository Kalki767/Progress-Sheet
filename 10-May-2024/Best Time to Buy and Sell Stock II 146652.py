# Problem: Best Time to Buy and Sell Stock II - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memory = {}
        def max_profit(index,buy):
            if index == len(prices):
                return 0
            state = (index,buy)
            if state not in memory:
                if buy == 1:
                    profit = max(-prices[index]+max_profit(index+1,0),max_profit(index+1,1))
                else:
                    profit = max(prices[index]+max_profit(index+1,1),max_profit(index+1,0))
                memory[state] = profit
            return memory[state]
        return max_profit(0,1)