class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        '''Approach: prefix sum here we are trying to find a subarray whose
        sum is divisible by k to achieve that we used a prefix sum to store
        the current sum and to find a particular subarray sum we need to
        subtract our starting point from our end point in our prefix sum
        so that our subarray to be divisible by k the two end points need
        to have the same modulo so while going once through our list we
        check if we have gotten the same modulo before if so add it to our
        result and add the key to our dictionary'''
        #Step1: create our modulo dictionary to store the modulos we have encountered so far
        modulo = defaultdict(int)
        modulo[0] = 1
        current_sum = 0
        result = 0

        '''Step2: iterate through the array while checking if the current sum
        modulo k exists in our dictionary if it does update our result'''
        for num in nums:
            current_sum += num
            remainder = current_sum%k
            result += modulo[remainder]
            modulo[remainder] += 1
        return result
        #Time Complexity:O(n)
        #Space Complexity:O(n)