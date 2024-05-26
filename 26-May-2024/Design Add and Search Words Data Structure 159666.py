# Problem: Design Add and Search Words Data Structure - https://leetcode.com/problems/design-add-and-search-words-data-structure/

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
        return self.check(word,current,0)

    def check(self,word,current,index):

        if index == len(word):
            return current.is_end

        if word[index] != '.':
            ind = ord(word[index]) - ord('a')
            if current.childrens[ind] is None:
                return False

            return self.check(word,current.childrens[ind],index+1)
            
        else:
            answer = False
            for j in range(26):
                if current.childrens[j] is not None:
                    answer = answer or self.check(word,current.childrens[j],index+1)
            return answer
                       

class WordDictionary:

    def __init__(self):
        self.trie = Trie()

    def addWord(self, word: str) -> None:
        self.trie.insert(word)

    def search(self, word: str) -> bool:
        return self.trie.search(word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)