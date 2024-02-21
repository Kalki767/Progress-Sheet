class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        '''Approach: Greedy. the problem asks to find the difference
        between a maximum and a minimum score from dividing the marbles into
        k bags. to find the maximum and minimum score since the first and
        last weights will be calculated no matter what way we divide they
        will cancel with each other at the last answer therefore we won't
        consider their costs. but we can vary where our partiton will be
        based on our value. so if the first index is one partition point
        then we took the cost to be the first element plus the second
        element but the first element would have been twice but since we 
        already eliminated the first and the last elements it doesn't matter
        so finally we will have a list of costs where cost at i is the
        cost of partitioning at i which will be the sum of end of the first bag
        or i and the start of the next bag which will be j. so to find the
        total score we need to sum the cost of the k bags together. to find
        the maximum and minimum we sort the cost and the sum of the cost of 
        the last k bags would be maximum and the first would be minimum'''
        n = len(weights)
        costs = [0]*(n-1)
        for index in range(n-1):
            costs[index] = weights[index] + weights[index+1]
        costs.sort()
        length = n-1
        return sum(costs[length-(k-1):]) - sum(costs[:k-1])
        #Time Complexity: O(n)
        #Space Complexity: O(n)