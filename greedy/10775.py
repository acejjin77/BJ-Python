import sys

input = sys.stdin.readline

n = int(input())
customer = list(map(int, input().split()))
customer.sort()

answer = 0

for i in range(n):
    answer += customer[i] * (n - i)

print(answer)

# n = int(input())
#
# customer = list(map(int, input().split()))
# customer.sort()
#
# wait = 0
# answer = 0
#
# for i in range(n):
#     wait += customer[i]
#     answer += wait
#
# print(answer)