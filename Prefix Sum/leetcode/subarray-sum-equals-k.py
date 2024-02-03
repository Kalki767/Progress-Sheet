class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''Approach: prefix sum compute prefix sum at each iteration and
        check if the removal of any subarray that comes before it can give
        us a subarray with sum k so to track the prefix sum we will use
        dictionary instead of list'''
        #Step1: assign a default dictionary and running sum to 0
        prefix_sum = defaultdict(int)
        running_sum = result = 0

        #Step2: start with an offset for the prefix sum
        prefix_sum[0] = 1

        '''Step3: iterate through the array and check if we can get a 
        subarray with sum k'''
        for num in nums:
            running_sum+=num
            difference = running_sum - k
            if difference in prefix_sum:
                result += prefix_sum[difference]
            prefix_sum[running_sum]+=1
        return result
    #Time Complexity:O(n)
    #Space Complexity:O(n)