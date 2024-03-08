class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        '''Approach: Backtracking.. The problem  asks to find the kth index 
        element of the nth row. To solve this problem we used backtracking to
        hold on from which division this value has come. Meaning since at each
        row we will have twice of the previous row therefore we can calculate
        from which branch it came from so we do that for each row and when we
        reach 1 or 2 that means we have reached our base case and we can go
        down anymore. Therefore we used a simple mathematics to find from which
        branch it just came by using the ceil function then we calculate for that
        thing again and again until we reach the base case. After that all e need 
        to do is iterate through our list in reversed manner and at each
        step calculate the value based on if the index that we have found using
        backtracking is even then it's the last number from the previous number
        that means if the number was zero then it would be one and if the number
        was one it would be zero. Therefore after updating the value at each
        iteration we just simply return the last value that is hold in our
        variable.'''
        result = []

        #backtracking function for calculating the branches at each step
        def backtrack(k):
            if k==1 or k==2 :
                result.append(k)
                return
            result.append(k)
            backtrack(ceil(k/2))
        backtrack(k)
        result.reverse()
        #update the value to be either 0 or 1 based on the first element
        if result[0] == 1:
            value = 0
        else:
            value = 1
        
        #iterate for each element in the result and continue updating it based on the conditions
        for index in range(1,len(result)):
            if result[index]%2==0:
                if value == 1:
                    value = 0
                else:
                    value = 1
            else:
                if value == 1:
                    value = 1
                else:
                    value = 0
        return value
        #Time Complexity: O(k) for both the recursion and the for loop
        #Space Complexity: O(k) for the list and for the call stack