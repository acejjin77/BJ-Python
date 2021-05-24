n = int(input())
s = list(map(str, input().split()))
x, y = 1, 1


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_type = ['L', 'R', 'U', 'D']

for move in s:
    for i in range(4):
        nx, ny = 0, 0
        if move == move_type[i]:
            nx = x + dx[i]
            ny = y + dy[i]

        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue

        x = nx
        y = ny

print(x, y)