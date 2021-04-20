import sys

n = int(sys.stdin.readline())
result = 0

while n >= 5:
    if n % 5 == 0:
        result += (n // 5)
        print(result)
        break
    n -= 3
    result += 1
else:
    print(-1)
