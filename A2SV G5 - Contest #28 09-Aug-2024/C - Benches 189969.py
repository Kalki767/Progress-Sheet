# Problem: C - Benches - https://codeforces.com/gym/540354/problem/C

n = int(input())
m = int(input())
nums = []

for _ in range(n):
    bench = int(input())
    nums.append(bench)

max_number = max(nums)
total_difference = sum(max_number - num for num in nums)

if total_difference >= m:
    # If the total difference is greater than or equal to m,
    # we can make all benches at least as high as the current max_number.
    minimum = max_number
else:
    # If the total difference is less than m,
    # we need to add the remaining m after leveling all benches to max_number.
    remaining = m - total_difference
    added = remaining // n
    minimum = max_number + added
    if remaining % n != 0:
        minimum += 1

# The maximum possible height if we add all m units to the tallest bench.
maximum = max_number + m

print(minimum, maximum)
