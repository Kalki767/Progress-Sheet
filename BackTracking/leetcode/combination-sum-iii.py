class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        '''Approach: BackTracking. The problem asks to find combination of
        numbers where the numbers are from one to nine and can be used at
        most once. To solve this we need to check for every combination
        starting from one using Backtracking. This problem is the same as
        the other combiantion problems only this one doesn't contain any
        duplicates. So we can try for each combination and when the length of
        our list is equal to k we check if the sum is equal to n if it's we
        append if not we simply return and continue iteration.'''
        answer = []
        def backtrack(index,total,result):
            if len(result) == k:
                if total == n:
                    answer.append(result[:])
                return
            for i in range(index,10):
                result.append(i)
                backtrack(i+1,total+i,result)
                result.pop()
        backtrack(1,0,[])
        return answer
        #Time Complexity: O(n * 2**n)
        #Space Complexity: O(d) where d is maximum depth of call stack which is k
        