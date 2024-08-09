# Problem: Sort the Jumbled Numbers - https://leetcode.com/problems/sort-the-jumbled-numbers/

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        #Step 1: Map the numbers of nums with a new number based on the given rule
        def mapnumber(number):
            value = str(number)
            new_number = 0
            for num in value:
                num = int(num)
                new_number = new_number*10 + mapping[num]
            return new_number
        
        '''Step2: iterate through each numbers and map them with new numbers. Since
        there might be two numbers with the same value we will also use the index
        as a second parameter to sort the numbers.'''

        mapped = {}
        for index, number in enumerate(nums):
            new_number = mapnumber(number)
            mapped[(new_number,index)] = number
        
        #Step3: sort the keys in increasing order
        values = list(mapped.keys())
        values.sort()

        #Step4: build our answer by iterating through the sorted array
        answer = []
        for val in values:
            answer.append(mapped[val])

        return answer

        '''Time Complexity: let the length of nums is n and length of nums[i] is m then
        the time complexity would be n*m and for the sorting we have nlogn so O(n*m + nlogn)
        Space Complexity: O(n)'''
