import sys

input = sys.stdin.readline

r, c = map(int, input().split())
v = [list(str(input())) for i in range(r)]
cnt = 0
dx = [-1, 0, 1]


def checkpipe(x, y):
    v[x][y] = 'o'
    if y == c - 1:
        return True

    for i in range(3):
        nx = x + dx[i]
        ny = y + 1
        if 0 <= nx < r and 0 <= ny < c and v[nx][ny] == '.':
            if checkpipe(nx, ny):
                return True
    return False


for i in range(r):
    if checkpipe(i, 0):
        cnt += 1

    # for i in range(r):
    #     for j in range(c):
    #         print(v[i][j], end=' ')
    #     print()
    # print()

print(cnt)
