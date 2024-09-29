# Problem: Find the Student that Will Replace the Chalk - https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/description/

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        '''Approach: Math. The problem asks to find the student who will replace the
        chalk a student can replace a chalk if the remaining chalks are strictly 
        less than the current chalk. To solve this problem all we have to do is
        first remove multiple rounds that will be made because there is no use in 
        iterating and decrementing them for that case we will take the sum of the 
        chalks and take the remainder of k divided by the sum after that we can 
        simply iterate and find out which kid should replace'''
        remainder = k % sum(chalk)
        index = 0
        while remainder > 0:
            if remainder < chalk[index]:
                break
            remainder -= chalk[index]
            index += 1
        return index
        #Time Complexity: O(n)
        #Space Complexity: O(1)