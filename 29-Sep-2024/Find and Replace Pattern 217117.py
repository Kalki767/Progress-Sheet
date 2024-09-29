# Problem: Find and Replace Pattern - https://leetcode.com/problems/find-and-replace-pattern/

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        '''Approach: HashMap. The problem asks by mapping each character with atmost
        one character can we get the required pattern or not. To solve this problem
        the bruteforce approach is to map every character on it's first occurence
        and when it occured again we check if it's the same with the previous mapping
        if not then this word cannot be mapped. Another edge case we need to handle 
        is the reverse mapping which is every character from the pattern should also
        be mapped with only one character se we need to check the reverse mapping too.
        After that if the word passed all those checks we simply return true. We can
        use a helper function to check the word validity.'''

        #a function to check if the current word is valid to be included in the answer
        def check(word):
            mapping = {}
            reverse = {}
            for i in range(len(word)):
                if word[i] in mapping and mapping[word[i]] != pattern[i]:
                    return False
                if pattern[i] in reverse and reverse[pattern[i]] != word[i]:
                    return False
                mapping[word[i]] = pattern[i]
                reverse[pattern[i]] = word[i]
            return True
        
        answer = []
        for word in words:
            if len(word) != len(pattern):
                continue
            if check(word):
                answer.append(word)

        return answer
        #Time Complexity: O(n*m) where n is the length of words and m is the length of pattern
        #Space Complexity: O(m)