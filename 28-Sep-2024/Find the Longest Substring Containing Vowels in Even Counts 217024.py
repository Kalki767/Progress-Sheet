# Problem: Find the Longest Substring Containing Vowels in Even Counts - https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        '''Approach: Bitmask. The problem asks to find the longest substring that
        contains even count of vowel for each vowel. And also this substring can
        contain consonants too. To solve this problem the first thing that came
        to mind is using sliding window. But the problem is we are expected to hold
        even count which means the number of each vowel can change. In this case we
        don't have a condition to move our window. That means we need another approach.
        One observation here is we need to track the number of each vowel till now.
        Now if we know that then let's think of it this way if we were wanting a
        window that has even sum we could check if the start and the current index
        have the same parity which is odd then the in between is an even. The same
        case applies here if we find the same state that means what's in between is
        a substring with even count. To count the frequency of each vowel we can use
        a hashmap but the easy way would be to use a bitmask since we can simply toggle
        the value.'''
        max_length = 0
        state = 0
        state_to_index = {0:-1}
        vowel_to_bit = {'a':0,'e':1,'i':2,'o':3,'u':4}

        #iterate through the string and update the state
        for index, char in enumerate(s):
            #if the current character is vowel update the state by toggling the state at that position
            if char in vowel_to_bit:
                position = vowel_to_bit[char]
                state ^= (1<<position)
            
            #if we have the same state before then we can take the maximum length
            if state in state_to_index:
                prev_index = state_to_index[state]
                length = index - prev_index
                max_length = max(max_length,length)
            else:
                state_to_index[state] = index

        return max_length
        #Time Complexity: O(n) 
        #Space Complexity: O(n) where n is the length of the string