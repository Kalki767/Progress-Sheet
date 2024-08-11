# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        #Approach: Range Query Prefix Sum
        #Step1: assign an array to update the queries that have taken place
        shifted = []
        queries = [0]*(len(s)+1)

        #Step2: update the queries on the left and right+1 indexes to keep track of which elements have been updated with one query
        for left,right,shift in shifts:
            if shift==0:
                queries[left]-=1
                queries[right+1]+=1
            else:
                queries[left]+=1
                queries[right+1]-=1
        current_sum =0

        #Step3: calculate the prefix_sum of the queries at each step to finally get by how much the current character has been shifted
        for index in range(len(s)):
            current_sum+=queries[index]
            queries[index]=current_sum

        #Step4: update the current character by the amounts it is shifted since python strings are immutable we used list
        for i in range(len(s)):
            new_char = chr((ord(s[i])-ord('a')+queries[i])%26+ord('a'))
            shifted.append(new_char)
        return "".join(shifted)
        #Time Complexity:O(n)
        #Space Complexity:O(n)
