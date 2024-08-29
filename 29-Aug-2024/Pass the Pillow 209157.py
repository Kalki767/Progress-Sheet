# Problem: Pass the Pillow - https://leetcode.com/problems/pass-the-pillow/

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        quotient = time // (n-1)
        if quotient % 2 == 0:
            return time - quotient * (n-1) + 1
        return n - (time - quotient * (n-1)) 
        