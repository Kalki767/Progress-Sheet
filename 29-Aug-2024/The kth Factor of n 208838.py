# Problem: The kth Factor of n - https://leetcode.com/problems/the-kth-factor-of-n/

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        '''though the problem can be solved in o(n) easily we can boil that 
        down to O(sqrt(n)). This can be done by creating two arrays whose total
        size is the factor of n. Therefore if a number is a factor of n then
        we can consider that the quotient is also a factor of n. therefore
        we store them in different arrays and upon retrieval in which one
        of the arrays the requested element is found if it's in the first we
        just return k-1 th element if it's in the second since it's reverse
        sorted we access it from the last.'''
        factors = []
        squares = []
        divisible = 1

        #for updating the two arrays
        while divisible * divisible < n:
            if n% divisible == 0:
                factors.append(divisible)
                squares.append(n//divisible)
            divisible += 1

        ''' if the square root is also a factor we didn't include it in the
        while loop because it would get repeated.'''
        if n%divisible == 0 and sqrt(n) == divisible:
            factors.append(divisible)
        
        #checking if k is out of bounds or either it is in the 1st or 2nd list
        if k > len(factors) + len(squares):
            return -1 
        elif 0 < k <= len(factors):
            return factors[k-1]
        else:
            k -= len(factors)
            m = len(squares)
            return squares[m-k]
        #Time Complexity: O(sqrt(n))
        #Space Complexity: O(n)
            