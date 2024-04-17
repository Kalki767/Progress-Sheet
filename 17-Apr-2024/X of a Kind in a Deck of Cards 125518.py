# Problem: X of a Kind in a Deck of Cards - https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        '''Approach: GCD. The problem asks to check if we can partition the
        array succesfully. Therefore since the number of partitons is not
        given we can decide that. To decide that we can take their greates
        common divisor so that all partitions should have that value as
        length.'''
        counter = Counter(deck)
        Gcd = counter[deck[0]]
        for key, val in counter.items():
            Gcd = gcd(Gcd,val)
        if Gcd != 1:
            return True
        return False
        #Time Complexity: O(nlogn)
        #Space Complexity: O(1)