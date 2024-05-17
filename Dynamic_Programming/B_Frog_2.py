import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():
    n,k = map(int,input().split())
    nums = list(map(int,input().split()))
    memory = {}
    dp = [float('inf') for _ in range(n)]
    dp[-1] = 0
    for index in range(n-2,-1,-1):
        length = min(index+k+1,n)
        answer = float('inf')
        for i in range(index+1,length):
            answer = min(answer, abs(nums[i]-nums[index]) + dp[i])
        dp[index] = answer
    print(dp[0])
if __name__ == "__main__":
    main()
