import sys

n = int(sys.stdin.readline())
tree = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
for i in range(1, n):
    for j in range(len(tree[i])):
        if j == 0:
            tree[i][j] += (tree[i - 1][j])

        elif j == i:
            tree[i][j] += (tree[i - 1][j - 1])

        else:
            tree[i][j] += (max(tree[i - 1][j], tree[i - 1][j - 1]))

print(max(tree[n - 1]))