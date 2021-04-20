import sys
import math

input = sys.stdin.readline

for i in range(int(input())):
    n, m = map(int, input().split())

    top = 1
    for i in range(m, m - n, -1):
        top *= i

    bot = 1
    for j in range(n, 0, -1):
        bot *= j

    print((top // bot))
