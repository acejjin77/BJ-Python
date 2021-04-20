import sys
from collections import deque

n, k = map(int, input().split())
people = deque([i for i in range(1, n + 1)])

print('<', end='')
while people:
    people.rotate(-k + 1)
    print(people.popleft(), end='')
    if people:
        print(', ', end='')
print('>')
