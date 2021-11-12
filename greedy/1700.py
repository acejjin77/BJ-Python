import sys

input = sys.stdin.readline

n, k = map(int, input().split())
s = list(map(int, input().split()))
plug = [0 for _ in range(n)]
cnt = 0

for i in range(k):
    if s[i] in plug:
        continue
    elif 0 in plug:
        plug[plug.index(0)] = s[i]
    
    else:
        a = 0
        for j in range(n):
            try:
                if a < s[i + 1:].index(plug[j]):
                    a = s[i + 1:].index(plug[j])
                    b = j
            except:
                a = -1
                b = j
                break
        plug[b] = s[i]
        cnt += 1

print(cnt)


