class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        #Approach: Sliding window with dynamic size
        #Step1: assign window to default dict and current_sum and max_sum to zero
        window = defaultdict(int)
        curr_sum=max_sum=0
        left=right=0

        #Step2:iterate through the list until the right pointer reaches it's end
        while right<len(nums):

            #Step3: add the current to the current sum and check if we found duplicate if so shrink the window if not expand the window
            window[nums[right]]+=1
            curr_sum+=nums[right]
            while window[nums[right]]>1:
                curr_sum-=nums[left]
                window[nums[left]]-=1
                left+=1
            max_sum=max(max_sum,curr_sum)
            right+=1
        return max_sum