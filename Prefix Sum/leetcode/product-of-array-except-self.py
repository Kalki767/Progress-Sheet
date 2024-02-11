class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''Approach: prefix sum since we cannot use division it's not
        allowed because it doesn't always guarantee the correct answer
        so to calculate the product without self we need both prefix
        product and postfix product so we store them in different arrays
        while traversing through the list storing both of them and the 
        answer at index i will be the product of those too'''

        '''Step1: initialize both arrays with a value of 1 because the 
        product before the first element and after the last element
        is 1'''
        prefix_product = [1]
        postfix_product = [1]
        n = len(nums)
        answer = [1]*n

        '''Step2:calculate both prefix product and postfix product while
        traversing through the array'''
        for i in range(n-1):
            prefix_product.append(prefix_product[i]*nums[i])
        for i in range(n-1):
            postfix_product.append(postfix_product[i]*nums[n-i-1])

        '''Step3: calculate the answer by multiplying the preifx and postfix
        but the postfix is in reversed order so we need to traverse the
        postfix backwards and the prefix forward'''
        for i in range(n):
            answer[i] = prefix_product[i]*postfix_product[n-i-1]

        return answer
        #Time Complexity:O(n)
        #Space Complexity:O(n)