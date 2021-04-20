from itertools import combinations, combinations_with_replacement

n, m = map(int, input().split())
[print(*i) for i in combinations_with_replacement(range(1, n + 1), m)]
