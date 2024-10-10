# Problem: Keyboard Row - https://leetcode.com/problems/keyboard-row/description/

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        s1 = set("qwertyuiop")
        s2 = set("asdfghjkl")
        s3 = set("zxcvbnm")
        ans = []
        for i in words:
            if set(i.lower()).issubset(s1) or set(i.lower()).issubset(s2) or set(i.lower()).issubset(s3):
                ans.append(i)
        return ans
