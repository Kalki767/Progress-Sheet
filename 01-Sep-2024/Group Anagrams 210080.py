# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''Approach: Sorting with Hashtable. The problem asks to group anagrams
        of string together. So to determine whether they are anagram or not we need
        to check if they have the same characters with the same frequency but their
        orders are messed up so we need to sort each word before checking if they
        are anagram or not. Then after sorting each value if the words are anagram
        then they would have one common sorted word. For that case we can use that
        word as key and the word before sorted as value. In that case all words that
        form anagram would end up stored under one key.'''
        answer = []
        mapped = defaultdict(list)

        for i in range(len(strs)):
            cur = strs[i]
            anagram = ''.join(sorted(list(cur)))
            mapped[anagram].append(cur)

        for key, value in mapped.items():
            answer.append(value)

        return answer
        #Time Complexity: O(100n) because in the worst case the length of a single word is 100
        #Space Complexity: O(n)