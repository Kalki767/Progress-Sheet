class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        '''Approach: Backtracking. The problem asks to find every combination
        of the letters. To find that we need to iterate through each character
        of the current index and after adding it to our result we need to backtrack
        the next element to add then since we are iterating through each character
        after one loop the last element will be popped and the next element will
        be appended. When our iteration reaches the end we append our result to
        our answer.'''
        letter = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        answer = []
        def backtrack(index,result):
            if index == len(digits):
                value = ''.join(result)
                if value!= "":#if we have empty string do nothing
                    answer.append(value[:])
                return
            current = digits[index] #find the current phoone number
            for character in letter[current]:#iterate through the current phone number characters
                result.append(character)
                backtrack(index+1,result)#go to the next phone number if there is any
                result.pop()
        backtrack(0,[])
        return answer
        #Time Complexity: O(n * 3**n) n is number of characters in a digit
        #Space Complexity: O(n) for call stack