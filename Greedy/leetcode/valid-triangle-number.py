class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        '''Approach: Greedy. The problem asks to find the number of valid
        triplets that could form a triangle. So to find the triplets easily
        we need to sort the input first so that we can have some pattern.
        we start iterating from the third element and check if there is any
        element before it that could sum up with it and is greater than the
        largest side which is our current element if we found that element
        we will try another combination by going backwards if not we will 
        move forward'''
        answer = 0
        nums.sort()
        for right in range(2,len(nums)):
            #start from the first to the current to find any valid triplets
            first_side = 0
            second_side = right - 1
            largest_side = nums[right]
            while first_side < second_side:
                #when a valid triplet is found update the second side
                if nums[first_side] + nums[second_side] > largest_side:
                    answer += second_side - first_side
                    second_side -= 1
                else:
                    #otherwise update the first side 
                    first_side += 1
        return answer
        #Time Complexity: O(n*2)
        #Space Complexity: O(1)