# Problem: Interesting drink - https://codeforces.com/problemset/problem/706/B/

from bisect import bisect_right

'''sort the input and use binary search because since we are looking for number of shops 
that he could buy every shop whose cost is less than the given money is a counted so we
find the insertion position for the current element which would give us every shop whose
cost is less than the given coin'''
n = int(input())
shops = list(map(int,input().split()))
shops.sort()
q = int(input())
for _ in range(q):
    coins = int(input())
    number_of_shops = bisect_right(shops,coins)
    print(number_of_shops)