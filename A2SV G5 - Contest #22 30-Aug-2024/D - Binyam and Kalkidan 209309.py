# Problem: D - Binyam and Kalkidan - https://codeforces.com/gym/531455/problem/D

n = int(input())
number = input()
digits = []
for digit in number:
    if digit == '4':
        digits.extend(['3','2','2'])
    elif digit == '6':
        digits.extend(['5','3'])
    elif digit == '8':
        digits.extend(['2','2','2','7'])
    elif digit == '9':
        digits.extend(['3','3','2','7'])
    elif digit in '2357':
        digits.extend(digit)
digits.sort(reverse=True)
print(int(''.join(digits)))