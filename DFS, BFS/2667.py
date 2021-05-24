from collections import deque

n = int(input())
s = [list(map(int, list(input().rstrip()))) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
answer = []


def bfs(x, y):
    queue = deque([[x, y]])
    s[x][y] = 0
    cnt = 1
    while queue:
        a, b = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < n and 0 <= ny < n and s[nx][ny] == 1:
                s[nx][ny] = 0
                queue.append([nx, ny])
                cnt += 1
    answer.append(cnt)


for i in range(n):
    for j in range(n):
        if s[i][j] == 1:
            bfs(i, j)

answer.sort()
print(len(answer))
for i in answer:
    print(i)
