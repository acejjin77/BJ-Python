from itertools import combinations
from functools import reduce
from collections import Counter

target = int(input())
count = 9 * (len(str(target))) - 1
answer = target - count


def sum_digit(number):
    return sum([int(i) for i in str(number)])


if target < 10:
    if (target % 2 == 0):
        print(target / 2)
    else:
        print(0)
else:
    for cards in range(count):
        if (answer + sum_digit(answer)) == target:
            print(answer)
            break
        else:
            answer += 1
        if (answer == target):
            print(0)
