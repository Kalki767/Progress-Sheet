class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        '''Approach: prefix sum. first we calculate the prefix sum then we
        decrement the current number multiplied by how many elements were 
        there till the current element by the prefix sum till that element
        and we do the same thing for the postfix element too and we add those
        two of them and store them in an array'''

        '''Step1:assign a list with zero to calculate the prefix sum and an
        answer list with the same length as nums'''
        prefix_sum = [0]
        n = len(nums)
        answer = [0]*n
        running_sum = 0

        #Step2: iterate through the array to calculate the prefix sum
        for num in nums:
            running_sum += num
            prefix_sum.append(running_sum)
        '''Step3: for each num in nums calculate the absolute differences
        using prefix sum and postfix sum'''
        for index in range(n):
            number_before = nums[index]*index
            number_after = nums[index]*(n-1-index)
            prefix = abs(number_before-prefix_sum[index])
            after_sum = prefix_sum[-1]-prefix_sum[index+1]
            postfix = abs(number_after-after_sum)
            
            answer[index] = prefix+postfix
        return answer
        #Time Complexity:O(n)
        #Space Complexity:O(n)