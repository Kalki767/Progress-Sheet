class Solution:
    def isValid(self, s: str) -> bool:
        '''Approach: Stack. check if an opened parenthesis have been closed
        by the same parenthesis if so remove the parenthesis if not append
        it to the stack. at the end if the stack is not empty then there are
        some parenthesis which are open or closed without having opening
        parenthesis'''
        stack = []
        for char in s:
            if not stack:
                stack.append(char)
            elif (stack[-1] == '{' and char == '}') or (stack[-1] == '[' and char == ']') or (stack[-1]=='(' and char == ')'):
                stack.pop()
            else:
                stack.append(char)
        if stack:
            return False
        return True
        #Time Complexity: O(n)
        #Space Complexity: O(n)