import sys

n = int(sys.stdin.readline())
tiles = [0] * 1000001

tiles[1] = 1
tiles[2] = 2
tiles[3] = 3
tiles[4] = 5

for i in range(4, n+1):
    tiles[i] = (tiles[i-1] + tiles[i-2]) % 15746

print(tiles[n])

