# Problem: Maximum Product of Word Lengths - https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        '''Approach: Bit Masking. The problem asks to find the maximum product of
        two words which doesn't contain the same letter. To solve this problem
        first we need to check every word for each word if they contain the same
        letter or not. For checking that we can iterate through them and match the
        letters or use a hashset for efficient matching. The third option will
        decrease the space that will be used. We are checking if some letter is there
        or not so we can simply toggle that element if it exists or leave it if it
        doesn't. One thing to notice mulitple words might have the same set of 
        letters but differnet frequency so we need to take the one with maximum
        length to get the maximum answer. So instead of a set we will be using a
        bitmask to check if they appear or not. After that we will iterate through
        the unique masks and if two words doesn't have a common letter between them
        then we multiply their lengths and take the maximum.'''
        ans = 0
        maxlen = defaultdict(int)
        for word in words:
            mask = 0
            for w in word:
                cur = ord(w) - 97
                mask = mask | (1<<cur)
            maxlen[mask] = max(maxlen[mask],len(word))
        for key in maxlen:
            for k in maxlen:
                if not (key & k):
                    cur = maxlen[key] * maxlen[k]
                    ans = max(ans,cur)
        return ans
        #Time Complexity: O(n**2)
        #Space Complexity: O(n)