import sys

input = sys.stdin.readline

n = int(input())
paper = [list(map(int, input().rstrip())) for i in range(n)]
w, b = 0, 0


def check(i, j, size):
    standard = paper[i][j]
    for x in range(i, i + size):
        for y in range(j, j + size):
            if paper[x][y] != standard:
                return False
    return True


def cut(i, j, size):
    global w, b

    if check(i, j, size):
        if paper[i][j]:
            print(1, end='')
        else:
            print(0, end='')
    else:
        size //= 2

        print('(', end='')
        cut(i, j, size)
        cut(i, j + size, size)
        cut(i + size, j, size)
        cut(i + size, j + size, size)
        print(')', end='')


cut(0, 0, n)
