# Problem: A - abbccc - https://codeforces.com/gym/530187/problem/A

n = int(input())
t = input()
s = []
index = 0
current = 0
while index < len(t):
    current += 1
    s.append(t[index])
    index += current
print(''.join(s))