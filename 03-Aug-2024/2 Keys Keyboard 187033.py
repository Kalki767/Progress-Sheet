# Problem: 2 Keys Keyboard - https://leetcode.com/problems/2-keys-keyboard/description/

class Solution:
    def minSteps(self, n: int) -> int:
        '''Approach: Math. The probelm asks to find the minimum number of operations
        we need to perform inorder to get n numbers of 'A' given the rules.For this
        case let's think if the current number of a's can be found by pasting some a's
        let's say m times if that's the case then it's optimal instead of copying 1 a
        n times because we can always get n a's by pasting 1 a n times. So for this
        matter we check if the current number of a's can be found by pasting some number
        of a's m times. We continue that way until we can't break it down further. This
        brings us to the concept of prime factorization. if we found the number of times
        we need to multiply that value to get the current value then we can assume that
        one would be the cost of copying and the other's would be const of pasting. Therefore
        all we have to do is find the prime factors of the given number n and add them
        together to find our result.'''

        answer = 0
        i = 2

        while n > 1 and i <= n:
            while n % i == 0 and n > 1:
                n //= i
                answer += i
            i += 1
            
        return answer
        #Time Complexity: O(n)
        #Space Complexity: O(1)
