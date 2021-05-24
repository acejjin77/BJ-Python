import sys

input = sys.stdin.readline

n = 1000 - int(input())
coins = [500, 100, 50, 10, 5, 1]
cnt = 0

for coin in coins:
    if n >= coin:
        cnt += n // coin
        n %= coin

    if n == 0:
        break

print(cnt)
