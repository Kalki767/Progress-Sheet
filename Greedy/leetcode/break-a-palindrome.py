class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        '''Approach: Greedy. the problem asks to find a non palindrome which
        is lexographically the smallest one from all the ways of making a 
        string non palindrome. we are being greedy on the chracter we chose
        to replace. if the character is a then there is no alphabet which is
        lexicographically smaller than it so we skip it. but if it's other
        than a we could change it to a the first index that's different from
        a. this might not work on cases like if the character we are replacing
        is in the middle or when the string is only made up of a we need to 
        handle that case'''
        if len(palindrome) == 1:
            return ""
        replaced = -1
        not_palindrome = [*palindrome]
        for index in range(len(palindrome)):
            '''if the character is a we skip it otherwise we have find the 
            index to be replaced'''
            if palindrome[index] == 'a':
                continue
            else:
                replaced = index
                break
        '''if the length of the string is odd and the character to be changed
        appears in the middle or if the string is only made from a then we need
        to change the last index'''
        if (len(palindrome)%2!=0 and replaced==len(palindrome)//2) or replaced== -1:
            not_palindrome[-1] = 'b'
        else:
            not_palindrome[replaced] = 'a'
        return "".join(not_palindrome) 
        #Time Complexity: O(n)
        #Space Complexity: O(n)
        