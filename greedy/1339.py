import sys

input = sys.stdin.readline
n = int(input())
s = []
alpha = [0] * 26
cnt = 9
result = 0

for i in range(n):
    s.append(str(input().strip()))

for sss in s:
    for i in range(len(sss)):
        alpha[ord(sss[::-1][i]) - 65] += 10 ** i

alpha.sort(reverse=True)

for a in alpha:
    result += a * cnt
    cnt -= 1

print(result)

