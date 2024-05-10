# Problem: Best Time to Buy and Sell Stock with Cooldown - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''Approach: Top Down Dynamic Programming. The problem asks to maximize
        profit given that we can perform as many transactions as we want but
        after we perform one full transaction we need to cooldown for one
        day that means if we decide to sell the stock that we have bought then
        we will skip the next day and go to the day after that day which is
        two steps away other than that the code is similar to the other stock
        problems. The basic difference is we can't buy a stock the moment we
        sell another stock. So at each day we have two choices either
        to buy or sell but that depends on the previous one if we have bought
        previous then we can't buy the current one and vice versa. Therefore
        if we know the state that we are currently at let's say the state is
        buy we can either decide to buy or skip it. If we buy it then the
        next transaction would be sell which will start at day that's two
        steps away from now if not it will stay the same. So we used 
        memoization to improve the time complexity of our algorithm so that 
        we could avoid repetitive work.'''
        memory = {}

        def max_profit(index,buy):
            #if we run out of days there would be no profit to make
            if index >= len(prices):
                return 0

            state = (index,buy)
            if state not in memory: #checking if we have already calculated this value
            
                if buy == 1: #if the state is to buy or not to buy the current stock
                    profit = max(-prices[index]+max_profit(index+1,0),max_profit(index+1,1))
                else:
                    profit = max(prices[index]+max_profit(index+2,1),max_profit(index+1,0))
                memory[state] = profit

            return memory[state]

        return max_profit(0,1)
        #Time Complexity: O(2*n)
        #Space Complexity: O(2*n)