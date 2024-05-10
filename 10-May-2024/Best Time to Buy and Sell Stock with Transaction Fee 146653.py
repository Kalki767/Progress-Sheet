# Problem: Best Time to Buy and Sell Stock with Transaction Fee - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        '''Approach: Top Down Dynamic Programming. The problem asks to maximize
        profit given that we can perform as many transactions we want but
        we will pay for every transaction we made which will decrease our
        profit. So since the only time we are going to have a positive profit
        is when we sell the stock we can only pay the transaction fee then.
        That means whenever we are calculating the profit we need to include
        the transaction fee with it. So at each day we have two choices either
        to buy or sell but that depends on the previous one if we have bought
        previous then we can't buy the current one and vice versa. Therefore
        if we know the state that we are currently at let's say the state is
        buy we can either decide to buy or skip it. If we buy it then the
        next transaction would be sell if not it will stay the same. So we
        used memoization to improve the time complexity of our algorithm
        so that we could avoid repetitive work.'''
        memory = {}
        def max_profit(index,buy):
            #if we exhausted all the days there would be no profit we could make
            if index == len(prices):
                return 0

            state = (index,buy)
            if state not in memory: #checking if we have already calculated this value
                
                if buy == 1: #if the state is to buy or not to buy the current stock
                    profit = max(-prices[index]+max_profit(index+1,0),max_profit(index+1,1))
                else:
                    profit = max(prices[index] - fee + max_profit(index+1,1),max_profit(index+1,0))
                memory[state] = profit

            return memory[state]

        return max_profit(0,1)
        #Time Complexity: O(2*n)
        #Space Complexity: O(2*n)