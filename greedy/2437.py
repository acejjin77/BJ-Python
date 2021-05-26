import sys

input = sys.stdin.readline
n = int(input())
s = list(map(int, input().split()))
num = 1

s.sort()

for i in range(n):
    if num < s[i]:
        break
    num += s[i]

print(num)
