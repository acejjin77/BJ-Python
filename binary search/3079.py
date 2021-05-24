import sys

input = sys.stdin.readline

m, n = map(int, input().split())
times = [int(input()) for _ in range(m)]

l = 0
r = n * max(times)
answer = 0

while l <= r:
    total = 0
    mid = (l + r) // 2
    for time in times:
        total += mid // time
    if total < n:
        l = mid + 1
        answer = mid
    else:
        r = mid - 1

print(answer + 1)