# Problem: Nim Game - https://leetcode.com/problems/nim-game/

class Solution:
    def canWinNim(self, n: int) -> bool:
        '''Approach: Math.The problem asks given that we can pick at most
        3 elements we want to check if we can win the game or not. There is
        one condition where we can't win the game which is when there are 4
        stones or multiples of stones left so no matter the way we pick up
        there is no way we could win because all we can do is pick elements
        from 1 up to 3 and the remaining elements would also be from 1 up
        to 3 therefore no matter what we pick our friend will win. So if
        the number of stones is a multiple of 4 then we can't win otherwise
        we can.''' 
        return n%4