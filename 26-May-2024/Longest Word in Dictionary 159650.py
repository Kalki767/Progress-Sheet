# Problem: Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/

class TrieNode:

    def __init__(self):
        self.childrens = [None] * 26
        self.is_end = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self,word):
        
        current = self.root
        for c in word:
            index = ord(c) - ord('a')
            if current.childrens[index] is None:
                current.childrens[index] = TrieNode()
            current = current.childrens[index]
        current.is_end = True

    def search(self,word):

        current = self.root
        for c in word:
            index = ord(c) - ord('a')
            if current.childrens[index] is None:
                return False
            current = current.childrens[index]

        return current.is_end

class Solution:
    def longestWord(self, words: List[str]) -> str:

        words.sort(key = lambda word : (len(word),word))
        trie = Trie()
        answer = words[0] if len(words[0]) == 1 else ""

        for word in words:
            if len(word) == 1:
                trie.insert(word)
            elif trie.search(word[:-1]):
                trie.insert(word)
                if len(word) > len(answer):
                    answer = word

        return answer