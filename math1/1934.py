import math
import sys

input = sys.stdin.readline

n = int(input())

for i in range(n):
    x, y = map(int, input().split())

    print(x*y//math.gcd(x, y))