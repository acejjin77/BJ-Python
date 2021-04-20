import sys
from itertools import combinations, permutations, combinations_with_replacement

input = sys.stdin.readline

n = int(input())
num_list = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())

max_answer = -1000000001
min_answer = 1000000001

op_set = []
op_set += '+' * plus
op_set += '-' * minus
op_set += '*' * mul
op_set += '%' * div

for case in permutations(op_set):
    answer = num_list[0]
    for i in range(len(case)):
        if case[i] == '+':
            answer += num_list[i + 1]
        elif case[i] == '-':
            answer -= num_list[i + 1]
        elif case[i] == '*':
            answer *= num_list[i + 1]
        elif case[i] == '%':
            if answer < 0:
                answer = -(-answer // num_list[i + 1])
            else:
                answer //= num_list[i + 1]

    if answer < min_answer:
        min_answer = answer
    if answer > max_answer:
        max_answer = answer

print(max_answer)
print(min_answer)
