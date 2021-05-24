from collections import deque

m, n = map(int, input().split())
s = [list(map(int, input().split())) for i in range(n)]
queue = deque()
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    for j in range(m):
        if s[i][j] == 1:
            queue.append([i, j])

while queue:
    a, b = queue.popleft()
    for i in range(4):
        nx = a + dx[i]
        ny = b + dy[i]
        if 0 <= nx < n and 0 <= ny < m and s[nx][ny] == 0:
            s[nx][ny] = s[a][b] + 1
            queue.append([nx, ny])


isTrue = False
result = -2
for i in s:
    for j in i:
        if j == 0:
            isTrue = True
        result = max(result, j)
if isTrue == True:
    print(-1)
elif result == -1:
    print(0)
else:
    print(result - 1)
