# Problem: Basic Calculator II - https://leetcode.com/problems/basic-calculator-ii/

class Solution:
    def calculate(self, s: str) -> int:
        index = 0
        for i in range(len(s)):
            if s[i] == ' ':
                continue
            index = i
            break
        start = []
        while index < len(s) and s[index] not in '/*+-':
            start.append(s[index])
            index += 1
        
        result = [(int(''.join(start)))]
        operand = []
        while index < len(s):

            if s[index] == ' ':
                index += 1
                continue
            if s[index]== '*' or s[index] == '/':
                top = result.pop()
                flag = False
                if top < 0:
                    flag = True
                top = abs(top)
                op = s[index]
                index += 1
                while s[index] == ' ':
                    index += 1
                next_val = []
                while index < len(s) and s[index] not in '/*+-':
                    next_val.append(s[index])
                    index += 1
                next_val = int(''.join(next_val))
                if next_val < 0:
                    if flag:
                        flag = False
                    else:
                        flag = True
                next_val = abs(next_val)
                if op == '*':
                    cur = top * next_val
                else:
                    cur = top // next_val
                if flag:
                    cur *= -1
                result.append(cur)
            else:
                flag = False
                if s[index] == '-':
                    flag = True
                operand.append('+')
                index += 1
                while s[index] == ' ':
                    index += 1
                next_val = []
                while index < len(s) and s[index] not in '/*+-':
                    next_val.append(s[index])
                    index += 1
                
                next_val = int(''.join(next_val))
                if flag:
                    next_val *= -1
                result.append(next_val)
        while operand:
            first = result.pop()
            second = result.pop()
            op = operand.pop()
            if op == '+':
                cur = first + second
            else:
                cur = second - first
            result.append(cur)
        return result[0]