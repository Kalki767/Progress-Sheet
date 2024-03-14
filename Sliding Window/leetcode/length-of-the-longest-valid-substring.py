class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        '''Approach: Sliding Window. The problem asks to find the length of the
        longest valid substring in which none of it's substrings exist in
        forbidden. So here we used sliding window to check if the current
        window is valid or not. But the question lays on how can we do that
        because we are checking the substring against an array of words that
        means we could have a forbidden substring inside our window whose
        start is not on the current pointer we are having. The problem can
        be solved just by adding one for loop inside our sliding window to
        check if there exists a forbidden string in our current window. But
        this would face a time complexity issue because our algorithm must run
        in O(n) according to the constraints. But the trick here is the inner
        for loop will only run in constant time because on the constraint it
        says that the maximum length of a forbidden word is 10 and since we
        are looking for a forbidden word all we have to do is run our for
        loop with a maximum of 10 times and check if there is a forbidden
        substring in it if there is we move our left pointer to the point we 
        find a forbidden substring and after this for loop we will always end
        up with a window which is valid so we can calculate the maximum length.
        Here we used some optimizations like storing the forbidden words in
        a set for a better lookup and our for loop should run at maximum for
        the maximum length that exists in the forbidden array. We used the min
        function because we want to check for forbidden words in our window
        only so we take the minimum of our window size and the maximum length.
        '''

        forbidden_set = set(forbidden) #store in a set for efficient lookup
        forbidden_maximum = max(len(x) for x in forbidden) #to have the maximum length of the word
        left = maximum_length = 0

        for right in range(len(word)): #iterate through the word in forward way
            length = min(right-left+1,forbidden_maximum) #set the boundary for the second for loop to run on
            for k in range(length): #iterate through the boundary and check if there is a forbidden word
                if word[right-k:right+1] in forbidden_set:
                    left = right - k + 1 #update the window until it becomes valid
                    break
            maximum_length = max(maximum_length, right - left + 1)

        return maximum_length
        #Time Complexity: 10n 10 for the inner loop so overall time complexity would be O(n)
        #Space Complexity: O(n) since we used a set to store forbidden words