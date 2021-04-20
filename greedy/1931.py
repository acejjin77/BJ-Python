import sys

input = sys.stdin.readline

n = int(input())
conf = [list(map(int, input().split())) for i in range(n)]

conf.sort(key=lambda x: x[0])
conf.sort(key=lambda x: x[1])

answer = 1
end_time = conf[0][1]

for i in range(1, n):
    if conf[i][0] >= end_time:
        end_time = conf[i][1]
        answer += 1

print(answer)

