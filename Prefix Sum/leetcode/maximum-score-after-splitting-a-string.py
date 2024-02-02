class Solution:
    def maxScore(self, s: str) -> int:
        #Approach: prefix sum
        '''Step1: count the number of ones and assign the max sum and
        number of zeros to 0'''
        count_of_ones = s.count("1")
        count_of_zeros = max_sum =0

        '''Step2: iterate through the string while updating the count of
        zeros and ones and taking the maximum of their sum'''
        for i in range(len(s)-1):
            if s[i]=="0":
                count_of_zeros+=1
            else:
                count_of_ones-=1
            max_sum = max(max_sum,count_of_zeros+count_of_ones)
        return max_sum
        #Time Complexity:O(n)
        #Space Complexity:O(1)