# Problem: Maximum XOR for Each Query - https://leetcode.com/problems/maximum-xor-for-each-query/

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        '''Approach: BitWise Manipulation. The problem asks to find the maximum
        k value that need to be xored so that the total xor is maximized and is
        having length of the maximum bit. First we need to find out the maximum
        value we can have with the given bit which will be the power of 2 to
        the maximum bit minus one because the power of two will have a length
        of the maximum bit when we do minus one we decrement the number of bit
        by one and we ensure that we have the maximum value. Therefore at each
        step to find k all we have to do is perform xor operation on the current
        value with the maximum value at the end we need to reverse the array.'''
        maximum = (1 << (maximumBit)) - 1 
        answer = []
        xor = 0
        for num in nums:
            xor = xor ^ num
            answer.append(xor^maximum)
        answer.reverse()
        return answer
        #Time Complexity: O(n)
        #Space Complexity: O(1)
        