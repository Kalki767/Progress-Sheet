# Problem: Longest Nice Substring - https://leetcode.com/problems/longest-nice-substring/

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        answer = ""
        for i in range(len(s)):
            lower = upper = 0
            for j in range(i,len(s)):
                word = s[i:j+1]
                if s[j].islower():
                    lower = lower | (1<<(ord(s[j])-ord('a')))
                else:
                    upper = upper | (1<<(ord(s[j])-ord('A')))
                if lower == upper and len(answer) < len(word):
                    answer = word
        return answer

        