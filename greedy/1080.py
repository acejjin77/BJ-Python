import heapq
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
a = [list(map(int, list(input().strip()))) for _ in range(n)]
b = [list(map(int, list(input().strip()))) for _ in range(n)]
cnt = 0
isTrue = True

def rev33(x, y):
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            a[i][j] = 1 - a[i][j]


for i in range(n - 2):
    for j in range(m - 2):
        if a[i][j] != b[i][j]:
            rev33(i, j)
            cnt += 1

for i in range(n):
    if a[i] != b[i]:
        isTrue = False
        break

if isTrue:
    print(cnt)
else:
    print(-1)