import sys

input = sys.stdin.readline

n = int(input())
scores = [int(input()) for _ in range(n)]
cnt = 0

for i in range(n - 1, 0, -1):
    if scores[i] <= scores[i - 1]:
        cnt += (scores[i - 1] - scores[i] + 1)
        scores[i - 1] = scores[i] - 1

print(scores)
print(cnt)
