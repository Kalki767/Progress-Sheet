class Solution:
    def mySqrt(self, x: int) -> int:
        '''Approach: Binary Search. The problem asks to find the square root
        of a number but we can't use any inbuilt function. So what we can do
        is try all integers in the range between 1 and the number. But this is
        not an optimal way one thing we know is the numbers greater than the
        half of the given number are not needed because they will always
        result in greater number. The next thing is if we just used the ordinary
        binary search with no modification we will end up having TLE. Therefore
        one thing we can do when the square of the mid is greater than the
        target we can shrink the right until it's square is less than or 
        equal to the target becuase of the half of our right is still greater
        than the target there is no use in calculating the mid over and over
        again because we know we would still shrink down. We need to handle
        some edge cases like when the input is zero or less than 4 which our
        approach would fail.'''
        if x == 0:
            return 0
        if  x < 4:
            return 1
        left , right = 1, x//2
        while left <= right:
            mid = left + (right - left)
            squared = mid * mid
            if squared < x:
                left = mid + 1
            elif squared > x:
                right = mid - 1
                while (right//2) * (right//2) > x:
                    right//=2
            else:
                return mid
        return left - 1
        #Time Complexity: O(logn)
        #Space Complexity: O(1)