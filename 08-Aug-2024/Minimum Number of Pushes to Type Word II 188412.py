# Problem: Minimum Number of Pushes to Type Word II - https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/

class Solution:
    def minimumPushes(self, word: str) -> int:
        counter = Counter(word)
        frequencies = list(counter.values())
        frequencies.sort(reverse = True)
        answer = 0
        round = 1
        for i in range(0,len(frequencies),8):
            bound = min(i+8,len(frequencies))
            answer += (round * sum(frequencies[i:bound]))
            round += 1
        return answer