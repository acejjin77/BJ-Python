import sys

sys.setrecursionlimit(10000)

input = sys.stdin.readline

n, m = map(int, input().split())
s = [[] * (n + 1) for _ in range(n + 1)]
visit = [0] * (n + 1)
cnt = 0

for _ in range(m):
    x, y = map(int, input().split())
    s[x].append(y)
    s[y].append(x)


def dfs(v):
    visit[v] = 1
    for c in s[v]:
        if visit[c] == 0:
            dfs(c)


for i in range(1, n + 1):
    if visit[i] == 0:
        dfs(i)
        cnt += 1

print(cnt)
