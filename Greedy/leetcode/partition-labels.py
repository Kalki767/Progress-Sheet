class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        '''Approach: Greedy. the problem is asking to partition the string
        into many parts as much as possible so that each letter appears in
        at most one partition. here we are being greedy on the number of 
        partitions. the number of partitions can be maximized if the size
        of each partition is minimum. so our goal is to find a minimum size
        substring in which each letters appear only in that substring.then
        we will return the sizes of each substrings.'''

        '''Step1: to find each substrings first we need a hashmap to count
        each occurence of the element and a result array to store our answer
        and a set to store how many unique elements we have encountered so far
        in our window'''
        window = set()
        counter = Counter(s)
        result = []
        left = have = 0

        '''Step2: iterate through the string while decrementing it's 
        frequency from our counter and checking if that element still exists
        then our substring doesn't fullfill the criteria and we move on if
        all elements from our window doesn't appear after that point we
        append the size of the window to result'''
        for right in range(len(s)):
            counter[s[right]] -= 1
            #if the character is not in our window update the have variable
            if s[right] not in window:
                have += 1
            window.add(s[right])
            '''if the element is no longer found in our counter then the
            number of elements that need to be checked is decremented by one'''
            if counter[s[right]] == 0:
                have -= 1
            if have == 0:
                result.append(right-left+1)
                left = right + 1
                window = set()
        return result
        #Time Complexity: O(n)
        #Space Complexity: O(n)