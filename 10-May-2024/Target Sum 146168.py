# Problem: Target Sum - https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        '''Approach: Top Down Dynamic Programming. The problem asks to find
        all the ways to get to the target. The given rules are we can use 2
        sign of a number. Both positive and negative. So at each step we
        can use either positive or negative of that element. So when we
        reach the end we check if our current sum is equal with our target
        in that case we count that as one way. So it's basically recursive
        solution but the problem is we might arrive to an index using different
        ways so in that case we don't need to recalculate for that state so
        we will use memoization for that.'''
        memory = {}
        def target_sum(index,value):
            if index >= len(nums):
                if value == target: #if the current value is equal with the target return one
                    return 1
                return 0

            #use memoization
            state = (index,value)
            if state not in memory:
                memory[state] = target_sum(index+1,value+nums[index]) + target_sum(index+1,value-nums[index])

            return memory[state]

        return target_sum(0,0)
        #Time Complexity: O(n)
        #Space Complexity: O(n)