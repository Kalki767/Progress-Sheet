class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        '''Approach: Queue. The problem asks how much time it takes to buy
        all tickets for the person at index k. Here the person after buying
        one ticket he goes to the back of the queue and if have no tickets
        to buy he will leave the queue. Therefore we need to maintain our
        queue by holding the indexes of the current people in our queue and
        when a person leaves the queue we pop out from the first. We store
        the indexes in our queue and not the tickets because the indexes
        refer to a unique person and they help keep track of how much the
        current person has. So the total time will be the time that the
        person waits and the person was served. when the person finishes his
        tickets we return how many times we run the loop'''
        answer = 0
        queue = deque()
        for right in range(len(tickets)):
            queue.append(right)
        while tickets[k] != 0:
            first_person = queue.popleft()
            tickets[first_person] -= 1
            if tickets[first_person]!= 0:
                queue.append(first_person)
            answer += 1
        return answer
        #Time Complexity: O(n)
        #Space Complexity: O(n)
