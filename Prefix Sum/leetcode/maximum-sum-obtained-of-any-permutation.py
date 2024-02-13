class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        '''Approach: prefix sum with range of queries. since we are trying
        find the maximum sum we need to find the index that was requested
        many times and put our maximum value at that index and so on'''
        #Step1: create a prefix sum to update range of values at each request
        prefix_sum = [0]*(len(nums)+1)

        '''Step2:iterate through requests to update the index values which are
        requested'''
        for start,end in requests:
            prefix_sum[start]+=1
            prefix_sum[end+1]-=1
        
        '''Step3:iterate through the prefix sum while calculating the sum at
        each iteration'''
        for index in range(1,len(prefix_sum)):
            prefix_sum[index]+=prefix_sum[index-1]
        
        '''Step4:sort the prefix sum to get the maximum requested indexes values
        to the first and sort the input to get the maximum values'''
        nums.sort(reverse=True)
        prefix_sum.sort(reverse=True)

        '''Step5:now we know how many times we are asked for a specific number
        therefore we can multiply the number of times a number is requested
        by the value and update our sum'''
        maximum_sum = 0
        for index in range(len(nums)):
            maximum_sum+=(nums[index]*prefix_sum[index])
        return maximum_sum%(10**9+7)
        #Time Complexity:O(n)
        #Space Complexity:O(n)
