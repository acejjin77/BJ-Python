import sys

input = sys.stdin.readline

n = int(input())
road = list(map(int, input().split()))
city = list(map(int, input().split()))

lowest_cost = 1000000001
answer = 0

for i in range(n - 1):
    if city[i] < lowest_cost:
        lowest_cost = city[i]
    answer += road[i] * lowest_cost

print(answer)
