# Problem: Different Ways to Add Parentheses - https://leetcode.com/problems/different-ways-to-add-parentheses/

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        '''Approach: Recursion. The problem asks to find all possible ways to compute
        the given expression and the result associated with each method of computing
        To solve this problem let's observe something. Let's say we divide the
        expression into two based on some operator then we will have the left division
        and the right division for both divisions we will have multiple ways of
        calculating the expression until the expression is only a number without any
        operator. After that we can go back and let's say if I have two ways of
        computing the left side and 3 ways of computing the right side then in total
        I will have 6 ways of computing it by dividing the expression at that operator.
        That means we are recursively deducing the expression smaller and smaller 
        until it become one or two since the longest length we can have is 2 because
        the maximum number is 99. '''
        #start with an empty list and build the list upon recursive calls
        result = []

        #if the current expression is empty then there is nothing to compute simply return the result
        if len(expression) == 0:
            return result
        
        #if the length of the expression is one or two check if it's a number and return it's int value
        if len(expression) <= 2 and expression[0].isdigit():
            return [int(expression)]
        
        #iterate on the current expression and divide the expression until we get to the basecase
        for i, char in enumerate(expression):
            #if the current character is a digit then skip it
            if char.isdigit():
                continue
            
            #otherwise divide the expression into two using the current operator
            left_div = self.diffWaysToCompute(expression[:i])
            right_div = self.diffWaysToCompute(expression[i+1:])

            #once you got the result back from both the recursive calls the calculate the result by iterating through the two lists
            for left in left_div:
                for right in right_div:
                    
                    if expression[i] == '+':
                        result.append(left+right)
                    elif expression[i] == '-':
                        result.append(left - right)
                    else: 
                        result.append(left*right)
        return result
        #Time Complexity: O(n*2**n) since we are iterating on the expression and we are trying to explore every possible way
        #Space Complexity: O(n) for recursion stack space
