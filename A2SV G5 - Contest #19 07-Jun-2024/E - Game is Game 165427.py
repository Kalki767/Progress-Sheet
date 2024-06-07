# Problem: E - Game is Game - https://codeforces.com/gym/527294/problem/E



import sys, threading

input = lambda: sys.stdin.readline().strip()

class TrieNode:
    def __init__(self):
        self.childrens = [None] *26
        self.win = False
        self.lose = False

class Trie:
    def find_root(self):
        return TrieNode()
    
    def insert(self,word,root):
        for ch in word:
            index = ord(ch) - ord('a')
            if root.childrens[index] is None:
                root.childrens[index] = TrieNode()
            root = root.childrens[index]
    
    def get_winners(self,root):
        isLeaf = True
        for i in range(26):
            if root.childrens[i] is not None:
                self.get_winners(root.childrens[i])
                isLeaf = False
                root.win = root.win or (not root.childrens[i].win)
                root.lose = root.lose or not root.childrens[i].lose
        if isLeaf:
            root.win = False
            root.lose = True
    def winners(self,root,k):
        if root.win is False:
            return 1
        elif root.win and root.lose:
            return 0
        else:
            if k %2 != 0:
                return 0
            return 1
def main():
    n, k = map(int,input().split())
    strings = []
    for _ in range(n):
        strings.append(input())

    trie = Trie()
    root = trie.find_root()
    for word in strings:
        trie.insert(word,root)
    trie.get_winners(root)
    result = trie.winners(root,k)
    if result:
        print('Second')
    else:
        print('First')
    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()

