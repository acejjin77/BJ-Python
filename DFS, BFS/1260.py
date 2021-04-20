import sys

input = sys.stdin.readline

n, m, v = map(int, input().split())
matrix = [[0] * (n + 1) for i in range(n + 1)]
visit = [0 for i in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    matrix[a][b], matrix[b][a] = 1, 1


def dfs(v):
    print(v, end=' ')
    visit[v] = 1
    for i in range(1, n + 1):
        if visit[i] == 0 and matrix[v][i] == 1:
            dfs(i)


def bfs(v):
    visit[v] = 0
    queue = [v]
    while queue:
        v = queue.pop(0)
        print(v, end=' ')
        for i in range(1, n + 1):
            if visit[i] == 1 and matrix[v][i] == 1:
                queue.append(i)
                visit[i] = 0


dfs(v)
print()
bfs(v)
