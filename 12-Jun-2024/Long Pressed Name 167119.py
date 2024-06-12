# Problem: Long Pressed Name - https://leetcode.com/problems/long-pressed-name/

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        #Step1: assign two pointers to the start of the array
        left=right=0

        #Step2: iterate through the array until one of them gets exhausted

        while left<len(name) and right<len(typed):
            counter =1
            #Step3: check if the characters doesn't match and return false
            if name[left]!=typed[right]:
                return False
            
            #Step4: if they match increment right and left pointer until a new character exists
            while left<len(name)-1 and name[left]==name[left+1]:
                left+=1
                counter+=1
            right+=1
            repeated=1
            while right<len(typed) and typed[right]==typed[right-1]:
                right+=1
                repeated+=1
            if repeated<counter:
                return False
            left+=1
            
            #Step5: if one of the arrays gets exhausted before the other one did return False
        if left<len(name) or right<len(typed):
            return False
        #Step6: if nothing is returned return True
        return True