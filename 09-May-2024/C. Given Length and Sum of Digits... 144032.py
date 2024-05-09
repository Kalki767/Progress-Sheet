# Problem: C. Given Length and Sum of Digits... - https://codeforces.com/contest/489/problem/C

def solve(): 
    m, s = map(int,input().split())
    res = []
    flag = True
    while s > 0:
        val = s//m
        if val > 9:
            flag = False
            break
        res.append(val)
        s -= val
        m -= 1
    if (s==0 and m > 1) or flag == False:
        return [-1,-1]
    
    def min_number():
        ans = res.copy()
        left, right = 0, len(ans) - 1
        while left < right:
            if left != 0:
                left_difference = ans[left]
            else:
                left_difference = ans[left] - 1
            right_difference = 9 - ans[right]
            if left_difference == right_difference:
                ans[left] -= left_difference
                ans[right] += right_difference
                left += 1
                right -= 1
            elif left_difference > right_difference:
                ans[right] = 9
                ans[left] -= right_difference
                right -= 1
            else:
                ans[left] -= left_difference
                ans[right] += left_difference
                left += 1
        result = 0
        for i in range(len(ans)):
            result = result * 10 + ans[i]
        return result
    def max_number():
        ans = res.copy()
        left, right = 0, len(ans) - 1
        while left < right:
            left_difference = 9 - ans[left]
            right_difference = ans[right]
            if left_difference == right_difference:
                ans[left] = 9
                ans[right] = 0
                left += 1
                right -= 1
            elif left_difference > right_difference:
                ans[right] = 0
                ans[left] += right_difference
                right -= 1
            else:
                ans[left] = 9
                ans[right] -= left_difference
                left += 1
        result = 0
        for i in range(len(ans)):
            result = result * 10 + ans[i]
        return result
    ans = min_number()
    result = []
    result.append(ans)
    ans = max_number()
    result.append(ans)
    return result
val = solve()
print(*val)