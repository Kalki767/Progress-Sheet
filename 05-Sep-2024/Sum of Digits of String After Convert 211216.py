# Problem: Sum of Digits of String After Convert - https://leetcode.com/problems/sum-of-digits-of-string-after-convert/

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        '''Approach: BruteForce. The problem asks to convert the given string into
        the corresponding integer and replace the current value by the sum of it's
        digits and repeat the same thing k times. To do that first we convert the 
        string to digit. Then we define a function to add the digits of the number
        and return a string of the number. Then we repeat this thing k times while
        updating the original replaced value.'''
        def add():
            result = 0
            for i in replaced:
                cur = int(i)
                result += cur
            return str(result)
        replaced = []
        for i in s:
            cur = ord(i) - 96
            cur = str(cur)
            replaced.extend(list(cur))
        
        for i in range(k):
            res = add()
            replaced = list(res)

        answer = "".join(replaced)
        return int(answer)
        #Time Complexity: O(n*k) where n is the length of the list
        #Space Complexity: O(n) 