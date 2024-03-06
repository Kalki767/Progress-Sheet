class Solution:
    def countGoodNumbers(self, n: int) -> int:
        '''Approach: Recursion. The problem asks to find the number of good
        numbers of size n based on the given condition. Here we can use
        permutation. Because at each position we have specific values that
        we can put there. That means we can multiply those values. So at
        the even position we have 5 choices since the digit can have trailing
        zeros and for the odd position we have 4 choices that means if we
        know how many odd and even palces we have we can just power 5 to
        the even and power 4 to the odd. Here we need to consider that if
        we don't use the pow function by including mod or implement the 
        power function recursively using the double asterisks for exponenting
        will raise a TLE. Finally we can multiply the values resulting from
        both the even and odd places and return the modulo of their result.'''
        even = n//2 + n%2
        mod = (10**9+7)
        prime = n//2 
        combination = pow(5, even, mod) * pow(4, prime, mod)
        return combination % mod
        #Time Complexity: O(logn)
        #Space Complexity: O(1)
