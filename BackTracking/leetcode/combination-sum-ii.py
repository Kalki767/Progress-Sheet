class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        '''Approach: BackTracking. The problem asks to find each combinations
        of the numbers which would sum up to the target but we cannot use the
        same element more than once. So this problem is the same as combination
        sum but with the difference here the input contains duplicates. To avoid
        duplicate answers in our result what we can do is after we got a combination
        whose sum is either greater than or equal to the target up on returning
        our iteration continues but this time we need to make sure we are using
        different element rather than the one used previously. Therefore we need
        to check if we got to the backtracking by if the current iteration is
        greater than the starting point then that means we are checking another
        combination and we continue until we find a new element.'''
        candidates.sort()
        answer = []
        def solve(index,total,result):
            if total > target:
                return
            elif total == target:
                answer.append(result[:])
                return
            for i in range(index,len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                result.append(candidates[i])
                solve(i+1,total+candidates[i],result)
                result.pop()
        solve(0,0,[])
        return answer
        #Time Complexity: O((2**n) * n)
        #Space Complexity: O(d) where d is maximum depth of call stack 
