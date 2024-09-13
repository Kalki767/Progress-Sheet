# Problem: Count Number of Nice Subarrays - https://leetcode.com/problems/count-number-of-nice-subarrays/

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        #Approach: Sliding Window with dynamic size
        '''Step1: assign the subarray to zero and a counter to count
            number of odd numbers in my window '''
        sub_array =counter=0
        left=right=0

        '''Step2: iterate through the array while incrementing the counter
        when odd number is encountered'''
        while right<len(nums):
            before_even=after_even=1
            if nums[right]%2!=0:
                counter+=1
            right+=1

            '''Step3: if the number of odd numbers is equal to 2 check
            the next elements if they are even countinue iterating and
            also move the left pointer until an odd number is encountered
            ''' 
            if counter==k:
                while right<len(nums) and nums[right]%2==0:
                    after_even+=1
                    right+=1
                while nums[left]%2==0:
                    before_even+=1
                    left+=1
                left+=1

                #Step4: update the subarray value
                sub_array+=(after_even*before_even)
                counter-=1
        return sub_array
        #Time Complexity:O(n)
        #Space Complexity:O(1)