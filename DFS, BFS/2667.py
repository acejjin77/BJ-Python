import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
queue = deque()
s = [list(map(int, list(input().rstrip()))) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
queue.append([0, 0])

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and s[nx][ny] == 1:
            queue.append([nx, ny])
            s[nx][ny] = s[x][y] + 1

s[0][0] = 1

print(s[n - 1][m - 1])