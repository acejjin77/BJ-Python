import sys

input = sys.stdin.readline

t = int(input())
for i in range(t):
    n = int(input())
    tree = list(map(int, input().split()))

    tree.sort()

    result = tree[1] - tree[0]

    for j in range(2, n):
        result = max(result, tree[j] - tree[j-2])
    print(result)