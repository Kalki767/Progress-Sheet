class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        '''Approach: Greedy. The problem asks to minimize the cost of flight
        if we distribute 2n peoples equally to city a and city b. Since we want
        to minimze the cost we want to calculate the difeerence between each
        cost of flight and we want to avoid a maximum difference. Therefore
        after calculating the difference we sort it and we take the first
        flight for the first n travels and the second flight for the next n
        flights.Then we sum those values together and that would be our result.
        We used a list in our dictionary because there might be two or more
        flights with the same difference.'''
        n = len(costs)
        cost_difference = defaultdict(list)

        #finding the difference in cost between the first and second flight
        for index in range(n):
            difference = costs[index][0] - costs[index][1]
            cost_difference[difference].append(index)

        #sorting the differences after storing them in a list
        different_costs = list(cost_difference.keys())
        different_costs.sort()
        counter = minimum_cost = 0
        
        #after sorting them iterate through each of them and update the cost
        for cost in different_costs:
            value = cost_difference[cost]
            for country in value:
                if counter >= n//2:
                    minimum_cost += costs[country][1]
                else:
                    minimum_cost += costs[country][0]
                counter += 1
                
        return minimum_cost
        #Time Complexity: O(n)
        #Space Complexity: O(n)
