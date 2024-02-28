class Solution:
    def decodeString(self, s: str) -> str:
        '''Approach: Stack. The problem asks to decode a string given the 
        encoded one. To decode a string we are given how many times it's 
        repeated therefore we need to multiply that string with the number
        before it. Sometimes there is case of nested brackets we need to
        handle that one too. Whenever we find a closing bracket we need to 
        find the number before the opening bracket and mutliply that string
        and append it to the stack. At last return the joined stack.'''
        stack = []
        for char in s:
            if char == ']':
                text = []
                number = []
                while stack[-1] != '[':
                    text.append(stack.pop())
                stack.pop()
                while stack and stack[-1].isdigit():
                    number.append(stack.pop())
                number = int("".join(number[::-1]))
                text = "".join(text[::-1])
                stack.append(number*text)
            else:
                stack.append(char)
        return "".join(stack)
        #Time Complexity: O(n)
        #Space Complexity: O(n)