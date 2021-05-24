import sys
from collections import deque

input = sys.stdin.readline

dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, -1, 1, 1, -1, 1, -1]

def bfs(x, y):
    s[x][y] = 0
    queue = deque([[x, y]])
    while queue:
        a, b = queue.popleft()
        for i in range(8):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < n and 0 <= ny < m and s[nx][ny] == 1:
                s[nx][ny] = 0
                queue.append([nx, ny])


while True:
    m, n = map(int, input().split())
    s = [list(map(int, input().split())) for i in range(n)]
    queue = deque()
    cnt = 0

    if not s:
        break

    for i in range(n):
        for j in range(m):
            if s[i][j] == 1:
                bfs(i, j)
                cnt += 1

    print(cnt)