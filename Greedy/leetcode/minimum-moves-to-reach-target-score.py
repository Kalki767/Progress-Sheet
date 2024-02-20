class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
       '''Approach: Greedy. the problem asks to minimize the number of moves
       needed to reach the target. we can achieve that by using the double
       operation frequently on larger numbers because that would decrease
       n moves to n//2. that means as n grows larger the amount we are 
       decreasing becomes larger. but we have a constraint on doubling we
       need to consider that. so to find the largest value to double we
       need to take the floor division of the target by two. since the target
       might not be divisible by two we need to increment our move by one to
       accomodate that'''
       #Step1: initalize moves with zero
       moves = 0

       '''Step2: run a loop until either we run out of double operation or
       we reached one by just doubling our current elements'''
       while maxDoubles and target > 1:
           if target%2 != 0:
               moves += 1
           target //= 2
           maxDoubles -= 1 
           moves += 1
       #Step3: if the target doesn't reach 1 then increment target -1 times
       moves += target - 1
       return moves
       #Time Complexity: O(n)
       #Space Complexity: O(1)