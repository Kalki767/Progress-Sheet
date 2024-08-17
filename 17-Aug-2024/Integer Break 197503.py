# Problem: Integer Break - https://leetcode.com/problems/integer-break/

class Solution:
    def integerBreak(self, n: int) -> int:
        '''Approach: Top Down Dynamic Programming. The problem asks to find
        the maximum product that we can have by dividing the array fully.
        First let's explore the brute force way which is trying every possible
        division that we can make and taking the maximum from all of them.
        This will give us the correct answer but it won't pass the time constraint
        so we will use memoization. How do we find each possible way? For each
        value we can subtract starting from one up to the current value itself
        and find the maximum product of that value it goes that way until it
        reaches the base case which is when the value is zero. The state will
        be the current value.'''
        if n == 2 or n == 3:
            return n - 1
        memory = {}

        def dp(index):
            if index == 0:
                return 1
            if index not in memory:
                answer = 1
                for i in range(1,index+1):
                    answer = max(answer,dp(index-i)*i)
                memory[index] = answer
            return memory[index]

        return dp(n)
        #Time Complexity: O(n**2)
        #Space Complexity: O(n)

        '''Bottom Up Approach
        if n == 2 or n == 3:
            return n - 1
        dp = [1 for _ in range(n+1)]
        for index in range(2,n+1):
            answer = index
            for i in range(1,index+1):
                answer = max(answer,dp[index-i]*i)
            dp[index] = answer
        return dp[n]
        '''