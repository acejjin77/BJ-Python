import sys
import heapq
from collections import deque

input = sys.stdin.readline
n, k = map(int, input().split())
v = [list(map(int, input().split())) for _ in range(n)]
c = list(int(input()) for _ in range(k))
h = []
res = 0
v = deque(sorted(v, key=lambda x: x[0]))
c.sort()

for bag in c:
    while v and bag >= v[0][0]:
        heapq.heappush(h, -v.popleft()[1])
    if h:
        res -= heapq.heappop(h)

print(res)