import sys
sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
result = 0


def dfs(x, y):
    case[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and case[nx][ny] == 1:
            dfs(nx, ny)


for h in range(0, 101):
    case = [[0] * n for _ in range(n)]
    cnt = 0

    for i in range(n):
        for j in range(n):
            if s[i][j] > h:
                case[i][j] = 1

    for i in range(n):
        for j in range(n):
            if case[i][j] == 1:
                dfs(i, j)
                cnt += 1

    result = max(result, cnt)

print(result)
