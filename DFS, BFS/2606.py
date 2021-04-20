import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
matrix = [[0] * (n) for i in range(n)]
visit = [0 for i in range(n)]
cnt = 0

for i in range(m):
    a, b = map(int, input().split())
    matrix[a - 1][b - 1], matrix[b - 1][a - 1] = 1, 1


def dfs(v):
    visit[v] = 1
    for i in range(n):
        if visit[i] == 0 and matrix[v][i] == 1:
            dfs(i)


dfs(0)
for i in range(1, n):
    if visit[i] == 1:
        cnt += 1

print(cnt)
