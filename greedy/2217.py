import sys

input = sys.stdin.readline

n = int(input())
rope = [int(input()) for _ in range(n)]
max_weight = 0

rope.sort(reverse=True)

for i in range(n):
    max_weight = max(max_weight, rope[i] * (i + 1))

print(max_weight)
