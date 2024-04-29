# Problem: Prime Pairs With Target Sum - https://leetcode.com/problems/prime-pairs-with-target-sum/description/

class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        '''Approach: Maths. The problem asks to find prime pairs that are
        less than or equal to the target and sum up to the target. To solve
        this problem first we need to find the prime numbers that are less
        than or equal to n. For that purpose we used the seive of eratosthenes
        After finding those prime numbers we need to find pairs we can do that
        by iterating through our list of prime numbers and if there exists
        a the target minus the prime number in our prime number list we will
        add them into our answer. But element lookup in a list is not an
        efficient task so we can use a set for efficient look up and also
        when we come to that value since it's pair is already used we need to
        skip it that means we could mark it as visited or non prime number
        not to use another space.'''

        #Step1: Handle edge cases since there is no prime element less than 2 return []
        if n <= 2:
            return []
        
        #Step2: implement sieve of erathosthenes
        prime = [True for _ in range(n)]
        prime[0] = prime[1] = False
        index = 2
        while index * index <= n:
            if prime[index]:
                current = index * index
                while current < n:
                    prime[current] = False
                    current += index
            index += 1
        
        #Step3: convert the list of prime numbers into set for efficient lookup
        prime_numbers = set()
        for i in range(n):
            if prime[i]:
                prime_numbers.add(i)
        
        #Step4: build your answer by iterating through list of prime numbers and finding pair
        answer = []
        for i in range(n):
            if prime[i]:
                if (n - i) in prime_numbers:
                    answer.append([i,n-i])
                    prime[n-i] = False
        
        return answer
        #Time Complexity: O(nlogn)
        #Space Complexity: O(n)
        