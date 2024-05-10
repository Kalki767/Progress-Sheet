# Problem: Best Time to Buy and Sell Stock - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minimum_price = prices[0]
        for price in prices:
            if price < minimum_price:
                minimum_price = price
            else:
                profit = max(profit,price-minimum_price)
        return profit