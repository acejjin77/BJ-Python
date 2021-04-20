import sys

n = int(sys.stdin.readline())

colors = [[0, 0, 0] for i in range(n)]

for i in range(n):
    colors[i][0], colors[i][1], colors[i][2] = map(int, input().split())

