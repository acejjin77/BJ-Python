import sys
import math

input = sys.stdin.readline

n, k = map(int, input().split())

top = 1
for i in range(n, n - k, -1):
    top *= i

bot = 1
for j in range(k, 0, -1):
    bot *= j

print((top // bot) % 10007)
