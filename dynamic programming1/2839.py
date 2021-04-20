import sys

n = int(sys.stdin.readline())
count = 0

num3 = [0] * 1000
min3 = 2000
min5 = 0

if n % 5 == 0:
    print(n//5)
else:
    while n > 2:
        if n % 3 == 0:
            num3[count] = n // 3
        else:
            num3[count] = 2000
        if num3[count] < min3:
            min5 = count
        n -= 5
        count += 1
    if num3[min5] + min5 == 2000:
        print(-1)
    else:
        print(num3[min5] + min5)
