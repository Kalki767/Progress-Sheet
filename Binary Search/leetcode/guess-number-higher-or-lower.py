# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        '''Approach: Binary Search. The problem asks to guess a number and
        the person will tell us whether what we guessed was higher lower or
        correct. Therefore since the input is already sorted meaning it's
        starting from 1 and end at n we can apply binary search to it and
        update our left and right based on the response of the person'''
        left, right = 1, n
        while left <= right:
            mid = left + (right - left)//2
            my_guess = guess(mid)
            if my_guess == -1:
                right = mid - 1
            elif my_guess == 1:
                left = mid + 1
            else:
                return mid
        #Time Complexity: O(logn)
        #Space Complexity: O(1)