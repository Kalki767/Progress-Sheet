# Problem: Number Complement - https://leetcode.com/problems/number-complement/

class Solution:
    def findComplement(self, num: int) -> int:
        bit = num.bit_length()
        value = pow(2,bit) - 1
        return num ^ value