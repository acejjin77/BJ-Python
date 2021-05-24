import sys

input = sys.stdin.readline

n = int(input())
times = [300, 60, 10]

if n % 10 != 0:
    print(-1)
else:
    for time in times:
        if n >= time:
            print(n // time, end=" ")
            n %= time
        else:
            print(0, end=" ")
