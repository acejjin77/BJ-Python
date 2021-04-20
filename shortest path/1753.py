import sys
import heapq

INF = 100000000
v, e = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline())
s = [[] for _ in range(v + 1)]
dp = [INF] * (v + 1)
heap = []

for i in range(e):
    u, v, w = map(int, sys.stdin.readline().split())
    s[u].append([v, w])
