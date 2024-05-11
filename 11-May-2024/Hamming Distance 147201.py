# Problem: Hamming Distance - https://leetcode.com/problems/hamming-distance/

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        answer = 0
        xor = x ^ y
        while xor:
            if xor & 1 == 1:
                answer += 1
            xor >>= 1
        return answer