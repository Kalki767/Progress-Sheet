# Problem: Meaningless Operations - https://codeforces.com/problemset/problem/1110/C

import math
'''Approach: Math and Bitwise Operation. We know from math that the gcd of any number and zero is the number itself. So when we check
if we can make one of them which would be the and operation we saw that it can only be done by flipping the given a when we directly
use this b to do xor on the given a we find that it would give us maximum number possible since we flipped the remaining it will
set all the bit's to one this means we will have that value as our answer but if the given number is equal with that value we
can't return it as an answer so using some math proofs we find that the maximum gcd would be the value that divides a succesfully.
Because no matter what operation is performed on a we can't have a bigger number.'''

def Gcd(a):
    greatest_divisor = 1
    square_root = int(math.sqrt(a))
    for i in range(2,square_root+1):
        if a % i == 0:
            greatest_divisor = max(greatest_divisor,i,a//i)
    return greatest_divisor
q = int(input())
for _ in range(q):
    a = int(input())
    bit_length = a.bit_length()
    maxi = 2 ** bit_length - 1
    if a != maxi:
        print(maxi)
    else:
        print(Gcd(a))

#Time Complexity: O(sqrt(a))
#Space Complexity: O(1)