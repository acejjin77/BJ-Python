from collections import deque

t = int(input())
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(t):
    m, n, k = map(int, input().split())
    s = [[0] * m for i in range(n)]
    cnt = 0

    for j in range(k):
        a, b = map(int, input().split())
        s[b][a] = 1

    for i in range(n):
        for j in range(m):
            if s[i][j] == 1:
                s[i][j] = 0
                queue = deque([[i, j]])
                while queue:
                    a, b = queue.popleft()
                    for k in range(4):
                        nx = a + dx[k]
                        ny = b + dy[k]
                        if 0 <= nx < n and 0 <= ny < m and s[nx][ny] == 1:
                            s[nx][ny] = 0
                            queue.append([nx, ny])
                cnt += 1
    print(cnt)
