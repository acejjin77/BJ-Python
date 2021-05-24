from collections import deque

n, m = map(int, input().split())
s = []
for i in range(n):
    s.append(list(input()))

s[0][0] = 1
queue = deque([[0, 0]])
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

while queue:
    a, b = queue.popleft()
    for i in range(4):
        x = a + dx[i]
        y = b + dy[i]
        if 0 <= x < n and 0 <= y < m and s[x][y] == '1':
                s[x][y] = s[a][b] + 1
                queue.append([x, y])

print(s[n-1][m-1])
