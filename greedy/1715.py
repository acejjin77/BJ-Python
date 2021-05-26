import heapq
import sys

input = sys.stdin.readline

n = int(input())
s = [int(input()) for _ in range(n)]

heapq.heapify(s)
result = 0

while len(s) > 1:
    c1 = heapq.heappop(s)
    c2 = heapq.heappop(s)
    result += c1 + c2
    heapq.heappush(s, c1 + c2)

print(result)