# Problem: Divide and equalize - https://codeforces.com/problemset/problem/1881/D

from collections import defaultdict

import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():
    total_counter = defaultdict(int)
    def solve():
        n = int(input())
        nums = list(map(int,input().split()))
        nums.sort()
        for num in nums:
            if num in total_counter:
                for k,v in total_counter[num].items():
                    counter[k] += v
            else:
                factors = prime_factors(num)
                for key, val in factors.items():
                    counter[key] += val
                total_counter[num] = factors
        for value in counter.values():
            if value % n != 0:
                return False
        return True

    def prime_factors(n):
        i = 2
        factors = defaultdict(int)
        while i*i <= n:
            while n % i == 0:
                factors[i] += 1
                n //= i
            i += 1
        if n > 1:
            factors[n] += 1
        return factors
    t = int(input())
    for _ in range(t):
        counter = defaultdict(int)
        if solve():
            print('YES')
        else:
            print('NO')
    

    
if __name__ == '__main__':
    
    

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()

