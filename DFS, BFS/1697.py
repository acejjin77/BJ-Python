from collections import deque

n, k = map(int, input().split())
visit = [0 for i in range(100001)]

queue = deque([n])

while queue:
    a = queue.popleft()
    if a == k:
        print(visit[a])
        break
    for num in [a + 1, a - 1, a * 2]:
        if 100000 >= num >= 0 == visit[num]:
            visit[num] = visit[a] + 1
            queue.append(num)
