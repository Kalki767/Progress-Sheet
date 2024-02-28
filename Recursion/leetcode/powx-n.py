class Solution:
    def myPow(self, x: float, n: int) -> float:
        '''Approach: Recursion. The problems asks to implement the power of x
        raised to n. To implement the power we are just multiplying the same
        number n times. But using a recursion while decrementing n by one 
        would result in stack overflow. Therefore we used a baisc intution
        that x raised to n is the same as x raised to n/2 squared. So we
        stored this value in some temporary variable and calculate the square
        of the temp variable if it's even and if it's odd multiply the square
        by the number x with base case of one. And also we need to handle 
        negative numbers differently.'''
        if n < 0:
            x = 1/x
            n = -1 *n
        if n == 0:
            return 1
        temp = self.myPow(x,n//2)
        return temp**2 if n%2 == 0 else temp**2*x
        #Time Complexity: O(logn)
        #Space Complexity: O(logn)