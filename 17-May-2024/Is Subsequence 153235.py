# Problem: Is Subsequence - https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        '''Approach: Bottom Up Dynamic Programming. The problem asks to check
        if the given string s is subsequence of t. To check that we need to
        find matching characters. When we match the first character we move
        to the next one if we didn't get a match we will keep searching. If
        we exhausted the string s then we simply return true if not we return
        false. We used a dynamic programming approach here. If the current
        character matches then we check for the previous row and col if that
        matches then it means this is subsequence if not that means we haven't
        found the previous element so we can't create a subsequence. If the
        characters doesn't match then we simply transfer what is in the previous
        column becuase if the previous character was a subsequence then this one
        can be too. So we used a tabulation method filling up our table starting
        from the end and coming to the front.'''

        #initalize our matrix for our tabulation
        dp = [[False for _ in range(len(t)+1)] for _ in range(len(s)+1)]
        for i in range(len(t)+1):
            dp[-1][i] = True
        
        #fill our answer starting from the end to the front
        for row in range(len(s)-1,-1,-1):
            for col in range(len(t)-1,-1,-1):
                if s[row] == t[col]:
                    dp[row][col] = dp[row+1][col+1]
                else:
                    dp[row][col] = dp[row][col+1]
                   
        return dp[0][0]
        #Time Complexity: O(n**2)
        #Space Complexity: O(n**2)

        '''Top Down Approach:
        memory = {}
        def dp(left,right):
            if left == len(s):
                return True
            elif right == len(t):
                return False
            state = (left,right)
            if state not in memory:
                if s[left] == t[right]:
                    memory[state] = dp(left+1,right+1)
                else:
                    memory[state] = dp(left,right+1)
            return memory[state]
        return dp(0,0)
        '''