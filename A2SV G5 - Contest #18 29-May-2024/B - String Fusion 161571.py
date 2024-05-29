# Problem: B - String Fusion - https://codeforces.com/gym/526229/problem/B

from collections import Counter, defaultdict


class Triecur:
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False
        self.cnt = 0


class Trie:
    def __init__(self):
        self.root = Triecur()

    def insert(self, word: str) -> None:
        current = self.root
        for c in word:
            index = ord(c) - ord('a')
            if current.children[index] is None:
                current.children[index] = Triecur()
            current =current.children[index]
            current.cnt += 1
        current.is_end = True

    def search(self, word: str,total_len,n) -> int:
        current = self.root
        total_len += (n*len(word))
        for c in word:
            index = ord(c) - ord('a')
            if current.children[index] is not None:
                total_len -= (current.children[index].cnt*2)
                current = current.children[index]
            else:
                return total_len
        return total_len

    
n = int(input())
s = []
trie = Trie()
for i in range(n):
    s.append(input())
total_len = sum([len(word) for word in s])
for word in s:
    trie.insert(word)
answer = 0
for word in s:
    answer += trie.search(word[::-1],total_len,n)
print(answer)
