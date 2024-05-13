# Problem: Minimum Cost For Tickets - https://leetcode.com/problems/minimum-cost-for-tickets/

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        '''Approach: Top-Down Dynamic Programming. The problem asks given the
        cost of buying tickets we are asked to return the minimum number of
        dollars needed to travel all the days. So what we basically did here
        is break the problem into subproblems. Starting from the first index
        we will have 3 choices either buying the one way ticket the 7 day or
        the 30 day pass. So depending on the ticket we bought we will reach
        that day and try going that way until we exhaust all the given days.
        That means the base case will be when we ran out of bounds. Here we
        will have overlapping subproblems so inorder to optimize time we will
        use memoization.'''
        memory = {}
        def Cost(index):
            if index >= len(days):
                return 0
            #use memoization for efficient algorithm
            if index not in memory:
                #find the next state using binary search since the days are already sorted
                seven_index = bisect_left(days,days[index]+7)
                thirty_index = bisect_left(days,days[index]+30)
                memory[index] = min(costs[0] + Cost(index+1),costs[1]+Cost(seven_index),costs[2]+Cost(thirty_index))

            return memory[index]

        return Cost(0)
        #Time Complexity: O(n)
        #Space Complexity: O(n)