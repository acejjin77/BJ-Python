import sys

input = sys.stdin.readline

n = int(input())
dw = []
result = [0 for i in range(1000)]
for _ in range(n):
    dw.append(list(map(int, input().split())))

dw.sort()

for i in range(n):
    result[dw[i][0]] = max(dw[i][1], result[dw[i][0]])

print(result)