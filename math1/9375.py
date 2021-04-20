import sys
import math

input = sys.stdin.readline

for i in range(int(input())):
    clothes_type = dict()
    answer = 1
    for j in range(int(input())):
        cloth = list(map(str, input().split()))
        if cloth[1] in clothes_type:
            clothes_type[cloth[1]] += 1
        else:
            clothes_type[cloth[1]] = 1

    for value in clothes_type.values():
        answer *= value + 1

    print(answer - 1)