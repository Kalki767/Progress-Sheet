# Problem: Combination Sum IV - https://leetcode.com/problems/combination-sum-iv/description/

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        '''Approach: Bottom Up Dynamic Programming. The problem asks to count
        the number of ways that would sum to the given target. And also the
        given constraint is that two permutations are counted alone. This
        problem is direct backtracking which simply tries every ways by
        generating them. So how do we do that? Track the target at each
        step and iterate over all nums because we need to start from the
        begining so that the permutation differs. After performing that all
        we need to do is store it in 1d array for later use'''
        dp = [0 for _ in range(target+1)]
        dp[0] = 1
        for i in range(1,target+1):
            pick = 0
            for num in nums:
                if num <= i:
                    pick += dp[i - num]
            dp[i] = pick
        return dp[target]
        # Time Complexity: O(n*target)
        #Space Complexity: O(target)

        #Top Down Approach
        # memory = {}
        # def dp(target):
        #     if target == 0:
        #         return 1
        #     if target in memory:
        #         return memory[target]
        #     pick = 0
        #     for num in nums:
        #         if num <= target:
        #             pick += dp(target - num)
        #     memory[target] = pick
        #     return memory[target]
        # return dp(target)