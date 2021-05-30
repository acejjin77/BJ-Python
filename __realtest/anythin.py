n = int(input())
coin = [500, 100, 50, 10]

for c in coin:
    print(n//c, end=' ')
    n %= c