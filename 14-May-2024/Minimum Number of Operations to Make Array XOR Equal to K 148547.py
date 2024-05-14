# Problem: Minimum Number of Operations to Make Array XOR Equal to K - https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k/

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        '''Approach: Bitwise Manipulation. The problem asks how many bits we
        need to flip so that xor of all numbers in nums becomes equal to k.
        To do that first we need to calculate the xor of all the numbers.
        Starting from the rightmost bit we check if that bit is different
        in the xor and k if so we need to flip it. How do we check if there
        was a difference by taking the xor of the two and check if that last
        bit is set by checking if it's divisible by two or not. After that shift
        both xor and k by one to the right.'''
        xor = 0
        answer = 0
        for num in nums:
            xor = xor ^ num
        while xor or k:
            if (xor ^ k) %2 != 0:
                answer += 1
            xor >>= 1
            k >>= 1
        return answer
        #Time Complexity: O(32)
        #Space Complexity: O(1)