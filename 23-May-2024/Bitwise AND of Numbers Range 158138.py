# Problem: Bitwise AND of Numbers Range - https://leetcode.com/problems/bitwise-and-of-numbers-range/

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        answer = 0
        length = right.bit_length()
        for i in range(length,-1,-1):
            if left & (1<<i) == right & (1<<i):
                answer = answer | (left & (1<<i))
            else:
                return answer
        return answer