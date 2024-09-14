# Problem: Find Players With Zero or One Losses - https://leetcode.com/problems/find-players-with-zero-or-one-losses

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_characters = set(allowed)
        answer = 0
        for word in words:
            flag = True
            for char in word:
                if char not in allowed_characters:
                    flag = False
                    break
            if flag:
                answer += 1
        return answer