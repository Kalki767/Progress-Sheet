# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        '''Approach: Cyclic sort. The problem asks to find the numbers that
        are duplicated in the given array. So to solve this problem it will
        be easy to sort the given array. But the tricky part is how can we
        sort the given array inplace without using any extra memory. To do
        that we can use cyclic sort but the problem arises since there might
        be duplicates we need to handle them. So after sorting the input array
        inplace we need to check if the index and the value matches or not if
        not we need to append the value to our list. '''
        index = 0
        while index < len(nums):
            insertion_index = nums[index] - 1

            #if the values to be swapped are the same there is no point in swapping so break out of the while loop
            while nums[insertion_index] != nums[index]:

                #swap it to put the current element in it's right position
                nums[insertion_index], nums[index] = nums[index], nums[insertion_index]
                insertion_index = nums[index] - 1
            index += 1
        result = []

        #if the current index + 1 is different from the value at that index append it to the answer
        for index, num in enumerate(nums):
            if num - 1 != index:
                result.append(num)
        return result
        
        #Time Complexity: O(n)
        #Space Complexity: O(1)