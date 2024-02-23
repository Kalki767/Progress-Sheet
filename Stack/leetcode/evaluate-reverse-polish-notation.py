class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        '''Approach: Stack. The problem asks to evaluate the given number
        which are in reverse polish notation. So to evaluate them if the
        current token is a number we would just append it. if it's an
        operation we perform it on the last two elements and we will
        append the result back in. after a full iteration we would be
        left with one element in the stack and we would return the integer
        of that number'''
        stack = []
        operations = {'+','-','/','*'}
        for token in tokens:
            if token in operations:
                first_operand = stack.pop()
                second_operand = stack.pop()
                result = int(eval(f"{second_operand} {token} {first_operand}"))
                stack.append(result)
            else:
                stack.append(token)
        return int(stack[0])
        #Time Complexity: O(n)
        #Space Complexity: O(n)