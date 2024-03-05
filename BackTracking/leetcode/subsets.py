class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''Approach: Backtracking. The problem asks to find the subsets of
        a given list. To find them we need to generate each subsets using
        each element. We used backtracking technique to go back to where we
        were before and go from there. We called the backtracking function
        twice because we want list whose size is not equal to the current
        size too. Therefore we append our result to our answer when our iteration
        is greater than or equal to the length therefore we go all the way
        down and when we reach our base case we append it to the list and
        backtrack again after that we return to the caller.'''
        answer = []
        def backtrack(index,result):
            if index >= len(nums):
                answer.append(result[:])
                return
            result.append(nums[index])
            backtrack(index+1,result)
            result.pop()
            backtrack(index+1,result)#to append result whose size if different from len(nums)
            return
        backtrack(0,[])
        return answer
        #Time Complexity: O(2**n * n) for call stack and for the list
        #Space Complexity: O(d) where d is maximum depth of call stack