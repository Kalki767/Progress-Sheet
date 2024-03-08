class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        '''Approach: Binary Search. The problem asks to find the winner at a
        given time based on the conditions that are stated for winning. So
        we calculate the winner while traversing through the persons and store
        it in a list so that we could access it after calculating the index of
        the given query. We used bisect right to find where the position of the
        current query will be in our timestamp and since the times and the 
        persons match we will just simply return the person at the winners.
        '''
        self.time_stamp = times[:]
        winner_frequency = defaultdict(int)
        self.winners = []
        current_winner = -1

        #calculating the winners at each time stamp
        for candidate in persons:
            winner_frequency[candidate] += 1
            #if there is a tie take the recent one if the current has more votes update the winner
            if winner_frequency[current_winner ] <= winner_frequency[candidate]:
                current_winner = candidate
            self.winners.append(current_winner)

    def q(self, t: int) -> int:
        #calculate the position of the winner
        right_index = bisect_right(self.time_stamp,t)
        return self.winners[right_index-1]
    #Time Complexity: O(n)
    #Space Complexity: O(n)


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)