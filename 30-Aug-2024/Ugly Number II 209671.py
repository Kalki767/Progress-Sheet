# Problem: Ugly Number II - https://leetcode.com/problems/ugly-number-ii/

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly_numbers = [0] *n
        ugly_numbers[0] = 1
        index_of2 = index_of3 = index_of5 = 0
        next_multiple_of_2, next_multiple_of_3, next_multiple_of_5 = 2, 3,5
        for i in range(1,n):
            next_ugly_number = min(next_multiple_of_2,next_multiple_of_3,next_multiple_of_5)
            ugly_numbers[i] = next_ugly_number

            if next_ugly_number == next_multiple_of_2:
                index_of2 += 1
                next_multiple_of_2 = ugly_numbers[index_of2] *2
            if next_ugly_number == next_multiple_of_3:
                index_of3 += 1
                next_multiple_of_3 = ugly_numbers[index_of3] *3
            if next_ugly_number == next_multiple_of_5:
                index_of5 += 1
                next_multiple_of_5 = ugly_numbers[index_of5] *5
        return ugly_numbers[-1]