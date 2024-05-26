# Problem: Turtle vs. Rabbit Race: Optimal Trainings - https://codeforces.com/contest/1933/problem/E


from bisect import bisect_left

import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():
    def solve():
        n = int(input())
        nums = list(map(int,input().split()))
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1]+num)
        q = int(input())
        answer = []
        for _ in range(q):
            left, u = map(int,input().split())
            found = u + prefix_sum[left-1]
            index = bisect_left(prefix_sum,found)
            flag = False
            if index == n + 1:
                answer.append(index-1)
            elif prefix_sum[index] == found:
                answer.append(index)
            elif index <= left:
                answer.append(left)
            else:
                first_val = prefix_sum[index] - prefix_sum[left-1]
                second_val = prefix_sum[index-1] - prefix_sum[left-1]
                curr = first_val - u - 1
                total1 = (u*(u+1))//2 - (curr*(curr+1))//2
                current = u - second_val + 1
                total2 = (u * (u + 1)) // 2 - (current * (current - 1)) // 2 
                if total1 > total2:
                    answer.append(index)
                else:
                    answer.append(index-1)
                
        print(*answer)
    t = int(input())
    for _ in range(t):
        solve()
    
if __name__ == '__main__':

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()


