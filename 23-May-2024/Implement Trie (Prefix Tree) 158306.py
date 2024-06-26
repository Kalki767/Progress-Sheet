# Problem: Implement Trie (Prefix Tree) - https://leetcode.com/problems/implement-trie-prefix-tree/

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ]
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root
        for character in word:
            val = ord(character) - ord('a')
            if current.children[val] == None:
                current.children[val] = TrieNode()
            current = current.children[val]
        current.is_end = True

    def search(self, word: str) -> bool:
        current = self.root
        for character in word:
            val = ord(character) - ord('a')
            if current.children[val] == None:
                return False
            current = current.children[val]
        return current.is_end

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for character in prefix:
            val = ord(character) - ord('a')
            if current.children[val] == None:
                return False
            current = current.children[val]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)