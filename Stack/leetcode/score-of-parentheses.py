class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        '''Approach: Stack. The problem asks to find the score of a
        parenthesis. The score is if a parenthsis stand by it's own it
        have a score of 1 if it  contains another parenthesis then it's
        score is the score of inner parenthesis multiplied by two. So
        we used stack to know when a parenthesis is closed and instead
        of appending the characters we used 0 and 1 to represent opening
        and closing parenthesis. Therefore when calculating a score we take
        the maximum of twice of the top of the stack and 1. we did this
        because we want to check whether or not the closed parenthesis
        contains another one in it. after that we will add that value to
        the top of the stack. the top of the stack will be returned'''
        stack = [0]
        for token in s:
            if token == '(':
                stack.append(0)
            else:
                value = max(stack.pop()*2,1)
                stack[-1] += value
        return stack[-1]
        #Time Complexity: O(n)
        #Space Complexity: O(n)
