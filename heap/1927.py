import sys
import heapq

input = sys.stdin.readline

n = int(input().strip())

heap = []

for i in range(n):
    num = int(input().strip())
    if num == 0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, num)
