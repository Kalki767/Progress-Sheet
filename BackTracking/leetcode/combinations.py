class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        '''Approach: Backtracking. The problem asks to find all combinations
        of n with size k. To find that we need to try each and every possible
        combinations and hold the ones with size k. Therefore at each stage
        we have two decision points whether to include that element or not
        so to acheive that we can include that element and use backtracking to
        get back to that element by popping it out again.'''
        answer = [] #To store the final combinations
        def backtrack(index,result):
            nonlocal answer
            if len(result) == k: #if our list is size k append it and return
                answer.append(result[:])
                return
            for i in range(index,n+1): #otherwise append the current element and backtrack until the base case is fullfilled
                result.append(i)
                backtrack(i+1,result)
                result.pop()
        backtrack(1,[])
        return answer
        #Time Complexity: O(2*n + C(n,k)*k)where C(n,k) is combination
        #Space Complexity: O(n) for call stack
            