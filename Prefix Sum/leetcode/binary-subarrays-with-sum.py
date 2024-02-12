class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        '''Approach: prefix sum with the help of hashtable to track the
        number of each prefix sum while traversing. in one traversal we
        check if it's possible to find a subarray with sum equal to goal
        by removing some portion of the list. we can check that by finding
        a subarray with sum equal to the current sum minus goal. sometimes
        we don't need to remove any portion that means a prefixsum of zero
        so we store zero at the inital'''

        '''Step1:create a dictionary for prefixsum to count the occurence
        of each prefixsum while traversing'''
        prefix_sum_counter = defaultdict(int)
        prefix_sum_counter[0] = 1
        total_subarray = current_sum = 0

        '''Step2: calculate prefix sum at each iteration and check if the
        difference exists in our hashmap that means we can remove that 
        portion of the array therefore in total we have the value at our
        difference ways of getting our goal sum'''
        for num in nums:
            current_sum+=num
            difference = current_sum-goal
            if difference in prefix_sum_counter:
                total_subarray+=prefix_sum_counter[difference]
            prefix_sum_counter[current_sum]+=1
        return total_subarray
        #Time Complexity:O(n)
        #Space Complexity:O(n)