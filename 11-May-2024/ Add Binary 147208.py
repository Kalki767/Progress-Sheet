# Problem:  Add Binary - https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        '''Approach: Bitwise Manipulation. The problem asks to add two binary
        numbers. So what we did here is normal binary addition using carry.
        So how do we know the value of the current bit? It's simple if we take
        xor of the three bits including the carry we can get the current bit.
        How about the carry? First we check if the carry was zero or one if
        it was zero then both the bits must be one so the next carry would
        be one otherwise it should be zero to check if both of them are one
        we use the and operator. If the previous carry was one then atleast
        one of the two bits must be one so to check if atleast one of the
        two bits is one we used the or operation otherwise the carry would
        be zero. So after finding the current bit we append it to our answer.
        And at last we need to reverse our answer to find the correct result.'''
        carry = 0
        answer = []
        i, j = len(a) - 1, len(b) - 1

        while i >=0 or j >= 0 or carry > 0:
            first = second = 0
            if i >= 0 and a[i] == '1':
                first = 1
            if j >= 0 and b[j] == '1':
                second = 1
            xor = first ^ second ^ carry
            answer.append(str(xor))
            if carry == 0 and first & second == 1:
                carry = 1
            elif carry == 1 and first | second == 1:
                carry = 1
            else:
                carry = 0
            i -= 1
            j -= 1
            
        answer.reverse()
        return "".join(answer)
        #Time Complexity: O(n)
        #Space Complexity: O(1)
        