# Problem: Make Sum Divisible by P   - https://leetcode.com/problems/make-sum-divisible-by-p/

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        '''Approach: Prefix Sum and Math. The problem asks to find out the minimum 
        length subarray that needs to be removed so that the total sum is divisble by
        p. To solve this problem let's dive deep into maths. We see that for the sum
        to be divisible it's remainder need to be zero. Let the remainder of the
        total sum is r1 and the removed subarray is remainder is r2 so when we 
        compute it (r1-r2)%k needs to be zero since both r1 and r2 are less than k
        for the remainder to be zero the difference need to be zero that means both
        remainders need to be equal. So we are looking for a subarray sum whose remainder
        is equal to the remainder of the total sum. For finding that sum let's again
        use some math combined with prefix sum. For finding the subarray sum let's
        say we have stored the remainders with their index so when calculating the
        sum we know that the current sum - some previous sum % p is equal with the
        target remainder we are trying to match. from this we can deduce that (r1-r2)%p
        is equal with the target where r1 and r2 are the remainders of the current
        sum and the previous sum from this we are trying to find r2 so let's shift
        them and we find that (r1-target)%p == r2%p so if this value already exists
        we can calculate the length and update our answer'''
        total_sum = sum(nums)
        target_mod = total_sum % p
        
        # If the total sum is already divisible by p, no need to remove any subarray
        if target_mod == 0:
            return 0

        # Dictionary to store the prefix sum mod p and the index
        prefix_map = {0: -1}  # To handle cases where removing the first few elements gives the result
        prefix_sum = 0
        min_len = len(nums)
        
        for i, num in enumerate(nums):
            prefix_sum = (prefix_sum + num) % p
            
            # We want to find a previous prefix sum that, when removed, leaves a sum divisible by p
            # To find such a prefix, we need prefix_sum % p == (prefix_sum - target_mod) % p
            target = (prefix_sum - target_mod) % p
            
            if target in prefix_map:
                # The subarray length is i - prefix_map[target]
                min_len = min(min_len, i - prefix_map[target])
            
            # Store the current prefix sum mod p and its index
            prefix_map[prefix_sum] = i
        
        # If we found a valid subarray, return its length, otherwise return -1
        return min_len if min_len < len(nums) else -1
        #Time Complexity: O(n)
        #Space Complexity: O(n)
        