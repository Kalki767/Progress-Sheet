class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        '''Approach: Greedy. the problem asks if we can return changes to
        the person correctly. here we are being greedy on giving the changes
        to the person with higher values. for example if we recieved a 20
        we became greedy and give the change using 10 and 5 rather than 3
        5 notes. so we check for the higher note if it's not available we
        check the 5 and if it's not available we have nothing to change'''

        #Step1: initially we don't have any notes so intitalize them with 0
        fives = tens = 0

        '''Step2: iterate through the list if the note is five no change
        if it's 10 we look for 5 and if it's 20 we look for 15'''
        for bill in bills:
            if bill == 5:
                fives += 1
            elif bill == 10:
                if fives == 0:
                    return False
                fives -= 1
                tens += 1
            else:
                if tens and fives:
                    tens -= 1
                    fives -= 1
                elif fives >= 3:
                    fives -= 3
                else:
                    return False
        return True 
        #Time Complexity: O(n)
        #Space Complexity: O(1)