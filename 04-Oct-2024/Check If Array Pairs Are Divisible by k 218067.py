# Problem: Check If Array Pairs Are Divisible by k - https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        '''Approach: HashMap. The problem asks to check if we can pair all the
        elements so that all of them are divisible by k. The sum of two numbers is
        divisible by k if and only if the sum of the remainders is divisible by k.
        because the other part is already divisible by k. We also know that a remainder
        is less than k which means the sum of the two remainders is less than 2k
        which means the sum of the two remainders have to be equal with k. Therefore
        all we have to do is count the number of each remainder and traverse again
        to check if we have a match for the current value. And also one thing to
        handle is since the modulo might mess with negative numbers make sure to
        handle that case.'''
        counter = defaultdict(int)
        
        # Count the remainder frequencies
        for num in arr:
            cur = num % k
            if cur < 0:  # Adjust negative modulo results
                cur += k
            counter[cur] += 1
        
        # Check if pairs can be formed
        for num in arr:
            cur = num % k
            if cur < 0:
                cur += k
            if cur == 0:  # Special case for zero remainder
                if counter[cur] % 2 != 0:
                    return False
            else:
                if counter[cur] != counter[k - cur]:
                    return False
        
        return True
        #Time Complexity: O(n)
        #Space Complexity: O(m) where n is total number of elements and m is the total number in the hashmap
