class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        '''Approach: Backtracking. The problem asked to find numbers which
        add up to the target from the candidates we can use one element frequently
        Here we check if only the summation of a single element would result in
        the target if it does we append that on our answer and try another element
        by popping out the last element if not we just return to our caller and
        try another combination. So we used backtracking for generating each and
        every combination. our base case is if the sum of the combination is either
        greater than or equal to the target.'''
        answer = []
        def backtrack(index,result):
            if sum(result) > target:#if the sum is greater return back to the caller
                return
            elif sum(result) == target:#if the combination is the answer add it to our list
                answer.append(result[:])
                return
            for i in range(index,len(candidates)):
                result.append(candidates[i])
                backtrack(index,result)#use the same element over and pver again
                result.pop()#after return pop the last element
                backtrack(index+1,result)#try a different path
                return
        backtrack(0,[])
        return answer
        #Time Complexity: O(n**n * n) for call stack and for the list
        #Space Complexity: O(d) d is maximum depth