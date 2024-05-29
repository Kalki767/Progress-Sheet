# Problem: D - BitPleasure Maximization - https://codeforces.com/gym/526229/problem/D

class TrieNode:
    def __init__(self):
        self.children = [None] * 2
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            index = int(ch)
            if not node.children[index]:
                node.children[index] = TrieNode()
            node = node.children[index]
        node.is_end_of_word = True

    def maximum_xor(self,word):
        current = self.root
        answer = 0
        for index,bit in enumerate(word):
            i = int(bit)
            opposite = 1 - i
            if current.children[opposite] is not None:
                answer = answer | (1<<63-index)
                current = current.children[opposite]
            else:
                current = current.children[i]
        return answer


trie = Trie()
n = int(input())
nums = list(map(int,input().split()))
nums.append(0)
xor = [0]
for num in nums:
    xor.append(xor[-1]^num)
for num in xor: 
    binary_str = format(num,'064b')
    trie.insert(binary_str)
answer = 0
current = 0
for index in range(n,-1,-1):
    current = current ^ nums[index]
    binary_str = format(current,'064b')
    answer = max(trie.maximum_xor(binary_str),answer)
 
print(answer)
