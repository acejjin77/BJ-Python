import sys
from collections import deque

input = sys.stdin.readline

a, b = map(int, input().split())
queue = deque([[a, 1]])
res = -1

while queue:
    t, cnt = queue.popleft()
    if t == b:
        res = cnt
        break
    if 2 * t <= b:
        queue.append([2 * t, cnt + 1])
    if int(str(t) + str(1)) <= b:
        queue.append([int(str(t) + str(1)), cnt + 1])

print(res)