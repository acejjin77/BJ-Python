import sys

input = sys.stdin.readline

n = int(input())
answer = [0] * n

for i in range(n):
    la, lb = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    b.sort()

    for num in a:
        s = 0
        e = len(b) - 1
        temp = -1
        while s <= e:
            mid = (s + e) // 2
            if b[mid] < num:
                temp = mid
                s = mid + 1
            else:
                e = mid - 1
        answer[i] += temp + 1

for ans in answer:
    print(ans)