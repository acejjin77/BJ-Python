import sys

n = int(input())
words = [str(input()) for i in range(n)]
vowels = ['A', 'E', 'I', 'O', 'U']
score = 0
breaker = 0
dup = []

for i in range(n):
    for alpha in words[i]:
        if alpha not in vowels:
            breaker = 1

    if (i != 0) & (words[i][0] != words[i - 1][-1]):
        breaker = 1

    if words[i] in dup:
        breaker = 1

    if breaker == 1:
        break
    else:
        score += len(words[i])
        dup.append(words[i])

print(score)
