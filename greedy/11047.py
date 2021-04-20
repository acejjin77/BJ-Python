import sys

input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for i in range(n)]
num = 0

coins.sort(reverse=True)

for coin in (coins):
    if coin > k:
        continue
    else:
        num += k // coin
        k %= coin
    if k == 0:
        break

print(num)
