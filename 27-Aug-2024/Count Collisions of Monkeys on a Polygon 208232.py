# Problem: Count Collisions of Monkeys on a Polygon - https://leetcode.com/problems/count-collisions-of-monkeys-on-a-polygon/

class Solution:
    def monkeyMove(self, n: int) -> int:
        '''Approach: Math. The problem asks to find the number of ways the monkeys
        can move so that atleast one collision happens. So let's try counting the
        number of ways they should move so that there is no collision. If we look
        closely the only way they won't collide is if they all move in the same
        direction. That's either in clockwise or counterclockwise. That means there
        are only 2 ways where there is no collision. Now the remaining thing is in
        how many ways can the monkey's move. Each monkey have two option either
        moving in clockwise or counterclockwise for that matter since each monkey
        can move in two ways over all we will have 2^n ways. That means the number
        of ways the monkey's will collide will be subtracting 2 from the total number
        of ways. We used the modulo to increase the speed.'''
        MOD = 10**9 + 7
        return (pow(2, n, MOD) - 2) % MOD
        #Time Complexity: O(logn)
        #Space Complexity: O(1)
