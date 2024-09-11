# Problem: Replace Words - https://leetcode.com/problems/replace-words/

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

        for i, c in enumerate(word):
            index = ord(c) - ord('a')
            if current.is_end == True:
                return word[:i]
            if current.childrens[index] is None:
                if current.is_end:
                    return word[:i]
                return ""
            current = current.childrens[index]

        return word

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        answer = []
        sentence = sentence.split()

        for word in dictionary:
            trie.insert(word)
        
        for word in sentence:
            result = trie.search(word)
            if len(result) == 0:
                answer.append(word)
            else:
                answer.append(result)
                
        return " ".join(answer)