# Problem: Baseball Game
 (Easy) - https://leetcode.com/problems/baseball-game/

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        '''Approach: Stack. The problem asks to evaluate a given basketball score
        based on the given rules. So since we are dealing with top values we can
        simply use stack to push and pop in constant time.'''
        stack = []
        for operation in operations:
            if operation == 'C':
                stack.pop()
            elif operation == 'D':
                stack.append(stack[-1]*2)
            elif operation == '+':
                stack.append(stack[-1]+stack[-2])
            else:
                stack.append(int(operation))
                
        return sum(stack)
        #Time Complexity: O(n)
        #Space Complexity: O(n)