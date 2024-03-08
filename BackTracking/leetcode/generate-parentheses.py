class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        '''Approach: Backtracking. The problem asks to generate every valid
        parenthesis given the number of parenthesis. The intution here is for
        a parenthesis to be valid while going through the parentheis starting
        from the begining to the end the number of closed parenthesis must be
        less than or equal to the number of opening brackets. So we always want
        an opening bracket to come first so we use an if condition to track
        the number of opened brackets till now. So we check that if we have
        reached n so that we could start appending closing bracket. But we don't
        have an else statement for appending closing brackets because in that
        case there is no way we would generate different valid parenthesis.
        Therefore when the if condition fails we move to the next if condition
        and append our value to check it we constantly called backtracking
        in both the if conditions and up on return we need to pop out whatsoever
        in our result therefore since the return function returns to the caller
        we need to have the pop in both of the if condition. When both the number 
        of opened and closed is equal to n we append that to our result.'''
        answer = []
        def backtrack(opened,closed,result):
            if opened == closed == n:
                text = ''.join(result)
                answer.append(text)
                return
            if opened < n:
                result.append('(')
                backtrack(opened+1,closed,result)
                result.pop()
            if closed < opened:
                result.append(')')
                backtrack(opened,closed+1,result)
                result.pop()
                
        backtrack(0,0,[])
        return answer
        #Time Complexity: O(2**n)
        #Space Complexity: O(n)