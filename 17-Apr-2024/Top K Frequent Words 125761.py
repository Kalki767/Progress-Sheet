# Problem: Top K Frequent Words - https://leetcode.com/problems/top-k-frequent-words/

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        '''Approach: Max Heap. The problem asks to find the k most frequent
        words. For this we can use a heap to store the freqeucnies as comparators
        and if they are a tie it would compare the words. Here we will use
        max heap because we want the maximum frequent words. And for a tie
        since we are using the min heap by just changing the frequency to
        make it max heap it would maintain in a sorted order. When we are done
        building our heap we can simply pop k elements from the heap and
        append them to our answer'''
        heap = []
        counter = Counter(words)
        for key, value in counter.items():
            heappush(heap,(-value,key))
        answer = []
        for _ in range(k):
            freq, word = heappop(heap)
            answer.append(word)
        return answer
        #Time Complexity: O(n + klogn) for pushing the elements into the heap and for popping k elements
        #Space Complexity: O(n) for building the heap