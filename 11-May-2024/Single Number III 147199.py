# Problem: Single Number III - https://leetcode.com/problems/single-number-iii/

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        '''Approach: BitWise Manipulation. The problem asks to find given an
        array of integers each element appears twice except for two elements
        which are distinct. So our task is to find these two distinct numbers
        How can we do that? First if we take the xor of all elements we will
        be left with the xor of two distinct numbers. Since the numbers are
        distinct there will be atleast one bit difference between the two
        numbers. That means if we find that different bit then we can group
        elements in to two parts. So what we need to do is find the rightmost
        setted bit and elements that have a set bit at that position goes
        to one group and those who doesn't have goes to another group. How
        do we know if a bit is set or not when performing an and operation
        if need to be different from 0 otherwise it's not setted. So if
        we do xor operation on both groups then since elements that appear
        twice will be in the same group then we will end up with the two
        distinct numbers.'''
        xor = 0
        b1 = b2 = 0
        for num in nums:
            xor = xor ^ num

        xor = (xor & xor-1) ^ xor #finding the rightmost set bit
        for num in nums:
            if xor & num == 0: #if the rightmost bit is set xor it in group one
                b1 ^= num
            else:
                b2 ^= num

        return [b1,b2]
        #Time Complexity: O(n)
        #Space Complexity: O(1)