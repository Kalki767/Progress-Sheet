# Problem: A - Se7en - https://codeforces.com/gym/537362/problem/A

def solve():
    '''Approach: Brute force. The problem asks to find a number that's divisible by 7 by changing the least number of digits.
    To do that we can simmply check by changing the first digit since the constraint is 1000 we can check the first and second
    digits it they will give a number that's divisible by 7 otherwise we can simply increment n by one until we find a number
    that's divisible by 7.'''
    n = int(input())
    if n % 7 == 0:
        return n
    number = list(str(n))
    for i in range(1,10):
        number[0] = str(i)
        num = int(''.join(number))
        if num % 7 == 0:
            return num
    number = list(str(n))
    for i in range(10):
        number[1] = str(i)
        num = int(''.join(number))
        if num % 7 == 0:
            return num
    while n % 7 != 0:
        n += 1
    return n
t = int(input())
for _ in range(t):
    print(solve())