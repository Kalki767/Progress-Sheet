class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''Approach: Backtracking. The problem asks to find all permutations
        of a given list. To acheive that what we can do is for each element
        check if it's already in the list or not if it's not we append and
        we call recursively backtrack on it. That way since we are always 
        starting ourloop from the 0 then we would only add elements that are
        not currently in our list and when the backtracking is done we pop
        out that element and continue with our iteration. Our base case is when
        the length of our result is equal with the length of our nums.'''
        answer = []
        def backtrack(result):
            if len(result) == len(nums):#if their lengths is equal append it
                answer.append(result[:])
                return
            for i in range(len(nums)):
                '''if the current element is not on the list append it and
                call the bactrack function otherwise keep iterating'''
                if nums[i] not in result: 
                    result.append(nums[i])
                    backtrack(result)
                    result.pop()
        backtrack([])
        return answer
        #Time Complexity: O(n * n!)
        #Space Complexity: O(d) where d is maximum depth of call stack