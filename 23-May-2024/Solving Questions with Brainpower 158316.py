# Problem: Solving Questions with Brainpower - https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        #Bottom Up Approach
        length = len(questions)
        dp = [0 for _ in range(length+1)]
        for index in range(length-1,-1,-1):
            pick = questions[index][0]
            next_index = index+questions[index][1]+1
            if next_index < length:
                pick += dp[next_index]
            not_pick = dp[index+1]
            dp[index] = max(pick,not_pick)
        return dp[0]

        #Top Down Approach
        # memory = {}
        # def dp(index):
        #     if index >= len(questions):
        #         return 0
        #     if index not in memory:
        #         pick = questions[index][0] + dp(index+questions[index][1]+1)
        #         not_pick = dp(index+1)
        #         memory[index] = max(pick,not_pick)
        #     return memory[index]
        # return dp(0)