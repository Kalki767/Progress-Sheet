# Problem: Most Profit Assigning Work - https://leetcode.com/problems/most-profit-assigning-work/

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        '''Approach: Greedy. The problem asks to calculate the maximum profit
        that could be achieved from each worker by performing some tasks. So
        as explained in the description one task can be performed by multiple
        workers. Therefore the first thing that we are sure is a worker can
        perform some task if it's associated difficulty is greater than or equal
        to the difficulty of that job. So we need to consider all the jobs that
        a worker can do but in the meantime we need the maximum profit among
        them. So we are being greedy on the profit. That means first we need
        to zip the profit and difficulty together because both refer to the
        same task. After that we need to sort both the zipped one and the
        workers because if we sort them then we can iterate through the workers
        and find the tasks whose difficulty is less than them and find the maximum
        profit among them. Finally we need to add the maximum profit gained
        for each worker and return that value.'''

        #Zipping the profit and difficulty together and sorting it
        profit_diff = list(zip(difficulty, profit))
        profit_diff.sort()
        length = len(profit_diff)
        worker.sort()

        #initially the maximum profit is zero and the current profit will be the maximum profit that can be found from previous tasks
        total_profit = 0
        current_profit = 0
        left = 0

        #iterate through the workers and find the profit earned by each worker
        for i in range(len(worker)):
            current = worker[i]

            #find tasks whose difficulty is less than the difficulty of the worker
            while left < length and current >= profit_diff[left][0]:
                current_profit = max(current_profit,profit_diff[left][1]) #take the maximum
                left += 1

            total_profit += current_profit #add the profit earned by the current worker to the total profit we have

        return total_profit

        #Time Complexity: O(nlogn + mlogm)
        #Space Complexity: O(n)