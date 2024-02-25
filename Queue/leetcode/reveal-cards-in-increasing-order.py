class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        '''Approach: Queue. The problem asks to find the order of the decks
        that would result in increasing order when revealed. to do that we
        can start from the maximum number and perform the operations in 
        a reverse manner which means append to the left and then pop from
        the right and append to the left. Because the revealing operation
        was pop from left and take the next element to the back. Therefore
        since we are starting from the largest number and reversing backwards
        this ensures that we will end up with the right reordering.out of 
        the for loop we need to add one operation due to appending the last
        element to the front'''
        queue = deque()
        deck.sort(reverse = True)
        for decks in deck:
            queue.appendleft(decks)
            num = queue.pop()
            queue.appendleft(num)
        queue.append(queue.popleft())
        return queue
        #Time Complexity: O(nlogn)
        #Space Complexity: O(n)