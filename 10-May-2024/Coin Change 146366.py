# Problem: Coin Change - https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''Approach: Top Down Dynamic Programming. The problem asks to find
        the minimum number of coins needed that would sum up to the given
        amount if we can't sum up the amount we will simply return -1. Here
        the intution break the bigger problem into smaller subproblems. let
        x is the amount then we will have n possible coins to take in the
        first round and the remaining amount would be decremented by the
        current coin we take. So the problem is minimized into smaller problem
        since we have taken one coin it's now adding the result of the
        remaining and one. If we manage to reach zero that means we were able
        to sum up to the amount and since we won't be needing any coin for
        zero we will return 0 otherwise we will return infinity because here
        we are trying to minimize our result instead of taking -1 we are taking
        infinity. So the recursive approach works fine but it won't pass 
        the time constraints so instead of recalculating the same thing
        we will use memoization and store it so that instead of calling
        the recursive we will access it in constant time complexity.'''
        memory = {}
        def change(target):

            if target < 0: #check if it's impossible to make the amount using the current combination
                return float('inf')

            if target == 0: # if it's possible simply return 0
                return 0

            #if the target is greater than 0 then take each coin and update the number of coins it would take   
            if target not in memory:
                best = float('inf')
                for coin in coins:
                    best = min(best,change(target-coin)+1)
                memory[target] = best
            return memory[target]

        answer = change(amount)
        return answer if answer != float('inf') else -1
        #Time Complexity: O(n)
        #Space Complexity: O(n)