class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''Approach: Montonic decreasing stack. Here we are trying to find
        the next greater element being on the current element. Therefore
        we continue our iteration and when we found an element that's greater
        than the top of the stack then we update that the next greater element
        of that element is the current element. otherwise if the current 
        element doesn't have any greater element it will be -1'''
        result = {num:-1 for num in nums2}
        stack = []
        for num in nums2:
            while stack and stack[-1] < num:
                result[stack[-1]] = num
                stack.pop()
            stack.append(num)
        answer = [result[num] for num in nums1]
        return answer
        #Time Complexity: O(n)
        #Space Complexity: O(n)