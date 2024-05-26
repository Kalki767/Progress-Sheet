# Problem: Maximum XOR of Two Numbers in an Array - https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

class TrieNode:
    def __init__(self):
        self.childrens = [None] * 2
        self.is_end = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self,word:str) -> None:
        current = self.root
        for c in word:
            index = int(c)
            if current.childrens[index] is None:
                current.childrens[index] = TrieNode()
            current = current.childrens[index]
        current.is_end = True
    def calculate(self,word):
        current = self.root
        answer = 0
        for i, c in enumerate(word):
            index = int(c)
            opposite_bit = 1 - index
            if current.childrens[opposite_bit] is not None:
                answer = answer | (1<<(31-i))
                current = current.childrens[opposite_bit]
            else:
                current = current.childrens[index]
        return answer
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = Trie()
        for num in nums:
            val = format(num,'032b')
            trie.insert(val)
        answer = 0
        for num in nums:
            val = format(num,'032b')
            answer = max(answer,trie.calculate(val))
        return answer