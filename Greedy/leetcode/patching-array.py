class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        '''Approach: Greedy. The problem asks to find the minimum number
        of patches that need to be added so that the list become patched
        until the given n. Here we are being greedy on the numbers that
        we are going to add into our array to make it patched. So our
        approach is if the current running sum of the array is greater
        than the next element then that element is already patched and we
        don't need to add any element but if the sum is less than that
        element that means we can't possibly have that number with our
        current elements and we need to patch one element. so the greediness
        comes here what element should we patch in. we want to patch in the
        maximum number as much as possible but that maximum number should
        be the current sum because it would patch every elements between
        the current sum and the element and also it is maximum. therefore
        we try to patch subarrays as we iterate while finding the local
        optimal for the subarrays to patch hoping it would result in a 
        global optimum'''
        current_sum = 1
        number = 1
        index = patched = 0
        while current_sum <= n:
            if index< len(nums) and current_sum >= nums[index]:
                current_sum += nums[index]
                index +=1
            else:
                patched += 1
                current_sum *= 2
        return patched
        #Time Complexity: O(n)
        #Space Complexity: O(1)