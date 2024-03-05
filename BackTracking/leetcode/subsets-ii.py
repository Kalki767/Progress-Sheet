class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        '''Approach: Backtracking. The problem asks to find subsets of 
        a given list in which the numbers are not distinct.But we don't want
        duplicates in our answer. Here we need to know that the order of the
        numbers doesn't matter if they have equal frequencies for each number
        they are treated as duplicates but the in operator cannot check that
        for us. Therefore if we sort the given input then we would end up having
        the same subsets and we can use the in operator to remove them. We use
        the same backtracking technique to generate the subsets.'''
        answer = []
        nums.sort()
        def backtrack(index,result):
            #if we reached the end and haven't encountered this subset before append it
            if index == len(nums) and result not in answer:
                answer.append(result[:])
                return
            for i in range(index,len(nums)):
                result.append(nums[index])
                backtrack(index+1,result)
                result.pop()
                backtrack(index+1,result)
                return
        backtrack(0,[])
        return answer
        #Time Complexity: O(2**n+ nlogn)
        #Space Complexity: O(d) d is maximum depth for call stack