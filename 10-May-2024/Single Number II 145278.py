# Problem: Single Number II - https://leetcode.com/problems/single-number-ii/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        '''Approach: BitWise. The problem asks to find the only single number
        that is appearing in the given array. What we are trying to do here
        is find how many bits are set on the current bit index. if we have
        a count of setted bits is not multiple of three then that means the
        single number has setted bit on that position. Therefore we went
        to our answer and set the bit at that position. The problem that
        will arise is negative overflow. So to handle negative numbers if
        the leftmost bit is one that means this number is negative so we
        subtract the current number and the power of the left most bit.'''
        answer = 0
        for bit_index in range(32):
            cnt = 0
            for num in nums:
                if num & (1<<bit_index) != 0:
                    cnt += 1
            if cnt % 3 == 1:
                answer = answer | (1<<bit_index)

        if answer & (1<<31):
            answer = answer - (1<<32)
        return answer
        #Time Complexity: O(n*32)
        #Space Complexity: O(1)