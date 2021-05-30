import sys

input = sys.stdin.readline

n, k = map(int, input().split())
s = list(map(int, input().split()))
plug = s[:n]
cnt = 0

for i in range(n, k):
    print(s[i], plug, s[i:i + n])
    if s[i] in plug:
        continue
    for j in range(n):
        if not plug[j] in s[i:i + n]:
            plug[j] = s[i]
            cnt += 1
            break

print(cnt)

