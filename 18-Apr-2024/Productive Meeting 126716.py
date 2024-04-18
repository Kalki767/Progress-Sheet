# Problem: Productive Meeting - https://codeforces.com/contest/1579/problem/D

'''Approach: The basic idea is to pick peoples so that they will talk more so for that
case we will choose two peoples who have the highest talk decrement by one and if they
are different from 0 add to the heap again. Therefore here we are being greedy'''
from heapq import heappop, heappush

def solve():
    n = int(input())
    nums = list(map(int,input().split()))
    heap = []
    answer = []
    result = 0
    for index, num in enumerate(nums):
        if num != 0: #if a person has zero talk no need to add him to the heap
            heappush(heap,(-num,index))
    while len(heap) > 1:
        #pop out peoples who have the highest talk
        first, first_ind = heappop(heap)
        second, second_ind = heappop(heap)
        answer.append([first_ind+1,second_ind+1])
        first = -first
        second = -second
        #check if they still have to talk or leave the group
        if first - 1 > 0:
            heappush(heap,(-(first-1),first_ind))
        if second - 1 > 0:
            heappush(heap,(-(second-1),second_ind))
    
    print(len(answer))
    for first, second in answer:
        print(first,second)
t = int(input())
for _ in range(t):
    solve() 
  