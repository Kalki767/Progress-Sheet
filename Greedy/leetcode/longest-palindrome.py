class Solution:
    def longestPalindrome(self, s: str) -> int:
        '''Approach: Greedy. the problem asks to maximize the size of the
        palindrome that could be formed from the string s. we can achieve
        that by counting the frequency of each element and take all characters
        whose frequency is a multiple of two and if they are greater than 
        one but not a multiple of two we can take their frequencies minus
        one because palindrome is all about repeating character so we want
        repeated character as much as possible. after that we need to calculate
        the sum of the frequencies which is the length of the string. if it's 
        equal with our palindrome length we leave it. if it's not we can
        increment it by one'''
        counter = Counter(s)
        maximum_length = 0
        for frequencies in counter.values():
            if frequencies == 1:
                continue
            else:
               maximum_length += frequencies - (frequencies%2)
        if len(s) > maximum_length:
            maximum_length += 1
        return maximum_length
        #Time Complexity: O(n)
        #Space Complexity: O(n)