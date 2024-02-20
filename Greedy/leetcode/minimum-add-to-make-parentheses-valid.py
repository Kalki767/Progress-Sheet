class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        '''Approach: Greedy. the problem is asking to find the minimum number
        of moves needed to make the parenthesis valid. here we are being
        greedy on the number of moves. since our goal is to make our
        parenthesis valid if we have a opened bracket then we will close it
        and viceversa so that we add minimum number of parenthesis. we will
        use stack to remove the part of the parenthesis which are already 
        valid'''
        # Step1: create stack to keep track of valid parenthesis
        parenthesis = []
        moves = 0

        #Step2: iterate through the string while updating our stack
        for index in range(len(s)):
            if len(parenthesis) == 0:
                parenthesis.append(s[index])
            elif s[index] == '(':
                parenthesis.append(s[index])
            elif s[index] == ')' and parenthesis[-1] == '(':
                parenthesis.pop()
            else:
                parenthesis.append(s[index])
        return len(parenthesis)
        #Time Complexity: O(n)
        #Space Complexity: O(n)