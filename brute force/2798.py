from itertools import combinations

card_num, target = map(int, input().split())
card_list = list(map(int, input().split()))

answer = 0

for cards in combinations(card_list, 3):
    temp_sum = sum(cards)
    if answer < temp_sum <= target:
        answer = temp_sum

print(answer)



