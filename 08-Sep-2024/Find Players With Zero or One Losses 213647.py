# Problem: Find Players With Zero or One Losses - https://leetcode.com/problems/find-players-with-zero-or-one-losses

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losers = {}
        teams = {j for i in matches for j in i}
        for i in matches:
            if i[1] in losers:
                losers[i[1]]+=1
            else:
                losers[i[1]]=1
        one_lose = [keys for keys,values in losers.items() if values==1]
        no_lose = list(teams-set(losers.keys()))
        return [sorted(no_lose),sorted(one_lose)]