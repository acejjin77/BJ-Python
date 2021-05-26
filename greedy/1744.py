import heapq
import sys

input = sys.stdin.readline

n = int(input())
minus = []
plus = []
result = 0

for _ in range(n):
    num = int(input())
    if num <= 0:
        minus.append(abs(num))
    elif num > 1:
        plus.append(num)
    else:
        result += 1

minus.sort(reverse=True)
plus.sort(reverse=True)

if len(minus) % 2 == 0:
    for i in range(0, len(minus), 2):
        result += minus[i] * minus[i + 1]
else:
    for i in range(0, len(minus) - 1, 2):
        result += minus[i] * minus[i + 1]
    result -= minus[-1]

if len(plus) % 2 == 0:
    for i in range(0, len(plus), 2):
        result += plus[i] * plus[i + 1]
else:
    for i in range(0, len(plus) - 1, 2):
        result += plus[i] * plus[i + 1]
    result += plus[-1]

print(result)