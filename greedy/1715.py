import sys

input = sys.stdin.readline

n = int(input())
decks = [int(input()) for _ in range(n)]

decks.sort()

if len(decks) < 3:
    print(sum(decks))

else:
    count = decks[0] + decks[1]

    for deck in decks[2:]:
        count += count + deck

    print(count)
