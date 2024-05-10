# Problem: IPO - https://leetcode.com/problems/ipo/

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        '''Approach: Greedy. The problem asks given an intial capital we are
        asked to find the maximize our profit given that we can only perform
        k projects. So we need to be greedy on our choices that means if
        we have multiple projects that could be done using our current capital
        we need to choose the one with the maximum profit so as to maximize
        our profit. The first thing that we will be needing is the projects
        that we could complete using the current capital. And how do we get
        that after we zip together the capital and the profit we can sort it
        using the capital as a key. Then we will hold the projects that we
        can complete using the current capital. After that we need to float
        out the one with maximum profit out of all those. Therefore at each
        stage we need a project that has maximum profit out of all the projects
        that we could complete. And which datastructure is better for that
        heap. So we will use max heap to float projects with maximum profit.
        '''
        #Step1: zip the profit and capital together and sort it
        capital_profit = []
        for i in range(len(profits)):
            capital_profit.append([capital[i],profits[i]])
        capital_profit.sort()
        max_heap = []
        index = 0

        #Step2:iterate until k since we have k projects and take maximum profit
        for i in range(k):

            #if the required capital is less than or equal to our current capital add it's profit tp our heap
            while index < len(profits) and capital_profit[index][0] <= w:
                curr_capital, profit = capital_profit[index]
                heappush(max_heap,-profit)
                index += 1
                
            #add the maximum profit to our capital
            if max_heap:
                curr_profit = -heappop(max_heap)
                w += curr_profit

        return w
        #Time Complexity: O((n+k)logm + nlogn) where m is number of elements in our heap
        #Space Complexity: O(n)
