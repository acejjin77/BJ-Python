import sys
import math

N = int(sys.stdin.readline())
num_list = []
for i in range(N):
    num_list.append(int(sys.stdin.readline()))

num_list.sort()

mog = num_list[-1] - num_list[0]
divisor = [mog]
for i in range(2, int(math.sqrt(mog)) + 1):
    if mog % i == 0:
        divisor.append(i)
        divisor.append(mog // i)

divisor = list(set(divisor))
divisor.sort()

for d in divisor:
    for i in range(N):
        if i == N - 1:
            print(d, end=" ")
        elif num_list[i] % d != num_list[i + 1] % d:
            break

# import math
# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
# num_list = [int(input()) for i in range(n)]
#
# num_list.sort()
#
# mog = num_list[-1] - num_list[0]
# div = [mog]
# answer = []
#
# for i in range(2, int(math.sqrt(mog)) + 1):
#     if mog % i == 0:
#         div.append(i)
#         div.append(mog // i)
#
# div = list(set(div))
#
# for d in div:
#     for i in range(n):
#         if i == n - 1:
#             answer.append(d)
#         elif num_list[i] % d != num_list[i + 1] % d:
#             break
#
